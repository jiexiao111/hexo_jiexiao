# coding: UTF-8

import os
from keras.optimizers import Nadam, Adam, SGD
from keras.callbacks import TensorBoard, ModelCheckpoint
from keras.models import load_model
from python_code.resnet_20 import build_resnet
from python_code.prepare_data import prepare_data
import argparse

parser = argparse.ArgumentParser("HCCR")
parser.add_argument('-batch_size', type=int, default=100)
parser.add_argument('-learn_rate', type=float, default=0.1)
parser.add_argument('-learn_decay', type=float, default=0.0001)
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

print("Begin prepare data.")
# 准备数据
train_gen, test_gen, num_class = prepare_data(pix, batch_size)

print("Begin build model.")
# 构建模型
model = build_resnet((pix, pix, 1), num_class)
model.compile(SGD(lr=learn_rate, momentum=learn_momentum, decay=learn_decay, nesterov=learn_nesterov),
              loss='categorical_crossentropy', metrics=['accuracy'])


# 设置每个 epoch 的回调操作
log_dir = '/aiml/dfs/checkpoint/train/'
weights_name = os.path.join(log_dir , 'weights.hdf5')
check_cb = ModelCheckpoint(filepath=weights_name, verbose=1, save_best_only=True)
board_cb = TensorBoard(log_dir=log_dir, histogram_freq=False, write_graph=False, write_images=False)

# 开始训练
print("Begin train.")
print("batch_size: %d, learn_rate: %f, learn_decay: %f" % (batch_size, learn_rate, learn_decay))
model.fit_generator(train_gen, steps_per_epoch=steps_per_epoch, epochs=max_epochs,
                    validation_data=test_gen, validation_steps=steps_per_test,
                    callbacks=[check_cb, board_cb])
