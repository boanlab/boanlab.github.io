---
layout: default
title: Change Permissions for Wordpress
parent: Wiki
---

# Configure Crontab

{: .no_toc }

## Table of contents

{: .no_toc .text-delta }

- TOC
  {:toc}

---

## How to change permissions for WordPress

```
sudo chown -R www-data:www-data wp-content
```

```
sudo find . -type d -exec chmod 755 {} \;
sudo find . -type f -exec chmod 644 {} \;
```
