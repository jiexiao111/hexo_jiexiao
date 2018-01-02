---
title: Anaconda 安装
date: 2017-12-29 23:58:33
categories: 操作系统
tags:
  - linux
---

<!-- 文章开头都用它了，整齐才好看 -->
{% note default %}
安装 anaconda
{% endnote %}

<!--more-->

# 检查操作系统类型
```
root@jiexiao:~/hexo_jiexiao# uname -a
Linux jiexiao 4.13.0-16-generic #19-Ubuntu SMP Wed Oct 11 18:35:14 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
```
可以看出是 64 位操作系统

# 下载和安装 anaconda
去[官网](https://www.anaconda.com/download/#linux) 下载安装包，通过 ``wget`` 下载，例如：
```
wget https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh
```
其中 ``5.0.1`` 表示 ``anaconda`` 的版本，``x86_64`` 表示 64 位操作系统

# 安装多版本 anaconda
```
bash Anaconda3-4.4.0-Linux-x86_64.sh

bash Anaconda2-4.4.0-Linux-x86_64.sh -b -p $HOME/anaconda3/envs/py2
rm -f $HOME/anaconda3/envs/py2/bin/conda*
rm -f $HOME/anaconda3/envs/py2/conda-meta/conda-*
rm -f $HOME/anaconda3/envs/py2/bin/activate
rm -f $HOME/anaconda3/envs/py2/bin/deactivate

cd $HOME/anaconda3/envs/py2/bin
ln -s ../../../bin/conda .
ln -s ../../../bin/activate .
ln -s ../../../bin/deactivate .
```

# 多版本切换 anaconda
[http://www.jianshu.com/p/d2e15200ee9b]
```
# 显示可用的 python 环境
conda info --envs
# 激活 python 环境
source activate py2
```

