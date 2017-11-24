---
title: Seq2Seq 模型分析及 Tensorflow NMT 源码分析
date: 2017-10-14 10:05:05
tags:
---

{% note default %}
近期主要任务为使用 Seq2Seq 模型，记录一些资料
{% endnote %}

<!--more-->

---

# 目录结构
[Tensorflow 的 NMT 项目 github 地址](https://github.com/tensorflow/nmt#encoder)
```python
nmt
->  nmt.py                       === >  训练入口文件
->  train.py                     === >
->  model.py                     === >  不带 Attention 结构的模型
->  attention_model.py           === >  不指定 --attention_architecture 时，带 Attention 结构的模型
->  gnmt_model.py                === >  --attention_architecture 被指定为 gnmt 或 gnmt_v2 时，带 Attention 结构的模型
->  model_test.py                === >
->  inference_test.py            === >
->  model_helper.py              === >
->  inference.py                 === >
->  scripts                      === >
    ->  bleu.py                  === >
    ->  rouge.py                 === >
->  utils                        === >
    ->  iterator_utils.py        === >
    ->  __init__.py              === >
    ->  misc_utils_test.py       === >
    ->  misc_utils.py            === >
    ->  vocab_utils.py           === >
    ->  evaluation_utils_test.py === >
    ->  common_test_utils.py     === >
    ->  iterator_utils_test.py   === >
    ->  vocab_utils_test.py      === >
    ->  nmt_utils.py             === >
    ->  evaluation_utils.py      === >
```

# 参数说明
```python
# 训练阶段参数：
--attention              不指定时，模型将不带有 Attantion 结构
--attention_architecture 指定 --attention 才能生效
# 预测阶段参数：
--inference_input_file   预测阶段的输入文件，用于区分训练和预测阶段
```

# 函数调用关系
nmt.py
train.py
model.py
model_helper.py
utils
attention_model.py

main
run_main
create_or_load_hparams
train
create_train_model
create_vocab_tables
get_iterator
AttentionModel:__init__
BaseModel:__init__
get_initializer
BaseModel:init_embeddings
BaseModel:build_graph
BaseModel:_get_learning_rate_warmup
BaseModel:_get_learning_rate_decay
gradient_clip
Model:_build_encoder
BaseModel:_build_decoder
get_device_str
BaseModel:_compute_loss


```

# 参考资料
论文：
seq2seq 第一篇文章
``1409.3215.pdf``

加入 context vector，可以处理变长数据
``1406.1078.pdf``

加入 attention 机制
``1508.04025.pdf``

官网介绍：
[https://www.tensorflow.org/tutorials/seq2seq]
其他：
[seq2seq 学习笔记](http://blog.csdn.net/Jerr__y/article/details/53749693)
[tensorflow 学习笔记（十一）：seq2seq Model 相关接口介绍](http://blog.csdn.net/u012436149/article/details/52976413)
[深度学习笔记（六）：Encoder-Decoder 模型和 Attention 模型](http://blog.csdn.net/u014595019/article/details/52826423)
[seq2seq 入门](http://www.jianshu.com/p/1d3de928f40c)
[Tensorflow 源码解读（一）：Attention Seq2Seq 模型](https://zhuanlan.zhihu.com/p/27769667)
[从 Encoder 到 Decoder 实现 Seq2Seq 模型](https://zhuanlan.zhihu.com/p/27608348)
[序列到序列的语言翻译模型代码 (tensorflow) 解析](https://www.grt1st.cn/posts/seq2seq-code/)
[谷歌神经网络机器翻译 NMT：人人可利用 TensorFlow 快速建立翻译模型（附教程）](http://www.sohu.com/a/157050254_642762)
