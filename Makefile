# 为了方便 git 管理, 将所有配置文件保存至同一个目录
all:
	# 安装 hexo
	npm install
	# 安装 powerline 字体, 安装后需要在 item2/putty 等工具中使用该字体
	-git clone https://github.com/powerline/fonts.git --depth=1
	sh ./fonts/install.sh
	-rm -rf fonts
	# 安装 tmux 状态栏, 需要手工执行, Ctrl + b, i
	-git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
	tmux source ~/.tmux.conf
	# 安装配置文件
	python3 ./vim_zsh_tmux/install.py
