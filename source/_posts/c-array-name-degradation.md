---
title: 数组名退化
date: 2017-11-30 23:31:47
categories: 编程语言
tags:
  - c 语言
---

{% note default %}
之前看到的一篇文章，出处忘了，以后打算按自己的理解重新写一下
{% endnote %}

<!--more-->

---

数组名退化

2016 年 2 月 1 日
10:41

个人的浅显认识， 欢迎批评指正. 

1. 什么是数组类型？ 

下面是 C99 中原话： 
An array type describes a contiguously allocated nonempty set of objects with a 
particular member object type, called the element type.36) Array types are characterized by their element type and by the number of elements in the array. An array type is said to be derived from its element type, and if its element type is T , the array type is sometimes called ‘‘array of T ’’. The construction of an array type from an element type is called ‘‘array type derivation’’.  

很显然， 数组类型也是一种数据类型， 其本质功能和其他类型无异：定义该类型的数据所占内存空间的大小以及可以对该类型数据进行的操作（及如何操作）. 

2. 数组类型定义的数据是什么？它是变量还是常量？ 
char s[10] = "china"; 
在这个例子中， 数组类型为 array of 10 chars（姑且这样写）, 定义的数据显然是一个数组 s. 

下面是 C99 中原话： 
  An lvalue is an expression with an object type or an incomplete type other than void; if an lvalue does not designate an object when it is evaluated, the behavior is undefined. When an object is said to have a particular type, the type is specified by the lvalue used to designate the object. A modifiable lvalue is an lvalue that does not have array type, does not have an incomplete type, does not have a const-qualified type, and if it is a structure or union, does not have any member (including, recursively, any member or element of all contained aggregates or unions) with a const-qualified type. 

看了上面的定义， 大家应该明白了 modifiable lvalue 和 lvalue 的区别， 大家也应该注意到 array type 定义的是 lvalue 而不是 modifiable lvalue. 所以说 s 是 lvalue. 

s 指代的是整个数组， s 的内容显然是指整个数组中的数据， 它是 china\0****（这里*表示任意别的字符）.s 的内容是可以改变的， 从这个意义上来说， s 显然是个变量. 

3. 数组什么时候会"退化" 

下面是 C99 中原话： 
Except when it is the operand of the sizeof operator or the unary & operator, or is a string literal used to initialize an array, an expression that has type ‘‘array of type’’ is converted to an expression with type ‘‘pointer to type’’ that points to the initial element of the array object and is not an lvalue. 

上面这句话说的很清楚了， 数组在除了 3 种情况外， 其他时候都要"退化"成指向首元素的指针. 
比如对 char s[10] = "china"; 
这 3 中例外情况是： 
(1) sizeof(s) 
(2) &s; 
(3) 用来初始化 s 的"china"; 


除了上述 3 种情况外，s 都会退化成 &s[0], 这就是数组变量的操作方式 

4. 数组与指针有什么不同？ 
4.1 初始化的不同 
char s[] = "china"; 
char *p = "china"; 

在第一句中，以 &s[0] 开始的连续 6 个字节内存分别被赋值为： 
'c', 'h', 'i', 'n', 'a', '\0' 

第二句中，p 被初始化为程序 data 段的某个地址，该地址是字符串"china"的首地址 

4.2 sizeof 的不同 

sizeof 就是要求一种数据（类型）所占内存的字节数. 对于 4.1 中的 s 和 p 
sizeof(s) 应为 6, 而 sizeof(p) 应为一个"指针"的大小. 

这个结果可以从 1 中对于数组类型的定义和 3 中数组什么时候不会"退化"中得出来. 

4.3 & 操作符 

对于 & 操作符， 数组同样不会退化. 
4.1 中的 s 和 p 分别取地址后，其意义为： 
&s 的类型为 pointer to array of 6 chars. 
&p 的类型为 pointer to pointer to char. 

4.4 s 退化后为什么不可修改 

除 3 种情况外，数组 s 在表达式中都会退化为"指向数组首元素的指针", 既 &s[0] 

举个例子 
int a; 
(&a)++; // 你想对谁 ++? 这显然是不对的 

对 (&s[0])++ 操作犹如 (&a)++, 同样是不对的，这就导致退化后的 s 变成不可修改的了. 

4.5 二维数组与二级指针 

char s[10]; 与 char *p; 
char s2[10][8]; 与 char **p2; 

s 与 p 的关系，s2 与 p2 的关系，两者相同吗？ 
紧扣定义的时候又到了. 
除 3 种情况外，数组在表达式中都会退化为"指向数组首元素的指针". 

s 退化后称为 &s[0], 类型为 pointer to char, 与 p 相同 
s2 退化后称为 &s2[0], 类型为 pointer to array of 8 chars, 与 p2 不同 
&s2[0] 时 s2[0] 还未退化，表示一个包含 8 个字节的数组

4.6 数组作为函数参数 

毫无疑问， 数组还是会退化. 

void func(char s[10]); <===> void func(char *s); 

void func(char s[10][8]); <===> void func(char (*s)[8]); 

4.7 在一个文件中定义 char s[8], 在另外一个文件中声明 extern char *s. 这样可以吗？ 

---------file1.c--------- 
char s[8]; 

---------file2.c--------- 
extern char *s; 


答案是不可以. 一般来说，在 file2.c 中使用*s 会引起 core dump, 这是为什么呢？ 

先考虑 int 的例子. 
---------file1.c--------- 
int a; 

---------file2.c--------- 
extern int a; 

file1.c 和 file2.c 经过编译后， 在 file2.o 的符号表中， a 的地址是尚未解析的 
file1.o 和 file2.o 在链接后， file2.o 中 a 的地址被确定。假设此地址为 0xbf8eafae 

file2.o 中对该地址的使用，完全是按照声明 extern int a; 进行的，即 0xbf8eafae 会被认为是整形 a 的地址 
比如 a = 2; 其伪代码会对应为 *((int *)0xbf8eafae) = 2; 

现在再看原来的例子. 

---------file1.c--------- 
char s[8]; 

---------file2.c--------- 
extern char *s; 

同样， file1.c 和 file2.c 经过编译后， 在 file2.o 的符号表中， s 的地址是尚未解析的 
file1.o 和 file2.o 在链接后， file2.o 中 s 的地址被确定。假设此地址为 0xbf8eafae 

file2.o 中对该地址的使用，完全是按照声明 extern char *s; 进行的，即 0xbf8eafae 会被认为是指针 s 的地址 
比如 *s = 2; 其伪代码会对应为 *(*((char **)0xbf8eafae)) = 2; 

*((char **)0xbf8eafae) 会是什么结果呢？ 
这个操作的意思是：将 0xbf8eafae 做为一个二级字符指针， 将 0xbf8eafae 为始址的 4 个字节 (32 位机）作为一级字符指针 
也就是将 file1.o 中的 s[0], s[1], s[2], s[3] 拼接成一个字符指针. 


那么*(*((char **)0xbf8eafae)) = 2; 的结果就是对 file1.o 中 s[0], s[1], s[2], s[3] 拼接成的这个地址对应 
的内存赋值为 2. 
这样怎么会正确呢？ 


下面看看正确的写法： 

---------file1.c--------- 
char s[8]; 

---------file2.c--------- 
extern char s[]; 


同样， file1.c 和 file2.c 经过编译后， 在 file2.o 的符号表中， s 的地址是尚未解析的 
file1.o 和 file2.o 在链接后， file2.o 中 s 的地址被确定。假设此地址为 0xbf8eafae 

file2.o 中对该地址的使用，完全是按照声明 extern char s[]; 进行的，即 0xbf8eafae 会被认为是数组 s 的地址 
比如 *s = 2; 其伪代码会对应为 *(*((char (*)[])0xbf8eafae)) = 2; 

*((char (*)[])0xbf8eafae) 会是什么结果呢？ 
这个操作的意思是：将 0xbf8eafae 做为一个指向字符数组的指针， 然后对该指针进行*操作. 
这就用到了数组的一个重要性质：  
对于数组 char aaa[10]; 来说， &aaa[0], &aaa, *(&aaa) 在数值上是相同的（其实， *(&aaa) 之所以在程序中 
会在值上等于 &aaa[0], 这也是退化的结果： *(&aaa) 就是数组名 aaa, aaa 退化为 &aaa[0]). 
所以， *((char (*)[])0xbf8eafae) 的结果在值上还是 0xbf8eafae, 在类型上退化成"指向数组首元素的指针" 


那么*(*((char (*)[])0xbf8eafae)) = 2; 
其伪代码就成为*((char *)0xbf8eafae) = 2; 即将数组 s 的第一个元素设为 2 


5. 小结论 

(a). 数组类型是一种特殊类型， 它定义的是数组变量， 是 lvalue 但不是 modifiable lvalue 
(b). 除了 3 种情况外 (sizeof, &, 用做数组初始化的字符串数组）, 数组会退化成"指向数组首元素的指针"

(c). 不要将数组名简单的看作不可修改的相应的指针， 它们还是有很多不同的


