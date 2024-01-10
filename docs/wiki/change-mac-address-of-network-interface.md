---
layout: default
title: Change MAC address of Network Interface
parent: Wiki
---

# Change MAC address of Network Interface
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

- TOC
{:toc}

---

## Commands

```
vi /etc/udev/rules.d/75-mac-spoof.rules
```

```
ACTION=="add", SUBSYSTEM=="net", ATTR{address}=="XX:XX:XX:XX:XX:XX", RUN+="/usr/bin/ip link set dev %k address YY:YY:YY:YY:YY:YY"
```
