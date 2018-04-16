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
rm /var/lib/apt/lists/lock
rm /var/cache/apt/archives/lock
rm /var/lib/dpkg/lock
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

# 5885 服务器启动报错
```
For success boot, you have to switch the auto-pxe on or permit the pxe request in Web-UI
Could not boot: Error 0x00000001 (http://ipxe.org/00000001)
```
Google 了一下``PXE``发现是无盘启动技术，第一反应是启动顺序出错，默认进入了网络启动，于是在启动时按下``F11``进入启动顺序配置界面选择硬盘启动

# jupyter 配置按章节折叠
```
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user
pip install jupyter_nbextensions_configurator
jupyter nbextensions_configurator enable --user
```
在``Nbextensions``选项卡中勾选``Collapsible Headings``
http://blog.csdn.net/w371500241/article/details/78561237

# apt-get 安装告警
```
dpkg: warning: files list file for package 'x' missing; assuming package has no files currently installed
```
从告警来看，貌似是说假设这个包已经安装了，但是没有文件？网上找到的办法就是重新安装所有告警的包，但是从后续的工作来看，这些告警都是无害的。
```
apt-get install -y "xxx" | grep "warning: files list file for package '" | grep -Po "[^'\n ]+'" | grep -Po "[^']+" |xargs -I {} apt-get install --reinstall {}
```

# bazel 构建报错
```
# root @ ubuntu in ~/workspace/mount/models-master [9:26:56]
$ bazel build -c opt textsum/...
.............................
INFO: Analysed 7 targets (14 packages loaded).
INFO: Found 7 targets...
Unhandled exception thrown during build; message: /root/workspace/mount/models-master/bazel-out (Operation not supported)
INFO: Elapsed time: 5.124s
FAILED: Build did NOT complete successfully
```
尝试了很多办法，最后发现这个错误的原因是 bazel 执行的路径不能在 mount 目录，拷贝出去即可

# 优化配置
## 调整 pep8 行内最大字符数
如果需要调整 pep8 的最大行字符数，可以直接更改一下文件
bundle/Python-mode-klen/pymode/libs/pylama/lint/pylama_pep8/pep8.py
```
MAX_LINE_LENGTH = 79
```

## vim 与系统剪切板连接
mac 系统中，如果 tmux 下 vim 和系统的剪切板无法通用，可以通过以下命令查看是否启用 ``reattach-to-user-namespace``
```
$ tmux show-option -gv default-command
reattach-to-user-namespace -l /bin/zsh
```

# ssh 超时断开
cp /etc/ssh/sshd_config /etc/ssh/sshd_config_bak
sed -i "s/#ClientAliveInterval 0/ClientAliveInterval 60/g" /etc/ssh/sshd_config
sed -i "s/#ClientAliveCountMax3/ClientAliveCountMax 3/g" /etc/ssh/sshd_config
service sshd restart

# 配置 Ubuntu 可以通过 ssh 连接
sed -i "s/#PermitRootLogin without-password/PermitRootLogin yes/g" /etc/ssh/sshd_config
service ssh restart

# 代码格式化工具
```
pip install yapf
```

# 代理配置
```
# npm config set proxy http://username:password@server:port
# npm config set https-proxy http://username:pawword@server:port
```

# tar 错误
tar: XXXXXX: Cannot change ownership to uid XXX, gid XXXX: Operation not permitted
使用 -no-same-owner 选项

# UnicodeEncodeError: 'ascii' codec can't encode character u'xxx' in position xxx: ordinal not in range(128)
export LC_ALL='en_US.utf8'
https://stackoverflow.com/questions/9942594/unicodeencodeerror-ascii-codec-cant-encode-character-u-xa0-in-position-20

# git 错误处理
错误：
fatal: unable to access 'https://github.com/robbyrussell/oh-my-zsh.git/': server certificate verification failed. CAfile: /etc/ssl/certs/ca-certificates.crt CRLfile: none
错误：Peer's Certificate issuer is not recognized.
方案：
git config --global http.sslVerify false

错误：error: RPC failed; curl 56 GnuTLS recv error (-110): The TLS connection was non-properly terminated
方案：
apt-get install build-essential fakeroot dpkg-dev
mkdir ~/git-openssl
cd ~/git-openssl
apt-get source git
apt-get build-dep git
apt-get install libcurl4-openssl-dev
dpkg-source -x git_2.7.4-0ubuntu1.dsc
cd git-2.7.4

修改 vi debian/control
libcurl4-gnutls-dev 改为 libcurl4-openssl-dev

编辑 vi debian/rules
删除 TEST =test

dpkg-buildpackage -rfakeroot -b
dpkg -i ../git_2.7.4-0ubuntu1_amd64.deb


```
Can't drop privileges for downloading as file 'git_2.7.4.orig.tar.xz' couldn't be accessed by user '_apt'. - pkgAcquire::Run (13: Permission denied)
sudo chown _apt /var/lib/update-notifier/package-data-downloads/partial/
```

# git 忘记 ``--recursive``
git submodule init
git submodule update

http://blog.csdn.net/stupid_3/article/details/79167983

文件交集
grep -F -f a.txt b.txt
文件差集
grep -F -v -f a.txt b.txt

MAC 在安装 YCM 时，必须使用系统自带的 python 不能使用 anaconda 的 python

# find 命令技巧
排除某类文件
```
find ./cache ! -name '*.html'
```
排除某个目录
```
find . -path './includes' -prune -o -print
```
排除多个目录
```
find /usr/ \( -path /usr/node-v6.11.3-linux-x64 -o -path /usr/textsum \) -prune -o -print |head
```
示例
```
# root @ ubuntu in /usr [11:25:33]
$ find . |head
.
./node-v6.11.3-linux-x64
./node-v6.11.3-linux-x64/CHANGELOG.md
./node-v6.11.3-linux-x64/share
./node-v6.11.3-linux-x64/share/man
./node-v6.11.3-linux-x64/share/man/man1
./node-v6.11.3-linux-x64/share/man/man1/node.1
./node-v6.11.3-linux-x64/share/doc
./node-v6.11.3-linux-x64/share/doc/node
./node-v6.11.3-linux-x64/share/doc/node/lldb_commands.py

# root @ ubuntu in /usr [11:25:44]
$ find . ! -name "*.md" |head
.
./node-v6.11.3-linux-x64
./node-v6.11.3-linux-x64/share
./node-v6.11.3-linux-x64/share/man
./node-v6.11.3-linux-x64/share/man/man1
./node-v6.11.3-linux-x64/share/man/man1/node.1
./node-v6.11.3-linux-x64/share/doc
./node-v6.11.3-linux-x64/share/doc/node
./node-v6.11.3-linux-x64/share/doc/node/lldb_commands.py
./node-v6.11.3-linux-x64/share/doc/node/gdbinit

# root @ ubuntu in /usr [11:26:06]
$ find . -path './node-v6.11.3-linux-x64' -prune -o -print |head
.
./textsum
./textsum/data
./textsum/data/text_data1
./textsum/data/text_data_train.txt
./textsum/data/data_convert_example.py
./textsum/data/vocab
./textsum/data/training
./textsum/data/bin_data_train
./textsum/data/text_data_test.txt

# root @ ubuntu in /usr [11:26:06]
$ find /usr/ \( -path /usr/node-v6.11.3-linux-x64 -o -path /usr/textsum -o -path /usr/share \) -prune -o -print |head
/usr/
/usr/local
/usr/local/man
/usr/local/share
/usr/local/share/jupyter
/usr/local/share/jupyter/nbextensions
/usr/local/share/jupyter/nbextensions/jupyter-js-widgets
/usr/local/share/jupyter/nbextensions/jupyter-js-widgets/extension.js.map
/usr/local/share/jupyter/nbextensions/jupyter-js-widgets/extension.js
/usr/local/share/jupyter/kernels
```

# ag 搜索特定文件
首先查询支持的文件类型
```
ag --list-file-types
```
然后按文件类型搜索关键字
```
ag xxx --python
```

# grep 递归搜索
```
grep -rn xxxx /dir
```
-n 是行号  -r 是递归

# python __future__ 模块
主要作用是在 python2 中引入 python3 的特性
## absolute_import
在 Python 2.4 或之前，Python 会先查找当前目录下有没有 string.py, 若找到了，则引入该模块。如果使用 absolute_import
则会引用标准库中的 string.py, 通过 from . import string 引入自定义的 string.py
## division
python2 中的 ``/`` 在两侧均为整数时，结果也为整数，python3 中 ``/`` 为精确除法，两侧整数结果依然为浮点，如果想实现取整则使用 ``//``
## print_function
禁用 ``print "xxx"`` 格式的调用

# 机器学习资料
http://d0evi1.com/tecbook/
