# coding=utf-8

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
        fun(*args, **kwargs)
        str_space.pop()
    return ret_fun

def DEBUG_PRINT(str_log):
    print("\33[1;31mDEBUG:\33[0m %s" % (str_log))
