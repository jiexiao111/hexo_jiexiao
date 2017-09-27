# 配置Ubuntu可以通过ssh连接
```python
vi /etc/ssh/sshd_config
# PermitRootLogin without-password --> PermitRootLogin yes
service ssh restart
```

# 安装YouCompeteMe

vim +BundleInstall +qall
cd ~/.vim/bundle/YouCompleteMe/
./install.py --clang-completer
```

## YouCompeteMe 无法跳转
可以通过 YcmDebugInfo, 查看日志, 遇到的问题:
* 执行 ./install.py 时, 默认环境变量的 python 不能用 anaconda 版本 
* 升级插件后, 重新执行 ./install.py
