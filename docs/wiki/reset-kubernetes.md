---
layout: default
title: Reset Kubernetes
parent: Wiki
---

# Reset Kubernetes
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

- TOC
{:toc}

---

## Reset Kubernetes

```
kubeadm reset
```

```
sudo systemctl stop kubelet
sudo systemctl stop docker
```

```
sudo rm -rf $HOME/.kube
sudo rm -rf /etc/cni
sudo rm -rf /var/lib/cni
sudo rm -rf /var/lib/etcd
sudo rm -rf /var/lib/kubelet/*
```

```
sudo systemctl start docker
sudo systemctl start kubelet
```
