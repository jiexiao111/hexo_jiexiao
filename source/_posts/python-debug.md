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
以下为完整示例，代码一共就两行，第一行导入 ``my_crash``, 第二行制造异常，然后运行就出现以下错误
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
