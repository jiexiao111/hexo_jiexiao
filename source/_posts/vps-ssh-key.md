---
title: 通过密钥进行 ssh 连接
date: 2017-12-29 22:57:50
categories: 操作系统
tags:
  - linux
---

<!-- 文章开头都用它了，整齐才好看 -->
{% note default %}
每次连接 vps 都需要一个超长的密码，很不方便，所以考虑通过秘钥连接
{% endnote %}

<!--more-->

---
# 生成秘钥
命令：
```
ssh-keygen -t rsa
```
执行过程如下：
```
$ ssh-keygen -t rsa

Generating public/private rsa key pair.
Enter file in which to save the key (/Users/jiexiao/.ssh/id_rsa): # 默认路径直接回车
/Users/jiexiao/.ssh/id_rsa already exists.
Overwrite (y/n)? y
Enter passphrase (empty for no passphrase): # 这里直接回车，否则登录时还需要输入密码
Enter same passphrase again:
Your identification has been saved in /Users/jiexiao/.ssh/id_rsa.
Your public key has been saved in /Users/jiexiao/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:NPT4fMqObmmFfnjIl0Ea+icJh56hLFhmSzqM1mfo+Bc jiexiao@MAC
The key's randomart image is:
+---[RSA 2048]----+
|        .        |
|       . o       |
|        + .      |
|       ..+.      |
|       oS=o .    |
|  =  E= +.oo     |
|oB.o.o.O *oo     |
|=o+oo+o %o*      |
|.oo++  +o*.      |
+----[SHA256]-----+
```

# 上传秘钥
命令：
```
ssh-copy-id -i ~/.ssh/id_rsa.pub root@45.32.90.198
```
执行过程如下：
```
$ ssh-copy-id -i ~/.ssh/id_rsa.pub root@45.32.90.198 # 注意 45.32.90.198 应该是目标主机的 IP
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/Users/jiexiao/.ssh/id_rsa.pub"
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
root@45.32.90.198's password: # 输入密码

Number of key(s) added:        1

Now try logging into the machine, with:   "ssh 'root@45.32.90.198'"
and check to make sure that only the key(s) you wanted were added.
```

# 连接验证
执行过程如下，可以看出登录不需要密码了
```
$ ssh root@45.32.90.198
Welcome to Ubuntu 17.10 (GNU/Linux 4.13.0-16-generic x86_64)
```

# 配置只允许通过秘钥登录
命令：
```
sed -i "s/#PasswordAuthentication yes/PasswordAuthentication no/g" /etc/ssh/sshd_config
sed -i "s/#PubkeyAuthentication yes/PubkeyAuthentication yes/g" /etc/ssh/sshd_config
service sshd restart
```

# 参考
[vultr 官方帮助网页](https://www.vultr.com/docs/how-do-i-generate-ssh-keys/)
[ssh 通过密钥进行连接](https://www.cnblogs.com/zydev/p/5779927.html)
