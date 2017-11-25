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
### shard
* 功能
将一个 Dataset 切分成 N 份，然后取出 1 份，在分布式训练时，避免资源竞争使用
* 描述
```
shard(
    num_shards,
    index
)

Args:
num_shards: A tf.int64 scalar tf.Tensor, 切分的份数
index:      A tf.int64 scalar tf.Tensor, 取出份数的 ID

Returns:
A Dataset.
```
* 示例
```python
$ ipython
Python 3.6.1 |Anaconda custom (64-bit)| (default, May 11 2017, 13:09:58)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.2.0 -- An enhanced Interactive Python. Type '?' for help.
In [1]: import tensorflow as tf
In [2]: from tensorflow.python.data import Dataset
In [3]: def print_dataset(d):
   ...:     d_iter = d.make_one_shot_iterator()
   ...:     with tf.Session() as sess:
   ...:         while True:
   ...:             try:
   ...:                 print(sess.run(d_iter.get_next()))
   ...:             except tf.errors.OutOfRangeError:
   ...:                 break
In [4]: a = Dataset.range(1, 4) # {1, 2, 3}
In [5]: print_dataset(a.shard(2, 0))
1
3
In [6]: print_dataset(a.shard(2, 1))
2
```
### skip
* 功能
丢弃一部分数据
* 描述
```
skip(count)

Args:
count: A tf.int64 scalar tf.Tensor, representing the number of elements of this dataset that should be skipped to form the new dataset. If count is greater than the size of this dataset, the new dataset will contain no elements. If count is -1, skips the entire dataset.

Returns:
A Dataset.
```
* 示例
```python
$ ipython
Python 3.6.1 |Anaconda custom (64-bit)| (default, May 11 2017, 13:09:58)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.2.0 -- An enhanced Interactive Python. Type '?' for help.
In [1]: import tensorflow as tf
In [2]: from tensorflow.python.data import Dataset
In [3]: def print_dataset(d):
   ...:     d_iter = d.make_one_shot_iterator()
   ...:     with tf.Session() as sess:
   ...:         while True:
   ...:             try:
   ...:                 print(sess.run(d_iter.get_next()))
   ...:             except tf.errors.OutOfRangeError:
   ...:                 break
In [4]: a = Dataset.range(1, 4) # {1, 2, 3}
In [5]: print_dataset(a.skip(1))
2
3
In [6]: print_dataset(a.skip(2))
3
```

### zip
* 功能
与 python 内置的 zip 类似
* 描述
```
zip(datasets)

Args:
datasets: A nested structure of datasets.

Returns:
A Dataset.
```

* 示例
```python
$ ipython
Python 3.6.1 |Anaconda custom (64-bit)| (default, May 11 2017, 13:09:58)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.2.0 -- An enhanced Interactive Python. Type '?' for help.
In [1]: from tensorflow.python.data import Dataset
In [2]: import tensorflow as tf
In [3]: def print_dataset(d):
   ...:     d_iter = d.make_one_shot_iterator()
   ...:     with tf.Session() as sess:
   ...:         while True:
   ...:             try:
   ...:                 print(sess.run(d_iter.get_next()))
   ...:             except tf.errors.OutOfRangeError:
   ...:                 break
   ...:
In [4]: a = Dataset.range(1, 4) # {1, 2, 3}
In [5]: b = Dataset.range(4, 7) # {4, 5, 6}
In [7]: c = Dataset.zip((Dataset.range(7, 12), Dataset.range(8, 13))) # { (7, 8), (8, 9), (9, 10) }
In [8]: d = Dataset.range(13, 15) # {13, 14}
In [9]: print_dataset(Dataset.zip((a, b)))
(1, 4)
(2, 5)
(3, 6)
In [10]: print_dataset(Dataset.zip((b, a)))
(4, 1)
(5, 2)
(6, 3)
In [11]: print_dataset(Dataset.zip((a, b, c)))
(1, 4, (7, 8))
(2, 5, (8, 9))
(3, 6, (9, 10))
In [12]: print_dataset(Dataset.zip((a, d)))
(1, 13)
(2, 14)
```
## tf.data.TextLineDataset
* 功能
按行读取文件，转化为 TextLineDataset 对象
* 描述
```
__init__(
    filenames,
    compression_type=None,
    buffer_size=None
)

Args:
filenames:        A tf.string tensor containing one or more filenames.
compression_type: (Optional.) A tf.string scalar evaluating to one of "" (no compression), "ZLIB", or "GZIP".
buffer_size:      (Optional.) A tf.int64 scalar denoting the number of bytes to buffer. A value of 0 results in the default buffering values chosen based on the compression type.
```
* 示例
```python
$ cat /tmp/test.txt
emerson
lake
palmer

$ ipython
Python 3.6.1 |Anaconda custom (64-bit)| (default, May 11 2017, 13:09:58)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.2.0 -- An enhanced Interactive Python. Type '?' for help.
In [1]: from tensorflow.python.data import TextLineDataset
In [2]: import tensorflow as tf
In [3]: def print_dataset(d):
   ...:     d_iter = d.make_one_shot_iterator()
   ...:     with tf.Session() as sess:
   ...:         while True:
   ...:             try:
   ...:                 print(sess.run(d_iter.get_next()))
   ...:             except tf.errors.OutOfRangeError:
   ...:                 break
In [4]: tmp = tf.data.TextLineDataset('/tmp/test.txt')
In [5]: print_dataset(tmp)
b'emerson'
b'lake'
b'palmer'
```

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

Args:
keys: Keys to look up. May be either a SparseTensor or dense Tensor.
name: A name for the operation (optional).

Returns:
A SparseTensor if keys are sparse, otherwise a dense Tensor.
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
```
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
