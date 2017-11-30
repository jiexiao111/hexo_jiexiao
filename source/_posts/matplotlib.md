---
title: matplotlib 学习
date: 2017-10-28 21:11:53
categories: 编程语言
tags:
  - python
---

{% note default %}
绘图也算常用...
{% endnote %}

# Hello, Matplotlib
```
import matplotpy.plot as plt
import numpy as np

X = np.line
```

# matplotlib 查看可用的中文字体
```python
from matplotlib.font_manager import FontManager
import subprocess
fm = FontManager()
mat_fonts = set(f.name for f in fm.ttflist)
#print(mat_fonts)
output = subprocess.check_output('fc-list :lang=zh -f "%{family}\n"', shell=True)
#print( '*' * 10, '系统可用的中文字体', '*' * 10)
#print (output)
zh_fonts = set(f.split(',', 1)[0] for f in output.decode('utf-8').split('\n'))
available = mat_fonts & zh_fonts
print ('*' * 10, '可用的字体', '*' * 10)
for f in available:
    print (f)
```

# matplotlib 显示中文的问题
* 第一步：下载字体：msyh.ttf （微软雅黑）
放在系统字体文件夹下：``/usr/share/fonts``
同时我也复制了下放在 matplotlib 的字体文件夹下了（不知道这一步是不是必须）
``/usr/local/lib/python3.5/dist-packages/matplotlib/mpl-data/fonts/ttf/``
* 第二步：修改 matplotlib 配置文件：
编辑 ``/usr/local/lib/python3.5/dist-packages/matplotlib/mpl-data/matplotlibrc``
删除 font.family 和 font.sans-serif 两行前的#，并在 font.sans-serif 后添加中文字体
Microsoft YaHei, ...（其余不变）
* 第三步：删除~/.cache/matplotlib 下文件 fontList.py3k.cache

* 第四步：代码里加入以下代码
```python
from matplotlib import rcParams
rcParams['font.family'] = 'Microsoft YaHei'
```

# 参考资料
[Matplotlib 教程](https://liam0205.me/2014/09/11/matplotlib-tutorial-zh-cn/)
[给深度学习入门者的 Python 快速教程 - numpy 和 Matplotlib 篇](https://zhuanlan.zhihu.com/p/24309547)
