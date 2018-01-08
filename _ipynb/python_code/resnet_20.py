from __future__ import division
from keras.layers import Input, Activation
from keras.layers import Conv2D, MaxPooling2D
from keras.units import plot_model
from keras.initializers import TruncatedNormal
from keras import backend as K

CONV_W_INIT =  TruncatedNormal(stddev=0.118)

def identity_block(input_tensor, kernel_size, filters, strides, kernel_initializers, padding, stage, block):
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
    stride1， stride2 = strides
    # 权重初始化函数
    init1, init2 = kernel_initializers
    # padding方式
    pad1, pad2 = paddings
    # 各层的名字
    conv_name_base = 'res' + str(stage) + block + '_branch'
    bn_name_base = 'bn' + str(stage) + block + '_branch'

    short_tensor = Activation('relu')(input_tensor)

    x = Conv2D(filters1, kernel_size1, padding=pad1, strides=stride1
               kernel_initializer=init1, name=conv_name_base + '2a')(input_tensor)
    x = BatchNormalization(axis=bn_axis, name=bn_name_base + '2a')(x)
    x = Activation('relu')(x)

    x = Conv2D(filters2, kernel_size2, padding=pad2, strides=stride2
               kernel_initializer=init2, name=conv_name_base + '2b')(x)
    x = BatchNormalization(axis=bn_axis, name=bn_name_base + '2b')(x)

    x = layers.add([short_tensor, x])
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
    stride1， stride2, stride3 = strides
    # 权重初始化函数
    init1, init2, init3 = kernel_initializers
    # padding方式
    pad1, pad2, pad3 = paddings
    # 各层的名字
    conv_name_base = 'res' + str(stage) + block + '_branch'
    bn_name_base = 'bn' + str(stage) + block + '_branch'


    input_tensor = Activation('relu')(input_tensor)

    shortcut = Conv2D(filters1, kernel_size1, padding=pad1, strides=stride1,
                      kernel_initializer=init1, name=conv_name_base + '2a')(input_tensor)
    shortcut = BatchNormalization(axis=bn_axis, name=bn_name_base + '2a')(shortcut)

    x = Conv2D(filters2, kernel_size2, padding=pad2, strides=stride2,
               kernel_initializer=init2, name=conv_name_base + '2b')(input_tensor)
    x = BatchNormalization(axis=bn_axis, name=bn_name_base + '2b')(x)
    x = Activation('relu')(x)

    x = Conv2D(filters3, kernel_size3, padding=pad3, strides=stride3,
               kernel_initializer=init3, name=conv_name_base + '2c')(input_tensor)
    x = BatchNormalization(axis=bn_axis, name=bn_name_base + '2c')(x)

    x = layers.add([shortcut, x])
    return x

def build_resnet(input_shape, num_outputs):

    if K.image_data_format() == 'channels_last':
        bn_axis = 3
    else:
        bn_axis = 1

    data1 = Input(shape=input_shape)

    x = identity_block(data1, [3, 3, 3], [16, 16, 16], stage=1, block='a')



def check_print():
    # 建立 ResNet_20
    model=build_resnet((28, 28, 1), 10)

    # 打印网络数据概况
    model.summary()

    # 打印模型结构
    plot_model(model,to_file='ResNet.png')


if __name__=='__main__':
    check_print()
