Server Manual
===

Author: 2022, Mo Zhou
License: CC-0

## 0. Architecture / Policy

Current architecture: Each server is treated as an individual standalone
GPU server. We have direct access to all these servers and the GPUs on them.
This is not a slurm cluster setup.

**Definition: a GPU server will be named "compute node", while a storage server
will be named "storage node" in this document for convenience.**

GPU Allocation policy: (1) In regular days: GPUs are open to everyone;
(2) One month before paper submission deadline: 2 GPUs per person on
a server. (Revision-Date: 2022-10-03)

WSE IT Contact: `wsehelp @jhu.edu`

## 1. Network and Access

### 1.1. Network Requirement

University network is needed to access our servers, because they are hosted at
MARCC. According to our observation, we can access the servers from the Hackman
lab, or the JHU VPN. JHU Library seems to be blocked.

#### 1.1.1. Network Diagnosis

To figure out whether your network is ready to connect, you may ping one
of them:

```shell
ping <server>
# If the server responds, the network connection should be fine.
```

The `<server>` is a placeholder mark where you should replace with the real
server hostname or server IP address (without the brackets). This notation is
commonly seen in Linux related documentations.  I'll keep the same convension
throughout this document.

To diagnose whethere it's a network issue or firewall issue, you may first
run traceroute from Hackman lab:

```shell
sudo traceroute -n <server>
```

And then use the same command from the location where you want to diagnose.
Compare the traceroute output. If the last several jumps are identical, it means
your IP address is blocked from accessing the 

#### 1.1.2. JHU VPN

Go to https://my.jh.edu and search for VPN. Then (1) download the VPN client
and setup following the instructions; (2) apply for the VPN access on the same
website where you download the VPN. VPN access is approved automatically and
instantly.

### 1.2. Basic SSH Connection

You need `openssh` client in order to access these machines. We may request
for the VNC access in the future in case you need it. Simply use the ssh
client to login:

```shell
ssh -v <JHED>@<server>
```

The password is the same as your JHED account. So the SSH authentication
was setup with LDAP.

Troubleshooting: If you get denied for ssh connection due to too many times
of wrong password, your IP address will be temporarily banned for ~15 minutes.
Use RSA key to avoid that.

#### 1.2.1. SSH Connextion w/ RSA Key

Google `ssh-keygen` and create a keypair for ssh access. This step can be
skipped if you want to use existing keypairs. Let's assume now we have
a keypair (private key at `~/.ssh/id_rsa`, public key at `~/.ssh/id_rsa.pub`).

Then copy the public key, login into every server with password and configure
the remote:
(you may use `ssh-copy-id <JHED>@<servers>` to distribute keys instead of
using the following manual process)

```shell
(local):~$ cd .ssh
(local):~$ cat id_rsa.pub
XXXXXX user@hostname
# Copy all the contents of the key
(local):~$ ssh <JHED>@<server>
(remote):~$ mkdir .ssh
(remote):~$ cd .ssh
(remote):~$ cat > authorized_keys
# paste the key in, then press Ctrl+c
```

Then edit our local config `~/.ssh/config`. If the directory and file do
not exit, just create empty ones. Then fill the config file with the following
content:

```
Host <server1> <server2> <server3> <...>
        User <JHED>
        identityfile ~/.ssh/id_rsa
```

Now exit from the current SSH sessions. Reconnect and we should be using
the RSA key for authentication. If the server still requests your JHED
password, you must have missed this step editing your local `~/.ssh/config`
file.

### 1.3. Parallel SSH Commands

*This section depends on RSA key setup for convenience.*

We use [ansible](https://www.ansible.com/) here.  First installing ansible on
the local side (e.g. `sudo apt install ansible` on Ubuntu).  Then we write a
text file `~/servers.txt`, containing one of the servers per line:

```
<server1>
<server2>
<server3>
<...>
```

Then we try parallel ping to see if we are correctly setting things up:

```
ansible -i servers.txt all -m ping -o
```

To run a command on the servers in parallel, do like the follows:

```
ansible -i servers.txt all -m shell -a 'nvidia-smi'
```

Note, 'gpustat' is better for querying GPU status in parallel. We will cover
that later. As for driver version... `nvidia-smi` saying cuda 11.6 means *up to*
11.6, not *must equal* 11.6.

Now, if you have `ssh-agent` or any daemon progress who keeps your password
for the private RSA key, then you should be able to access these servers
directly without typing any password anymore.
Ansible documentation is available here
https://docs.ansible.com/ansible/latest/index.html

Some environment vairables may be helpful for ansible:
https://docs.ansible.com/ansible/latest/reference_appendices/config.html ,
such as `ANSIBLE_FORCE_COLOR`, and `ANSIBLE_INVENTORY`, etc.

```
export ANSIBLE_FORCE_COLOR=True
export ANSIBLE_INVENTORY=~/servers.txt
```

In case of ansible error due to `no enough space left in /home`, append this to
the ansible command line: `-e 'ansible_remote_tmp=/tmp/<jhed>'`.

## 2. Server Storage

### 2.1. Storage Area (Compute Nodes)

1. These servers are not running RAID. Our `/data` directory is currently a
temporary storage area based on a single U2 NVME SSD. So any data stored on
these servers is at risk of sudden irreversible loss.
**Keep it in mind: properly and regularly backup your important data.**

2. These servers have been configured with two different storage areas.
`/home` should be used minimally. `/data` is a higher performing file system,
and any data that needs to be processed should reside here.
`/home` only has 100GB space (although resizable), so please really don't
put datasets and bulky files here. In the worse case, attempts to login
to the server may fail due to "no enough space left in /home".

### 2.2. Coordination (Compute Nodes)

5. Everyone has write access to /data. I suggest the following layout for
using the public storage area:

```
/data/common : put your bulky dataset here
/data/<JHED> : other files
```

You may want to use symlink between `/home/<JHED>/*` and `/data/<JHED>/*` to
redirect your files. We will follow this convention throughout this document.

Please the `/data` directory as a temporary storage, and keep in mind to
move less frequently used and archival files to the storage server.

### 2.3. Shared Storage Server (ZFS exported through NFS)

- Network Connections: 10GbE (TCP)
- Disk Array Configuration: (8x16TB RAIDz2 + 8x16TB RAIDz2), +L2ARC (2TB nvme) +ZIL (2TB nvme)
- Raw/Effective Space: 16 * 16 TB Raw. The effective space is 166TiB.
- NFS Mount Point (on compute node): `/nfs`  (FIXME)
- ZFS Mount Point (on storage node): `/pool1`
- User quota: 8TiB

(On storage server) Use `zpool list -v` and `zfs list -tall` to list the zpool
and zfs dataset information including data usage.  Use `zpool status -v` to
check the zpool status.

## 3. Parallel Setup of Deep Learning Environment

In this section, we setup the servers in parallel, following a consistent
and uniform configuration.

### 3.1. Create directories and symlinks

```shell
ansible -i servers.txt all -m shell -a 'ls /data'
ansible -i servers.txt all -m shell -a 'mkdir -p /data/<JHED>/Downloads'
ansible -i servers.txt all -m file -a 'src=/data/<JHED>/Downloads dest=/home/<JHED>/Downloads state=link'
```

Document for [ansible.builtin.shell](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/shell_module.html),
[ansible.builtin.file](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/file_module.html)

### 3.2. Download and Setup Anaconda

We install it in the [silent-mode](https://docs.anaconda.com/anaconda/install/silent-mode/)

```shell
ansible -i servers.txt all -m shell -a 'chdir=Downloads wget -c https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-x86_64.sh'
ansible -i servers.txt all -m shell -a 'mkdir -p /data/<JHED>/anaconda3'
ansible -i servers.txt all -m shell -a 'ln -s /data/<JHED>/anaconda3 .'
ansible -i servers.txt all -m shell -a 'bash Downloads/Anaconda3-2021.11-Linux-x86_64.sh -b -p ~/anaconda3 -u'
```

Then you may setup your shell following the instruction here https://docs.anaconda.com/anaconda/install/silent-mode/

I did not setup the shell variables for the Conda. So my following commands
will also work whether you have set it up or not.  Now we install `gpustat` for
quick GPU status lookup. 

```
ansible -i servers.txt all -m shell -a '~/anaconda3/bin/pip3 install gpustat'
```

In the future, if the shell tells you it cannot find commands such as `conda`,
you must have forgotten to setup the shell variables following the anaconda
instructions. If you are as lazy as me, just use this to configure anaconda
in bash (or zsh):

```
ansible -i servers.txt all -m shell -a 'echo export PATH="/home/<JHED>/anaconda3/bin:\$PATH" >> ~/.bashrc'
```

### 3.3. Parallel Server Status query

#### 3.3.1. GPU Status

Following the above instructions step-by-step, we should be able to query
the GPU status in parallel.

```
ansible -i servers.txt all -m shell -a '~/anaconda3/bin/gpustat'
```

You may lookup command usage with `man` or `tldr`.

And the output of gpustat will look like this:

```
xxx4.wse.jhu.edu | CHANGED | rc=0 >>
xxx4                 Thu Apr  7 20:53:17 2022  510.47.03
[0] NVIDIA RTX A6000 | 67'C, 100 % | 45168 / 49140 MB | xxxxx(44705M) gdm(4M)
[...]
xxx2.wse.jhu.edu | CHANGED | rc=0 >>
xxx2                 Thu Apr  7 20:53:17 2022  510.47.03
[0] NVIDIA RTX A5000 | 31'C,   0 % |   308 / 24564 MB |
[...]
xxx3.wse.jhu.edu | CHANGED | rc=0 >>
xxx3                 Thu Apr  7 20:53:17 2022  510.47.03
[0] NVIDIA RTX A5000 | 31'C,   0 % |   308 / 24564 MB |
[...]
xxx1.wse.jhu.edu | CHANGED | rc=0 >>
xxx1                 Thu Apr  7 20:53:18 2022  510.47.03
[0] NVIDIA RTX A6000 | 32'C,   0 % |   460 / 49140 MB | gdm(4M)
[...]
```

#### 3.3.2. Other System Status

CPU / Ram status

```
ansible -i servers.txt all -m shell -a 'top -b -n1 | head -n5'
ansible -i servers.txt all -m setup -a 'filter="*mem*"'
```

System status with Inxi (we need to optionally install this)

```
# install this perl script
ansible -i servers.txt all -m shell -a 'mkdir bin'
ansible -i servers.txt all -m shell -a 'chdir=bin wget -c https://github.com/smxi/inxi/raw/master/inxi'
ansible -i servers.txt all -m shell -a 'chmod +x bin/inxi'
# show basic system information
ansible -i servers.txt all -m shell -a '~/bin/inxi'
# show full system information
ansible -i servers.txt all -m shell -a '~/bin/inxi -Fz'
# show some system information (I picked these sections)
ansible -i servers.txt all -m shell -a '~/bin/inxi -mDPI'
```

Redhat has an article on inxi as well: https://www.redhat.com/sysadmin/learn-more-inxi

## 3.4. Install Pytorch

Following https://pytorch.org , I personally chooise the latest version (1.11.0)
for example. So I just directly copy that installation command:

```
ansible -i servers.txt all -m shell -a '~/anaconda3/bin/conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch -y'
```

Note, the argument `-y` is appended to the install command in order to avoid conda prompt.
Wait for several minutes untill the installation is finished.

Then let's do a quick test:

```shell
$ ansible -i servers.txt all -m shell -a '~/anaconda3/bin/python3 -c \'import torch as th; print(th.__version__, "|", th.cuda.device_count())\''

xxx4.wse.jhu.edu | CHANGED | rc=0 >>
1.11.0 | 10
xxx3.wse.jhu.edu | CHANGED | rc=0 >>
1.11.0 | 10
xxx2.wse.jhu.edu | CHANGED | rc=0 >>
1.11.0 | 10
xxx1.wse.jhu.edu | CHANGED | rc=0 >>
1.11.0 | 10
```

## 3.5. Parallel Setup of Homebrew (Linuxbrew)

Since we do not have root access (which is a good thing to some extent as
we have dedicated admins), we are only able to use package managers which
does not require root access, like homebrew. The standard `apt` for
Ubuntu/Debian system is not valid here.

According to homebrew installation guide (https://docs.brew.sh/Installation),
we can do the following steps to install homebrew in parallel:

```shell
ansible -i servers.txt all -m shell -a 'mkdir homebrew; curl -L https://github.com/Homebrew/brew/tarball/master | tar xz --strip 1 -C homebrew'
ansible -i servers.txt all -m shell -a 'echo export PATH="/home/<JHED>/homebrew/bin:\$PATH" >> ~/.bashrc'
ansible -i servers.txt all -m shell -a '~/homebrew/bin/brew --version'  # verify install
```

Here are some handy / optional utilities

```shell
ansible -i servers.txt all -m shell -a '~/homebrew/bin/brew search fish'
ansible -i servers.txt all -m shell -a '~/homebrew/bin/brew install fish'
ansible -i servers.txt all -m shell -a '~/homebrew/bin/brew install fzf'
ansible -i servers.txt all -m shell -a '~/homebrew/bin/brew install ncdu'
ansible -i servers.txt all -m shell -a '~/homebrew/bin/brew install tig'
ansible -i servers.txt all -m shell -a '~/homebrew/bin/brew install ranger'
ansible -i servers.txt all -m shell -a '~/homebrew/bin/brew install sysstat'
ansible -i servers.txt all -m shell -a '~/homebrew/bin/brew install julia'
```

## A. Server List / IP Address.

Please lookup my email. This manual is public, so the domain names or IP
addresses are not supposed to be written here.

## B. Server Architecture Choise

There are two options for a group of GPU servers: (1) form a computer cluster
with job management (e.g. slurm); (2) treat as individual standalone GPU
servers. The two options correspond to completely different server
architectures.

* Slurm cluster has three groups of nodes (a node is a server or virtual server),
namely (1) login node; (2) storage node(s); (3) computation nodes. Users are
blocked from direct access to storage nodes and computation nodes. Only login
node is accessible to users, and jobs are submitted and scheduled through slurm.

* No slurm means each server is treated as standalone server. Login node
is not used here. Storage node (server) is optional. All users have direct
access to all computation resources.

Pros and Cons comparing "use slurm" and "no slurm"

| Index | Aspect | Use Slurm | No Slurm |
| ------| ------ | --------- | -------- |
| 1 | Disk IO | read/write on NFS [1] | native NVME read/write |
| 2 | Access | can only access login node | can access all |
| 3 | max num of GPU we can use | fixed and mandatory [2] | extremely flexible based on communication |
| 4 | job queue | fair FIFO queue | no queue [3] |
| 5 | maintenance | wse IT | wse IT |
| 6 | cost | extra optical networking (cables and routers) | no extra device |
| 7 | learning curve | needs to learn more than basic usage | basic usage |
| 8 | interactive development | interactive debugging not straightforward | straightforward |
| 9 | GPU usage | takes the whole GPU even if GPU util 1% | can manually stack jobs on the same card |

[1] NFS (actually any file system over network) performance is very bad at
random small file read (e.g. imagenet). Disk read will become a significant
performance bottleneck unless files are cached by linux VFS in memory.
In a typical case, NVME drive over NFS could perform worse than HDD in
random small file I/O tasks.

[2] slurm rules are mandatory. For example, even if 50 out of 100 GPUs
are idle, a user can only occupy 10 GPUs according to the quota 10.
When slurm is not used, user can temporarily occupy all the idle GPUs.

[3] when there is no job queue, abusive users could result in mess and
interfere with the others.

## C. Troubleshooting

1. Idle tmux session ends automatically and unexpectedly

This is due to server maintainer team sets an automatic bash timeout `TMOUT=600` at `/etc/profile.d/timeout.sh`.
It means that a bash being idle for 600 seconds will end automatically. And eventually the whole tmux session will end and disappear.
Possible workaround includes (1) start a `sh` at the end of the command in tmux window, e.g. `python3 train.py; sh`

## D. Reference Makefile

```makefile
ping:
        ansible -i ~/servers.txt all -m ping -o \
                -e 'ansible_remote_tmp=/tmp/JHED'

gpustat:
        ansible -i ~/servers.txt all -m shell -a '~/anaconda3/bin/gpustat' \
                -e 'ansible_remote_tmp=/tmp/JHED'

inxi:
        ansible -i ~/servers.txt all -m shell -a '~/bin/inxi' \
                -e 'ansible_remote_tmp=/tmp/JHED'

storage:
        ansible -i servers.txt all -m shell -a 'df -h | grep -P "/home|/data"' \
                -e 'ansible_remote_tmp=/tmp/JHED'
```
