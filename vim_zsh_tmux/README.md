
# 配置Ubuntu可以通过ssh连接


```python
vi /etc/ssh/sshd_config
# PermitRootLogin without-password --> PermitRootLogin yes
service ssh restart
```

# 安装YouCompeteMe


```python
vim +BundleInstall +qall
cd ~/.vim/bundle/YouCompleteMe/
./install.py --clang-completer
```
