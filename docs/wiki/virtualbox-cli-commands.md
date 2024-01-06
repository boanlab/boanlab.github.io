---
layout: default
title: Virtualbox CLI Commands
parent: Wiki
---

# Virtualbox CLI Commands
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

- TOC
{:toc}

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