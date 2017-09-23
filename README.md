如果需要安装 hexo 需要提前安装好 git 和 node.js

```
git clone --recursive git@github.com:jiexiao111/hexo_jiexiao.git
cd hexo_jiexiao
make
```

如果需要调整 pep8 的最大行字符数, 可以直接更改一下文件
bundle/Python-mode-klen/pymode/libs/pylama/lint/pylama_pep8/pep8.py
```
MAX_LINE_LENGTH = 79
```
