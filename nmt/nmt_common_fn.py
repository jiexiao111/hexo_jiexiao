# coding=utf-8

import sys
from enum import Enum

str_space = []

def decorator_trace_call(fun):
    def ret_fun(*args, **kwargs):
        str_args = []
        args_name = fun.__code__.co_varnames
        for n in range(len(args_name)):
            if n >= len(args):
                break
            str_args.append("%s=%s" % (args_name[n], args[n]))
        for arg in kwargs.items():
            str_args.append("%s=%s" % (arg[0], arg[1]))
        print('%s%s(%s)' % ("".join(str_space), fun.__name__, ", ".join(str_args)))
        str_space.append("  ")
        ret = fun(*args, **kwargs)
        str_space.pop()
        return ret
    return ret_fun

def DEBUG_PRINT(str_log):
    print("\33[1;31mDEBUG:\33[0m %s" % (str_log))

# 定义打印日志的等级
Log_Level = Enum('Log_Level', ('Debug', 'Info', 'Warning', 'Error'))
PRINT_LEVEL = Log_Level.Debug

def print_out(s, f=None, new_line=True, level=Log_Level.Debug):
    """ 可以将日志打印至文件或者终端 """
    if level.value < PRINT_LEVEL.value:
        return

    if isinstance(s, bytes):
        s = s.decode("utf-8")

    if f:
        f.write(s.encode("utf-8"))
        if new_line:
            f.write(b"\n")

    s = "".join(str_space) + s
    print(s, end="", file=sys.stdout)
    if new_line:
        sys.stdout.write("\n")
    sys.stdout.flush()
