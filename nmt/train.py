# coding=utf-8

import os
import time

import tensorflow as tf

from .nmt_common_fn import *
from . import model as nmt_model
from . import attention_model
from . import gnmt_model
from . import model_helper
from . import inference
from .utils import misc_utils as utils

@decorator_trace_call
def train(hparams, scope=None, target_session=""):
    log_device_placement = hparams.log_device_placement
    out_dir = hparams.out_dir
    num_train_steps = hparams.num_train_steps
    steps_per_stats = hparams.steps_per_stats
    steps_per_external_eval = hparams.steps_per_external_eval
    steps_per_eval = 10 * hparams.steps_per_stats
    avg_ckpts = hparams.avg_ckpts
    model_dir = hparams.out_dir
    summary_name = "train_log"

    # 设置 steps_per_external 的默认值
    if not steps_per_external_eval: steps_per_external_eval = 5 * steps_per_eval

    # 根据配置决定网络模型
    if not hparams.attention:
        model_creator = nmt_model.Model
    else:
        if hparams.encoder_type == 'gnmt' or hparams.attention_architecture in ['gnmt', 'gnmt_v2']:
            model_creator = gnmt_model.GNMTModel
        elif hparams.attention_architecture  == 'standard':
            model_creator = attention_model.AttentionModel
        else:
            raise ValueError("Unkown architecture: %s" % hparams.attention_architecture)

    # 创建模型
    train_model = model_helper.create_train_model(model_creator, hparams, scope)
    infer_model = model_helper.create_infer_model(model_creator, hparams, scope)
    eval_model = model_helper.create_eval_model(model_creator, hparams, scope)

    # 加载验证集
    dev_src_file = "%s.%s" % (hparams.dev_prefix, hparams.src)
    dev_tgt_file = "%s.%s" % (hparams.dev_prefix, hparams.tgt)
    sample_src_data = inference.load_data(dev_src_file)
    sample_tgt_data = inference.load_data(dev_tgt_file)

    # 生成 Log 文件
    log_file = os.path.join(out_dir, "log_%d" % time.time())
    log_f = tf.gfile.GFile(log_file, mode="a")
    print_out("# log_file: %s" % log_file, log_f)

    # 创建 Session，train/eval/infer 为三个不同的 Session
    config_proto = utils.get_config_proto(log_device_placement=log_device_placement,
                                          num_intra_threads=hparams.num_intra_threads,
                                          num_inter_threads=hparams.num_inter_threads)
    train_sess = tf.Session(target=target_session, config=config_proto, graph=train_model.graph)

