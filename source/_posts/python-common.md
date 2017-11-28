---
title: python 常用三方库
date: 2017-11-28 16:58:11
tags:
---

{% note default %}
方便查询
{% endnote %}

<!--more-->

---

# tqdm
* 功能
进度条
* 描述
```python
__init__(self,
 iterable=None,  # 必选参数
 desc=None,
 total=None,     # 有些 iter 无法获取完整长度，需要自行计算
 leave=True,
 file=None,
 ncols=None,
 mininterval=0.1,
 maxinterval=10.0,
 miniters=None,
 ascii=None,
 disable=False,
 unit='it',
 unit_scale=False,
 dynamic_ncols=False,
 smoothing=0.3,
 bar_format=None,
 initial=0,
 position=None,
 postfix=None,
 unit_divisor=1000,
 gui=False,
 **kwargs)
```
* 示例
```python
$ ipython
In [1]: from time import sleep
In [2]: from tqdm import tqdm
In [3]: for i in tqdm(range(10)):                              # 基本 Demo
   ...:     sleep(1)
100%|#####################################################| 10/10 [00:07<00:00,  1.28it/s]
In [5]: import os
In [6]: for x in tqdm(os.walk('/tmp/my_test/')):               # os.walk 返回的生成器无法直接获取长度，所以进度条没有完成率
   ...:     sleep(1)
5it [00:05,  1.00s/it]
In [7]: count = len([x for x in os.walk('/tmp/my_test/')])
In [8]: for x in tqdm(os.walk('/tmp/my_test/'), total=count):  # 先计算 os.walk 长度，然后传入 total
   ...:     sleep(1)
100%|#####################################################| 5/5 [00:02<00:00,  1.58it/s]
```
