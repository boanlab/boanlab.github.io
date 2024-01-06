---
layout: default
title: Reset Docker
parent: Wiki
---

# Reset Docker
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

- TOC
{:toc}

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
