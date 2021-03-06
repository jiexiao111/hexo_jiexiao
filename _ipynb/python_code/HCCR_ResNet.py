# coding: UTF-8

import os
from keras.optimizers import Nadam, Adam, SGD
from keras.callbacks import TensorBoard, ModelCheckpoint, ReduceLROnPlateau
from keras.models import load_model
from resnet_20 import build_resnet
from prepare_data import prepare_data
from ResNet_Keras import ResnetBuilder
import argparse

parser = argparse.ArgumentParser("HCCR")
parser.add_argument('-batch_size', type=int, default=100)
parser.add_argument('-learn_rate', type=float, default=0.1)
parser.add_argument('-learn_decay', type=float, default=0.0001)
parser.add_argument('-gaus_trn_max', type=int, default=-1)
parser.add_argument('-gaus_trn_min', type=int, default=-1)
parser.add_argument('-gaus_tst', type=int, default=-1)
parser.add_argument('-dila_trn_max', type=int, default=-1)
parser.add_argument('-dila_trn_min', type=int, default=-1)
parser.add_argument('-dila_tst', type=int, default=-1)
parser.add_argument('-rescale_intensity', action='store_true', default=False)
parser.add_argument('-threshold_otsu', action='store_true', default=False)
parser.add_argument('-norm_input', action='store_true', default=False)
parser.add_argument('-load_model_name', type=str, default="None")
parser.add_argument('-resnet_type', type=str, default="Resnet20")
flag = parser.parse_args()

batch_size = flag.batch_size
learn_rate = flag.learn_rate
learn_momentum = 0.9
learn_decay = flag.learn_decay
learn_nesterov = True
steps_per_epoch = 1000
steps_per_test = 100
max_epochs = 20000
pix = 64
load_model_name = flag.load_model_name
resnet_type = flag.resnet_type

print("Begin prepare data.")
# 准备数据
pre_config ={}
pre_config['gaussian_train_max'] = flag.gaus_trn_max
pre_config['gaussian_train_min'] = flag.gaus_trn_min
pre_config['gaussian_test'] = flag.gaus_tst
pre_config['dilation_train_max'] = flag.dila_trn_max
pre_config['dilation_train_min'] = flag.dila_trn_min
pre_config['dilation_test'] = flag.dila_tst
pre_config['rescale_intensity'] = flag.rescale_intensity
pre_config['threshold_otsu'] = flag.threshold_otsu
pre_config['norm_input'] = flag.norm_input
train_gen, test_gen, num_class = prepare_data(pix, batch_size, pre_config)

print("Begin build model.")
# 构建模型
if resnet_type == "Resnet20":
    model = build_resnet((pix, pix, 1), num_class)
    model.compile(SGD(lr=learn_rate, momentum=learn_momentum, decay=learn_decay, nesterov=learn_nesterov),
                  loss='categorical_crossentropy', metrics=['accuracy'])
    print("Build Resnet20.")
else:
    model = ResnetBuilder.build_resnet_18((pix, pix, 1), num_class)
    model.compile(Adam(), loss='categorical_crossentropy', metrics=['accuracy'])s
    print("Build Resnet18.")



# 设置每个 epoch 的回调操作
log_dir = '/aiml/dfs/checkpoint/train/'
log_dir = os.path.join(log_dir, load_model_name)
weights_name = os.path.join(log_dir , "weights-{epoch:02d}-{val_acc:.2f}.hdf5")
reduce_cb = ReduceLROnPlateau(patience=4, verbose=1)
check_cb = ModelCheckpoint(weights_name, verbose=1, save_best_only=True)
board_cb = TensorBoard(log_dir=log_dir, histogram_freq=False, write_graph=False, write_images=False)

# 开始训练
print("Begin train.")
print("batch_size: %d, learn_rate: %f, learn_decay: %f" % (batch_size, learn_rate, learn_decay))
# weights_file = '/aiml/code/weights.hdf5'
weights_file = load_model_name + '.hdf5'
if os.path.exists(weights_file):
    print("Load weights." + weights_file)
    model.load_weights(weights_file)
model.fit_generator(train_gen, steps_per_epoch=steps_per_epoch, epochs=max_epochs,
                    validation_data=test_gen, validation_steps=steps_per_test,
                    callbacks=[check_cb, board_cb, reduce_cb])
