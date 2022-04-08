Server Manual
===

Author: 2022, Mo Zhou
License: CC-0

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
the RSA key for authentication.

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
that later.

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

## 2. Server Storage

### 2.1. Storage Area

1. maintenance team: "These servers are not running RAID.
So any data stored on these servers is at risk of sudden irreversible loss."
The NVME disks are simply combined into a large volume group (8TB), which
looks like a RAID0 setup. (a single broken disk could render the whole
storage pool inaccessible).
**Keep it in mind: properly and regularly backup your important data.**

2. maintenance team: "These servers have been configured with two different
storage areas. `/home` should be used minimally. `/data` is a higher performing file system,
and any data that needs to be processed should reside here.
`/home` only has 100GB space (although resizable), so please really don't
put datasets and bulky files here.

### 2.2. Coordination

5. Everyone has write access to /data. I suggest the following layout for
using the public storage area:

```
/data/common : put your bulky dataset here
/data/<JHED> : other files
```

You may want to use symlink between `/home/<JHED>/*` and `/data/<JHED>/*` to
redirect your files. We will follow this convention throughout this document.

## 3. Reference Setup of Deep Learning Environment

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
[1] NVIDIA RTX A6000 | 75'C,  99 % | 45062 / 49140 MB | xxxxx(44599M) gdm(4M)
[2] NVIDIA RTX A6000 | 77'C,  99 % | 45158 / 49140 MB | xxxxx(44695M) gdm(4M)
[3] NVIDIA RTX A6000 | 78'C,  99 % | 45256 / 49140 MB | xxxxx(44793M) gdm(4M)
[4] NVIDIA RTX A6000 | 35'C,   0 % |   460 / 49140 MB | gdm(4M)
[5] NVIDIA RTX A6000 | 32'C,   0 % |   460 / 49140 MB | gdm(4M)
[6] NVIDIA RTX A6000 | 33'C,   0 % |   460 / 49140 MB | gdm(4M)
[7] NVIDIA RTX A6000 | 33'C,   0 % |   460 / 49140 MB | gdm(4M)
[8] NVIDIA RTX A6000 | 32'C,   0 % |   460 / 49140 MB | gdm(4M)
[9] NVIDIA RTX A6000 | 32'C,   0 % |   460 / 49140 MB | gdm(4M)
xxx2.wse.jhu.edu | CHANGED | rc=0 >>
xxx2                 Thu Apr  7 20:53:17 2022  510.47.03
[0] NVIDIA RTX A5000 | 31'C,   0 % |   308 / 24564 MB |
[1] NVIDIA RTX A5000 | 32'C,   0 % |   308 / 24564 MB |
[2] NVIDIA RTX A5000 | 31'C,   0 % |   308 / 24564 MB |
[3] NVIDIA RTX A5000 | 31'C,   0 % |   308 / 24564 MB |
[4] NVIDIA RTX A5000 | 32'C,   0 % |   308 / 24564 MB |
[5] NVIDIA RTX A5000 | 32'C,   0 % |   308 / 24564 MB |
[6] NVIDIA RTX A5000 | 33'C,   0 % |   308 / 24564 MB |
[7] NVIDIA RTX A5000 | 31'C,   0 % |   308 / 24564 MB |
[8] NVIDIA RTX A5000 | 33'C,   0 % |   308 / 24564 MB |
[9] NVIDIA RTX A5000 | 33'C,   0 % |   308 / 24564 MB |
xxx3.wse.jhu.edu | CHANGED | rc=0 >>
xxx3                 Thu Apr  7 20:53:17 2022  510.47.03
[0] NVIDIA RTX A5000 | 31'C,   0 % |   308 / 24564 MB |
[1] NVIDIA RTX A5000 | 32'C,   0 % |   308 / 24564 MB |
[2] NVIDIA RTX A5000 | 31'C,   0 % |   308 / 24564 MB |
[3] NVIDIA RTX A5000 | 31'C,   0 % |   308 / 24564 MB |
[4] NVIDIA RTX A5000 | 32'C,   0 % |   308 / 24564 MB |
[5] NVIDIA RTX A5000 | 31'C,   0 % |   308 / 24564 MB |
[6] NVIDIA RTX A5000 | 32'C,   0 % |   308 / 24564 MB |
[7] NVIDIA RTX A5000 | 31'C,   0 % |   308 / 24564 MB |
[8] NVIDIA RTX A5000 | 32'C,   0 % |   308 / 24564 MB |
[9] NVIDIA RTX A5000 | 34'C,   0 % |   308 / 24564 MB |
xxx1.wse.jhu.edu | CHANGED | rc=0 >>
xxx1                 Thu Apr  7 20:53:18 2022  510.47.03
[0] NVIDIA RTX A6000 | 32'C,   0 % |   460 / 49140 MB | gdm(4M)
[1] NVIDIA RTX A6000 | 35'C,   0 % |   460 / 49140 MB | gdm(4M)
[2] NVIDIA RTX A6000 | 34'C,   0 % |   460 / 49140 MB | gdm(4M)
[3] NVIDIA RTX A6000 | 35'C,   0 % |   460 / 49140 MB | gdm(4M)
[4] NVIDIA RTX A6000 | 35'C,   0 % |   460 / 49140 MB | gdm(4M)
[5] NVIDIA RTX A6000 | 34'C,   0 % |   460 / 49140 MB | gdm(4M)
[6] NVIDIA RTX A6000 | 37'C,   0 % |   460 / 49140 MB | gdm(4M)
[7] NVIDIA RTX A6000 | 34'C,   0 % |   460 / 49140 MB | gdm(4M)
[8] NVIDIA RTX A6000 | 33'C,   0 % |   460 / 49140 MB | gdm(4M)
[9] NVIDIA RTX A6000 | 36'C,   0 % |   460 / 49140 MB | gdm(4M)
```

#### 3.3.2. Other System Status

CPU / Ram status

```
ansible -i servers.txt all -m shell -a 'top -b -n1 | head -n5'
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

Following https://pytorch.org , I personally chooise Pytorch 1.8.2 (LTS)
for example. So I just directly copy that installation command:

```
ansible -i servers.txt all -m shell -a '~/anaconda3/bin/conda install pytorch torchvision torchaudio cudatoolkit=11.1 -c pytorch-lts -c nvidia -y'
```

Note, the argument `-y` is appended to the install command in order to avoid conda prompt.

## A. Server List / Definitions / Misc.

Please lookup my email. This manual is public, so the domain names or IP
addresses are not supposed to be written here. Neither does any information
that may reveal identity.

`wsehelp @jhu.edu` is the best contact point for WSE IT.

driver version: nvidia-smi saying cuda 11.6 means up to 11.6, not must equal 11.6.