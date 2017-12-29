install:
	# 安装 zsh 配置 oh-my-zsh
	apt-get install -y zsh
	chsh -s /bin/zsh
	curl -L https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh | sh
	# 安装配置文件
	python3 ./vim_zsh_tmux/install.py
	# 安装 vim
	git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
	vim +PluginInstall +qall
	apt-get install -y ctags
	# 编译 youcompleteme
	apt-get install -y build-essential cmake
	apt-get install -y python-dev python3-dev
	python ~/.vim/bundle/YouCompleteMe/install.py --clang-completer 2>&1
	# 安装 hexo 如果需要代理配置如下
	# npm config set proxy http://username:password@server:port
	# npm config set https-proxy http://username:pawword@server:port
	npm install
	# 安装 powerline 字体, 安装后需要在 item2/putty 等工具中使用该字体
	git clone https://github.com/powerline/fonts.git --depth=1
	sh ./fonts/install.sh
	rm -rf fonts
	# 安装 tmux 状态栏, 需要手工执行, Ctrl + b, i
	git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
	tmux source ~/.tmux.conf
