# coding: UTF-8

import os
import numpy as np
import struct
import random
import pickle
import scipy
import PIL.Image
from numpy.ctypeslib import ndpointer
from ctypes import *
from keras.preprocessing import image
from skimage import exposure, filters
import skimage.morphology as sm
from multiprocessing import Pool


train_gnt_dir = '/aiml/data/Handwriting_Recognition/HWDB1.1trn_gnt/'
test_gnt_dir = '/aiml/data/Handwriting_Recognition/HWDB1.1tst_gnt/'

train_zip = '/aiml/data/train.zip'
test_zip = '/aiml/data/test.zip'

train_dir = '/aiml/data/train/'
test_dir = '/aiml/data/test/'

DEBUG = True
if not DEBUG:
    infer_dir = '/aiml/data/'
else:
    infer_dir = '/aiml/data/test_bak/00002'

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
    print("Start create dict.")
    if os.path.exists('char_dict.pkl'):
        f = open('char_dict.pkl', 'rb')
        char_dict = pickle.load(f)
        print("Dict file is exists.")
        return char_dict
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

def resize_with_python(img):
    # 补方
    pad_size = abs(img.shape[0]-img.shape[1]) // 2
    if img.shape[0] < img.shape[1]:
        pad_dims = ((pad_size, pad_size), (0, 0))
    else:
        pad_dims = ((0, 0), (pad_size, pad_size))
        img = np.lib.pad(img, pad_dims, mode='constant', constant_values=255)
    # 缩放
    img = scipy.misc.imresize(img, (64 - 4*2, 64 - 4*2))
    img = np.lib.pad(img, ((4, 4), (4, 4)), mode='constant', constant_values=255)
    assert img.shape == (64, 64)

    return img

# 来不及了，能用就行
pdll = None
def resize_with_c(origin_img):
    # 转化为 ctyes 类型的输入
    height, width = origin_img.shape
    origin_img = origin_img.flatten()
    origin_img = np.array(origin_img).astype(np.uint16)
    origin_img_ctype = (c_ubyte * len(origin_img))()
    for i in np.arange(len(origin_img)):
        origin_img_ctype[i]= int(origin_img[i])

    global pdll
    if not pdll:
        print("Hell")
        # 调用 C++ 接口处理
        so_file = '/aiml/code/resize_img.so'
        if not os.path.exists(so_file):
            so_file = './resize_img.so'
        if not os.path.exists(so_file):
            so_file = './code/HCCR_v5/resize_img.so'
        pdll = CDLL(so_file)

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
        resize_img = resize_with_python(image)
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
    return x

def unzip_cb(x):
    os.system('unzip %s -d %s' % (x[0], x[1]))

# 全局变量虽然丑，但是 Keras 的回调函数怎么传参数确实不知道
global_config = {}

def preprocess_fun(x, gaussian_sigma, dilation_square, threshold_otsu, rescale_intensity, norm_input):
    if norm_input:
        std_px = 63.556923
        mean_px = 222.517471
        x = x - mean_px / std_px
    if threshold_otsu:
        thresh = filters.threshold_otsu(x) #返回一个阈值
        x = (x <= thresh )* 1.0 #根据阈值进行分割
    if gaussian_sigma > 0:
        x = exposure.rescale_intensity(x)
        x = filters.gaussian(x, sigma=gaussian_sigma)
    if dilation_square > 0:
        x = sm.dilation(x.reshape(64, 64), sm.square(dilation_square))
        x = x.reshape(64, 64, 1)
    if rescale_intensity:
        x = exposure.rescale_intensity(x)
    return x

def train_preprocess(x):
    global global_config
    gaussian_train_max = global_config['gaussian_train_max']
    gaussian_train_min = global_config['gaussian_train_min']
    gaussian_test = global_config['gaussian_test']
    dilation_train_max = global_config['dilation_train_max']
    dilation_train_min = global_config['dilation_train_min']
    dilation_test = global_config['dilation_test']
    rescale_intensity = global_config['rescale_intensity']
    threshold_otsu = global_config['threshold_otsu']
    norm_input = global_config['norm_input']

    if gaussian_train_max > 0:
        gaussian_sigma = random.random() * gaussian_train_max
    else:
        gaussian_sigma = gaussian_test

    if dilation_train_max > 0:
        dilation_square = random.randint(dilation_train_min, dilation_train_max)
    else:
        dilation_square = dilation_test

    x = preprocess_fun(x, gaussian_sigma, dilation_square,
                       threshold_otsu, rescale_intensity, norm_input)

    return x

def test_preprocess(x):
    global global_config
    gaussian_test = global_config['gaussian_test']
    dilation_test = global_config['dilation_test']
    rescale_intensity = global_config['rescale_intensity']
    threshold_otsu = global_config['threshold_otsu']
    norm_input = global_config['norm_input']

    x = preprocess_fun(x, gaussian_test, dilation_test,
                       threshold_otsu, rescale_intensity, norm_input)
    return x

def prepare_data(pix, batch_size, pre_config):
    global global_config
    global_config = pre_config
    print(global_config)
    # 解压数据集
    if os.path.exists(train_zip) and not os.path.exists(train_dir):
        pool = Pool(2)
        pool.map(unzip_cb, [(test_zip, '/aiml/data'), (train_zip, '/aiml/data')])

    # 生成训练集
    if os.path.exists(train_gnt_dir) and not os.path.exists(train_dir):
        # 生成分类字典
        char_dict = create_dict()
        counter = create_image_dir(train_gnt_dir, train_dir, char_dict)
        print("Finish create train data: %d." % counter)
    else:
        print("Cannot find train gnt: " + train_gnt_dir)

    # 生成测试集
    if os.path.exists(test_gnt_dir) and not os.path.exists(test_dir):
        counter = create_image_dir(test_gnt_dir, test_dir, char_dict)
        print("Finish create test data: %d." % counter)
    else:
        print("Cannot find test gnt: " + test_gnt_dir)

    print("Finish create_image_dir.")

    train_data = image.ImageDataGenerator(preprocessing_function=train_preprocess)
    test_data = image.ImageDataGenerator(preprocessing_function=test_preprocess)

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
    print("Total train sample: %d, test sample: %d." % (num_train, num_test))
    print("Input shape: " + str(image_shape))
    print("Image value: [%d, %d]" % (image_min, image_max))

    return train_gen, test_gen, num_class

def get_resize_pixs(resize_fun):
    img_list = []
    if DEBUG:
        file_names = os.listdir(infer_dir)
    else:
        file_names = [str(x) + '.png' for x in np.arange(500) + 1]

    for file_name in file_names:
        image_origin = PIL.Image.open(os.path.join(infer_dir, file_name))
        resize_img = resize_fun(np.array(image_origin.convert('L')))
        if resize_img.shape != (64, 64):
            print("Error resize!")
        img_list.append(resize_img)
    return img_list

def get_inference_pix(pre_config, img_list):
    global global_config
    global_config = pre_config
    preprocess_list =  [test_preprocess(x) for x in img_list]
    preprocess_list = np.array(preprocess_list).reshape(len(preprocess_list), 64, 64, 1)
    return preprocess_list

if __name__=='__main__':

    # 生成分类字典
    char_dict = create_dict()

    # 生成训练集
    if os.path.exists(train_gnt_dir):
        counter = create_image_dir(train_gnt_dir, train_dir, char_dict, False)
        print("Finish create train data: %d." % counter)
    else:
        print("Cannot find train gnt: " + train_gnt_dir)

    # x_train_once = np.expand_dims(x_train_once,1)
    # mean_px = x_train_once.mean().astype(np.float32)
    # std_px = x_train_once.std().astype(np.float32)

    # 生成测试集
    if os.path.exists(test_gnt_dir):
        counter = create_image_dir(test_gnt_dir, test_dir, char_dict)
        print("Finish create test data: %d." % counter)
    else:
        print("Cannot find test gnt: " + test_gnt_dir)

    # print("Mean: %f STD: %f" % (mean_px, std_px))
    # print("Finish create_image_dir.")
