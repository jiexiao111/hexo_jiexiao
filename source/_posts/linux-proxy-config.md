---
title: Linux 下代理配置
date: 2018-01-02 10:32:53
categories: 操作系统
tags:
  - linux
---

<!-- 文章开头都用它了，整齐才好看 -->
{% note default %}
经常会用到一些代理配置，这里做个汇总
{% endnote %}

<!--more-->

---

# wget
```
cat > ~/.wgetrc
# For example ftp_proxy, ftp-proxy and ftpproxy are the same.
https_proxy = http://USERNAME:PASSWD@URL:PORT
http_proxy = http://USERNAME:PASSWD@URL:PORT
ftp_proxy = http://USERNAME:PASSWD@URL:PORT
# If you do not want to use proxy at all, set this to off.
use_proxy = on
```

# curl
```
cat > ~/.curlrc
--proxy http://USERNAME:PASSWD@URL:PORT
```

# global
```
cat > /home/proxy.sh
# http 配置
ftp_proxy=http://USERNAME:PASSWD@URL:PORT
export ftp_proxy
https_proxy=http://USERNAME:PASSWD@URL:PORT
export https_proxy
http_proxy=http://USERNAME:PASSWD@URL:PORT
export http_proxy
```

# git
```
# git 配置
git config --global http.proxy http://china\\\USERNAME:PASSWD@URL:PORT
git config --global https.proxy https://china\\\USERNAME:PASSWD@URL:PORT
```

# pip
```
pip3 --proxy=http://USERNAME:PASSWD@URL:PORT install tensorflow
```
```
$ cat ~/.pip/pip.conf
[global]
trusted-host = mirrors.aliyun.com
index-url = http://mirrors.aliyun.com/pypi/simple
proxy = http://USERNAME:PASSWD@proxyhk.huawei.com:8080
```

# conda
```
$ cat ~/.condarc
channels:
- defaults

# Show channel URLs when displaying what is going to be downloaded and
# in 'conda list'. The default is False.
show_channel_urls: True
allow_other_channels: True

proxy_servers:
    http: http://USERNAME:PASSWD@URL:PORT
    https: http://USERNAME:PASSWD@URL:PORT

ssl_verify: False
```

# apt-get
```
$ cat /etc/apt/apt.conf
Acquire::http::Proxy "http://USERNAME:PASSWD@URL:PORT";
Acquire::https::Proxy "http://USERNAME:PASSWD@URL:PORT";
```

# yum
```
cat /etc/yum.conf
proxy=http://URL:PORT
proxy_username=USERNAME
proxy_password=PASSWD
```
