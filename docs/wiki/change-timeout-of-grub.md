---
layout: default
title: Change Timeout of Grub
parent: Wiki
---

# Configure Crontab

{: .no_toc }

## Table of contents

{: .no_toc .text-delta }

- TOC
  {:toc}

---

## Configuration

```
sudo vi /boot/grub/grub.cfg
```

```
replace "set timeout=x" to "set timeout=y"

x = the original value
y = the value that you want to set
```
