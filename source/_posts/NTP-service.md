---
title: ubuntu 设置 ntp 服务
date: 2017-11-30 23:24:30
categories: 操作系统
tags:
  - linux
---

# ntp 服务方式：
* 编辑 ``/etc/ntp.conf`` 中的 ``pool 10.169.103.58 iburst`` 行，指定需要同步的 IP
* service ntp start

# crontab 方式：

## Windows 启用 NTP 服务端
1. 通过开始菜单，输入 regedit 命令后打开注册表设定画面，此时请一定备份注册表文件。
2. 修改以下选项的键值  HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\TimeProviders\  NtpServer 内的「Enabled」设定为 1，打开 NTP 服务器功能
3. 修改以下键值  HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\Config\  AnnounceFlags 设定为 5, 该设定强制主机将它自身宣布为可靠的时间源，从而使用内置的互补金属氧化物半导体 (CMOS) 时钟。
4. 在 dos 命令行执行以下命令，确保以上修改起作用
net stop w32time
net start w32time

## linux 启动定时循环对时
1. linux 下执行 crontab -e
2. 输入：``*/1 * * * * /usr/sbin/ntpdate 192.168.255.55 > /var/log/cron 2>&1``
注： 2>&1 表示将错误信息也打印至文件
3. 执行 crontab -l 查看是否设置成功
4. service cron restart 重启服务
5. ps -A|grep cron 查看进程
6. tail /var/log/cron 查看对时结果
7. ``apt install sysv-rc-conf`` 安装服务管理工具
8. 关闭 ntp 服务

