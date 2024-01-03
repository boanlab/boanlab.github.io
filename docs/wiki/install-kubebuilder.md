---
title: Install KubeBuilder
author: Jaehyun Nam
date: 2022-07-19
category: default
layout: post
---

## Install KubeBuilder

- Download KubeBuilder and extract it to tmp

```
curl -L https://go.kubebuilder.io/dl/2.3.1/$(go env GOOS)/$(go env GOARCH) | tar -xz -C /tmp/
sudo mv /tmp/kubebuilder_2.3.1_$(go env GOOS)_$(go env GOARCH) /usr/local/kubebuilder
```

- Add KubeBuilder into PATH

```
echo 'export PATH=$PATH:/usr/local/kubebuilder/bin' >> ~/.bashrc
. ~/.bashrc
```