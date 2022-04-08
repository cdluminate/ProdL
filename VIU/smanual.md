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

### 1.1.3. Basic SSH Connection

You need `openssh` client in order to access these machines. We may request
for the VNC access in the future in case you need it. Simply use the ssh
client to login:

```shell
ssh -v <JHED>@<server>
```

The password is the same as your JHED account. So the SSH authentication
was setup with LDAP.

### 1.1.4. SSH Connextion w/ RSA Key

Google `ssh-keygen` and create a keypair for ssh access. This step can be
skipped if you want to use existing keypairs. Let's assume now we have
a keypair (private key at `~/.ssh/id_rsa`, public key at `~/.ssh/id_rsa.pub`).

Then copy the public key, login into every server with password and configure
the remote:

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

## 2. Go through Basic Deep Learning Setup

```shell
ansible -i servers.txt all -m shell -a 'wget -c https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-x86_64.sh'
```

## A. Server List / Definitions / Misc.

Please lookup my email. This manual is public, so the domain names or IP
addresses are not supposed to be written here. Neither does any information
that may reveal identity.

`wsehelp @jhu.edu` is the best contact point for WSE IT.
