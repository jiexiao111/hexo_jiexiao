---
title: TODO
date: 2017-10-14 10:30:44
tags:
---

{% note default %}
一些来不及整理的内容先保存在这里
{% endnote %}

<!--more-->

---

# 多版本切换 anaconda
[http://www.jianshu.com/p/d2e15200ee9b]
```
# 显示可用的 python 环境
conda info --envs
# 激活 python 环境
source activate py2
```

# 学习 git
以下文件包含 git 常用命令的缩写
```
~/.oh-my-zsh/plugins/git
```

# 解决 zsh 和 tmux 下，vim 配色显示不一致
编辑~/.zshrc:
``alias tmux="TERM=screen-256color-bce tmux"``
编辑 ~/.tmux.conf:
``set -g default-terminal "xterm"``
参考 [https://stackoverflow.com/questions/10158508/lose-vim-colorscheme-in-tmux-mode]

# 修改 CapsLock 为 Ctrl
## Win7
* 点击 Win+R 键

* 在输入框键入 regedit，打开注册表

* 进入 HKEY_LOCAL_MACHINE -> System -> CurrentControlSet -> Control -> KeyBoard Layout。记住，一定是 keyBoard Layout，而不是 KeyBoard Layouts

* 右键菜单，然后选择 New -> Binary value

* 重命名 New Value #1 -> Scancode Map

* 右键菜单 Scancode Map -> Modify

输入如下值，保存

0000 00 00 00 00 00 00 00 00
0008 03 00 00 00 1D 00 3A 00
0010 3A 00 1D 00 00 00 00 00
0018

前两行和最后一行，都是固定的，全部为 0。第三行，表示你修改了几个键，其实我们只是改了两个键，不过最后那一行也要算进去，所以是 3。
重点是在第四行和第五行。3A00，代表 Caps Lock， 1D00，代表 Ctrl。这一行，意思即为，将 Caps Lock 映射为 Ctrl
第五行，就不用说了，意思刚好相反。
修改完毕后，重新登录 Windows 即可生效！
下面附上各个键位值的参考：

```
Escape 01 00
Tab 0F 00
Caps Lock 3A 00
Left Alt 38 00
Left Ctrl 1D 00
Left Shift 2A 00
Left Windows 5B E0
Right Alt 38 E0
Right Ctr l1D E0
Right Shift 36 00
Right Windows 5C E0
Backspace 0E 00
Delete 53 E0
Enter 1C 00
Space 39 00
Insert 52 E0
HOME 47 E0
End 4F E0
Num Lock 45 00
Page Down 51 E0
Page Up 49 E0
Scroll Lock 46 00
```

## MAC
* 选取苹果菜单 >“系统偏好设置”，然后点按“键盘”。
* 点按“修饰键”按钮。
* 从想要更改的修饰键旁边的弹出式菜单中选取一项操作，然后点按“好”。

# python3 import docx 错误
* pip uninstall docx
* 下载 [python_docx-0.8.6-py2.py3-none-any.whl](http://www.lfd.uci.edu/~gohlke/pythonlibs/)
* pip install python_docx-0.8.6-py2.py3-none-any.whl

# ubuntu 设置 ntp 服务器
## ntp 服务方式：
* 编辑 ``/etc/ntp.conf`` 中的 ``pool 10.169.103.58 iburst`` 行，指定需要同步的 IP
* service ntp start

## crontab 方式：
1. 通过开始菜单，输入 regedit 命令后打开注册表设定画面，此时请一定备份注册表文件。
2. 修改以下选项的键值  HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\TimeProviders\  NtpServer 内的「Enabled」设定为 1，打开 NTP 服务器功能
3. 修改以下键值  HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\Config\  AnnounceFlags 设定为 5, 该设定强制主机将它自身宣布为可靠的时间源，从而使用内置的互补金属氧化物半导体 (CMOS) 时钟。
4. 在 dos 命令行执行以下命令，确保以上修改起作用
net stop w32time
net start w32time
5. linux 下执行 crontab -e
6. 输入：``*/1 * * * * /usr/sbin/ntpdate 192.168.255.55 > /var/log/cron 2>&1``
注： 2>&1 表示将错误信息也打印至文件
7. 执行 crontab -l 查看是否设置成功
8. service cron restart 重启服务
9. ps -A|grep cron 查看进程
10. tail /var/log/cron 查看对时结果
11. ``apt install sysv-rc-conf`` 安装服务管理工具
12. 关闭 ntp 服务

# python 性能分析
(http://python.jobbole.com/87621/)

# ubunt 无法 mount 文件
apt-get install -y cifs-utils

# 机器学习教程
[斯坦福大学 CS231n 卷积神经网络与图像识别](http://cs231n.stanford.edu/)
[吴恩达 Deep Learning Specialization](https://www.coursera.org/specializations/deep-learning)
[Udacity 免费深度学习课程](https://www.udacity.com/course/deep-learning—ud730)
[Geoffrey Hinton 的 Neural Networks For Machine Learning](https://www.coursera.org/learn/neural-networks)
[斯坦福大学 CS224d 自然语言处理深度学习](http://cs224d.stanford.edu/)
[Ian Goodfellow 的 DeepLearning 书籍](https://exacity.github.io/deeplearningbook-chinese/)
[良心 GitHub 项目：各种机器学习任务的顶级结果（论文）汇总）](https://github.com//RedditSota/state-of-the-art-result-for-machine-learning-problems)

# apt-get 非正常退出后，出现 dpkg –configure -a 时，暴力解决
rm /var/lib/dpkg/updates/*

# latex
如果你只用 latex 画图的话，可以只看 pgfmanual 这个宏包就行了，安装完 texlive，文档都会一起安装了
[安装](https://liam0205.me/texlive/)
[在线体验](https://www.sharelatex.com/project)
《102 分钟学会 latex》


[「 Neural Networks and Deep Learning 」中文翻译（连载完毕）](https://hit-scir.gitbooks.io/neural-networks-and-deep-learning-zh_cn/content/)
