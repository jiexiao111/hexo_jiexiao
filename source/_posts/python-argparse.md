---
title: argparse 函数
date: 2017-11-22 17:18:40
tags:
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

#
