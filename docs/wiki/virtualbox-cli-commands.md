---
title: VirtualBox CLI Commands
author: Jaehyun Nam
date: 2022-07-18
category: default
layout: post
---

## Commands

```
vboxmanage list vms
vboxmanage list runningvms

vboxmanage startvm [VM name]
vboxmanage controlvm [VM name] poweroff
vboxmanage controlvm [VM name] acpipowerbutton

vboxmanage unregistervm [VM name] --delete
```