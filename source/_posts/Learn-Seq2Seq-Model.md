---
title: Seq2Seq 模型分析及 Tensorflow NMT 源码分析
date: 2017-10-14 10:05:05
categories: 机器学习
tags:
  - Tensorflow
  - NLP
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
    nmt.py                       # 训练入口文件，主要实现参数解析
    train.py                     # 训练
    inference.py                 # 评估
    inference_test.py            # inference 单元测试
    model.py                     # 不带 Attention 结构的模型
    model_test.py                # model 单元测试
    attention_model.py           # 不指定 --attention_architecture 时，带 Attention 结构的模型
    gnmt_model.py                # --attention_architecture 被指定为 gnmt 或 gnmt_v2 时，带 Attention 结构的模型
    model_helper.py              # 构造模型的通用函数
    scripts                      #
        bleu.py                  # bleu 评分
        rouge.py                 #
    utils                        #
        __init__.py              # 模块
        iterator_utils.py        # 构造输入输出的通用函数
        iterator_utils_test.py   # iter 单元测试
        misc_utils.py            # 其他
        misc_utils_test.py       # misc 单元测试
        vocab_utils.py           # 构造词典
        vocab_utils_test.py      # vocab 单元测试
        evaluation_utils.py      # 预测相关
        evaluation_utils_test.py # eval 单元测试
        nmt_utils.py             # 翻译
        common_test_utils.py     # common 单元测试
```

# 参数说明

## network
```python
--num_units                    # 每层网络的神经元个数，默认 32，Demo 中使用了 128
--num_layers                   # 网络的深度，默认使用 2
--encoder_type                 # 编码层的结构，默认 uni（单向 RNN），可以选择 bi（双向 RNN），gnmt（单双混合）
--residual                     #
--time_major                   #
--num_embeddings_partitions    #
```
## attention mechanisms
```python
--attention                    # 不指定时，模型将不带有 Attantion 结构
--attention_architecture       # 指定 --attention 才能生效
--output_attention             #
--pass_hidden_state            #
```
## optimizer
```python
--optimizer                    #
--learning_rate                #
--warmup_steps                 #
--warmup_scheme                #
--start_decay_step             #
--decay_steps                  #
--decay_factor                 #
--learning_rate_decay_scheme   #
--num_train_steps              # 训练次数，默认 12000
--colocate_gradients_with_ops  #
```
## initializer
```python
--init_op                      # 模型初始化函数，默认 uniform, 可选 uniform | glorot_normal | glorot_uniform
--init_weight                  # 当 --init_op 为 uniform 时生效，默认为 0.1
```
## data
```python
--src                          # 源文件后缀
--tgt                          # 目标文件后缀
--train_prefix                 # 训练数据文件全路径，不包含后缀
--dev_prefix                   # 验证数据文件全路径，不包含后缀
--test_prefix                  # 测试数据文件全路径，不包含后缀
--out_dir                      # 模型存放目录
```
## Vocab
```python
--vocab_prefix                 # 词典文件全路径，不包含后缀
--sos                          # 句子开始的标记
--eos                          # 句子结束的标记
--share_vocab                  # 输入输出是否使用同一个字典
--check_special_token          #
```
## Sequence lengths
```python
--src_max_len                  # 训练输入数据的最大长度，默认 50
--tgt_max_len                  # 训练输出数据的最大长度，默认 50
--src_max_len_infer            #
--tgt_max_len_infer            #
```
## Default settings works well
```python
--unit_type                    #
--forget_bias                  #
--dropout                      # 默认 0.2
--max_gradient_norm            #
--source_reverse               #
--batch_size                   #
--steps_per_stats              # 每训练 N 次打印一次统计信息，默认 100
--max_train                    #
--num_buckets                  # 训练集分桶数量，默认 5
```
## SPM
```python
--subword_option               #
```
## Misc
```python
--num_gpus                     # GPU 个数，默认 1，默认情况下多 GPU 无法获得性能提升
--log_device_placement         #
--metrics                      # 翻译结果的评价函数，默认 bleu，可以多选，如，(bleu,rouge,accuracy)
--steps_per_external_eval      #
--scope                        #
--hparams_path                 #
--random_seed                  #
--override_loaded_hparams      # 如果不指定该参数，则训练参数从 hparams 文件中读取
```
## Inference
```python
--ckpt                         #
--inference_input_file         # 预测阶段的输入文件，用于区分训练和预测阶段
--inference_list               #
--infer_batch_size             #
--inference_output_file        #
--inference_ref_file           #
--beam_width                   # 暂时没搞懂意图，但是在 inference 后，将结果写入文件时，影响 --num_translations_per_input 参数
--length_penalty_weight        #
--num_translations_per_input   # 模型在 inference 过程中，推荐的输出个数
```
## Job info
```python
--jobid                        #
--num_workers                  #
```

# 函数调用关系
注意：如果要对照 ``Tensorboard`` 中的 ``Graph`` 看代码要记得在 ``Tensorboard`` 左侧的下拉选项中选择 ``train_log``, 否则看不到预处理相关节点

```python
main
  run_main
    create_or_load_hparams                               #
    train                                                #
      create_train_model                                 # 构建训练模型、输入输出、字典，指定 mode 为 TRAIN
        create_vocab_tables                              # 创建 token 与 id 的映射字典
        get_iterator                                     # 将训练数据处理成符合条件的输入输出
          key_func                                       # 训练数据按 bucket 分组
          key_func                                       # 训练数据按 bucket 分组
          BatchedInput                                   # 通过 name 访问 get_iterator 返回值的便利函数
        AttentionModel:__init__                          # model_creator 可能对应不同的 BaseModel 子类
          BaseModel:__init__                             # 构建训练模型
            get_initializer                              # 选择 Variable 的初始化函数
            BaseModel:init_embeddings                    # 创建 word embedding 矩阵
            BaseModel:build_graph                        # 构建 Seq2Seq 计算图
              Model:_build_encoder                       # 根据配置创建 uni/bi 结构的编码层，gnmt 结构重写了该函数
                _build_encoder_cell                      # 创建编码层，直接调用了 create_rnn_cell，目前无重写
                create_rnn_cell                          # 创建单层或者多层 RNN
                _cell_list                               # 创建多层 RNN
                _single_cell                             # 创建单层 RNN
              BaseModel:_build_decoder                   #
                BaseModel:_get_infer_maximum_iterations  #
                Model:_build_decoder_cell                # 每种模型都重写了该函数
              get_device_str                             #
              BaseModel:_compute_loss                    #
            BaseModel:_get_learning_rate_warmup          #
            BaseModel:_get_learning_rate_decay           #
            gradient_clip                                #
      create_eval_model                                  #
      create_infer_model                                 #
      load_data                                          #
      get_config_proto                                   #
      create_or_load_model                               #
      run_full_eval                                      #
        run_sample_decode                                # 抽样打印预测结果
          create_or_load_model                           # 加载 infer 模型
          _sample_decode                                 # 抽取一个测试集中的一个样本，输出 nmt 的预测结果
        run_internal_eval                                # 获取验证集、测试集的混淆值
          create_or_load_model                           # 加载 infer 模型
          _internal_eval                                 # 获取混淆值，写入 tensorborad，注意 eval 的数据在这里喂入
            compute_perplexity                           # 计算混淆值
              BaseModel:eval                             # 计算 eval_loss/predict_count/batch_size
              safe_exp                                   # 执行表达式，如果出现上溢则返回 inf
        run_external_eval                                # 计算测试和验证集的 bleu/rouge/accuracy
          create_or_load_model                           # 加载 infer 模型
            _external_eval #
        _format_results                                  # 格式化字符串，将 ppl/[bleu/rouge/accuracy] 的结果格式化
      init_stats                                         #
      update_stats                                       #
      check_stats                                        #
      add_summary                                        #
```

# API 说明
## BatchedInput
* 功能
没有实现直接继承了 collections.namedtuple。 如果返回原始的 tuple， 则仅能通过 index 访问 item 。collections.namedtuple 可以通过 item 的 name 进行访问。可以将 namedtuple 理解为 c 中的 struct 结构，其首先将各个 item 命名，然后对每个 item 赋予数据。
* 示例
```python
$ ipython3
In [1]: import collections
In [2]: coordinate = collections.namedtuple('Collections', ['x', 'y'])
In [4]: co = coordinate(10, 20)
In [5]: co.x
Out[5]: 10
In [6]: co.y
Out[6]: 20
```
## get_iterator
* 功能
产生训练数据，需要注意的是仅当调用 BatchedInput.initializer 才会重新执行 shuffle/padding/batch 等数据预处理。而每次使用 BatchedInput 的其他任意成员都会默认调用 tf.data.Iterator 的 get_next() 函数

* 示例
```python
$ ipython
In [1]: import tensorflow as tf
In [2]: from tensorflow.python.data import Dataset
In [3]: dataset = Dataset.range(5)
In [4]: dataset = dataset.map(lambda x: (x, x))
In [5]: d_iter = dataset.make_one_shot_iterator()
In [6]: x, y = d_iter.get_next()
In [7]: sess = tf.Session()
In [8]: sess.run(x)
Out[8]: 0
In [9]: sess.run(x)
Out[9]: 1
In [10]: sess.run(y) # 前两次获取 x 第三次获取 y，但是 y 已经取到了 2，说明前两次 sess.run(x) 隐含调用了 get_next()
Out[10]: 2
In [12]: sess.run((x, y))
Out[12]: (3, 3)
In [13]: sess.run((x, y)) # 这里说明，每次 sess.run 才会调用一次 get_next()，而不是获取一次 x 或者 y 的值调用一次 get_next()
Out[13]: (4, 4)
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
