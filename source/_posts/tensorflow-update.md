---
title: tensorflow update 注意事项
date: 2017-11-22 15:21:55
tags:
---


{% note default %}
tensorflow 1.4 安装遇到的问题记录
{% endnote %}

<!--more-->

---

# 升级 1.4 问题一
注意：pip 命令需要添加代理
执行 ``pip install --ignore-installed --upgrade tensorflow`` 出现以下错误：
```
In [1]: import tensorflow as tf
/root/anaconda3/lib/python3.6/importlib/_bootstrap.py:205: RuntimeWarning: compiletime version 3.5 of module 'tensorflow.python.framework.fast_tensor_util' does not match runtime version
 3.6
   return f(*args, **kwds)
```
于是下载了一个特殊版本的 whl 然后安装
```
curl --insecure -o tensorflow-1.4.0rc1-cp36-cp36m-linux_x86_64.whl https://raw.githubusercontent.com/lakshayg/tensorflow-build/master/tensorflow-1.4.0rc1-cp36-cp36m-linux_x86_64.whl
pip install --ignore-installed --upgrade tensorflow-1.4.0rc1-cp36-cp36m-linux_x86_64.whl
```

# 升级 1.4 问题二
运行后出现错误 ``GLIBCXX_3.4.22' not found``
```
add-apt-repository ppa:ubuntu-toolchain-r/test
apt-get update       # 更新源
apt-get upgrade      # 更新已安装的包
apt-get dist-upgrade # 升级系统
apt-get install build-essential
apt-get install aptitude
apt-get install libstdc++6
```
通过``strings /usr/lib/x86_64-linux-gnu/libstdc++.so.6 | grep GLIBCXX`` 检查下``GLIBCXX_3.4.22``是否存在
