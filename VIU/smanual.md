VIU Server Manual
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

## 2. Go through Basic Deep Learning Setup

ansible -i viu.txt all -m shell -a 'wget -c https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-x86_64.sh'

## A. Server List

Lookup my email please. This manual is public and the domain names or IP
addresses are not supposed to be written here.
