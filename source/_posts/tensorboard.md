---
title: tensorboard
date: 2017-11-29 21:18:37
tags:
---

<!-- 文章开头都用它了，整齐才好看 -->
{% note default %}
Tensorboard 非常常用，但是经常临时忘记如何使用，所以自己总结一遍
{% endnote %}

<!--more-->

---

# 最简 Dome
```python
$ ipython
In [1]: import tensorflow as tf
In [2]: x_data = tf.placeholder(tf.float32) # Graph 中唯一的节点
In [3]: sess = tf.Session()
In [4]: tf.summary.FileWriter('/tmp/my_test/', sess.graph)
Out[4]: <tensorflow.python.summary.writer.writer.FileWriter at 0x7f3e60027320>
```
