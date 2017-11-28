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

# chardet.detect
* 功能
检测编码格式
* 描述
```
detect(byte_str)
```
* 示例
```python
$ ipython
In [1]: import chardet
In [2]: with open('/tmp/my_test/006.tc', 'rb') as f:  # 查询编码
   ...:     encode = chardet.detect(f.read())
In [3]: with open('/tmp/my_test/006.tc', encoding=encode['encoding']) as f:
   ...:     tmp = f.read()
In [4]: with open('/tmp/my_test/006.tc') as f:  # 直接 open 会出现编码问题
   ...:     tmp = f.read()
---------------------------------------------------------------------------
UnicodeDecodeError                        Traceback (most recent call last)
<ipython-input-4-fc8ced863c36> in <module>()
      1 with open('/tmp/my_test/006.tc') as f:
----> 2     tmp = f.read()
      3
~/anaconda3/lib/python3.6/codecs.py in decode(self, input, final)
    319         # decode input (taking the buffer into account)
    320         data = self.buffer + input
--> 321         (result, consumed) = self._buffer_decode(data, self.errors, final)
    322         # keep undecoded input until the next call
    323         self.buffer = data[consumed:]
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb0 in position 61: invalid start byte
```

# os.listdir
* 功能
非递归的返回子目录和子文件
* 描述
```
listdir(path=None)
```
* 示例
```
$ ipython
In [2]: import os
In [3]: [x for x in os.listdir('/tmp/my_test/')]
Out[3]: ['1.MSCP', '2.VP', '4.Scene', '3.vPW']
```

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

# os.path.splitext
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

