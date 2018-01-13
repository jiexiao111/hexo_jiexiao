# coding: UTF-8

from __future__ import division
from keras import layers
from keras import backend as K
from keras.models import Model
from keras.layers import Input, Activation, BatchNormalization, Flatten, Dense
from keras.layers import Conv2D, MaxPooling2D, AveragePooling2D
from keras.utils import plot_model
from keras.initializers import TruncatedNormal

CONV_W_INIT =  TruncatedNormal(stddev=0.118)

def identity_block(input_tensor, kernel_size, filters, strides, kernel_initializers, paddings, stage, block):
    # BatchNormal 的操作维度
    if K.image_data_format() == 'channels_last':
        bn_axis = 3
    else:
        bn_axis = 1
    # 卷积核的数量
    filters1, filters2 = filters
    # 卷积核的长宽
    kernel_size1, kernel_size2 = kernel_size
    # 卷积步长
    stride1, stride2 = strides
    # 权重初始化函数
    init1, init2 = kernel_initializers
    # padding方式
    pad1, pad2 = paddings
    # 各层的名字
    conv_name_base = 'res' + str(stage) + block + '_branch'
    bn_name_base = 'bn' + str(stage) + block + '_branch'

    x = Conv2D(filters1, kernel_size1, padding=pad1, strides=stride1,
               kernel_initializer=init1, name=conv_name_base + '2a')(input_tensor)
    x = BatchNormalization(axis=bn_axis, name=bn_name_base + '2a')(x)
    x = Activation('relu')(x)

    x = Conv2D(filters2, kernel_size2, padding=pad2, strides=stride2,
               kernel_initializer=init2, name=conv_name_base + '2b')(x)
    x = BatchNormalization(axis=bn_axis, name=bn_name_base + '2b')(x)

    x = layers.add([input_tensor, x])
    x = Activation('relu')(x)
    return x

def conv_block(input_tensor, kernel_size, filters, strides, kernel_initializers, paddings, stage, block):
    # BatchNormal 的操作维度
    if K.image_data_format() == 'channels_last':
        bn_axis = 3
    else:
        bn_axis = 1
    # 卷积核的数量
    filters1, filters2, filters3 = filters
    # 卷积核的长宽
    kernel_size1, kernel_size2, kernel_size3 = kernel_size
    # 卷积步长
    stride1, stride2, stride3 = strides
    # 权重初始化函数
    init1, init2, init3 = kernel_initializers
    # padding方式
    pad1, pad2, pad3 = paddings
    # 各层的名字
    conv_name_base = 'res' + str(stage) + block + '_branch'
    bn_name_base = 'bn' + str(stage) + block + '_branch'

    shortcut = Conv2D(filters1, kernel_size1, padding=pad1, strides=stride1,
                      kernel_initializer=init1, name=conv_name_base + '2a')(input_tensor)
    shortcut = BatchNormalization(axis=bn_axis, name=bn_name_base + '2a')(shortcut)

    x = Conv2D(filters2, kernel_size2, padding=pad2, strides=stride2,
               kernel_initializer=init2, name=conv_name_base + '2b')(input_tensor)
    x = BatchNormalization(axis=bn_axis, name=bn_name_base + '2b')(x)
    x = Activation('relu')(x)

    x = Conv2D(filters3, kernel_size3, padding=pad3, strides=stride3,
               kernel_initializer=init3, name=conv_name_base + '2c')(x)
    x = BatchNormalization(axis=bn_axis, name=bn_name_base + '2c')(x)

    x = layers.add([shortcut, x])
    x = Activation('relu')(x)
    return x

def build_resnet(input_shape, num_outputs):

    if K.image_data_format() == 'channels_last':
        bn_axis = 3
    else:
        bn_axis = 1

    img_input = Input(shape=input_shape)
    x = Conv2D(16, [3, 3], strides=1, padding='same',
               kernel_initializer=TruncatedNormal(stddev=0.118), name='conv1')(img_input)
    x = BatchNormalization(axis=bn_axis, name='bn_conv1')(x)
    x = Activation('relu')(x)

    x = identity_block(x, kernel_size=[3, 3], filters=[16, 16],
                       strides=[1, 1], paddings=['same', 'same'],
                       kernel_initializers=[TruncatedNormal(stddev=0.118), TruncatedNormal(stddev=0.118)],
                       stage=1, block='a')
    x = identity_block(x, kernel_size=[3, 3], filters=[16, 16],
                       strides=[1, 1], paddings=['same', 'same'],
                       kernel_initializers=[TruncatedNormal(stddev=0.118), TruncatedNormal(stddev=0.118)],
                       stage=1, block='b')
    x = identity_block(x, kernel_size=[3, 3], filters=[16, 16],
                       strides=[1, 1], paddings=['same', 'same'],
                       kernel_initializers=[TruncatedNormal(stddev=0.118), TruncatedNormal(stddev=0.118)],
                       stage=1, block='c')

    x = conv_block(x, kernel_size=[1, 3, 3], filters=[32,32, 32],
                   strides=[2, 2, 1], paddings=['valid', 'same', 'same'],
                   kernel_initializers=[TruncatedNormal(stddev=0.25),
                                        TruncatedNormal(stddev=0.083),
                                        TruncatedNormal(stddev=0.083)],
                   stage=2, block='a')
    x = identity_block(x, kernel_size=[3, 3], filters=[32, 32],
                       strides=[1, 1], paddings=['same', 'same'],
                       kernel_initializers=[TruncatedNormal(stddev=0.083), TruncatedNormal(stddev=0.083)],
                       stage=2, block='b')
    x = identity_block(x, kernel_size=[3, 3], filters=[32, 32],
                       strides=[1, 1], paddings=['same', 'same'],
                       kernel_initializers=[TruncatedNormal(stddev=0.083), TruncatedNormal(stddev=0.083)],
                       stage=2, block='c')

    x = conv_block(x, kernel_size=[1, 3, 3], filters=[64, 64, 64],
                   strides=[2, 2, 1], paddings=['valid', 'same', 'same'],
                   kernel_initializers=[TruncatedNormal(stddev=0.176776695297),
                                        TruncatedNormal(stddev=0.059),
                                        TruncatedNormal(stddev=0.059)],
                   stage=3, block='a')
    x = identity_block(x, kernel_size=[3, 3], filters=[64, 64],
                       strides=[1, 1], paddings=['same', 'same'],
                       kernel_initializers=[TruncatedNormal(stddev=0.059), TruncatedNormal(stddev=0.059)],
                       stage=3, block='b')
    x = identity_block(x, kernel_size=[3, 3], filters=[64, 64],
                       strides=[1, 1], paddings=['same', 'same'],
                       kernel_initializers=[TruncatedNormal(stddev=0.059), TruncatedNormal(stddev=0.059)],
                       stage=3, block='c')

    x = AveragePooling2D((3, 3), name='avg_pool')(x)
    x = Flatten()(x)
    x = Dense(num_outputs, activation='softmax', name='output',
              kernel_initializer=TruncatedNormal(stddev=0.01))(x)
    model = Model(img_input, x, name='resnet20')
    return model

def check_print():
    # 建立 ResNet_20
    model=build_resnet((28, 28, 1), 10)

    # 打印网络数据概况
    model.summary()

    # 打印模型结构
    plot_model(model,to_file='ResNet.png')

if __name__=='__main__':
    check_print()
