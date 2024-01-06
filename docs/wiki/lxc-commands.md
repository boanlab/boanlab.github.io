---
layout: default
title: LXC Commands
parent: Wiki
---

# LXC Commands
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

- TOC
{:toc}

---

## LXC Commands

- create a container

```
sudo lxc-create -n [NAME] -t ubuntu
```

- start a container

```
sudo lxc-start -n [NAME] -d
```

- stop a container

```
sudo lxc-stop -n [NAME]
```

- remove a container

```
sudo lxc-destroy -n [NAME]
```

- show the list of containers

```
sudo lxc-ls --fancy
```

- edit the configuration of a container

```
sudo vi /var/lib/lxc/[NAME]/config
```

```
# general configuration
lxc.start.auto = 1
lxc.start.delay = 5

# network configuration
lxc.network.type = veth
lxc.network.flags = up
lxc.network.link = br0
lxc.network.hwaddr = 00:00:00:00:00:00
lxc.network.ipv4 = [IP address]/[CIDR]
```