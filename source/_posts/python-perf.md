---
title: python 性能分析
date: 2017-11-08 19:24:43
tags:
---

<!-- 文章开头都用它了，整齐才好看 -->
{% note default %}
预处理过程中，如果出现非常慢的情况，通常需要进行性能剖析
{% endnote %}

<!--more-->

---

# cProfile 使用

## 装饰器实现
以下是从网上抄的装饰器

```python
import cProfile
import pstats
import os

# 性能分析装饰器定义
def do_cprofile(filename):
    """
    Decorator for function profiling.
    """
    def wrapper(func):
        def profiled_func(*args, **kwargs):
            # Flag for do profiling or not.
            DO_PROF = os.getenv("PROFILING")
            if DO_PROF:
                profile = cProfile.Profile()
                profile.enable()
                result = func(*args, **kwargs)
                profile.disable()
                # Sort stat by internal time.
                sortby = "tottime"
                ps = pstats.Stats(profile).sort_stats(sortby)
                ps.dump_stats(filename)
            else:
                result = func(*args, **kwargs)
            return result
        return profiled_func
    return wrapper
```

## 装饰器使用
装饰器的使用，下面的修改将使程序的 perf 信息保存至 mkm_run.prof 文件

```python
# 应用装饰器来分析函数
    @do_cprofile("./mkm_run.prof")
    def run(self, **kwargs):
```

需要注意的是，使用前需要导入环境变量，即，执行 pytyon 脚本前，执行一下 shell 指令
```shell
export PROFILING=y
```

# 实际问题举例
之前遇到一个实际的问题，我在读取 5W 个脚本进行预处理的时候，预计执行时间为 80 小时，使用 cProfile 分析后，发现根因是因为 5W 个文件是 mount 的远程目录，网络条件不好，导致处理非常缓慢，下面是我用于复现的简化代码，借此我们看看用 cProfile 是怎么描述这个问题的
```python
import os

# 读取 10 个文件的信息
def test(dir_path):
    tmp = []
    dir_child = os.walk(dir_path)
    for x in range(10):
        tmp.append(next(dir_child))
    print(len(tmp))

test('/root/workspace/ruby_data_local/')
```

通过 time 查看，我仅仅是读取了 10 文件信息就使用了 5.675s
```shell
$ time python tmp.py
10
python tmp.py  0.07s user 0.01s system 1% cpu 5.675 total
```

结合 cProfile 具体分析，看看输出是什么样子，以下是完整代码：
```python
import os
import cProfile
import pstats
import os

# 性能分析装饰器定义
def do_cprofile(filename):
    """
    Decorator for function profiling.
    """
    def wrapper(func):
        def profiled_func(*args, **kwargs):
            # Flag for do profiling or not.
            DO_PROF = os.getenv("PROFILING")
            if DO_PROF:
                profile = cProfile.Profile()
                profile.enable()
                result = func(*args, **kwargs)
                profile.disable()
                # Sort stat by internal time.
                sortby = "tottime"
                ps = pstats.Stats(profile).sort_stats(sortby)
                ps.dump_stats(filename)
            else:
                result = func(*args, **kwargs)
            return result
        return profiled_func
    return wrapper

@do_cprofile("./mkm_run.prof")
def test(dir_path):
    tmp = []
    dir_child = os.walk(dir_path)
    for x in range(10):
        tmp.append(next(dir_child))
    print(len(tmp))

test('/root/workspace/ruby_data/')
```

执行 ``export PROFILING=y; python tmp.py``, 执行后，会生成分析文件 ``mkm_run.prof``, 然后启动 ipython 查看具体信息：
```
In [1]: import pstats

In [2]: p = pstats.Stats("./mkm_run.prof")

In [3]: p.sort_stats('cumtime').print_stats(10, 1.0, '.*')
Wed Nov  8 20:11:57 2017    ./mkm_run.prof

         501 function calls (352 primitive calls) in 5.813 seconds

   Ordered by: cumulative time
   List reduced from 18 to 10 due to restriction <10>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    5.813    5.813 tmp.py:30(test)
   125/10    2.906    0.023    5.813    0.581 {built-in method builtins.next}
    51/17    0.001    0.000    5.813    0.342 os.py:277(walk)
        9    0.000    0.000    2.129    0.237 posixpath.py:166(islink)
        9    2.129    0.237    2.129    0.237 {built-in method posix.lstat}
       10    0.775    0.078    0.775    0.078 {built-in method posix.scandir}
        9    0.001    0.000    0.001    0.000 posixpath.py:73(join)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
      105    0.000    0.000    0.000    0.000 {method 'is_dir' of 'posix.DirEntry' objects}
        9    0.000    0.000    0.000    0.000 posixpath.py:39(_get_sep)


Out[3]: <pstats.Stats at 0x7feb240e7d68>

In [4]: p.print_callees("test")
   Ordered by: cumulative time
   List reduced from 18 to 1 due to restriction <'test'>

Function         called...
                     ncalls  tottime  cumtime
tmp.py:30(test)  ->       1    0.000    0.000  {built-in method builtins.len}
                         10    0.000    5.813  {built-in method builtins.next}
                          1    0.000    0.000  {built-in method builtins.print}
                         10    0.000    0.000  {method 'append' of 'list' objects}
```

其中 ``p.sort_stats('cumtime').print_stats(10, 1.0, '.*')`` 输出的信息表示以下含义：
* ncalls：表示函数调用的次数；
* tottime：表示指定函数的总的运行时间，除掉函数中调用子函数的运行时间；
* percall：（第一个 percall）等于 tottime/ncalls；
* cumtime：表示该函数及其所有子函数的调用运行的时间，即函数开始调用到返回的时间；
* percall：（第二个 percall）即函数运行一次的平均时间，等于 cumtime/ncalls；
* filename:lineno(function)：每个函数调用的具体信息

可以看出 tmp.py 文件中的第 30 行的 test 函数占用了 5.813s 时间，然后，执行 ``p.print_callees("test")`` 查看 test 函数调用了哪些函数，发现耗时的就是 walk 函数 返回的迭代器的 next 调用，于是就找到了性能瓶颈。

# pstats 使用举例：
```python
import pstats

# 创建 Stats 对象
p = pstats.Stats("result.out")

# strip_dirs(): 去掉无关的路径信息
# sort_stats(): 排序，支持的方式和上述的一致
# print_stats(): 打印分析结果，可以指定打印前几行

# 和直接运行 cProfile.run("test()") 的结果是一样的
p.strip_dirs().sort_stats(-1).print_stats()

# 按照函数名排序，只打印前 3 行函数的信息，参数还可为小数，表示前百分之几的函数信息
p.strip_dirs().sort_stats("name").print_stats(3)

# 按照运行时间和函数名进行排序
p.strip_dirs().sort_stats("cumulative", "name").print_stats(0.5)

# 如果想知道有哪些函数调用了 sum_num
p.print_callers(0.5, "sum_num")

# 查看 test() 函数中调用了哪些函数
p.print_callees("test")
```

# 参考
[http://python.jobbole.com/87621/]
