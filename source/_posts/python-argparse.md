---
title: argparse 函数
date: 2017-11-22 17:18:40
categories: 编程语言
tags:
  - python
---

{% note default %}
python 参数解析函数介绍
{% endnote %}

<!--more-->

---

# 写在前面
尽量用 argparse 替代 optparse

# 设置解析器、定义参数、解析参数
设置解析器：使用 argparse 的第一步就是创建一个解析器对象 ``ArgumentParser``
定义参数： 通过 ``add_argument()`` 指定参数
解析参数： 通过 ``parse_args()`` 解析命令行参数，默认从 sys.argv[1:] 中获取参数
```python
import argparse
parser = argparse.ArgumentParser(description='This is a PyMOTW sample program')
parser.add_argument('-c', type=int, default=32, help="help info.")
FLAG = parser.parse_args()
```
将以上代码保存至 ``/tmp/tmp.py`` 然后就可以通过 ``python /tmp/tmp.py -h`` 查看帮助信息了
```shell
usage: tmp.py [-h] [-c C]

This is a PyMOTW sample program

optional arguments:
  -h, --help  show this help message and exit
  -c C        help info.
```

使用时可以通过 ``FLAG.c`` 进行引用

# 设置必选参数
```
parser.add_argument('-c', type=str, required=True)
```

# nargs
## ``N``
指定每个参数的个数
```python
$ ipython
In [1]: import argparse
In [2]: parser = argparse.ArgumentParser()
In [3]: parser.add_argument('arg1', nargs=2)
Out[3]: _StoreAction(option_strings=[], dest='arg1', nargs=2, const=None, default=None, type=None, choices=None, help=None, metavar=None)
In [5]: parser.add_argument('--arg2', nargs=2)
Out[5]: _StoreAction(option_strings=['--arg2'], dest='arg2', nargs=2, const=None, default=None, type=None, choices=None, help=None, metavar=None)
In [6]: parser.add_argument('arg3', nargs=3)
Out[6]: _StoreAction(option_strings=[], dest='arg3', nargs=3, const=None, default=None, type=None, choices=None, help=None, metavar=None)
In [11]: parser.parse_args('--arg2 a b c d e f g'.split())
Out[11]: Namespace(arg1=['c', 'd'], arg2=['a', 'b'], arg3=['e', 'f', 'g'])
In [12]: parser.parse_args('a b --arg2 c d e f g'.split())
Out[12]: Namespace(arg1=['a', 'b'], arg2=['c', 'd'], arg3=['e', 'f', 'g'])
# 使用时，务必保证参数个数匹配
In [14]: parser.parse_args('--arg2 a b c d e f'.split())
usage: ipython [-h] [--arg2 ARG2 ARG2] arg1 arg1 arg3 arg3 arg3
ipython: error: the following arguments are required: arg3
An exception has occurred, use %tb to see the full traceback.
SystemExit: 2
/root/anaconda3/lib/python3.6/site-packages/IPython/core/interactiveshell.py:2890: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.
  warn("To exit: use 'exit', 'quit', or Ctrl-D.", stacklevel=1)
```

## ``?``
零个或一个参数
```python
$ ipython
In [1]: import argparse
In [3]: parser = argparse.ArgumentParser()
In [4]: parser.add_argument('arg1', nargs='?', const='c', default='d')
Out[4]: _StoreAction(option_strings=[], dest='arg1', nargs='?', const='c', default='d', type=None, choices=None, help=None, metavar=None)
In [6]: parser.add_argument('--arg2', nargs='?', const='e', default='f')
Out[6]: _StoreAction(option_strings=['--arg2'], dest='arg2', nargs='?', const='e', default='f', type=None, choices=None, help=None, metavar=None)
In [9]: parser.parse_args('A --arg2 C'.split())
Out[9]: Namespace(arg1='A', arg2='C')
In [10]: parser.parse_args('--arg2 A B'.split())
Out[10]: Namespace(arg1='B', arg2='A')
In [12]: parser.parse_args('--arg2 A '.split())
Out[12]: Namespace(arg1='d', arg2='A')
# 不包含参数值时，参数等于 ``const``
In [13]: parser.parse_args('--arg2'.split())
Out[13]: Namespace(arg1='d', arg2='e')
# 不包含参数前缀和值的时候，参数等于 ``default``
In [14]: parser.parse_args([])
Out[14]: Namespace(arg1='d', arg2='f')
```

## ``*``
任意个数
```python
$ ipython
In [1]: import argparse
In [2]: parser = argparse.ArgumentParser()
In [3]: parser.add_argument('arg1', nargs='*')
Out[3]: _StoreAction(option_strings=[], dest='arg1', nargs='*', const=None, default=None, type=None, choices=None, help=None, metavar=None)
In [4]: parser.add_argument('--arg2', nargs='*')
Out[4]: _StoreAction(option_strings=['--arg2'], dest='arg2', nargs='*', const=None, default=None, type=None, choices=None, help=None, metavar=None)
In [6]: parser.parse_args('A B --arg2 C D E'.split())
Out[6]: Namespace(arg1=['A', 'B'], arg2=['C', 'D', 'E'])
```

## ``+``
至少一个
```python
$ ipython
In [1]: import argparse
In [2]: parser = argparse.ArgumentParser()
In [3]: parser.add_argument('arg1', nargs='+')
Out[3]: _StoreAction(option_strings=[], dest='arg1', nargs='+', const=None, default=None, type=None, choices=None, help=None, metavar=None)
In [4]: parser.add_argument('--arg2', nargs='+')
Out[4]: _StoreAction(option_strings=['--arg2'], dest='arg2', nargs='+', const=None, default=None, type=None, choices=None, help=None, metavar=None)
In [5]: parser.parse_args('A --arg2 B'.split())
Out[5]: Namespace(arg1=['A'], arg2=['B'])
# 至少有一个参数
In [6]: parser.parse_args('--arg2 A'.split())
usage: ipython [-h] [--arg2 ARG2 [ARG2 ...]] arg1 [arg1 ...]
ipython: error: the following arguments are required: arg1
An exception has occurred, use %tb to see the full traceback.
SystemExit: 2
/root/anaconda3/lib/python3.6/site-packages/IPython/core/interactiveshell.py:2890: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.
  warn("To exit: use 'exit', 'quit', or Ctrl-D.", stacklevel=1)
```

## ``argparse.REMAINDER``
剩余的所有
```python
$ ipython
In [1]: import argparse
In [2]: parser = argparse.ArgumentParser()
In [3]: parser.add_argument('--arg1')
Out[3]: _StoreAction(option_strings=['--arg1'], dest='arg1', nargs=None, const=None, default=None, type=None, choices=None, help=None, metavar=None)
In [4]: parser.add_argument('arg2')
Out[4]: _StoreAction(option_strings=[], dest='arg2', nargs=None, const=None, default=None, type=None, choices=None, help=None, metavar=None)
In [6]: parser.add_argument('arg3', nargs=argparse.REMAINDER)
Out[6]: _StoreAction(option_strings=[], dest='arg3', nargs='...', const=None, default=None, type=None, choices=None, help=None, metavar=None)
In [7]: parser.parse_args('--arg1 A B C --arg4 D E'.split())
Out[7]: Namespace(arg1='A', arg2='B', arg3=['C', '--arg4', 'D', 'E'])
```

# 参考
[argparse - 命令行选项与参数解析（译）](http://blog.xiayf.cn/2013/03/30/argparse/)
