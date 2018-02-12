# coding=utf-8

import argparse
import sys
import warnings

warnings.filterwarnings("ignore")
import tensorflow as tf

from . import train
from . import inference
from .nmt_common_fn import *

FLAGS = None

@decorator_trace_call
def add_arguments(paser):
    pass

@decorator_trace_call
def create_hparams(flags):
    pass

@decorator_trace_call
def run_main(flags, default_hparams, train_fn, inference_fn):
    pass

@decorator_trace_call
def main(unused_argv):
    default_hparams = create_hparams(FLAGS)
    train_fn = train.train
    inference_fn = inference.inference
    run_main(FLAGS, default_hparams, train_fn, inference_fn)

if __name__ == "__main__":
    nmt_parser = argparse.ArgumentParser()
    add_arguments(nmt_parser)
    FLAGS, unparsed = nmt_parser.parse_known_args()
    tf.app.run(main=main, argv=[sys.argv[0]])
