# coding: UTF-8

import os
import numpy as np
import struct
import pickle
import PIL.Image
from numpy.ctypeslib import ndpointer
from ctypes import *
from keras.preprocessing import image
from skimage import exposure, filters
import skimage.morphology as sm

train_gnt_dir = '/aiml/data/Handwriting_Recognition/HWDB1.1trn_gnt/'
test_gnt_dir = '/aiml/data/Handwriting_Recognition/HWDB1.1tst_gnt/'

train_dir = '/aiml/data/train/'
test_dir = '/aiml/data/test/'

# 读取图像和对应的汉字
def read_from_gnt_dir(gnt_dir=train_gnt_dir):
    def one_file(f):
        header_size = 10
        while True:
            header = np.fromfile(f, dtype='uint8', count=header_size)
            if not header.size: break
            sample_size = header[0] + (header[1]<<8) + (header[2]<<16) + (header[3]<<24)
            tagcode = header[5] + (header[4]<<8)
            width = header[6] + (header[7]<<8)
            height = header[8] + (header[9]<<8)
            if header_size + width*height != sample_size:
                break
            image = np.fromfile(f, dtype='uint8', count=width*height).reshape((height, width))
            yield image, tagcode

    for file_name in os.listdir(gnt_dir):
        if file_name.endswith('.gnt'):
            file_path = os.path.join(gnt_dir, file_name)
            with open(file_path, 'rb') as f:
                for image, tagcode in one_file(f):
                    yield image, tagcode

# 建立图像分类的字典
def create_dict(gnt_dir=train_gnt_dir):
    char_set = set()
    for _, tagcode in read_from_gnt_dir(gnt_dir):
        tagcode_unicode = struct.pack('>H', tagcode).decode('gb2312')
        char_set.add(tagcode_unicode)
    char_list = list(char_set)
    char_dict = dict(zip(sorted(char_list), range(len(char_list))))
    print("Len dict: %d" % len(char_dict))
    f = open('char_dict.pkl', 'wb')
    pickle.dump(char_dict, f)
    f.close()
    return char_dict

def resize_with_c(origin_img):
# 转化为 ctyes 类型的输入
    height, width = origin_img.shape
    origin_img = origin_img.flatten()
    origin_img = np.array(origin_img).astype(np.uint16)
    origin_img_ctype = (c_ubyte * len(origin_img))()
    for i in np.arange(len(origin_img)):
        origin_img_ctype[i]= int(origin_img[i])

    # 调用 C++ 接口处理
    pdll = CDLL('./code/HCCR_v5/resize_img.so')
    pdll.process.argtypes = [c_ubyte * len(origin_img), c_ushort, c_ushort]
    pdll.process.restype = ndpointer(dtype=c_int, shape=(64, 64))
    resize_img = pdll.process(origin_img_ctype, width, height)

    # 将输出转化为 np.array
    return resize_img

# 生成训练数据
x_train_once = []
def create_image_dir(gnt_dir, dst_dir, char_dict, flag=False):
    train_counter = 0
    for image, tagcode in read_from_gnt_dir(gnt_dir):
        tagcode_unicode = struct.pack('>H', tagcode).decode('gb2312')
        resize_img = resize_with_c(image)
        if resize_img.shape != (64, 64):
            print("Error resize!")
        if flag:
            x_train_once.append(resize_img)
        im = PIL.Image.fromarray(resize_img)
        dir_name = dst_dir + '%0.5d'%char_dict[tagcode_unicode]
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        im.convert('L').save(dir_name+'/' + str(train_counter) + '.png')
        train_counter += 1
        if train_counter % 10000 == 0:
            print("Create file: %d" % train_counter)
    return train_counter

def preprocess_1(x):
    x = filters.gaussian(x, sigma=1)
    x = exposure.rescale_intensity(x)
    return x

def preprocess_2(x):
    x = sm.dilation(x, sm.square(2))
    x = exposure.rescale_intensity(x)
    return x

def preprocess_3(x):
    x = filters.gaussian(x, sigma=1)
    x = sm.dilation(x, sm.square(2))
    x = exposure.rescale_intensity(x)
    return x

# TODO 浮点
def return_0_2():
    return random.random() * 2

# TODO 整数
def return_1_3():
    return random.randint(1,3)

def preprocess_4(x):
    x = filters.gaussian(x, sigma=return_0_2())
    x = exposure.rescale_intensity(x)
    return x

def preprocess_5(x):
    x = sm.dilation(x, sm.square(return_1_3()))
    x = exposure.rescale_intensity(x)
    return x

def preprocess_6(x):
    x = filters.gaussian(x, sigma=return_0_2())
    x = sm.dilation(x, sm.square(return_1_3()))
    x = exposure.rescale_intensity(x)
    return x

def prepare_data(pix, batch_size):
    # 生成训练集
    if os.path.exists(train_gnt_dir):
        # 生成分类字典
        char_dict = create_dict()
        counter = create_image_dir(train_gnt_dir, train_dir, char_dict)
        print("Finish create train data: %d." % counter)
    else:
        print("Cannot find train gnt: " + train_gnt_dir)

    # 生成测试集
    if os.path.exists(test_gnt_dir):
        counter = create_image_dir(test_gnt_dir, test_dir, char_dict)
        print("Finish create test data: %d." % counter)
    else:
        print("Cannot find test gnt: " + test_gnt_dir)

    print("Finish create_image_dir.")

    train_data = image.ImageDataGenerator(preprocessing_function=preprocess_1)
    test_data = image.ImageDataGenerator(preprocessing_function=preprocess_1)

    train_gen = train_data.flow_from_directory(train_dir, color_mode='grayscale', target_size=(pix, pix), batch_size=batch_size)
    test_gen = train_data.flow_from_directory(test_dir, color_mode='grayscale', target_size=(pix, pix), batch_size=batch_size)
    print("Finish create ImageDataGenerator.")

    # 类别数量
    if hasattr(train_gen, 'num_classes'):
        num_class = train_gen.num_classes
    else:
        num_class = train_gen.num_class

    # 训练样本数量
    num_train = train_gen.n

    # 测试样本数量
    num_test = test_gen.n

    # 确认读取的图片的格式/取值范围
    image_sample = train_gen.next()[0]
    image_shape = image_sample.shape
    image_max = np.max(image_sample)
    image_min = np.min(image_sample)

    # 查看返回的标签类型，“categorical” 表示为 one-hot 标签
    print("Target Type: " + train_gen.class_mode)
    print("Total class: %d" % num_class)
    print("Total train sample: %d, test sample: %d.: " % (num_train, num_test))
    print("Input shape: " + str(image_shape))
    print("Image value: [%d, %d]" % (image_min, image_max))

    return train_gen, test_gen, num_class

if __name__=='__main__':

    # 生成分类字典
    char_dict = create_dict()

    # 生成训练集
    if os.path.exists(train_gnt_dir):
        counter = create_image_dir(train_gnt_dir, train_dir, char_dict, True)
        print("Finish create train data: %d." % counter)
    else:
        print("Cannot find train gnt: " + train_gnt_dir)

    x_train_once = np.expand_dims(x_train_once,1)
    mean_px = x_train_once.mean().astype(np.float32)
    std_px = x_train_once.std().astype(np.float32)

    # 生成测试集
    if os.path.exists(test_gnt_dir):
        counter = create_image_dir(test_gnt_dir, test_dir, char_dict)
        print("Finish create test data: %d." % counter)
    else:
        print("Cannot find test gnt: " + test_gnt_dir)

    print("Mean: %f STD: %f" % (mean_px, std_px))
    print("Finish create_image_dir.")
