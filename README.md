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

mac 系统中, 如果 tmux 下 vim 和系统的剪切板无法通用, 可以通过以下命令查看是否启用 ``reattach-to-user-namespace``
$ tmux show-option -gv default-command
reattach-to-user-namespace -l /bin/zsh
