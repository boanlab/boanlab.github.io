---
layout: default
title: Install KubeBuilder
parent: Wiki
---

# Install KubeBuilder
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

- TOC
{:toc}

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