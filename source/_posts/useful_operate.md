---
title: 常用操作汇总
date: 2017-11-11 11:11:11
categories: 工具使用
tags:
  - 汇总
---

{% note default %}
汇总一些琐碎的，非快捷键的操作，当某个工具的操作过多时再独立为一篇博客
{% endnote %}

<!--more-->

---

# mac
## 窗口切换
原生的 MAC 窗口切换简直无法直视，最简单的一点，多个 Chrome 窗口都无法切换，于是找到两款不错的工具
``snap``: 实现 ``Command + num`` 打开 Dock
``HyperSwitch``: 实现 ``Command + ` `` 切换同一个进程的多个窗口

## 命令结果粘贴至剪切板
``ls |pbcopy``

# jupyter
## .ipynb 转 .md
```shell
jupyter nbconvert --to markdown README.ipynb
```

## 生成 jupyter 配置文件
```shell
jupyter notebook --generate --allow-root
```

## 生成 ipython 配置文件
```
ipython profile create
```
## jupyter 取消密码

* 编辑 /root/.jupyter/jupyter_notebook_config.py，然后重启 jupyter
```shell
c.NotebookApp.token = '';
```
## 主题设置
jt -t grade3 -fs 11 -nfs 12 -tfs 12 -tf sourcesans -nf sourcesans -cellw 88% -altp -f source

## 显示多行结果
* 修改前
```python
line1 = "this is from line 1"
line2 = "this is from line 2"

line1
line2
```
    'this is from line 2'
* 修改永久生效，编辑.ipython/profile_default/ipython_config.py，然后重启 jupyter
```python
ipython profile create # 如果没有默认配置文件， 则生成一个新的
c.InteractiveShell.ast_node_interactivity = 'all'
```
* 修改临时生效
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
```
* 修改后
```python
line1 = "this is from line 1"
line2 = "this is from line 2"

line1
line2
```
    'this is from line 1'
    'this is from line 2'
---

# chrome
## 分析网页加载速度
* 在 chrome 流量器中按 F12 或者单击鼠标右键 ->检查，打开调试栏 ->Network, 刷新网页就可以看到以下信息了
{% img  '/images/chrome_perf.png' %}
-
---

# vim
## vim 粘贴格式错误
最方便的方法就是在.vimrc 中加一句：
set pastetoggle=<F9>
以后在插入模式下，只要按 F9 键就可以切换自动缩进。

## 无法 undo
* 如果文件名中包含中文，则无法 undo

## 保存折叠
.vimrc 添加以下
```shell
au BufWinLeave *.* mkview
au BufWinEnter *.* silent loadview
```

## 文本替换

### 替换当前行中的内容

* 替换第一个匹配项：``:s/from/to/``
* 替换所有匹配项：``:s/from/to/g``
* 替换所有匹配项，替换前需确认：``:s/from/to/gc``

``注意：这里的 from 和 to 都可以是任何字符串，其中 from 还可以是正则表达式``

### 替换某一行的内容

* 当前行：``:.s/from/to/g``
* 第 33 行：``33s/from/to/g``
* 最后一行：``:$s/from/to/g``

### 替换某些行的内容

* [10 行，20 行』:                 ``:10,20s/from/to/g``
* [1 行，最后一行』:              ``:1,$s/from/to/g``
* [1 行，当前行』:                ``:1,.s/from/to/g``
* 『当前行，最后一行』:           ``:.,$s/from/to/g``
* 『标记 a 所在行，标记 b 所在行』:   ``:'a,'bs/from/to/g``
* 所有行：``:%s/from/to/g``

### 特殊情况
* 替换空格为换行符 ``:s/ /\r/g``

### 替换命令的完整形式
完整语法：``:[range]s/from/to/[flags]``
* ``s/from/to/``  表示 from 替换成 to, from 可以是正则表达式：
* ``[range]`` 可以为：
    * 光标所在的行：``不写 range``
    * 光标所在的行：``.``
    * 所有行：``%``
    * 第一行：``1``
    * 最后一行：``$``
    * 第 33 行：``33``
    * 标记 a 所在的行：``'a``
    * 光标所在行的下一行：``.+1``
    * 光标所在行的上一行：``$-1``
    * 第 22 ~ 33 行：``22,33``
    * 第 1 行 ~ 最后一行：``1,$``
    * 第 1 行 到 当前行：``1,.``
    * 当前行 到 最后一行：``.,$``
    * 标记 a 所在的行 到 标记 b 所在的行：``'a,'b``
    * 从当前位置向上搜索，找到的第一个 chapter 所在的行：``?chapter?``
    * 从当前位置向下搜索，找到的第一个 chapter 所在的行：``/chapter/``
    ``注意，上面的所有用于 range 的表示方法都可以通过 +、- 操作来设置相对偏移量``
* ``[flags]`` 可以为：
    * 替换第一个：``无``
    * 替换所有：``g``
    * 要求确认：``c``
    * 忽略错误：``e``
    ``注意：上面的所有 flags 都可以组合起来使用，比如 gc 表示对指定范围内的所有匹配项进行替换，并且在每一次替换之前都会请用户确认``

## 插入命令输出
```
:r !command
```

## 内容排序
选中需要排序的文本，执行 ``:sort``

```
:sort!  对全文逆序排列
:sort u 对全文排序并去除重复行
:sort! u    对全文逆序排列并去除重复行
:sort i 对全文排序同时忽略大小写
```


# Linux
## xsel 剪切板
将 ls 命令输出的结果放入剪切板
```
ls |xsel
```

