---
title: 手写汉字识别
date: 2018-01-02 22:37:46
categories: 机器学习
tags:
  - Tensorflow
---

{% note default %}
部门组织的 AI 编程比赛，正好拿来熟悉下
{% endnote %}

<!--more-->

---

# 数据集下载
```
wget http://www.nlpr.ia.ac.cn/databases/download/feature_data/HWDB1.1trn_gnt.zip
wget http://www.nlpr.ia.ac.cn/databases/download/feature_data/HWDB1.1tst_gnt.zip
```
解压文件，需要注意的是 HWDB1.1trn_gnt.zip 需要解压两次

# 读取数据
```
import os
import numpy as np
import struct

train_data_dir = "HWDB1.1trn_gnt"
test_data_dir = "HWDB1.1tst_gnt"

# 读取图像和对应的汉字
def read_from_gnt_dir(gnt_dir=train_data_dir):
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
```

# 在 Tensorboard 中显示图片

http://www.blogs8.cn/posts/Ezqbef9
https://zhuanlan.zhihu.com/p/30197320
# 参考
[手写汉字识别](http://blog.csdn.net/u014365862/article/details/53869837)
[使用 Tensorboard 显示图片](https://www.cnblogs.com/tengge/p/6390148.html)
