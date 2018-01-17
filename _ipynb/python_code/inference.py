# coding: UTF-8

import pickle
import numpy as np
import os
from keras.models import load_model
from prepare_data import get_inference_pix, resize_with_c, resize_with_python, get_resize_pixs

target_file = '/aiml/result/result.txt'
all_preds = []

# 转换字典
dict_word2id = pickle.load(open('/aiml/code/char_dict.pkl', 'rb'))
dict_id2word = {v:k for k, v in dict_word2id.items()}

# Resize 图片
resize_pixs = get_resize_pixs(resize_with_c)

# Resnet_6_14
pre_config = {'gaussian_train_max': -1,
              'gaussian_train_min':  -1,
              'gaussian_test': -1,
              'dilation_train_max': -1,
              'dilation_train_min': -1,
              'dilation_test': -1,
              'threshold_otsu': False,
              'rescale_intensity': False,
              'norm_input': False}
infer_pixs = get_inference_pix(pre_config, resize_pixs)

model_1 = load_model('/aiml/code/Resnet_6_14_2.hdf5')
all_preds.append(model_1.predict(infer_pixs))
model_2 = load_model('/aiml/code/Resnet_6_14_1.hdf5')
all_preds.append(model_2.predict(infer_pixs))

# Resnet_6_8
pre_config = {'gaussian_train_max': 2,
              'gaussian_train_min':  0,
              'gaussian_test': 1,
              'dilation_train_max': -1,
              'dilation_train_min': -1,
              'dilation_test': -1,
              'threshold_otsu': False,
              'rescale_intensity': True,
              'norm_input': False}
infer_pixs = get_inference_pix(pre_config, resize_pixs)

model_3 = load_model('/aiml/code/Resnet_6_08_1.hdf5')
all_preds.append(model_3.predict(infer_pixs))


# argmax
infer_result = np.stack(all_preds).mean(axis=0)
infer_result_argmax = np.argmax(infer_result, axis=1)

# 写入文件
with open(target_file, 'w') as f:
    for word in [dict_id2word[x] for x in infer_result_argmax]:
        f.write(word)
