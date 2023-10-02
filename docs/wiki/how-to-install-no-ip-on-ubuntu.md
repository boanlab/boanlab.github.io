---
layout: default
title: How to install No-IP on Ubuntu
parent: Wiki
---

# How to install No-IP on Ubuntu
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

- TOC
{:toc}

---

## How to compile the No-IP Client

- Install build-essential

    ```
    sudo apt-get update
    sudo apt-get -y install build-essential
    ```

- Download and install the No-IP Client

    ```
    cd /usr/local/src/
    sudo wget http://www.noip.com/client/linux/noip-duc-linux.tar.gz
    sudo tar xvfz noip-duc-linux.tar.gz
    cd noip-{xxxx}
    sudo make install
    ```

    ```
    < enter the login information and link this host with a specific domain name >
    ```

## How to configure the No-IP Client

- Create the No-IP daemon

    ```
    sudo vi /etc/systemd/system/noip2.service
    ```

    ```
    [Unit]
    Description=No-Ip Dynamic DNS Update Service
    After=network.target

    [Service]
    Type=forking
    ExecStart=/usr/local/bin/noip2

    [Install]
    WantedBy=multi-user.target
    ```

- Start the No-IP service

    ```
    sudo systemctl daemon-reload
    sudo systemctl enable noip2
    sudo systemctl start noip2
    ```
