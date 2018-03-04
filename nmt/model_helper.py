# coding=utf-8

from .nmt_common_fn import *

@decorator_trace_call
def create_train_model(model_creator, hparams, scope=None, num_workers=1, jobid=0, extra_args=None):
    pass

@decorator_trace_call
def create_infer_model(model_creator, hparams, scope=None, extra_args=None):
    pass

@decorator_trace_call
def create_eval_model(model_creator, hparams, scope=None, extra_args=None):
    pass
