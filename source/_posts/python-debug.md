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
将以下脚本保存至 crash_on_ipy.py
```
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
使用时，仅需要 ``import crash_on_ipy`` 即可
