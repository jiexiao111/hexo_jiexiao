import os


def create_link(src, dst):

    current_path = os.path.split(os.path.realpath(__file__))[0]
    src = os.path.join(current_path, src)
    dst = os.path.expanduser(dst)
    dst_bak = dst + '_bak'

    if not os.path.exists(dst):
        if not os.path.isdir(src):
            os.link(src, dst)
        else:
            os.symlink(src, dst)
        print("成功安装 %s" % dst)
    elif os.stat(src) == os.stat(dst):
        print("已经安装 %s 不需要重新安装" % dst)
    else:
        os.rename(dst, dst_bak)
        if not os.path.isdir(src):
            os.link(src, dst)
        else:
            os.symlink(src, dst)
        print("备份 %s 为 %s 成功安装 %s" % (dst, dst_bak, dst))


create_link('./.vimrc', '~/.vimrc')
create_link('./gdbinit', '~/.gdbinit')
create_link('./vimrcs', '~/.vim_config')
create_link('./.zshrc', '~/.zshrc')
create_link('.tmux.conf', '~/.tmux.conf')
create_link('./.style.yapf', '~/.style.yapf')
create_link('ipython_config.py', '~/.ipython/profile_default/ipython_config.py')
create_link('jupyter_notebook_config.py', '~/.jupyter/jupyter_notebook_config.py')
