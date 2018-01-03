zsh:
	# 安装 zsh 配置 oh-my-zsh
	apt-get install -y zsh
	chsh -s /bin/zsh
	@curl -L https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh | sh
	@python3 ./vim_zsh_tmux/install.py -s './.zshrc' -d '~/.zshrc'

vim:
	# 修改配置文件
	@python3 ./vim_zsh_tmux/install.py -s './.vimrc' -d '~/.vimrc'
	@python3 ./vim_zsh_tmux/install.py -s './vimrcs' -d '~/.vim_config'
	# 安装 vim
	apt-get install -y ctags
	git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
	vim +PluginInstall +qall
	# 编译 youcompleteme
	apt-get install -y build-essential cmake
	apt-get install -y python-dev python3-dev
	python ~/.vim/bundle/YouCompleteMe/install.py --clang-completer 2>&1

tmux:
	# 安装 powerline 字体, 安装后需要在 item2/putty 等工具中使用该字体
	git clone https://github.com/powerline/fonts.git --depth=1
	sh ./fonts/install.sh
	rm -rf fonts
	# 安装 tmux 插件, 需要手工执行, Ctrl + b, Shift + i
	git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
	@python3 ./vim_zsh_tmux/install.py -s '.tmux.conf' -d '~/.tmux.conf'
	tmux source ~/.tmux.conf
	@echo "Please Enter <Ctrl + b> and <Shift + i>"

npm:
	# 安装 node.js
	wget https://nodejs.org/dist/v8.9.3/node-v8.9.3.pkg
	tar -vxf node-v8.9.3-linux-x64.tar.xz -C /usr/
	echo 'export PATH="/usr/node-v6.11.3-linux-x64/bin:$PATH' >> ~/.bashrc
	echo 'export PATH="/usr/node-v6.11.3-linux-x64/bin:$PATH' >> ~/.zshrc
	source ~/.bashrc
	source ~/.zshrc
	# 安装 hexo 如果需要代理配置如下
	# npm config set proxy http://username:password@server:port
	# npm config set https-proxy http://username:pawword@server:port
	npm install

yapf:
	# 安装代码格式化工具
	apt-get install -y yapf
	@python3 ./vim_zsh_tmux/install.py -s './.style.yapf' -d '~/.style.yapf'
	

other:
	# gdb 配置文件
	@python3 ./vim_zsh_tmux/install.py -s './gdbinit' -d '~/.gdbinit'
	# ipython 配置文件
	@python3 ./vim_zsh_tmux/install.py -s 'ipython_config.py' -d '~/.ipython/profile_default/ipython_config.py'
	# jupyter 配置文件
	@python3 ./vim_zsh_tmux/install.py -s 'jupyter_notebook_config.py' -d '~/.jupyter/jupyter_notebook_config.py'
