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

# tf

##  Building Graphs

### Defining new operations

#### tf.TensorShape
* 功能
表示某个 shape 的 Tensor

## Constants, Sequences, and Random Values

### Constant Value Tensors

#### tf.fill
* 功能
创建元素为同一标量的 Tensor
* 描述
```
fill(
    dims,
    value,
    name=None
)

Args:
dims:  A Tensor of type int32. 1-D. Represents the shape of the output tensor.
value: A Tensor. 0-D (scalar). Value to fill the returned tensor.
name:  A name for the operation (optional).

Returns:
A Tensor. Has the same type as value.
```
* 示例
```python
$ ipython
In [1]: import tensorflow as tf
In [2]: tmp = tf.fill([2, 3], 9)
In [3]: with tf.Session().as_default():
   ...:     tmp.eval()
Out[3]:
array([[9, 9, 9],
       [9, 9, 9]], dtype=int32)
```

### Sequences

#### tf.range
* 功能
构建 tensor 序列
* 描述
```
range(limit, delta=1, dtype=None, name='range')
range(start, limit, delta=1, dtype=None, name='range')

Args:
start: 序列的起点，默认为 0, 包含
limit: 序列的终点，不包含
delta: 增量，可以为负
dtype: 元素类型
name:  A name for the operation. Defaults to "range".

Returns:
An 1-D Tensor of type dtype.
```
* 示例
```python
$ ipython3
In [1]: import tensorflow as tf
In [2]: with tf.Session():
   ...:     tf.range(5).eval()
   ...:     tf.range(3, 1, -0.5).eval()
Out[2]: array([0, 1, 2, 3, 4], dtype=int32)
Out[2]: array([ 3. ,  2.5,  2. ,  1.5], dtype=float32)
```


## Control Flow

### Logical Operators

#### tf.logical_and/tf.logical_or/tf.logical_xor/tf.logical_not
* 功能
逻辑运算符
* 描述
```
logical_and(
    x,
    y,
    name=None
)

Args:
x: A Tensor of type bool.
y: A Tensor of type bool.
name: A name for the operation (optional).

Returns:
A Tensor of type bool.
```

* 示例
```python
$ ipython3
In [1]: import tensorflow as tf
In [2]: t1 = tf.constant([True, True, False, False])
In [3]: t2 = tf.constant([False, True, False, True])
In [4]: with tf.Session():
   ...:     tf.logical_and(t1, t2).eval()
   ...:     tf.logical_or(t1, t2).eval()
   ...:     tf.logical_xor(t1, t2).eval()
   ...:     tf.logical_not(t1).eval()
Out[4]: array([False,  True, False, False], dtype=bool)
Out[4]: array([ True,  True, False,  True], dtype=bool)
Out[4]: array([ True, False, False,  True], dtype=bool)
Out[4]: array([False, False,  True,  True], dtype=bool)
```

## Math

### Basic Math Functions

#### tf.maximum
* 功能
取 max...

#### tf.minimum
* 功能
取 min...

## Strings

### Splitting

#### tf.string_split
* 功能
Split elements of source based on delimiter into a SparseTensor
* 描述
```
string_split(
    source,
    delimiter=' ',
    skip_empty=True
)

Args:
source: 1-D string Tensor, the strings to split.
delimiter: 0-D string Tensor, the delimiter character, the string should be length 0 or 1.
skip_empty: A bool. 默认值是 True 所以默认不会产生空子串

Returns:
A SparseTensor of rank 2, the strings split according to the delimiter. The first column of the indices corresponds to the row in source and the second column corresponds to the index of the split component in this row.
```
* 示例
```python
$ ipython3
In [1]: load /Users/jiexiao/workspace/tmp.py
In [2]: # %load /Users/jiexiao/workspace/tmp.py
   ...:
   ...: import tensorflow as tf
   ...: from tensorflow.python.data import Dataset
   ...: def print_dataset(d):
   ...:     d_iter = d.make_one_shot_iterator()
   ...:     with tf.Session() as sess:
   ...:         while True:
   ...:             try:
   ...:                 print(sess.run(d_iter.get_next()))
   ...:             except tf.errors.OutOfRangeError:
   ...:                 break
In [3]: tmp = Dataset.from_tensor_slices(['jie xiao', 'huawei'])
In [4]: print_dataset(tmp.map(lambda x: tf.string_split([x]).values))
[b'jie' b'xiao']
[b'huawei']
```
    可以注意到 ``tf.string_split`` 函数的参数至少是 1D 的 tensor，另外，``tf.string_split`` 的返回值必须取 value 才能作为 Dataset 的元素，这里给出另一个例子
```python
$ ipython3
In [1]: import tensorflow as tf
In [2]: with tf.Session() as sess:
   ...:     sess.run(tf.string_split(['jie xiao', 'hua wei', 'gong zuo san nian']))
Out[2]:
SparseTensorValue(indices=array([[0, 0],
       [0, 1],
       [1, 0],
       [1, 1],
       [2, 0],
       [2, 1],
       [2, 2],
       [2, 3]]), values=array([b'jie', b'xiao', b'hua', b'wei', b'gong', b'zuo', b'san', b'nian'], dtype=object), dense_shape=array([3, 4]))
```
    可以看出，返回的 SparseTensorValue 对象中， values 才是我们需要的内容。``dense_shape`` 表示保存切分后元素的矩阵大小，我的输入有三个元素，切分后，三个元素分别为 2、2、4 个元素，所以最终至少需要 [3, 4] 大小的矩阵保存。 indices 表示 [3, 4] 中有效信息的索引，例如，[0, 0] 对应的是输入的第一个元素被切开后的第一个子串。

## Tensor Transformations

### Casting

#### tf.cast
* 功能
类型转换
* 描述
```
cast(
    x,
    dtype,
    name=None
)

Args:
x: A Tensor or SparseTensor.
dtype: The destination type.
name: A name for the operation (optional).

Returns:
A Tensor or SparseTensor with same shape as x.
```
* 示例
```python
$ ipython3
In [1]: import tensorflow as tf
In [2]: with tf.Session().as_default():
   ...:     tmp = tf.constant([1.1, 2.8], dtype=tf.float32)
   ...:     tmp.eval()
   ...:     tf.cast(tmp, tf.int32).eval()
Out[2]: array([ 1.10000002,  2.79999995], dtype=float32)
Out[2]: array([1, 2], dtype=int32)
```

#### tf.to_int64
* 功能
目前的理解等同于 tf.cast(x, dtype=int64)

### Shapes and Shaping

#### tf.reshape
* 功能
Reshape...
* 描述
```
reshape(
    tensor,
    shape,
    name=None
)

Args:
tensor: A Tensor.
shape: A Tensor. Must be one of the following types: int32, int64. Defines the shape of the output tensor.
name: A name for the operation (optional).

Returns:
A Tensor. Has the same type as tensor
```
* 示例
```python
$ ipython3
In [1]: import tensorflow as tf
In [2]: with tf.Session():
   ...:     tf.reshape(tf.range(12), [4, 3]).eval()
   ...:     tf.reshape(tf.range(12), [4, -1]).eval() # -1 时自动计算
   ...:     tf.reshape(tf.range(1), []).eval()  # 向量转标量
   ...:
Out[2]:
array([[ 0,  1,  2],
       [ 3,  4,  5],
       [ 6,  7,  8],
       [ 9, 10, 11]], dtype=int32)
Out[2]:
array([[ 0,  1,  2],
       [ 3,  4,  5],
       [ 6,  7,  8],
       [ 9, 10, 11]], dtype=int32)
Out[2]: 0
```

#### tf.size
* 功能
获取 tensor 中元素个数
* 描述
```
size(
    input,
    name=None,
    out_type=tf.int32
)

Args:
input: A Tensor or SparseTensor.
name: A name for the operation (optional).
out_type: (Optional) The specified output type of the operation (int32 or int64). Defaults to tf.int32.

Returns:
A Tensor of type out_type. Defaults to tf.int32.
```
* 示例
```python
$ ipython3
In [1]: import tensorflow as tf
In [2]: t = tf.constant([[[1, 1, 1], [2, 2, 2]], [[3, 3, 3], [4, 4, 4]]])
In [3]: with tf.Session() as sess:
   ...:     tf.size(t).eval()
Out[3]: 12
```

### Slicing and Joining

#### tf.concat
* 功能
按照某个维度连接 Tensor
* 描述
```
concat(
    values,
    axis,
    name='concat'
)

Args:
values: A list of Tensor objects or a single Tensor.
axis: 0-D int32 Tensor. Dimension along which to concatenate. Must be in the range [-rank(values), rank(values)).
name: A name for the operation (optional).

Returns:
A Tensor resulting from concatenation of the input tensors.
```
* 示例
```python
$ ipython3
In [1]: import tensorflow as tf
In [2]: t1 = tf.reshape(tf.range(6), [2, 3]) # [[0, 1, 2], [3, 4, 5]]
In [3]: t2 = tf.reshape(tf.range(6, 12), [2, 3]) # [[ 6,  7,  8], [ 9, 10, 11]]
In [4]: with tf.Session().as_default():
   ...:     tf.concat([t1, t2], 0).eval()
   ...:     tf.concat([t1, t2], 1).eval()
Out[4]:
array([[ 0,  1,  2],
       [ 3,  4,  5],
       [ 6,  7,  8],
       [ 9, 10, 11]], dtype=int32)
Out[4]:
array([[ 0,  1,  2,  6,  7,  8],
       [ 3,  4,  5,  9, 10, 11]], dtype=int32)
```

#### tf.reverse
* 功能
翻转 tensor 的某个维度中的元素
* 描述
```
reverse(
    tensor,
    axis,
    name=None
)

tensor: A Tensor. Must be one of the following types: uint8, int8, uint16, int16, int32, int64, bool, half, float32, float64, complex64, complex128, string. Up to 8-D.
axis:   A Tensor. Must be one of the following types: int32, int64. 1-D. The indices of the dimensions to reverse. Must be in the range [-rank(tensor), rank(tensor)).
name:   A name for the operation (optional).
```
* 示例
```python
$ ipython3
In [1]: import tensorflow as tf
In [2]: tmp = tf.reshape(tf.range(12), [1,2,2,3])
In [3]: with tf.Session().as_default():
   ...:     tmp.eval()
   ...:     tf.reverse(tmp, [1]).eval()
   ...:     tf.reverse(tmp, [-1]).eval()
   ...:     tf.reverse(tmp, [3]).eval()
   ...:     tf.reverse(tmp, [1, 2]).eval()
Out[3]:
array([[[[ 0,  1,  2],
         [ 3,  4,  5]],
        [[ 6,  7,  8],
         [ 9, 10, 11]]]], dtype=int32)
Out[3]:
array([[[[ 6,  7,  8],
         [ 9, 10, 11]],
        [[ 0,  1,  2],
         [ 3,  4,  5]]]], dtype=int32)
Out[3]:
array([[[[ 2,  1,  0],
         [ 5,  4,  3]],
        [[ 8,  7,  6],
         [11, 10,  9]]]], dtype=int32)
Out[3]:
array([[[[ 2,  1,  0],
         [ 5,  4,  3]],
        [[ 8,  7,  6],
         [11, 10,  9]]]], dtype=int32)
Out[3]:
array([[[[ 9, 10, 11],
         [ 6,  7,  8]],
        [[ 3,  4,  5],
         [ 0,  1,  2]]]], dtype=int32)
```

# tf.data

## tf.data.Dataset

### apply
* 功能
对 Dataset 的元素使用一个转换函数，转换函数目前多定义于 ``tf.contrib.data``
* 描述
```
apply(transformation_func)

Args:
transformation_func: A function that takes one Dataset argument and returns a Dataset.

Returns:
The Dataset returned by applying transformation_func to this dataset.
```
* 示例
参考 ``tf.contrib.data.group_by_window``

### filter
* 功能
过滤...
* 描述
```
filter(predicate)

Args:
predicate: A function mapping a nested structure of tensors (having shapes and types defined by self.output_shapes and self.output_types) to a scalar tf.bool tensor.

Returns:
A Dataset.
```
* 示例
```python
$ ipython3
In [1]: load /Users/jiexiao/workspace/tmp.py
In [2]: # %load /Users/jiexiao/workspace/tmp.py
   ...: import tensorflow as tf
   ...: from tensorflow.python.data import Dataset
   ...: def print_dataset(d):
   ...:     d_iter = d.make_one_shot_iterator()
   ...:     with tf.Session() as sess:
   ...:         while True:
   ...:             try:
   ...:                 print(sess.run(d_iter.get_next()))
   ...:             except tf.errors.OutOfRangeError:
   ...:                 break
In [3]: a = Dataset.range(11)
In [4]: print_dataset(a.filter(lambda x: x > 6))
7
8
9
10
```

### make_initializable_iterator
* 功能
创建一个 Dataset 的迭代器，可以对比 make_one_shot_iterator
* 描述
```
make_initializable_iterator(shared_name=None)

Args:
shared_name: (Optional.) If non-empty, the returned iterator will be shared under the given name across multiple sessions that share the same devices (e.g. when using a remote server).

Returns:
An Iterator over the elements of this dataset.
```
* 示例
```python
$ ipython
In [1]: from tensorflow.python.data import Dataset
In [2]: import tensorflow as tf
In [3]: dataset = Dataset.range(5)
In [4]: d_iter = dataset.make_initializable_iterator()
In [5]: with tf.Session() as sess:
   ...:     sess.run(d_iter.initializer)
   ...:     print(d_iter.get_next().eval())
   ...:     sess.run(d_iter.initializer)
   ...:     print(d_iter.get_next().eval())
   ...:
0
0
```

### make_one_shot_iterator
* 功能
创建一个 Dataset 的迭代器，可以对比 make_initializable_iterator, 主要区别是：返回的迭代器不能调用 initializer，所以只能遍历一次
* 描述
```
make_one_shot_iterator()
```
* 示例
```python
$ ipython
In [1]: from tensorflow.python.data import Dataset
In [2]: import tensorflow as tf
In [3]: dataset = Dataset.range(5)
In [4]: d_iter = dataset.make_one_shot_iterator()
In [5]: with tf.Session() as sess:
   ...:     print(d_iter.get_next().eval())
   ...:     print(d_iter.get_next().eval())
0
1
```

### map
* 功能
对 Dataset 中的所有元素执行指定函数
* 描述
```
map(
    map_func,
    num_parallel_calls=None
)

Args:
map_func: A function mapping a nested structure of tensors (having shapes and types defined by self.output_shapes and self.output_types) to another nested structure of tensors.
num_parallel_calls: (Optional.) A tf.int32 scalar tf.Tensor, representing the number elements to process in parallel. If not specified, elements will be processed sequentially.

Returns:
A Dataset.
```
* 示例
```python
$ ipython3
In [1]: load /Users/jiexiao/workspace/tmp.py
In [2]: # %load /Users/jiexiao/workspace/tmp.py
   ...: import tensorflow as tf
   ...: from tensorflow.python.data import Dataset
   ...: def print_dataset(d):
   ...:     d_iter = d.make_one_shot_iterator()
   ...:     with tf.Session() as sess:
   ...:         while True:
   ...:             try:
   ...:                 print(sess.run(d_iter.get_next()))
   ...:             except tf.errors.OutOfRangeError:
   ...:                 break
   ...: a = Dataset.range(1, 4) # {1, 2, 3}
In [3]: print_dataset(a.map(lambda x: x * 2))
2
4
6
```

### padded_batch
* 功能
将 Dataset 分为固定大小的 ``batch_size``, 同时将每个 batch 进行 padding，padding 长度默认为当前 batch 中的最大值
* 描述
```
padded_batch(
    batch_size,
    padded_shapes,
    padding_values=None
)

Args:
batch_size:     A tf.int64 scalar tf.Tensor, 每个 batch 的大小
padded_shapes:  Dataset 中每个数据的 shape，如果出现 tf.TensorShape([None]) 则表示 padding 至当前 batch 中的最大值
padding_values: (Optional.)  padding 的值，默认为 0 或者 ''

Returns:
A Dataset.
```
* 示例
```python
$ ipython
In [1]: load /root/workspace/tmp.py
In [2]: # %load /root/workspace/tmp.py
   ...: import tensorflow as tf
   ...: from tensorflow.python.data import Dataset
   ...: def print_dataset(d):
   ...:     d_iter = d.make_one_shot_iterator()
   ...:     with tf.Session() as sess:
   ...:         while True:
   ...:             try:
   ...:                 print(sess.run(d_iter.get_next()))
   ...:             except tf.errors.OutOfRangeError:
   ...:                 break
In [3]: dataset = tf.data.Dataset.range(10)
In [4]: dataset = dataset.map(lambda x: {'x': tf.fill([tf.cast(x, tf.int32)], x), 'y': tf.fill([tf.cast(x, tf.int32)], x)})
In [5]: print_dataset(dataset) # 这里有 10 个元素，且每个元素包含的子项不一样多
{'x': array([], dtype=int64), 'y': array([], dtype=int64)}
{'x': array([1]), 'y': array([1])}
{'x': array([2, 2]), 'y': array([2, 2])}
{'x': array([3, 3, 3]), 'y': array([3, 3, 3])}
{'x': array([4, 4, 4, 4]), 'y': array([4, 4, 4, 4])}
{'x': array([5, 5, 5, 5, 5]), 'y': array([5, 5, 5, 5, 5])}
{'x': array([6, 6, 6, 6, 6, 6]), 'y': array([6, 6, 6, 6, 6, 6])}
{'x': array([7, 7, 7, 7, 7, 7, 7]), 'y': array([7, 7, 7, 7, 7, 7, 7])}
{'x': array([8, 8, 8, 8, 8, 8, 8, 8]), 'y': array([8, 8, 8, 8, 8, 8, 8, 8])}
{'x': array([9, 9, 9, 9, 9, 9, 9, 9, 9]), 'y': array([9, 9, 9, 9, 9, 9, 9, 9, 9])}
In [6]: dataset = dataset.padded_batch(4, padded_shapes={'x': [None], 'y': [None]})
In [7]: print_dataset(dataset) # 这里只剩下 3 个 batch 了，每个 batch 中的元素的子项数量是一致的，都是当前 batch 中的最大值
{'x': array([[0, 0, 0],
       [1, 0, 0],
       [2, 2, 0],
       [3, 3, 3]]), 'y': array([[0, 0, 0],
       [1, 0, 0],
       [2, 2, 0],
       [3, 3, 3]])}
{'x': array([[4, 4, 4, 4, 0, 0, 0],
       [5, 5, 5, 5, 5, 0, 0],
       [6, 6, 6, 6, 6, 6, 0],
       [7, 7, 7, 7, 7, 7, 7]]), 'y': array([[4, 4, 4, 4, 0, 0, 0],
       [5, 5, 5, 5, 5, 0, 0],
       [6, 6, 6, 6, 6, 6, 0],
       [7, 7, 7, 7, 7, 7, 7]])}
{'x': array([[8, 8, 8, 8, 8, 8, 8, 8, 0],
       [9, 9, 9, 9, 9, 9, 9, 9, 9]]), 'y': array([[8, 8, 8, 8, 8, 8, 8, 8, 0],
       [9, 9, 9, 9, 9, 9, 9, 9, 9]])}
```

### prefetch
* 功能
个人感觉就是为了在性能和占用内存间选一个合适的界限
* 描述
```
prefetch(buffer_size)

Args:
buffer_size: A tf.int64 scalar tf.Tensor, representing the maximum number elements that will be buffered when prefetching.

Returns:
A Dataset.
```

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
### shuffle
* 功能
对 Dataset 中的数据进行重新排序
* 描述
```
shuffle(
    buffer_size,
    seed=None,
    reshuffle_each_iteration=None
)

Args:
buffer_size:              A tf.int64 scalar tf.Tensor, 目前的理解是用于内存管理，控制每次加载到内存中的元素个数
seed:                     (Optional.) A tf.int64 scalar tf.Tensor, representing the random seed that will be used to create the distribution. See tf.set_random_seed for behavior.
reshuffle_each_iteration: (Optional.) A boolean, which if true indicates that the dataset should be pseudorandomly reshuffled each time it is iterated over. (Defaults to True.)

Returns:
A Dataset.
```
    [buffer_size 使用场景](https://stackoverflow.com/questions/45124719/memory-management-in-tensorflows-dataset-api)
    [buffer_size 理解](https://stackoverflow.com/questions/46444018/meaning-of-buffer-size-in-dataset-map-dataset-prefetch-and-dataset-shuffle)
* 示例
```python
$ ipython3
Python 3.6.1 (default, Apr  4 2017, 09:40:21)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.1.0 -- An enhanced Interactive Python. Type '?' for help.
In [1]: load /Users/jiexiao/workspace/tmp.py
In [2]: # %load /Users/jiexiao/workspace/tmp.py
   ...: import tensorflow as tf
   ...: from tensorflow.python.data import Dataset
   ...: def print_dataset(d):
   ...:     d_iter = d.make_one_shot_iterator()
   ...:     with tf.Session() as sess:
   ...:         while True:
   ...:             try:
   ...:                 print(sess.run(d_iter.get_next()))
   ...:             except tf.errors.OutOfRangeError:
   ...:                 break
   ...: a = Dataset.range(1, 4) # {1, 2, 3}
In [3]: print_dataset(a.shuffle(10))
2
1
3
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
## tf.data.Iterator

### get_next
* 功能
通过 Iterator 从 Dataset 中取数据
* 描述
```
get_next(name=None)

Args:
name: (Optional.) A name for the created operation.

Returns:
A nested structure of tf.Tensor objects.
```
* 示例
```python
$ ipython
In [1]: from tensorflow.python.data import Dataset
In [2]: import tensorflow as tf
In [3]: dataset = Dataset.range(5)
In [4]: d_iter = dataset.make_one_shot_iterator()
In [5]: with tf.Session() as sess:
   ...:     print(d_iter.get_next().eval())
   ...:     print(d_iter.get_next().eval())
0
1
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

# tf.contrib.data

## tf.contrib.data.group_by_window
* 功能
将训练数据划分为多组，然后对每组数据进行 padding、shuffle、batch 等操作
* 描述
```
group_by_window(
    key_func,
    reduce_func,
    window_size=None,
    window_size_func=None
)

Args:
key_func: 将 Tensor 映射为一个 ID。典型场景：根据训练数据的输入输出长度，产生一个合适的 bucket id。
reduce_func: 从 Dataset 中取出 window_size 个元素，然后对这些元素进行 padding、shuffle、batch 等操作
window_size: 表示 window_size, 作为 reduce_func 的第一个参数传入，与 window_size_func 互斥
window_size_func: 通过 key_func 计算的 ID 来计算 window_size, 与 window_size 参数互斥

Returns:
A Dataset transformation function, which can be passed to tf.data.Dataset.apply.
```
* 示例
```python
$ ipython
In [1]: load /root/workspace/tmp.py
In [2]: # %load /root/workspace/tmp.py
   ...: import tensorflow as tf
   ...: from tensorflow.python.data import Dataset
   ...: def print_dataset(d):
   ...:     d_iter = d.make_one_shot_iterator()
   ...:     with tf.Session() as sess:
   ...:         while True:
   ...:             try:
   ...:                 print(sess.run(d_iter.get_next()))
   ...:             except tf.errors.OutOfRangeError:
   ...:                 break
In [3]: dataset = Dataset.range(12)
In [4]: dataset = dataset.apply(tf.contrib.data.group_by_window(key_func=lambda x: x%2, reduce_func=lambda x, els: els.batch(3), window_size=3))
In [5]: print_dataset(dataset) # 这里 window_size 为 3，所以首先从双数数列取了 3 个元素，划分为 1 个大小为 3 的  batch，然后从单数数列取了 3 个元素，重复...
[0 2 4]
[1 3 5]
[ 6  8 10]
[ 7  9 11]
In [6]: dataset = Dataset.range(12)
In [7]: dataset = dataset.apply(tf.contrib.data.group_by_window(key_func=lambda x: x%2, reduce_func=lambda x, els: els.batch(3), window_size=5))
In [8]: print_dataset(dataset) # 这里 window_size 为 5，所以首先从双数数列取了 5 个元素，划分为 1 个大小为 3 的 batch 和 1 个大小为 2 的 batch，然后从单数数列取了 5 个，重复...
[0 2 4]
[6 8]
[1 3 5]
[7 9]
[10]
[11]
```
	[stackoverflow 关于该函数使用的说明](https://stackoverflow.com/questions/45292517/how-do-i-use-the-group-by-window-function-in-tensorflow)

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
# 参考
[TensorFlow 全新的数据读取方式：Dataset API 入门教程](http://blog.csdn.net/linuxandroidwince/article/details/78551022)
