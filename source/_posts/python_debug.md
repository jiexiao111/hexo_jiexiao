---
title: python 调试技巧
date: 2017-11-23 16:52:43
tags:
---

{% note default %}
python 调试技巧
{% endnote %}

<!--more-->

---

# python 异常退出时进入 ipdb
将以下脚本保存至 ``my_crash.py``, 为了方便使用，可以通过 ``sys.path`` 查询默认包路径，将 ``my_crash.py`` 放至某个默认路径，例如：``/root/anaconda3/lib/python3.6``
```python
import sys

class ExceptionHook:
    instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            from IPython.core import ultratb
            self.instance = ultratb.FormattedTB(mode='Plain',
                 color_scheme='Linux', call_pdb=1)
        return self.instance(*args, **kwargs)

sys.excepthook = ExceptionHook()
```

使用时，仅需要 ``import my_crash`` 即可
以下为完整示例，代码一共就两行，第一行导入 ``my_crash``, 第二行制造异常，运行后就自动进入 ipdb 了
```shell
$ python /tmp/tmp.py
Traceback (most recent call last):
  File "/tmp/tmp.py", line 2, in <module>
    1/0
ZeroDivisionError: division by zero

> /tmp/tmp.py(2)<module>()
      1 import my_crash
----> 2 1/0

ipdb>
```

# ipython 中快速调试函数
进入 ipython 的配置目录
```shell
cd `ipython locate profile`/startup
```
创建 tool.py 文件，然后把以下代码粘贴进去
```python
def debug(f, *args, **kwargs):
    from IPython.core.debugger import Pdb
    pdb = Pdb(color_scheme='Linux')
    return pdb.runcall(f, *args, **kwargs)
```
然后就可以在 ipython 中快速 debug 了。 下面这个例子中， ``f`` 函数接受三个参数，于是我就可以通过 ``debug(f, 1, 2, 3)`` 直接进行调试了
```shell
$ ipython
Python 3.6.1 |Anaconda custom (64-bit)| (default, May 11 2017, 13:09:58)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.2.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: cat /tmp/tmp.py
def f(x, y, z):
    tmp = x + y
    return  tmp / z

In [2]: %load /tmp/tmp.py

In [3]: # %load /tmp/tmp.py
   ...: def f(x, y, z):
   ...:     tmp = x + y
   ...:     return  tmp / z
   ...:

In [4]: debug(f, 1, 2, 3)
/root/anaconda3/bin/ipython:3: DeprecationWarning: The `color_scheme` argument is deprecated since version 5.1
  # -*- coding: utf-8 -*-
> <ipython-input-3-586af56f5d02>(3)f()
      1 # %load /tmp/tmp.py
      2 def f(x, y, z):
----> 3     tmp = x + y
      4     return  tmp / z

ipdb> a
x = 1
y = 2
z = 3
ipdb>
```

# 触发断点后进入 ipython
优势是 ipython 中可以非常方便的编写包含嵌套的代码，而且可以方便的引用全局 / 局部变量
```python
def my_break(local_ns=None, global_ns=None):
    # An interactive shell is useful for debugging/development.
    import IPython
    user_ns = {}
    if local_ns:
        user_ns.update(local_ns)
    if global_ns:
        user_ns.update(global_ns)
    IPython.start_ipython(argv=[], user_ns=user_ns)
```

为了使用方便，将以上代码拷贝至 ``/root/anaconda3/lib/python3.6/my_break.py``, 以下为具体实例
```shell
$ python /tmp/tmp.py
Python 3.6.1 |Anaconda custom (64-bit)| (default, May 11 2017, 13:09:58)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.2.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: cat /tmp/tmp.py
from my_break import my_break
var_global = 'global'

def f():
    var_locals = 'local'
    my_break(locals(), globals())

f()

In [2]: var_global
Out[2]: 'global'

In [3]: var_locals
Out[3]: 'local'

In [4]:
```
执行到 my_break() 函数后就进入了 ipython 交互界面，可以看出我们可以使用局部和全局变量

# 使用 pdb 的 command 动态添加日志
``pdb`` 的 command 命令非常适合调试，以下为示例：
```
$ python -m pdb /tmp/tmp.py
> /tmp/tmp.py(1)<module>()
-> from time import sleep
(Pdb) l
  1  -> from time import sleep
  2     for x in range(3):
  3         print('old log')
  4         sleep(1)
  5
[EOF]
(Pdb) b 3
Breakpoint 1 at /tmp/tmp.py:3
(Pdb) commands
(com) print('new log %d' % x)
(com) c
(Pdb) c
new log 0
> /tmp/tmp.py(3)<module>()
-> print('old log')
old log
new log 1
> /tmp/tmp.py(3)<module>()
-> print('old log')
old log
new log 2
> /tmp/tmp.py(3)<module>()
-> print('old log')
old log
The program finished and will be restarted
> /tmp/tmp.py(1)<module>()
-> from time import sleep
(Pdb)
```
