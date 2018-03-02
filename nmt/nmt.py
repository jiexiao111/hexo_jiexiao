# coding=utf-8

import argparse
import sys
import warnings

warnings.filterwarnings("ignore")
import tensorflow as tf

import my_crash
from . import train
from . import inference
from .nmt_common_fn import *

FLAGS = None

@decorator_trace_call
def add_arguments(paser):
    """ 定义模型参数 """
    # 定义新的类型 bool
    paser.register('type', 'bool', lambda x: x.lower() == 'bool')

    """ 网络结构相关参数 """
    # 巧妙的利用了 nargs='?' 当指定 --residual 时为 True, 否则为 False
    paser.add_argument('--residual', type='bool', nargs='?', const=True, default=False, help='是否加入残差网络')

    """ 注意力结构相关参数 """

    """ 优化函数相关参数 """

    """ 初始化函数相关参数 """

    """ 词典相关参数 """

    """ 序列长度相关参数 """

    """ inference 相关参数 """

    """ 任务信息 """

    """ 其他 """

    """ 较少需要修改的参数 """

@decorator_trace_call
def create_hparams(flags):
    pass

@decorator_trace_call
def run_main(flags, default_hparams, train_fn, inference_fn):
    """ 开始训练 """


@decorator_trace_call
def main(unused_argv):
    default_hparams = create_hparams(FLAGS)
    train_fn = train.train
    inference_fn = inference.inference
    run_main(FLAGS, default_hparams, train_fn, inference_fn=inference_fn)

if __name__ == "__main__":
    nmt_parser = argparse.ArgumentParser()
    add_arguments(nmt_parser)
    FLAGS, unparsed = nmt_parser.parse_known_args()
    tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)
