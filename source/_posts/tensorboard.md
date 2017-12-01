---
title: tensorboard
date: 2017-11-29 21:18:37
categories: 机器学习
tags:
  - Tensorflow
---

<!-- 文章开头都用它了，整齐才好看 -->
{% note default %}
Tensorboard 非常常用，但是经常临时忘记如何使用，所以自己总结一遍
{% endnote %}

<!--more-->

---

# 最简 Dome
以下四行代码就可以在 tensorboard 中显示 Graphs 了，尽管只有一个节点
```python
$ ipython
In [1]: import tensorflow as tf
In [2]: x_data = tf.placeholder(tf.float32)                 # Graph 中唯一的节点
In [3]: sess = tf.Session()                                 # 创建 session
In [4]: tf.summary.FileWriter('/tmp/my_test/', sess.graph)  # 将信息写入指定目录
Out[4]: <tensorflow.python.summary.writer.writer.FileWriter at 0x7f3e60027320>
```
然后执行 ``tensorboard --logdir=/tmp/my_test/``，如果没有报错就可以在浏览器中通过 ``http://localhost:6006/`` 查看效果了
![最简单的例子](/images/Tensorboard/1.png)

# 正常一些的 Demo
计算图只有一个点实在说不过去，MNIST 的计算图我也觉得太复杂，那么一元一次方程就最合适了
```python
$ ipython3
In [1]: load /Users/jiexiao/workspace/tmp2.py
In [2]: # %load /Users/jiexiao/workspace/tmp2.py
   ...: import tensorflow as tf
   ...:
   ...: # 定义计算图
   ...: in_x = tf.placeholder(tf.float32)                       # 输入
   ...: in_y = tf.placeholder(tf.float32)                       # 输出
   ...: W = tf.Variable(tf.random_uniform([1], -200.0, 200.0))  # 待求的斜率
   ...: b = tf.Variable(tf.zeros([1]))                          # 待求的偏置
   ...: y = W * in_x + b                                        # 一元一次方程
   ...: loss = tf.reduce_mean(tf.square(y - in_y))              # 模型根据 in_x 计算出的 y 真实的输出 in_y 的差值
   ...: optimizer = tf.train.GradientDescentOptimizer(0.7)      # 选择优化函数
   ...: train = optimizer.minimize(loss)                        # 梯度下降，使 W 和 b 不断逼近真实值
   ...:
   ...: # 保存可视化信息
   ...: sess = tf.Session()
   ...: writer = tf.summary.FileWriter('/tmp/my_test/', sess.graph)
```
下面的结果看起来就好多啦
![2](/images/Tensorboard/2.png)

# 优化标签显示
可以看到 Graph 中的节点名字都是都是 ``Variable_1`` 这样的，为了更好的可读性，我们在之前代码的基础上添加 ``tf.name_scope`` 和 ``name`` 参数
```python
$ ipython3
In [1]: load /Users/jiexiao/workspace/tmp2.py
In [2]: # %load /Users/jiexiao/workspace/tmp2.py
   ...: import tensorflow as tf
   ...:
   ...: # 定义计算图
   ...: in_x = tf.placeholder(tf.float32, name='in_x') # 为单个 tensor 命名
   ...:
   ...: in_y = tf.placeholder(tf.float32, name='in_y')
   ...:
   ...: with tf.name_scope('W'): # 将多个 tensor 组合成一个 scope 然后命名
   ...:     W = tf.Variable(tf.random_uniform([1], -200.0, 200.0))
   ...:
   ...: with tf.name_scope('b'):
   ...:     b = tf.Variable(tf.zeros([1]))
   ...:
   ...: with tf.name_scope('y'):
   ...:     y = W * in_x + b
   ...:
   ...: with tf.name_scope('loss'):
   ...:     loss = tf.reduce_mean(tf.square(y - in_y))
   ...:
   ...: with tf.name_scope('optimizer'):
   ...:     optimizer = tf.train.GradientDescentOptimizer(0.7)
   ...:
   ...: with tf.name_scope('train'):
   ...:     train = optimizer.minimize(loss)
   ...:
   ...: # 保存可视化信息
   ...: sess = tf.Session()
   ...: writer = tf.summary.FileWriter('/tmp/my_test/', sess.graph)
```
这样看起来就非常棒了
![3](/images/Tensorboard/3.png)

# tf.summary.scalar
# tf.summary.histogram

# tf.summary.image
# tf.summary.audio
# tf.summary.text

# 参考
[tensorflow 第一个简单案例](http://www.jianshu.com/p/d6606d9204c2)
