1. 安装 git 和 make
    ```
    apt-get install -y git make
    ```

1. git clone 工程
    ```
    git clone --recursive https://github.com/jiexiao111/hexo_jiexiao.git
    cd hexo_jiexiao
    ```

1. 配置 shadowsocks
```
./shadowsocks-go.sh
bash ruisu.sh
bash serverspeeder.sh
```

1. 安装 anaconda
参考博客 https://jiexiao111.github.io/2017/12/29/ubuntu-install-anaconda.html

1. 安装 zsh
```
make zsh
```

1. 安装 tmux
```
tmux
make tmux
Ctrl + b, Shift + i
```

1. 安装 vim
```
make vim
cd ~/.vim/bundle/YouCompleteMe
./install.py --clang-completer
```

1. 安装 npm
```
make npm
```

1. 安装 yapf
```
make yapf
```

1. 安装 other
```
make other
```
