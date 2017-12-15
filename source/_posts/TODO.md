---
title: TODO
date: 2017-10-14 10:30:44
categories: 其他
tags:
  - todo
---

{% note default %}
一些来不及整理的内容先保存在这里
{% endnote %}

<!--more-->

---

# 多版本切换 anaconda
[http://www.jianshu.com/p/d2e15200ee9b]
```
# 显示可用的 python 环境
conda info --envs
# 激活 python 环境
source activate py2
```

# 学习 git
以下文件包含 git 常用命令的缩写
```
~/.oh-my-zsh/plugins/git
```

# 解决 zsh 和 tmux 下，vim 配色显示不一致
编辑~/.zshrc:
``alias tmux="TERM=screen-256color-bce tmux"``
编辑 ~/.tmux.conf:
``set -g default-terminal "xterm"``
参考 [https://stackoverflow.com/questions/10158508/lose-vim-colorscheme-in-tmux-mode]

# python3 import docx 错误
* pip uninstall docx
* 下载 [python_docx-0.8.6-py2.py3-none-any.whl](http://www.lfd.uci.edu/~gohlke/pythonlibs/)
* pip install python_docx-0.8.6-py2.py3-none-any.whl

# 机器学习教程
[斯坦福大学 CS231n 卷积神经网络与图像识别](http://cs231n.stanford.edu/)
[吴恩达 Deep Learning Specialization](https://www.coursera.org/specializations/deep-learning)
[Udacity 免费深度学习课程](https://www.udacity.com/course/deep-learning—ud730)
[Geoffrey Hinton 的 Neural Networks For Machine Learning](https://www.coursera.org/learn/neural-networks)
[斯坦福大学 CS224d 自然语言处理深度学习](http://cs224d.stanford.edu/)
[Ian Goodfellow 的 DeepLearning 书籍](https://exacity.github.io/deeplearningbook-chinese/)
[良心 GitHub 项目：各种机器学习任务的顶级结果（论文）汇总）](https://github.com//RedditSota/state-of-the-art-result-for-machine-learning-problems)

# apt-get 非正常退出后，出现 dpkg –configure -a 时，暴力解决
rm /var/lib/dpkg/updates/*

# latex
如果你只用 latex 画图的话，可以只看 pgfmanual 这个宏包就行了，安装完 texlive，文档都会一起安装了
[安装](https://liam0205.me/texlive/)
[在线体验](https://www.sharelatex.com/project)
《102 分钟学会 latex》


[「 Neural Networks and Deep Learning 」中文翻译（连载完毕）](https://hit-scir.gitbooks.io/neural-networks-and-deep-learning-zh_cn/content/)

# ubuntu 执行 mount 报错
ubuntu 下如果 mount 的是 window 的共享目录，会出现以下错误：
```
# mount -t cifs -o XXX_PATH LOCAL_PATH
mount: XXX_PATH is write-protected, mounting read-only
mount: cannot mount XXX_PATH read-only
```
执行以下命令即可：
```
apt-get install -y cifs-utils
```

# Flask 单元测试
[官方网站](https://pythonhosted.org/Flask-Testing/)

官方给出的例子如下：
```
#coding=utf8
from flask import Flask,jsonify
from flask_testing import TestCase
import unittest

app = Flask(__name__)

@app.route("/ajax/")
def some_json():
    return jsonify(success=True)

class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_some_json(self):
        response = self.client.get("/ajax/")
        '''''
               判断还回的 JSON 对像是不是{'success':True}
        '''
        self.assertEqual(response.json, dict(success=True))

if  __name__ =='__main__':
    unittest.main()
```

# Structuring Your TensorFlow Models
https://github.com/tensorflow/models/blob/master/tutorials/rnn/ptb/ptb_word_lm.py
存在的问题：整个 Graph 都定义在 PTBModel 的 init 函数中，可读性和重用性不太好

https://github.com/tensorflow/models/blob/master/tutorials/embedding/word2vec_optimized.py
存在的问题：直接将整个 init 函数拆分成了多份，但是整个计算图依然在 build_graph 一个函数中实现，正常的看代码的顺序是 main——train——self._train_thread_body——self._train——train——build_graph——__init__
较为冗长的调用关系，重复的命名，无法直观的看出 train 就是我们计算图中关键的节点。根本原因是 build_graph 中集合了整张图的描述。

按照我们的正常思维，计算图会有输入、预测函数、损失函数、优化函数、输出，如果按照以上部分将计算图分割，将能提高重用性和可读性
http://danijar.com/structuring-your-tensorflow-models/
弄两张 Scopes 对比，没有添加 Scopes 时的调试信息

# 删除除了某个文件的其他文件
```
rm -rf !(*.zip)
```

# 解压至压缩文件名创建的目录下
```python
import os

file_names = os.listdir()
zip_files = [x for x in file_names if os.path.splitext(x)[1] == '.zip']
unzip_cmds = ['unzip %s -d %s' % (x, os.path.splitext(x)[0]) for x in zip_files]

for cmd in unzip_cmds:
    os.system(cmd)
```
# 解压目录下的所有文件
```python
import os
import argparse

file_names = os.walk()
zip_files = [(root, file) for root, dirs, files in file_names for file in files if os.path.splitext(file)[1] == '.zip']
unzip_cmds = ['unzip -o %s -d %s' % (os.path.join(x[0], x[1]), x[0]) for x in zip_files]

for cmd in unzip_cmds:
    os.system(cmd)
```
# outlook 联系人组
https://support.office.com/zh-cn/article/%E5%9C%A8-Outlook%E2%80%8B%E2%80%8B-%E4%B8%AD%E5%88%9B%E5%BB%BA%E8%81%94%E7%B3%BB%E4%BA%BA%E7%BB%84%E6%88%96%E9%80%9A%E8%AE%AF%E7%BB%84%E5%88%97%E8%A1%A8-88ff6c60-0a1d-4b54-8c9d-9e1a71bc3023?ui=zh-CN&rs=zh-CN&ad=CN

# python 读取文件编码错误
```
open(file_name, encoding=encode_type, errors='ignore')
```

# python request 乱码
http://xiaorui.cc/2016/02/19/%E4%BB%A3%E7%A0%81%E5%88%86%E6%9E%90python-requests%E5%BA%93%E4%B8%AD%E6%96%87%E7%BC%96%E7%A0%81%E9%97%AE%E9%A2%98/
