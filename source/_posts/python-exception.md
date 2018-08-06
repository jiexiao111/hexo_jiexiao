---
title: python exception
categories: 编程语言
tags:
  - python
---

{% note default %}
之前没有关注过 python 的异常处理，走读官方文档的过程中顺便记录一下
{% endnote %}

<!--more-->

---

BaseException 是所有异常的基类，但是，不能用户定义的类直接继承，用户应该继承的是 Exception。
* args 参数
    ```python
    raise Exception("Exception Test.")
    ```
    输出
    ```python
    Traceback (most recent call last):
    File "/tmp/tmp.py", line 1, in <module>
        raise Exception("Exception Test.")
        Exception: Exception Test. # 异常对象的初始化参数
    ```
* with_traceback(tb)
	在 python3 中，会打印每一层异常的 traceback，而在 python2 中则更需要 ``with_traceback`` 函数
	```python
	def div():
		2 / 0
	try:
		div()
	except ZeroDivisionError as e:
		raise ValueError(e)
	```
	输出
	```python
	Traceback (most recent call last):
	File "/tmp/tmp.py", line 4, in <module>
		div()
	File "/tmp/tmp.py", line 2, in div
		2 / 0
	ZeroDivisionError: division by zero

	During handling of the above exception, another exception occurred:

	Traceback (most recent call last):
	File "/tmp/tmp.py", line 6, in <module>
		raise ValueError(e)
	ValueError: division by zero
    ```
    如果显式的使用 with_traceback 则会打印两次前一个异常的 traceback
    ```
	import sys

	def div():
		2 / 0
	try:
		div()
	except ZeroDivisionError as e:
		raise ValueError(e).with_traceback(sys.exc_info()[2])

    ```
	输出
	```
    Traceback (most recent call last):
    File "/tmp/tmp.py", line 6, in <module>
        div()
    File "/tmp/tmp.py", line 4, in div
        2 / 0
    ZeroDivisionError: division by zero

    During handling of the above exception, another exception occurred:

    Traceback (most recent call last):
    File "/tmp/tmp.py", line 8, in <module>
        raise ValueError(e).with_traceback(sys.exc_info()[2])
    File "/tmp/tmp.py", line 6, in <module>
        div()
    File "/tmp/tmp.py", line 4, in div
        2 / 0
    ValueError: division by zero
    ```

# SystemExit

# KeyboardInterrupt

# GeneratorExit

# Exception
