---
layout: default
title: Configure Apache Access Log
parent: Wiki
---

# Configure Apache Access Log
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

- TOC
{:toc}

---

## Configuration

```
vi /etc/apache2/conf/httpd.conf
```

```
# Enable the following modules
LoadModule logio_module modules/mod_logio.so
LoadModule log_config_module modules/mod_log_config.so

# Find LogFormat and add the follwoing line
LogFormat "\%{\%Y/%m/\%d \%T}t.\%{msec_frac}t SIP \%a DIP \%A DPORT \%p PID \%P Time \%D ResponseSize \%B Received \%I / Sent \%O Protocol \%H Method \%m URL \%U\%q Status \%>s" common

# Comment other lines related to logging
```
