---
title: python 文件操作相关函数
date: 2017-11-28 10:23:25
tags:
---

{% note default %}
方便查询
{% endnote %}

<!--more-->

---

# os.path.relpath
* 功能
获取相对路径
* 描述
```
relpath(path, start=None)
```
* 示例
```python
$ ipython
In [1]: pwd
Out[1]: '/root'
In [2]: import os
In [3]: os.path.relpath('/root/workspace/') # 默认相对当前路径
Out[3]: 'workspace'
In [4]: os.path.relpath('/root/workspace/', '/home/') # 可以指定起始路径
Out[4]: '../root/workspace'
```

# os.path.splittext
* 功能
剥离文件名后缀
* 描述
```
splitext(p)
```
* 示例
```python
$ ipython
In [6]: os.path.splitext('/tmp/my_test/parser_result.txt')[-1]
Out[6]: '.txt'
In [7]: os.path.splitext('/tmp/my_test/parser_result.txt')
Out[7]:
('/tmp/my_test/parser_result',
 '.txt')
```

# os.walk
* 功能
递归的返回子目录和子文件
* 描述
```
walk(top, topdown=True, onerror=None, followlinks=False)
```
* 示例
```python
# 遍历目录
$ ipython
In [1]: import os
In [2]: def print_dir(root_dir):
   ...:     list_dirs = os.walk(root_dir)
   ...:     for root, dirs, files in list_dirs:
   ...:         for d in dirs:
   ...:             print(os.path.join(root, d))
   ...:         for f in files:
   ...:             print(os.path.join(root, f))
In [3]: print_dir('/tmp/my_test')
/tmp/my_test/1.MSCP
/tmp/my_test/2.VP
/tmp/my_test/4.Scene
```

