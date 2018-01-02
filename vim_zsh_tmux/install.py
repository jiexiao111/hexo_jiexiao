import os
import argparse

parser = argparse.ArgumentParser('Create File Link.')
parser.add_argument('-s', type=str, help='source file.')
parser.add_argument('-d', type=str, help='destination file.')
Flag = parser.parse_args()

def create_link(src, dst):

    current_path = os.path.split(os.path.realpath(__file__))[0]
    src = os.path.join(current_path, src)
    dst = os.path.expanduser(dst)
    dst_bak = dst + '_bak'

    if not os.path.exists(dst):
        if not os.path.exists(os.path.dirname(dst)):
            print("未安装组件，放弃配置 %s" % dst)
            return
        if not os.path.isdir(src):
            os.link(src, dst)
        else:
            os.symlink(src, dst)
        print("成功配置 %s" % dst)
    elif os.stat(src) == os.stat(dst):
        print("已经配置 %s 不需要重新配置" % dst)
    else:
        os.rename(dst, dst_bak)
        if not os.path.isdir(src):
            os.link(src, dst)
        else:
            os.symlink(src, dst)
        print("备份 %s 为 %s 成功配置 %s" % (dst, dst_bak, dst))

create_link(Flag.s, Flag.d)
