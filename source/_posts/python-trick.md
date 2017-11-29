---
title: Python Trick
date: 2017-11-29 19:50:32
tags:
---

{% note default %}
python 语法糖等等杂项
{% endnote %}

<!--more-->

---

# 查看 python 版本信息
在未进行 Python Shell 之前：
```
python –version
```
进入 Python Shell 之后，有两种方法
```python
help()
import sys sys.version
```

# pip 安装超时
```python
$ cat > ~/.pip/pip.conf
[global]
timeout = 6000
index-url = http://pypi.douban.com/simple/
[install]
use-mirrors = true
mirrors = http://pypi.douban.com/simple/
trusted-host = pypi.douban.com
```

# python 判断是否可迭代
```python
$ ipython
In [1]: [x for x in [None, '123', '456', 6] if hasattr(x, '__iter__')]
Out[1]: ['123', '456']
```

# python list 降维
```python
$ ipython
In [1]: sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [])
Out[1]: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```
