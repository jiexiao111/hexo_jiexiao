# coding=utf-8

def decorator_trace_call(fun):
    def ret_fun(*args, **kwargs):
        print('Call function %s' % (fun.__name__))
        print(args)
        print(kwargs)
        fun(*args, **kwargs)
    return ret_fun
