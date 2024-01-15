---
title: Install ONOS
author: Jaehyun Nam
date: 2022-07-18
category: default
layout: post
---

## Test Environment

```
# Tested on Ubuntu 18.04
# CPU: 8, Memory: 8GB
```

## How to install ONOS

```
wget -P /tmp/ https://boanlab.com/downloads/jdk/jdk-8u202-linux-x64.tar.gz
```

```
sudo mkdir -p /usr/lib/java
sudo tar xvfz /tmp/jdk-8u202-linux-x64.tar.gz -C /usr/lib/java/
```

```
echo "PATH=$PATH:/usr/lib/java/jdk1.8.0_202/bin" | sudo tee -a /etc/environment
echo "JAVA_HOME=/usr/lib/java/jdk1.8.0_202/" | sudo tee -a /etc/environment
echo "JRE_HOME=/usr/lib/java/jdk1.8.0_202/jre" | sudo tee -a /etc/environment
```

```
. /etc/environment
. ~/.bashrc
```

```
sudo update-alternatives --install "/usr/bin/java" "java" "/usr/lib/java/jdk1.8.0_202/bin/java" 1
sudo update-alternatives --install "/usr/bin/javac" "javac" "/usr/lib/java/jdk1.8.0_202/bin/javac" 1
sudo update-alternatives --install "/usr/bin/javaws" "javaws" "/usr/lib/java/jdk1.8.0_202/bin/javaws" 1
```

```
sudo apt-get update
sudo apt-get -y install git zip unzip curl python
```

```
echo "deb [arch=amd64] https://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list
curl https://bazel.build/bazel-release.pub.gpg | sudo apt-key add -
```

```
sudo apt-get update
sudo apt-get -y install bazel bazel-1.2.1
```

```
cd ~
git clone -b onos-1.15 https://github.com/opennetworkinglab/onos
```

```
cat << EOF >> ~/.bashrc
export ONOS_ROOT="$(pwd)/onos"
source \$ONOS_ROOT/tools/dev/bash_profile
EOF
```

```
. ~/.bashrc
```

```
cd ~/onos
bazel build onos
```

