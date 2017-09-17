---
title: 常用操作汇总
categories: 工具使用
tags:
  - 工具使用
---

{% note default %}
汇总一些琐碎的, 非快捷键的操作, 当某个工具的操作过多时再独立为一篇博客
{% endnote %}

<!--more-->

---

# jupyter
## .ipynb 转 .md
```shell
jupyter nbconvert --to markdown README.ipynb
```

## jupyter取消密码
* 生成配置文件
```shell
jupyter notebook --generate --allow-root
```

* 编辑/root/.jupyter/jupyter_notebook_config.py，然后重启jupyter
```shell
c.NotebookApp.token = '';
```
## 显示多行结果
* 修改前
```python
line1 = "this is from line 1"
line2 = "this is from line 2"

line1
line2
```
    'this is from line 2'
* 修改永久生效，编辑.ipython/profile_default/ipython_config.py，然后重启jupyter
```python
ipython profile create # 如果没有默认配置文件， 则生成一个新的
c.InteractiveShell.ast_node_interactivity = 'all'
```
* 修改临时生效
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
```
* 修改后
```python
line1 = "this is from line 1"
line2 = "this is from line 2"

line1
line2
```
    'this is from line 1'
    'this is from line 2'
---

# git
## 保存提交密码
* 更好的方式是使用秘钥
```shell
git config --global credential.helper store
```

## 生成秘钥
* [git 官方帮助](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/) 描述的非常清楚, 如果是 Linux 系统, 首先通过命令生成秘钥, 注意下面命令中的 jiexiao111@gmail.com 是你注册 github 时的邮箱
```python
ssh-keygen -t rsa -C jiexiao111@gmail.com
```

* 想办法把下面这个文件的内容拷贝出来
```shell
~/.ssh/id_rsa.pub
```

* 然后打开你的 github 主页, 依次点击 Settings->SSH and GPG keys->New SSH key, 然后 Title 随便取个名字，再把 ~/.ssh/id_rsa.pub 中的内容拷贝到 Key 中, Add SSH key 完成添加
{% img  '/images/add_ssh.png' %}

## 解决git中文乱码
```python
git config --global core.quotepath false
```

## 撤销 commit 但是保留修改
```shell
git reset --soft [commit_id] 就可以回滚到某一个commit，然后保留下修改的内容
```

## 比较文件
<https://gist.github.com/jhjguxin/3271961>

---

# chrome
## 分析网页加载速度
* 在 chrome 流量器中按 F12 或者单击鼠标右键->检查, 打开调试栏->Network, 刷新网页就可以看到以下信息了
{% img  '/images/chrome_perf.png' %}

---

# vim
## 无法 undo
* 如果文件名中包含中文, 则无法 undo

## 保存折叠
.vimrc 添加以下
```shell
au BufWinLeave *.* mkview
au BufWinEnter *.* silent loadview
```

---
