---
layout: default
title: Add New disk on Linux
parent: Wiki
---

# Add New disk on Linux
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

- TOC
{:toc}

---

## Configuration

- Make a new partition

```
sudo fdisk /dev/sdb (new disk device descriptor)
```

```
Command (m for help): d (first, remove the previous partition if it exists)
Command (m for help): n (then, create a new one)
Command action

e extended
p primary partition
=> p (set the new partition as a primary partition)

Partition number (1-4):
... (use default values) ...
Command (m for help): w (write the change on the disk)
```

- Format the new partition

```
sudo mkfs.ext4 /dev/sdb1 (new partition device descriptor)
```

- Get the UUID of the new partition

```
sudo blkid
```

```
(Write down the UUID of the new partition on your note)
```

- Edit the fstab configuration file

```
sudo vi /etc/fstab
```

```
Add the following line
UUID="the UUID of the new disk" [mount location] defaults 0 1
(See fstab man page for a description of all options)
```

- Reboot

```
sudo reboot
```
