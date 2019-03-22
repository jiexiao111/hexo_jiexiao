---
title: numpy 文档走读记录
date: 2018-11-02 10:26:50
categories: 编程语言
tags:
  - python
---

<!-- 概述 -->
{% note default %}
numpy 作为最基础的 python 库，官方文档还是有必要看一下的，所以决定对看到的内容进行记录和梳理
{% endnote %}

<!-- End -->

---

# np

* ``np.info()`` 与 ``help()`` 的作用均是查看函数或者对象的帮助信息，但是如果函数通过 ``C`` 语言实现，则无法通过 ``help()`` 获取帮助信息，必须使用 ``np.info``

* ``np.lookfor()`` 能够查找相关的函数

* 子模块包括 ``doc``、``lib``、``random``、``linalg``、``fft``、``polynomial``、``testing``、``f2py``、``distutils``、``test``、``show_config``、``dual``、``matlib``

* ``np.<TAB>`` 可以进行补全

* ``np.*cos*?<ENTER>`` 可以根据正则表达式进行补全

* ``np.sort?<ENTER>`` 可以查看帮助信息

* ``np.sort??<ENTER>`` 可以查看源码

* 通常来说 ``functions`` 通常返回对象的拷贝, 即不改变输入，``methods`` 通常返回引用，即修改输入的对象。eg:
```python
In [22]: x = np.array([2, 1, 3]); x.sort(); x
Out[22]: array([1, 2, 3])

In [23]: x = np.array([2, 1, 3]); np.sort(x); x
Out[23]: array([1, 2, 3])
Out[23]: array([2, 1, 3])
```

# np.doc
需要执行 ``from numpy import doc`` 才可以使用该模块

## np.doc.basics
定义 ``numpy`` 的支持的类型以及类型之间的转换
