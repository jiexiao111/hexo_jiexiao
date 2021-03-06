---
title: 正则表达式
date: 2017-10-27 21:40:38
categories: 编程技术
tags:
  - 正则表达式
---

{% note default %}
经常用的工具 vi、grep、awk、sed、python 都涉及正则表达式的使用，经常在需要使用的时候想不起来，所以记录一下将常用的记录一下
{% endnote %}

<!--more-->

---

# 元字符

## 常用
代码      | 说明
----      | ------
.         | 匹配除换行符以外的任意字符
\w        | 匹配字母或数字或下划线
\s        | 匹配任意的空白符
\d        | 匹配数字
\b        | 匹配单词的开始或结束
^         | 匹配字符串的开始
$         | 匹配字符串的结束
\         | 转义字符
[xyz]     | 匹配所包含的任意一个字符
x&#124;y   | 匹配 x 或 y

## 反义
代码     | 说明
----     | ------
\W       | 匹配任意不是字母，数字，下划线的字符
\S       | 匹配任意不是空白符的字符
\D       | 匹配任意非数字的字符
\B       | 匹配不是单词开头或结束的位置
[^aeiou] | 匹配除了 aeiou 这几个字母以外的任意字符

## 分组
分类     | 代码           | 语法	说明
----     | ------
捕获     | `(exp)`        | 匹配 exp, 并捕获文本到自动命名的组里
捕获     | `(?<name>exp)` | 匹配 exp, 并捕获文本到名称为 name 的组里，也可以写成 (?'name'exp)
捕获     | `(?:exp)`      | 匹配 exp, 不捕获匹配的文本，也不给此分组分配组号
零宽断言 | `(?=exp)`      | 匹配 exp 前面的位置
零宽断言 | `(?<=exp)`     | 匹配 exp 后面的位置
零宽断言 | `(?!exp)`      | 匹配后面跟的不是 exp 的位置
零宽断言 | `(?<!exp)`     | 匹配前面不是 exp 的位置
注释     | `(?#comment)`  | 这种类型的分组不对正则表达式的处理产生任何影响，用于提供注释让人阅读

## 启用“忽略模式里的空白符”选项
```
(?<=    # 断言要匹配的文本的前缀
<(\w+)> # 查找尖括号括起来的字母或数字（即 HTML/XML 标签）
)       # 前缀结束
.*      # 匹配任意文本
(?=     # 断言要匹配的文本的后缀
<\/\1>  # 查找尖括号括起来的内容：前面是一个"/"，后面是先前捕获的标签
)       # 后缀结束
```

## 限定符
代码  | 说明
----  | ------
*     | 重复零次或更多次
+     | 重复一次或更多次
?     | 重复零次或一次
{n}   | 重复 n 次
{n,}  | 重复 n 次或更多次
{n,m} | 重复 n 到 m 次

## 贪婪与懒惰
代码   | 说明
----   | ------
*?     | 重复任意次，但尽可能少重复
+?     | 重复 1 次或更多次，但尽可能少重复
??     | 重复 0 次或 1 次，但尽可能少重复
{n,m}? | 重复 n 到 m 次，但尽可能少重复
{n,}?  | 重复 n 次以上，但尽可能少重复

默认为贪婪，``a.\*?b`` 和 ``a.\*b`` 同时作用于 ``aabaab``，第一个正则表达式匹配整个字符串 ``aabaab``， 第二个匹配 ``aab`` 和 ``aab``
**为什么第一个匹配是 aab（第一到第三个字符）而不是 ab（第二到第三个字符）？简单地说，因为正则表达式有另一条规则，比懒惰／贪婪规则的优先级更高：最先开始的匹配拥有最高的优先权**

# vi/sed/ag/awk/python 区别

环境         | `\d` | `()` `+` <code>&#124;</code> | 分组 | 零宽断言
---          | ---  | ---------------              | ---  | ---
sed/vi/grep/ | n    | `-r` 或者添加 ``\``          | y    | n

# 删除括号内的内容
```
import re
reg_bracket = re.compile('\(.*?\)')
reg_bracket.sub(' ', 'test (del) end')
```
# 参考资料
[正则表达式 30 分钟入门教程](http://deerchao.net/tutorials/regex/regex.htm#resources)
[菜鸟教程——正则表达式](http://www.runoob.com/regexp/regexp-intro.html)
