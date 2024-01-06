---
layout: default
title: Configure Crontab
parent: Wiki
---

# Configure Crontab
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

- TOC
{:toc}

---

## Configure Crontab

```
sudo crontab -e
```

```
[Minute] [Hour] [Day] [Month] [Day_of_week] [Command]
(Sunday: 0, Monday: 1, Tuesday: 2, Wednesday: 3, Thursday: 4, Friday: 5, Saturday: 6)
```

```
The path in [Command] must be an absolute path.
```