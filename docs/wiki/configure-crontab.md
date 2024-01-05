---
title: Configure Crontab
author: Jaehyun Nam
date: 2022-07-19
category: default
layout: post
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