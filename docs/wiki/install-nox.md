---
title: Install NOX
author: Jaehyun Nam
date: 2022-07-18
category: default
layout: post
---

## Test Environment

```
# Tested on Ubuntu 14.04
# Requirement: gcc-4.6 and g++-4.6
```

## How to install NOX

```
cd ~
wget https://boanlab.com/downloads/sdn/nox.tar.gz
tar xvfz nox.tar.gz
```

```
mv nox/run_nox.sh ~
sudo apt-get -y install gcc-4.6 g++-4.6 autoconf
sudo mv /usr/bin/gcc /usr/bin/gcc.bak
sudo ln -s /usr/bin/gcc-4.6 /usr/bin/gcc
sudo mv /usr/bin/g++ /usr/bin/g++.bak
sudo ln -s /usr/bin/g++-4.6 /usr/bin/g++
```

```
sudo apt-get -y install python-dev libtbb-dev libssl-dev libtool twisted* libbz2-dev libicu-dev
```

```
cd ~/nox/boost-1.46.1/boost_1_46_1
./bootstrap.sh --exec-prefix=/usr/local
./bjam
sudo ./bjam install
sudo ldconfig
```

```
cd ~/nox/nox
./boot.sh
mkdir build
cd build
../configure
make
```

