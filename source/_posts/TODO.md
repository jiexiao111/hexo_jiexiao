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

## MAC
* 选取苹果菜单 >“系统偏好设置”，然后点按“键盘”。
* 点按“修饰键”按钮。
* 从想要更改的修饰键旁边的弹出式菜单中选取一项操作，然后点按“好”。

# python3 import docx 错误
* pip uninstall docx
* 下载 [python_docx-0.8.6-py2.py3-none-any.whl](http://www.lfd.uci.edu/~gohlke/pythonlibs/)
* pip install python_docx-0.8.6-py2.py3-none-any.whl
