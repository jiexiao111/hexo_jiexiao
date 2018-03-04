# coding=utf-8

import argparse
import sys
import warnings
import random

warnings.filterwarnings("ignore")
import tensorflow as tf
import numpy as np

import my_crash
from . import train
from . import inference
from .nmt_common_fn import *
from .utils import misc_utils as utils

FLAGS = None

@decorator_trace_call
def add_arguments(parser):
    """ 定义模型参数 """
    # 定义新的类型 bool
    parser.register('type', 'bool', lambda x: x.lower() == 'bool')

    """ 网络结构相关参数 """
    # 巧妙的利用了 nargs='?' 当指定 --residual 时为 True, 否则为 False
    parser.add_argument('--residual', type='bool', nargs='?', const=True, default=False, help='是否加入残差网络')
    parser.add_argument('--encoder_type', type=str, default="uni", help="uni 表示单向RNN，bi 表示双向 RNN，gnmt， gnmt 单双向 RNN 混合，\
                        默认为 uni，可选择：uni | bi | gnmt")

    """ 注意力结构相关参数 """
    parser.add_argument("--attention", type=str, default="", help='指定 attention 的类型，即不使用 attention 机制，默认为 ""， \
                        可选择：luong | scaled_luong | bahdanau | normed_bahdanau')
    parser.add_argument("--attention_architecture", type=str, default="standard", help="默认 standard，可选择：standard | gnmt | gnmt_v2")

    """ 调优相关参数 """
    parser.add_argument("--num_train_steps", type=int, default=12000, help="训练的 steps 数，默认 12000")

    """ 初始化函数相关参数 """

    """ 训练数据相关参数 """
    parser.add_argument("--out_dir", type=str, default=None, required=True, help="模型及日志保存的目录")
    parser.add_argument("--src", type=str, default=None, help="输入文件的后缀，如：en")
    parser.add_argument("--tgt", type=str, default=None, help="输出文件的后缀，如：de")
    parser.add_argument("--train_prefix", type=str, default=None, help="训练集的前缀")
    parser.add_argument("--dev_prefix", type=str, default=None, help="验证集的前缀")
    parser.add_argument("--test_prefix", type=str, default=None, help="测试集的前缀")

    """ 词典相关参数 """

    """ 序列长度相关参数 """

    """ inference 相关参数 """
    parser.add_argument("--inference_input_file", type=str, default=None, help="区分 inference/train 过程的标识，指定用于 inference 的输入文件")

    """ 任务信息 """
    parser.add_argument("--jobid", type=int, default=0, help="当前任务的ID，默认 0")
    parser.add_argument("--num_workers", type=int, default=1, help="总的任务个数, inference 过程中有效，默认 1")
    parser.add_argument("--num_inter_threads", type=int, default=0, help="inter_op_parallelism_threads 的值，\
                        默认 0 表示由 Tensorflow 自行决定，表示多个运算符op并行程度")
    parser.add_argument("--num_intra_threads", type=int, default=0, help="intra_op_parallelism_threads 的值，\
                        默认 0，表示有 Tensorflow 自行决定，表示运算符op内部的并行程度")

    """ 其他 """
    parser.add_argument("--random_seed", type=int, default=None, help="随机数种子，须大于零")
    parser.add_argument("--hparams_path", type=str, default=None, help="指定参数文件路径，便于使用之前的设置的参数")
    parser.add_argument("--log_device_placement", type="bool", nargs="?", const=True, default=False, help="开启后，调试 GPU 内存分配")
    parser.add_argument("--steps_per_external_eval", type=int, default=None, help="每隔N步，做一次 external eval，默认为 50 * steps_per_stats")
    parser.add_argument("--avg_ckpts", type="bool", nargs="?", const=True, default=False, help="开启后，将对最近保存的 N 个模型做 external eval，并求平均")

    """ 较少需要修改的参数 """
    parser.add_argument("--steps_per_stats", type=int, default=100, help="每隔N步打印统计信息，打印 10次统计信息保存一次模型，并做一次 eval，默认 100")

@decorator_trace_call
def create_hparams(flags):
    return tf.contrib.training.HParams(
        # 网络结构相关参数
        residual = flags.residual,
        encoder_type = flags.encoder_type,

        # 注意力结构相关参数
        attention = flags.attention,
        attention_architecture = flags.attention_architecture,

        # 调优相关参数
        num_train_steps = flags.num_train_steps,

        # 初始化函数相关参数

        # 训练数据相关参数
        out_dir = flags.out_dir,
        src = flags.src,
        tgt = flags.tgt,
        train_prefix = flags.train_prefix,
        dev_prefix = flags.dev_prefix,
        test_prefix = flags.test_prefix,

        # 词典相关参数

        # 序列长度相关参数

        # inference 相关参数

        # 任务信息
        num_inter_threads = flags.num_inter_threads,
        num_intra_threads = flags.num_intra_threads,

        # 其他
        random_seed = flags.random_seed,
        log_device_placement = flags.log_device_placement,
        steps_per_external_eval = flags.steps_per_external_eval,
        avg_ckpts = flags.avg_ckpts,

        # 较少需要修改的参数
        steps_per_stats = flags.steps_per_stats
    )

@decorator_trace_call
def create_or_load_hparams(out_dir, default_hparams, hparams_path, save_hparams=True):
    """ 创建或者加载参数 """
    return default_hparams

@decorator_trace_call
def run_main(flags, default_hparams, train_fn, inference_fn):
    """ 开始训练 """
    # 设置 jobid
    jobid = flags.jobid
    num_workers = flags.num_workers
    print_out("# JobID: %d" % jobid)

    # 指定随机数的种子
    random_seed = flags.random_seed
    if random_seed is not None and random_seed > 0:
        print_out("# Random Seed: %d" % random_seed)
        random.seed(random_seed + jobid)
        np.random.seed(random_seed + jobid)

    # 创建模型及日志保存的目录
    out_dir = flags.out_dir
    if not tf.gfile.Exists(out_dir): tf.gfile.MakeDirs(out_dir)

    # 加载 / 新建参数
    hparams = create_or_load_hparams(out_dir, default_hparams, flags.hparams_path, save_hparams=(flags.jobid == 0))

    if flags.inference_input_file:
        inference_fn()
    else:
        train_fn(hparams)


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
