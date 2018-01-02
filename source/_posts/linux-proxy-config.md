---
title: linux_proxy_config
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
