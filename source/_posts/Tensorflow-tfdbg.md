---
title: Tensorflow tfdbg
date: 2017-10-17 19:26:06
tags:
---

{% note default %}
Tensorflow 中使用 python 描述计算图，再使用 C++ 后端进行训练时就非常不容跟踪调试，
Tensorflow 提供了 tfdbg 模块用于解决这个问题，但是网上的资料较少，所以将自己的一些理解写出来供参考
{% endnote %}

<!--more-->

---

# 启用 tfdbg

[官网上](https://www.tensorflow.org/programmers_guide/debugger) 关于 tfdbug 的使用说的非常清楚，仅需要在创建 session 后，使用 session 前加入以下代码：
```python
from tensorflow.python import debug as tf_debug
sess = tf_debug.LocalCLIDebugWrapperSession(sess)
```
然后像往常一样启动你的训练模型即可，启动后，可以看到以下界面：
![启动界面](/images/Tensorflow-tfdbg/Tensorflow-tfdbg_1.png)

---

# tfdbg 基本使用

## 开始调试
为了方便说明，就使用官方教程中的例子，执行以下命令：
```bash
python -m tensorflow.python.debug.examples.debug_mnist --debug
```
*注意：该例子会在第一次执行时从网上下载训练数据，务必保证能访问网络资源，公司内部的同事就需要配置代理*

* 第一步一般都是输入命令：``run`` 就可以看到以下界面了
![运行](/images/Tensorflow-tfdbg/Tensorflow-tfdbg_2.png)

## print_tensor
执行 ``run`` 之后，我们可以点击 ``list_tensors`` 列表中的带下划线的文字了，例如，点击 ``hidden/Wx_plus_b/MatMuls:0`` 就可以看到以下界面
![print_tensor](/images/Tensorflow-tfdbg/Tensorflow-tfdbg_3.png)

* 第一个问题，这个矩阵表示什么呢？
    首先，在``/usr/local/lib/python3.6/site-packages/tensorflow/python/debug/examples/debug_mnist.py``中找到对应的代码
    ```python
    def nn_layer(input_tensor, input_dim, output_dim, layer_name, act=tf.nn.relu):
        """Reusable code for making a simple neural net layer."""
        # Adding a name scope ensures logical grouping of the layers in the graph.
        with tf.name_scope(layer_name):
        # This Variable will hold the state of the weights for the layer
        with tf.name_scope("weights"):
            weights = weight_variable([input_dim, output_dim])
        with tf.name_scope("biases"):
            biases = bias_variable([output_dim])
        with tf.name_scope("Wx_plus_b"):
            preactivate = tf.matmul(input_tensor, weights) + biases

        activations = act(preactivate)
        return activations
    ```
    其实，这个矩阵就是 ``preactivate`` 的值，为什么这里不直接显示 ``preactivate`` 的变量名呢？ 因为 Tensorflow 的后端根本不知道这个局部变量，后端能获取的只有 Tensor（比如 tf.Variable） 或者 Option（比如 tf.matmul）, 所以，我们得出结论，点击 ``list_tensors`` 列表中的 Tensor/Option 后，显示的就是这个 Tensor 的值或者 Option 的运算结果和维度信息，这对我们理解模型相当有帮助，比如，有些难以理解的运算我们可以根据运算结果演算一遍。

* 第二个问题，``hidden/Wx_plus_b/MatMuls:0`` 是怎么和代码对应起来的？
    Tensorflow 中，所有的 Tensor/Option 都有唯一的名字，命名的规则是 ``tf.name_scope + name 参数``
    ```python
    with tf.name_scope("Any_Scope"):
        with tf.name_scope("First_Scope"):
            V1 = tf.Variable(shape, name='First')
        with tf.name_scope("Second_Scope"):
            V2 = tf.Variable(shape)
            V3 = tf.Variable(shape)
    ```
    这段代码中，V1/V2/V3 对应的 Tensor 的名字分别为：``Any_Scope/First_Scope/First``、``Any_Scope/Second_Scope/Variable``、``Any_Scope/Second_Scope/Variable_1`` 可以看出，如果不指定 ``name 参数`` 则默认为 Tensor/Option 的类名，如果相同 Scope 中有相同 name 的 Tensor/Option 则自动为名称添加序号
    在问题一中，``layer_name`` 为 ``hidden``，所以 ``preactivate = tf.matmul(input_tensor, weights) + biases`` 的名称就是 ``hidden/Wx_plus_b/MatMuls:0``


## node_info
### 输入及输出信息
点击 ``hidden/Wx_plus_b/MatMuls:0`` 后默认显示的就是上一小节提到的 ``print_tensor``，此时我们可以点击 ``node_info``，点击后显示以下信息：
![node_info](/images/Tensorflow-tfdbg/Tensorflow-tfdbg_4.png)
红框中的信息包括：1、MatMul 操作通过 cpu 执行 2、两个操作数分别为训练的输入数据 ``x-input`` 和表示权重的 ``Variable`` 3、输出的结果被用于加法操作
### 调用栈信息
此时可以按 ``pagedown`` 向下滑动，查看代码调用栈：
![callstack](/images/Tensorflow-tfdbg/Tensorflow-tfdbg_5.png)
清晰的展示出，``main`` 函数调用了 ``nn_layer`` 函数，然后执行了 87 行的 MatMuls 操作，同时，如果不清楚库函数定义所在的文件，也可以在这里找到。
### 当前代码行对应的其他 Tensor/Option
此时，可以点击 ``Line:  87``, 就可以看到 87 行相关的其他 Tensor/Option 的信息了
![other_tensor](/images/Tensorflow-tfdbg/Tensorflow-tfdbg_6.png)
``nn_layer`` 一共被调用了两次，且 87 行包含了两个操作 （MatMuls、add）, 所以一共是四个 Option 信息，此时，点击 ``softmax/Wx_plus_b/MatMuls:0`` 可以看到以下信息：
![list_inputs](/images/Tensorflow-tfdbg/Tensorflow-tfdbg_7.png)

## list_inputs
点击 ``list_inputs`` 可以看到 ``softmax/Wx_plus_b/MatMuls:0`` 详细输入：
![list_inputs](/images/Tensorflow-tfdbg/Tensorflow-tfdbg_8.png)
可以看出，``softmax/Wx_plus_b/MatMuls:0`` 的左操作数是 ``hidden/Relu``， 右操作数是 ``softmax/weights/Variable/read``，``hidden/Relu`` 只有一个操作数 ``hidden/Wx_plus_b/add``, 依次类推，可以查看计算 ``softmax/Wx_plus_b/MatMuls:0`` 的每一步操作

## list_outputs
点击 ``list_outputs`` 可以看到 ``softmax/Wx_plus_b/MatMuls:0`` 的输出的详细用途：
![list_output](/images/Tensorflow-tfdbg/Tensorflow-tfdbg_9.png)
首先，输出被用于 ``softmax/Wx_plus_b/MatMuls``，依次类推，最终被用于加权平均

## run_info
点击 ``run_info`` 可以看到以下信息：
![run_info](/images/Tensorflow-tfdbg/Tensorflow-tfdbg_10.png)
这里可以点击红框部分查看训练 / 测试样本的输入 / 输出

# 单步运行
输入 ``s`` 就可以单步调试了，``s -t 10`` 可以执行 10 步，需要注意的是，一定是执行 ``run`` 命令后才可以执行 ``s`` 命令
![step](/images/Tensorflow-tfdbg/Tensorflow-tfdbg_11.png)

# 理解记忆调试命令
鼠标点击能查看的信息毕竟有限，直接看 help 又不好理解，好在 tfdbg 中始终会显示当前显示信息所对应的命令：
![step](/images/Tensorflow-tfdbg/Tensorflow-tfdbg_13.png)
很明显 ``pt`` 就表示 ``print_tensor``，如果需要了解 ``pt`` 的更多参数，就可以执行 ``help pt``
![step](/images/Tensorflow-tfdbg/Tensorflow-tfdbg_12.png)
我们可以试试 ``pt -a accuracy/accuracy/Cast:0``
![step](/images/Tensorflow-tfdbg/Tensorflow-tfdbg_14.png)


