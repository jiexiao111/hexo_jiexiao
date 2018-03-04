# coding=utf-8

import tensorflow as tf
from ..nmt_common_fn import *

@decorator_trace_call
def get_config_proto(log_device_placement=False, allow_soft_placement=True, num_intra_threads=0, num_inter_threads=0):
    # log_device_placement: 是否打印设备分配日志
    # allow_soft_placement： 是否允许 Tensorflow 自行分配设备
    config_proto = tf.ConfigProto(log_device_placement=log_device_placement, allow_soft_placement=allow_soft_placement)
    # 刚开始分配少量显存，然后按需增加，由于不会释放，会导致碎片产生
    config_proto.gpu_options.allow_growth = True

    if num_intra_threads:
        config_proto.intra_op_parallelism_threads = num_intra_threads
    if num_inter_threads:
        config_proto.inter_op_parallelism_threads = num_inter_threads

    return config_proto
