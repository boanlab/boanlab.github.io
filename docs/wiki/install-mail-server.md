---
title: Install Mail Server (iRedMail)
author: Jaehyun Nam
date: 2022-07-18
category: default
layout: post
---

## How to set up iRedMail

- Configure Hostname

```
hostnamectl set-hostname mail.example.com
vi /etc/hosts
```

```
127.0.0.1 mail.example.com mail
```

- Download iRedMail package

```
wget https://github.com/iredmail/iRedMail/archive/1.4.0.tar.gz
```

- Install iRedMail on Ubuntu

```
tar xvfz 1.4.0.tar.gz
cd iRedMail-1.4.0
chmod +x iRedMail.sh
sudo ./iRedMail.sh
```

```
[ Welcome and thanks for your use ] -> 
[ Default mail storage path ] ->  (if you need, you can change the path)
[ Preferred web server ] -> Nginx 
[ Choose preferred backend used to store mail accounts ] -> PostgresSQL 
[ Your first mail domain name ] -> mail.example.com  (change it to yours)
[ Password for the mail domain administrator ] -> PASSWORD 
[ Optional components ] -> SOGo, netdata, iRedAdmin, Fail2ban 

Continue? [y|N] y

< Question > ... with SSHD ports: xx. [Y|n]
```

```
sudo reboot
```

- Install SSL certificate

```
sudo cp [public key, fullchain.pem] /etc/ssl/certs/iRedMail.crt
sudo cp [private key, privkey.pem] /etc/ssl/private/iRedMail.key
```

```
sudo reboot
```

- Access iRedMail Admin panel

```
https://mail.example.com/iredadmin/

postmaster@mail.example.com
PASSWORD

[Login]

...
```

- Access iRedMail webmail

```
# Common
https://mail.example.com
# RoundCube
https://mail.example.com/mail/
# SOGo
https://mail.example.com/SOGo
```

