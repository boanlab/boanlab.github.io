---
title: Install Operator-SDK
author: Jaehyun Nam
date: 2022-07-19
category: default
layout: post
---

## Install Operator-SDK

```
RELEASE_VERSION=v1.0.0
curl -OJL https://github.com/operator-framework/operator-sdk/releases/download/${RELEASE_VERSION}/operator-sdk-${RELEASE_VERSION}-x86_64-linux-gnu
chmod +x operator-sdk-${RELEASE_VERSION}-x86_64-linux-gnu
sudo mv operator-sdk-${RELEASE_VERSION}-x86_64-linux-gnu /usr/local/bin/operator-sdk
```