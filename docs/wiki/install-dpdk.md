---
title: Install DPDK
author: Jaehyun Nam
date: 2022-07-18
category: default
layout: post
---

## Test Environment

```
# Tested on Ubuntu 16.04
```

## How to install DPDK

- Check if DPDK is supported

    ```
    sudo ethtool -i [NIC]
    (http://dpdk.org/doc/nics)
    ```

- Configure CPU and memory

    ```
    sudo vi /etc/default/grub
    ```

    ```
    GRUB_CMDLINE_LINUX_DEFAULT="default_hugepagesz=1G hugepagesz=1G hugepages=4" (1GB huge page setup)
    GRUB_CMDLINE_LINUX_DEFAULT="default_hugepagesz=2M hugepagesz=2M hugepages=2048" (2MB huge page setup)
    ```

    ```
    sudo update-grub
    ```

    ```
    echo 'vm.nr_hugepages=4' >> /etc/sysctl.conf (1GB huge page setup)
    echo 'vm.nr_hugepages=2048' >> /etc/sysctl.conf (2MB huge page setup)
    ```

    ```
    sudo reboot
    ```

    ```
    grep -i huge /proc/meminfo
    ```

- Install DPDK

    ```
    echo "export DPDK_DIR=/usr/src/dpdk-stable-17.11.3" >> ~/.bashrc
    echo "export DPDK_TARGET=x86_64-native-linuxapp-gcc" >> ~/.bashrc
    echo "export DPDK_BUILD=\$DPDK_DIR/\$DPDK_TARGET" >> ~/.bashrc
    . ~/.bashrc
    ```

    ```
    sudo apt-get install -y make coreutils gcc-multilib python libnuma-dev
    curl -LO http://fast.dpdk.org/rel/dpdk-17.11.3.tar.xz
    sudo tar xvfJ dpdk-17.11.3.tar.xz -C /usr/src/
    ```

    ```
    # install DPDK either manually
    cd $DPDK_DIR
    sudo make install T=$DPDK_TARGET DESTDIR=install
    ```

    ```
    # or using a DPDK-setup script
    cd $DPDK_DIR/usertools
    sudo ./dpdk-setup.sh
    ```

    ```
    sudo reboot
    ```

