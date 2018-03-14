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

# tf.assert_negative

* 功能
断言 x 中所有值为负数

* 描述
    ```python
    tf.assert_negative(
        x,
        data=None,
        summarize=None,
        message=None,
        name=None
    )
    ```

* 示例
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

# tf.assert_positive

# tf.assert_proper_iterable

# tf.assert_non_negative

# tf.assert_non_positive

# tf.assert_equal

# tf.assert_integer

# tf.assert_less

# tf.assert_less_equal

# tf.assert_greater

# tf.assert_greater_equal

# tf.assert_rank

# tf.assert_rank_at_least

# tf.assert_type

# tf.is_non_decreasing

# tf.is_numeric_tensor

# tf.is_strictly_increasing

