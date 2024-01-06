---
layout: default
title: Install Owncloud
parent: Wiki
---

# Install Owncloud
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

- TOC
{:toc}

---

## Install APM

```
sudo apt-get -y install lamp-server^
sudo apt-get -y install php5-gd php-xml-parser php5-intl smbclient curl libcurl3 php5-curl
```

```
sudo a2enmod rewrite
sudo a2enmod headers
```

```
sudo vi /etc/apache2/sites-default
```

```
AllowOverride None -> AllowOverride All
```

```
sudo service apache2 restart
```

## Install OwnCloud

```
wget http://download.owncloud.org/community/owncloud-latest.tar.bz2
sudo tar -xjf owncloud-latest.tar.bz2 -C /var/www/html
```

```
cd /var/www/html
sudo chown -R www-data:www-data owncloud
sudo find . -type d -exec chmod 755 {} \;
sudo find . -type f -exec chmod 644 {} \;
```

```
mysql -u root -p
```

```
mysql> CREATE DATABASE owncloud;
mysql> GRANT ALL ON owncloud.* TO 'owncloud'@'localhost' IDENTIFIED BY 'some_password';
```