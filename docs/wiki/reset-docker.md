---
title: Reset Docker
author: Jaehyun Nam
date: 2022-07-19
category: default
layout: post
---

## Reset Docker

```
docker rm -f `docker ps -aq`
docker volume rm -f `docker volume ls -q`
docker network rm -f `docker network ls -q`
```

```
sudo systemctl stop docker
```

```
sudo umount /var/lib/docker/volumes
sudo rm -rf /var/lib/docker
```

```
sudo systemctl start docker
```
