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

# multiprocessing.Pool / multiprocessing.dummy.Pool

```
multiprocessing.Pool(processes=None, initializer=None, initargs=(), maxtasksperchild=None)
multiprocessing.dummy.Pool(processes=None, initializer=None, initargs=())
```

## map
* 功能
并行处理
计算密集型任务使用多进程，IO 密集型任务使用多线程
* 描述
```
map(func, iterable, chunksize=None)
```
* 示例
```python
$ ipython
In [1]: %cpaste
Pasting code; enter '--' alone on the line to stop or use Ctrl-D.
:def fib(n):
    if n<= 2:
        return 1
    return fib(n-1) + fib(n-2):::
:--
In [2]: import time
In [3]: from multiprocessing import Pool
In [4]: pool = Pool(2)
In [5]: %time pool.map(fib, [35] * 2)
CPU times: user 8 ms, sys: 0 ns, total: 8 ms
Wall time: 4.02 s # 使用多进程明显提升了效率
Out[5]: [9227465, 9227465]
In [6]: %time [x for x in map(fib, [35] * 2)]
CPU times: user 7.71 s, sys: 4 ms, total: 7.72 s
Wall time: 7.7 s # 不使用多进程的情况
Out[6]: [9227465, 9227465]
```
    [理解 Python 并发编程一篇就够了 - 进程篇](http://www.dongwm.com/archives/%E4%BD%BF%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E5%B9%B6%E5%8F%91%E7%BC%96%E7%A8%8B-%E8%BF%9B%E7%A8%8B%E7%AF%87/)
    [Python 多核并行计算](https://abcdabcd987.com/python-multiprocessing/)

## imap / imap_unordered
* 功能
监控并行处理的进度
* 描述
```
imap(func, iterable, chunksize=1)
可能会比 map 慢很多
```

* 示例
```python
$ ipython
In [1]: from tqdm import tqdm
In [2]: from multiprocessing import Pool
In [3]: def fib(n):
   ...:     if n <= 2:
   ...:         return 1
   ...:     return fib(n - 1) + fib(n - 2)
In [4]: it = [35] * 6
In [5]: tmp = tqdm(total=len(it))
  0%|                                                                | 0/6 [00:00<?, ?it/s]
In [6]: pool = Pool(3)
In [7]: for _ in pool.imap_unordered(fib, it):
   ...:     tmp.update()
100%|################################################################| 6/6 [00:36<00:00, 12.11s/it]
```
	性能对比如下，通常可以接受：
```python
$ ipython
In [1]: from multiprocessing import Pool
In [2]: def fib(n):
   ...:     if n <= 2:
   ...:         return 1
   ...:     return fib(n - 1) + fib(n - 2)
In [3]: it = [5] * 10000
In [4]: pool = Pool(3)
In [5]: def test():
   ...:     for _ in pool.imap_unordered(fib, it):
   ...:         tmp = _
In [6]: def test1():
   ...:     pool.map(fib, it)
In [7]: %time test()
CPU times: user 904 ms, sys: 388 ms, total: 1.29 s
Wall time: 1.05 s
In [8]: %time test1()
CPU times: user 4 ms, sys: 4 ms, total: 8 ms
Wall time: 14 ms
In [9]: %time test()
CPU times: user 1.84 s, sys: 472 ms, total: 2.31 s
Wall time: 10.8 s
In [10]: %time test1()
CPU times: user 12 ms, sys: 0 ns, total: 12 ms
Wall time: 9.75 s
```
