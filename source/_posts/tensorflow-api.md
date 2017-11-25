---
title: Tensorflow API 整理
date: 2017-11-25 15:04:15
tags:
---

{% note default %}
Tensorflow API 整理，方便自己查阅
{% endnote %}

<!--more-->

---

# tf.data
## tf.data.Dataset
* 功能
* 描述
* 示例

# tf.contrib.lookup
## tf.contrib.lookup.HashTable
### lookup
* 功能
根据 token 和 ID 的映射表，给出目标串的 ID

* 描述
```
lookup(
    keys,
    name=None
)
```
* 示例
```python
$ ipython
Python 3.6.1 |Anaconda custom (64-bit)| (default, May 11 2017, 13:09:58)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.2.0 -- An enhanced Interactive Python. Type '?' for help.
In [1]: import tensorflow as tf
In [2]: with  tf.Session().as_default():
   ...:     default_val = -1
   ...:     keys = tf.constant(["brain", "salad", "surgery"])
   ...:     values = tf.constant([0, 1, 2], tf.int64)
   ...:     table = tf.contrib.lookup.HashTable(tf.contrib.lookup.KeyValueTensorInitializer(keys, values), default_val)
   ...:     input_string = tf.constant(["brain", "salad", "tank"])
   ...:     table.init.run()
   ...:     table.lookup(input_string).eval()
Out[2]: array([ 0,  1, -1])
```

## tf.contrib.lookup.index_table_from_file
* 功能
根据字典文件，建立 token 到 ID 的映射
* 描述
```shell
index_table_from_file(
    vocabulary_file=None,
    num_oov_buckets=0,
    vocab_size=None,
    default_value=-1,
    hasher_spec=tf.contrib.lookup.FastHashSpec,
    key_dtype=tf.string,
    name=None
)

Args:
vocabulary_file: The vocabulary filename, may be a constant scalar Tensor.
num_oov_buckets: 如果关键字未在字典里出现，关键字将使用 hash 算法指定 [vocabulary size, vocabulary size + num_oov_buckets - 1] 范围内的 ID,
                 如果不指定 num_oov_buckets 则未知关键字的 ID 会被指定为 default_value
vocab_size:      Number of the elements in the vocabulary, if known.
default_value:   The value to use for out-of-vocabulary feature values. Defaults to -1.
hasher_spec:     A HasherSpec to specify the hash function to use for assignation of out-of-vocabulary buckets.
key_dtype:       The key data type.
name:            A name for this op (optional).

Returns:
返回一个 tf.contrib.lookup.HashTable 对象
The lookup table to map a key_dtype Tensor to index int64 Tensor.
```
* 示例
```python
$ cat > /tmp/test.txt
emerson
lake
palmer

$ ipython
Python 3.6.1 |Anaconda custom (64-bit)| (default, May 11 2017, 13:09:58)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.2.0 -- An enhanced Interactive Python. Type '?' for help.
In [1]: import tensorflow as tf
In [2]: features = tf.constant(["emerson", "lake", "and", "palmer"])
In [3]: table = tf.contrib.lookup.index_table_from_file(vocabulary_file="/tmp/test.txt", num_oov_buckets=1)
In [4]: ids = table.lookup(features)
In [5]: with tf.Session().as_default():
   ...:     tf.tables_initializer().run()
   ...:     ids.eval()
   ...:
Out[5]: array([0, 1, 3, 2])
```
