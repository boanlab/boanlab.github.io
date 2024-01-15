---
title: Install L2TP over IPSec
author: Jaehyun Nam
date: 2022-07-18
category: default
layout: post
---

## Installation

```
sudo apt-get update
sudo apt-get -y install strongswan xl2tpd
```

## Configuration

```
sudo vi /etc/ipsec.conf
```

```
config setup

conn %default
    ikelifetime=60m
    keylife=20m
    rekeymargin=3m
    keyingtries=1
    keyexchange=ikev1
    authby=secret
    ike=aes128-sha1-modp1024,3des-sha1-modp1024!
    esp=aes128-sha1-modp1024,3des-sha1-modp1024!

conn L2TP-PSK
    keyexchange=ikev1
    left=%defaultroute
    auto=add
    authby=secret
    type=transport
    leftprotoport=17/1701
    rightprotoport=17/1701
    # set this to the ip address of your vpn server
    right=[VPN Server IP Address]
```

```
sudo vi /etc/ipsec.secrets
```

```
: PSK "your_pre_shared_key"
```

```
sudo vi /etc/xl2tpd/xl2tpd.conf
```

```
[lac myVPN]
lns = [VPN Server IP Address]
ppp debug = yes
pppoptfile = /etc/ppp/options.l2tpd.client
length bit = yes
```

```
sudo vi /etc/ppp/options.l2tpd.client
```

```
ipcp-accept-local
ipcp-accept-remote
refuse-eap
require-mschap-v2
noccp
noauth
logfile /var/log/xl2tpd.log
idle 1800
mtu 1410
mru 1410
defaultroute
usepeerdns
debug
connect-delay 5000
name your_user_name
password your_password
```

```
sudo mkdir -p /var/run/xl2tpd
sudo touch /var/run/xl2tpd/l2tp-control
sudo service strongswan restart
sudo service xl2tpd restart
sudo service ipsec restart
```

## Connection

```
ipsec up L2TP-PSK
sudo bash -c 'echo "c myVPN" > /var/run/xl2tpd/l2tp-control'
sleep 10
ip a
```

## Routing

```
sudo ip route add [specific IP address to connect via VPN] via $(ip address show dev ppp0 | grep -Po '(?<=peer )(\b([0-9]{1,3}\.){3}[0-9]{1,3}\b)') dev ppp0
```

## Disconnection

```
sudo bash -c 'echo "d myVPN" > /var/run/xl2tpd/l2tp-control'
ipsec down L2TP-PSK
```

## Debugging

```
dmesg
less /var/log/xl2tpd.log
```

