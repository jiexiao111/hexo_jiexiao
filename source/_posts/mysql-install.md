---
title: mysql 安装备忘
date: 2017-11-21 15:17:15
categories: 工具使用
tags:
  - 数据库
---

{% note default %}
做个备忘
{% endnote %}

<!--more-->

---

# 检查 mysql 是否已经安装
```
yum list installed | grep mysql
```

# 删除已经安装的 mysql
```
yum -y remove mysql-libs.x86_64
```

# 添加安装源
```
wget dev.mysql.com/get/mysql-community-release-el6-5.noarch.rpm
yum localinstall mysql-community-release-el6-5.noarch.rpm
yum repolist all | grep mysql
yum-config-manager --disable mysql55-community
yum-config-manager --disable mysql56-community
yum-config-manager --enable mysql57-community-dmr
yum repolist enabled | grep mysql
```

# 安装
```
yum install mysql-community-server
```

# 启动
```
service mysqld start
```

# 自启动
```
chkconfig --list | grep mysqld
chkconfig mysqld on
```

# 安装 mysqlclient
```
yum install python-devel mysql-devel
pip install mysqlclient
```

# 参考
[CentOS 6.5/6.6 安装（install）mysql 5.7 最完整版教程](https://segmentfault.com/a/1190000003049498)
[mysqlclient 的 github 地址](https://github.com/PyMySQL/mysqlclient-python)
