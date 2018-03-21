---
title: Tensorflow API 整理：Asserts and boolean checks
date: 2018-03-14 15:11:15
categories: 机器学习
tags:
  - Tensorflow
---

{% note default %}
Asserts and boolean checks
{% endnote %}

<!--more-->

---

## tf.assert_negative

### 功能

断言 x 中所有值为负数

### 描述


```python
tf.assert_negative(
    x,
    data=None,
    summarize=None,
    message=None,
    name=None
)
```

### 示例

正常执行


```python
import tensorflow as tf
tmp = tf.fill([2,3], -9)
with tf.control_dependencies([tf.assert_negative(tmp)]):
    output = tf.reduce_sum(tmp)
with tf.Session().as_default():
    output.eval()
```

触发断言


```python
import tensorflow as tf
tmp = tf.fill([2,3], 9)
with tf.control_dependencies([tf.assert_negative(tmp)]):
    output = tf.reduce_sum(tmp)
with tf.Session().as_default():
    output.eval()
```

* data: 触发断言时，需要打印的 Tensor
* summarize:data 中每个 Tensor 打印的元素个数
* message: 打印信息前缀
* name:op 名称


```python
import tensorflow as tf

tmp = tf.fill([2, 3], 9)
tmp1 = tf.fill([2, 3], -9)

with tf.control_dependencies([tf.assert_negative(tmp, [tmp, tmp1], summarize=5, message='jiexiao', name='assert_ng')]):
    output2 = tf.reduce_sum(tmp)

with tf.Session().as_default():
    output2.eval()
```

## tf.assert_positive

### 功能

断言 x 中所有值为整数

### 描述


```python
tf.assert_positive(
    x,
    data=None,
    summarize=None,
    message=None,
    name=None
)
```

### 示例

参考 tf.assert_negative

## tf.assert_proper_iterable

### 功能

判断 values 是不是一个合适的迭代器，如果 values 是一个 Tensor, SparseTensor, np.array, tf.compat.bytes_or_texts_types 则报错。或者不是迭代器也报错。
这个函数时有用处的，因为张量 Tensor 或者数组 np.array 本身也是可迭代的 (iterable).

### 描述


```python
tf.assert_proper_iterable(values)
```

### 示例

不清楚什么类型能够不触发断言


```python
import tensorflow as tf
tmp = tf.fill([2,3], -9)
with tf.control_dependencies([tf.assert_proper_iterable(tmp)]):
    output = tf.reduce_sum(tmp)
with tf.Session().as_default():
    output.eval()
```

## tf.assert_non_positve

### 功能

断言 x 中的所有值非正

### 描述


```python
tf.assert_non_positive(
    x,
    data=None,
    summarize=None,
    message=None,
    name=None
)
```

### 示例

参考 tf.assert_negative

## tf.assert_non_negative

### 功能

断言 x 中的所有值非负

### 描述


```python
tf.assert_non_negative(
    x,
    data=None,
    summarize=None,
    message=None,
    name=None
)
```

### 示例

参考 tf.assert_negative

## tf.assert_equal

### 功能

断言 x 和 y 中的所有元素值一样

### 描述


```python
tf.assert_equal(
    x,
    y,
    data=None,
    summarize=None,
    message=None,
    name=None
)
```

### 示例

正常执行


```python
import tensorflow as tf

tmp_1 = tf.fill([3,3], 9)
tmp_2 = tf.fill([3,3], 9)
with tf.control_dependencies([tf.assert_equal(tmp_1, tmp_2)]):
    output = tf.reduce_sum(tmp_1)
with tf.Session().as_default():
    output.eval()
```

触发断言


```python
import tensorflow as tf

tmp_1 = tf.fill([3,3], 9)
tmp_2 = tf.fill([3,3], 8)
with tf.control_dependencies([tf.assert_equal(tmp_1, tmp_2)]):
    output = tf.reduce_sum(tmp_1)
with tf.Session().as_default():
    output.eval()
```

## tf.assert_integer

### 功能

断言 x 中的每个元素的类型为整型

### 描述


```python
tf.assert_integer(
    x,
    message=None,
    name=None
)
```

### 示例

正常执行


```python
import tensorflow as tf
tmp = tf.fill([3,3], 9)
with tf.control_dependencies([tf.assert_integer(tmp)]):
    output = tf.reduce_sum(tmp)
with tf.Session().as_default():
    output.eval()
```




    81



触发断言


```python
import tensorflow as tf
tmp = tf.fill([3,3], 9.0)
with tf.control_dependencies([tf.assert_integer(tmp)]):
    output = tf.reduce_sum(tmp)
with tf.Session().as_default():
    output.eval()
```

## tf.assert_less

### 功能

断言 x 中的每个元素小于 y 中的相同位置的元素

### 描述


```python
tf.assert_less(
    x,
    y,
    data=None,
    summarize=None,
    message=None,
    name=None
)
```

### 示例

正常执行


```python
import tensorflow as tf
tmp_1 = tf.constant([1, 9, 3, 4])
tmp_2 = tf.constant([0, 8, 2, 3])
with tf.control_dependencies([tf.assert_less(tmp_2, tmp_1)]):
    output = tf.reduce_sum(tmp_1)
with tf.Session().as_default():
    output.eval()
```




    17



触发断言


```python
import tensorflow as tf
tmp_1 = tf.constant([1, 8, 3, 4])
tmp_2 = tf.constant([0, 8, 2, 3])
with tf.control_dependencies([tf.assert_less(tmp_2, tmp_1)]):
    output = tf.reduce_sum(tmp_1)
with tf.Session().as_default():
    output.eval()
```

## tf.assert_less_equal

### 功能

断言 x 中的每个元素小于等于 y 中的相同位置的元素

### 描述


```python
tf.assert_less_equal(
    x,
    y,
    data=None,
    summarize=None,
    message=None,
    name=None
)
```

### 示例

参考 tf.assert_less

## tf.assert_greater

### 功能

断言 x 中的每个元素大于 y 中的相同位置的元素

### 描述


```python
tf.assert_greater(
    x,
    y,
    data=None,
    summarize=None,
    message=None,
    name=None
)
```

### 示例

参考 tf.assert_less

## tf.assert_greater_equal

### 功能

断言 x 中的每个元素大于等于 y 中的相同位置的元素

### 描述


```python
tf.assert_greater_equal(
    x,
    y,
    data=None,
    summarize=None,
    message=None,
    name=None
)
```

### 示例

参考 tf.assert_less

## tf.assert_rank

### 功能

断言 x 的维度等于 rank

### 描述


```python
tf.assert_rank(
    x,
    rank,
    data=None,
    summarize=None,
    message=None,
    name=None
)
```

### 示例

正常执行


```python
import tensorflow as tf
tmp = tf.fill([3, 3], 9)
with tf.control_dependencies([tf.assert_rank(tmp, 2)]):
    output = tf.reduce_sum(tmp)
with tf.Session().as_default():
    output.eval()
```

触发断言


```python
import tensorflow as tf
tmp = tf.fill([3, 3, 3], 9)
with tf.control_dependencies([tf.assert_rank(tmp, 2)]):
    output = tf.reduce_sum(tmp)
with tf.Session().as_default():
    output.eval()
```

## tf.assert_rank_at_least

### 功能

断言 x 的维度大于等于 rank

### 描述


```python
tf.assert_rank_at_least(
    x,
    rank,
    data=None,
    summarize=None,
    message=None,
    name=None
)
```

### 示例

参考 tf.assert_rank

## tf.assert_type

### 功能

断言 x 中元素的类型为 tf_type

### 描述


```python
tf.assert_type(
    tensor,
    tf_type,
    message=None,
    name=None
)
```

### 示例

正常执行


```python
import tensorflow as tf
tmp = tf.fill([3, 3], 9)
with tf.control_dependencies([tf.assert_type(tmp, tf.int32)]):
    output = tf.reduce_sum(tmp)
with tf.Session().as_default():
    output.eval()
```

触发断言


```python
import tensorflow as tf
tmp = tf.fill([3, 3], 9.0)
with tf.control_dependencies([tf.assert_type(tmp, tf.int32)]):
    output = tf.reduce_sum(tmp)
with tf.Session().as_default():
    output.eval()
```

## tf.is_non_decreasing

### 功能

判断 x 中不存在递减的片段

### 描述


```python
tf.is_non_decreasing(
    x,
    name=None
)
```

### 示例


```python
import tensorflow as tf
tmp = tf.constant([1, 2, 2, 4])
output = tf.cond(tf.is_non_decreasing(tmp), lambda: tf.add(tmp, 20), lambda: tf.add(tmp, 2))
with tf.Session().as_default():
    output.eval()
```




    array([21, 22, 22, 24], dtype=int32)




```python
import tensorflow as tf
tmp = tf.constant([1, 3, 2, 4])
output = tf.cond(tf.is_non_decreasing(tmp), lambda: tf.add(tmp, 20), lambda: tf.add(tmp, 2))
with tf.Session().as_default():
    output.eval()
```




    array([3, 5, 4, 6], dtype=int32)



## tf.is_numeric_tensor

### 功能

判断 x 的类型为 tensor 且 tensor 的类型为数值型

### 描述


```python
tf.is_numeric_tensor(tensor)
```

### 示例


```python
import tensorflow as tf
output = tf.constant([1, 2, 2, 4])
if tf.is_numeric_tensor(output):
    output = tf.add(output, 20)
with tf.Session().as_default():
    output.eval()
```




    array([21, 22, 22, 24], dtype=int32)




```python
import tensorflow as tf
output = tf.constant([1, 2, 2, 4])
if tf.is_numeric_tensor(1):
    output = tf.add(output, 20)
with tf.Session().as_default():
    output.eval()
```




    array([1, 2, 2, 4], dtype=int32)



## tf.is_strictly_increasing

### 功能

断言 x 中是严格递增的

### 描述


```python
tf.is_strictly_increasing(
    x,
    name=None
)
```

### 示例


```python
import tensorflow as tf
output = tf.constant([1, 2, 2, 4])
output = tf.cond(tf.is_strictly_increasing(output), lambda: tf.add(output, 20), lambda: tf.add(output, 2))
with tf.Session().as_default():
    output.eval()
```




    array([3, 4, 4, 6], dtype=int32)




```python
import tensorflow as tf
output = tf.constant([1, 2, 3, 4])
output = tf.cond(tf.is_strictly_increasing(output), lambda: tf.add(output, 20), lambda: tf.add(output, 2))
with tf.Session().as_default():
    output.eval()
```




    array([21, 22, 23, 24], dtype=int32)


