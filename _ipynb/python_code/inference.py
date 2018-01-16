# coding: UTF-8

import pickle
import numpy as np
import os
from keras.models import load_model
from prepare_data import get_inference_pix, resize_with_c, resize_with_python, get_resize_pixs

target_file = '/aiml/result/result.txt'

# 转换字典
dict_word2id = pickle.load(open('/aiml/code/char_dict.pkl', 'rb'))
dict_id2word = {v:k for k, v in dict_word2id.items()}

# Resize 图片
resize_pixs = get_resize_pixs(resize_with_c)

# 其中一个模型
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

model = load_model('/aiml/code/weights.hdf5')
infer_result = model.predict(infer_pixs)

# argmax
infer_result_argmax = np.argmax(infer_result, axis=1)

# 写入文件
with open(target_file, 'w') as f:
    for word in [dict_id2word[x] for x in infer_result_argmax]:
        f.write(word)
