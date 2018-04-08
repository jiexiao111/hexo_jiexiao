---
title: 配置 Samba 实现 Linux 与 Windows 共享文件
date: 2018-04-08 10:05:59
categories: 操作系统
tags:
  - linux
---

<!-- 文章开头都用它了，整齐才好看 -->
{% note default %}
如果是 Linux 访问 Windows 共享目录，直接使用 mount 即可，而 Windows 访问 Linux 则需要利用 Samba
{% endnote %}

<!--more-->

---
# 安装与配置
## 安装
```
sudo apt-get install samba
```
## 创建共享目录，并修改权限
```
mkdir /home/gzd/smbshare
// 由于 Windows 下的文件夹需可读可写可执行，需更改权限为 777
sudo chmod 777 /home/gzd/smbshare
```
## 修改配置文件 ``vim /etc/samba/smb.conf``，增加以下内容
```
[share]
path = /aiml/data/DevMind/06.SRC/01.TestCaseBot/02.TestAWBot/AW_Recommand_V2
public = yes
writable = yes
valid users = root
create mask = 0644
force create mode = 0644
directory mask = 0755
force directory mode = 0755
available = yes
```
配置说明
* [share] 表示共享文件夹的别名，之后将直接使用这个别名
* force create mode 与 force directory mode 的设置是因为 Windows 下与 Linux 下文件和文件夹的默认权限不同造成的，Windows 下新建的文件是可执行的，必须强制设定其文件权限。
* valid users 设置为你当前的 Linux 用户名，例如我的是 gzd，因为第一次打开共享文件夹时，需要验证权限。

## 设置登陆密码
```
touch /etc/samba/smbpasswd
smbpasswd -a root
```
## 启动服务
```
/etc/init.d/samba restart
```
# 测试服务
## Linux 测试
安装 smbclient
```
apt-get install smbclient
```
测试
```
smbclient -L //localhost/share
```
命令输出
```
WARNING: The "syslog" option is deprecated
Enter root's password:
Domain=[WORKGROUP] OS=[Windows 6.1] Server=[Samba 4.3.11-Ubuntu]

        Sharename       Type      Comment
        ---------       ----      -------
        print$          Disk      Printer Drivers
        share           Disk
        share_code      Disk
        IPC$            IPC       IPC Service (ubuntu server (Samba, Ubuntu))
Domain=[WORKGROUP] OS=[Windows 6.1] Server=[Samba 4.3.11-Ubuntu]

        Server               Comment
        ---------            -------
        UBUNTU               ubuntu server (Samba, Ubuntu)

        Workgroup            Master
        ---------            -------
        WORKGROUP
```

## Windows 测试
在 Windows 资源管理器中直接输入，即可访问
```
\\10.158.207.212\share
```
