---
title: Pandas 使用总结
date: 2017-11-28 14:27:02
categories: 编程语言
tags:
  - python
---

{% note default %}
pandas 使用整理
{% endnote %}

<!--more-->

---

# pandas.DataFrame
* 功能
初始化一个 DataFrame 对象
* 描述
* 示例
```python
In [1]: import pandas as pd
In [2]: df = pd.DataFrame([['file1', 'path1', 'type1'], ['file2', 'path2', 'type2']], columns=['filename', 'filepath', 'filetype'])
In [3]: df
Out[3]:
  filename filepath filetype
0    file1    path1    type1
1    file2    path2    type2
```

# pandas.DataFrame.to_excel
* 功能
生成 excel 文件
* 描述
* 示例
```python
$ ipython
In [1]: import pandas as pd
In [2]: df = pd.DataFrame([['file1', 'path1', 'type1'], ['file2', 'path2', 'type2']], columns=['filename', 'filepath', 'filetype'])
In [3]: df
Out[3]:
  filename filepath filetype
0    file1    path1    type1
1    file2    path2    type2
In [4]: df.to_excel('foo.xlsx', sheet_name='Sheet1')
```
