---
title: TODO
date: 2017-10-14 10:30:44
tags:
---

{% note default %}
一些来不及整理的内容先保存在这里
{% endnote %}

<!--more-->

---

# 多版本切换 anaconda
[http://www.jianshu.com/p/d2e15200ee9b]
```
# 显示可用的 python 环境
conda info --envs
# 激活 python 环境
source activate py2
```

# 学习 git
以下文件包含 git 常用命令的缩写
```
~/.oh-my-zsh/plugins/git
```

# 解决 zsh 和 tmux 下，vim 配色显示不一致
编辑~/.zshrc:
``alias tmux="TERM=screen-256color-bce tmux"``
编辑 ~/.tmux.conf:
``set -g default-terminal "xterm"``
参考 [https://stackoverflow.com/questions/10158508/lose-vim-colorscheme-in-tmux-mode]

# 修改 CapsLock 为 Ctrl
## Win7
* 点击 Win+R 键

* 在输入框键入 regedit，打开注册表

* 进入 HKEY_LOCAL_MACHINE -> System -> CurrentControlSet -> Control -> KeyBoard Layout。记住，一定是 keyBoard Layout，而不是 KeyBoard Layouts

* 右键菜单，然后选择 New -> Binary value

* 重命名 New Value #1 -> Scancode Map

* 右键菜单 Scancode Map -> Modify

输入如下值，保存

0000 00 00 00 00 00 00 00 00
0008 03 00 00 00 1D 00 3A 00
0010 3A 00 1D 00 00 00 00 00
0018

前两行和最后一行，都是固定的，全部为 0。第三行，表示你修改了几个键，其实我们只是改了两个键，不过最后那一行也要算进去，所以是 3。
重点是在第四行和第五行。3A00，代表 Caps Lock， 1D00，代表 Ctrl。这一行，意思即为，将 Caps Lock 映射为 Ctrl
第五行，就不用说了，意思刚好相反。
修改完毕后，重新登录 Windows 即可生效！
下面附上各个键位值的参考：

```
Escape 01 00
Tab 0F 00
Caps Lock 3A 00
Left Alt 38 00
Left Ctrl 1D 00
Left Shift 2A 00
Left Windows 5B E0
Right Alt 38 E0
Right Ctr l1D E0
Right Shift 36 00
Right Windows 5C E0
Backspace 0E 00
Delete 53 E0
Enter 1C 00
Space 39 00
Insert 52 E0
HOME 47 E0
End 4F E0
Num Lock 45 00
Page Down 51 E0
Page Up 49 E0
Scroll Lock 46 00
```

## MAC
* 选取苹果菜单 >“系统偏好设置”，然后点按“键盘”。
* 点按“修饰键”按钮。
* 从想要更改的修饰键旁边的弹出式菜单中选取一项操作，然后点按“好”。

# python3 import docx 错误
* pip uninstall docx
* 下载 [python_docx-0.8.6-py2.py3-none-any.whl](http://www.lfd.uci.edu/~gohlke/pythonlibs/)
* pip install python_docx-0.8.6-py2.py3-none-any.whl

# ubuntu 设置 ntp 服务器
## ntp 服务方式：
* 编辑 ``/etc/ntp.conf`` 中的 ``pool 10.169.103.58 iburst`` 行，指定需要同步的 IP
* service ntp start

## crontab 方式：
1. 通过开始菜单，输入 regedit 命令后打开注册表设定画面，此时请一定备份注册表文件。
2. 修改以下选项的键值  HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\TimeProviders\  NtpServer 内的「Enabled」设定为 1，打开 NTP 服务器功能
3. 修改以下键值  HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\Config\  AnnounceFlags 设定为 5, 该设定强制主机将它自身宣布为可靠的时间源，从而使用内置的互补金属氧化物半导体 (CMOS) 时钟。
4. 在 dos 命令行执行以下命令，确保以上修改起作用
net stop w32time
net start w32time
5. linux 下执行 crontab -e
6. 输入：``*/1 * * * * /usr/sbin/ntpdate 192.168.255.55 > /var/log/cron 2>&1``
注： 2>&1 表示将错误信息也打印至文件
7. 执行 crontab -l 查看是否设置成功
8. service cron restart 重启服务
9. ps -A|grep cron 查看进程
10. tail /var/log/cron 查看对时结果
11. ``apt install sysv-rc-conf`` 安装服务管理工具
12. 关闭 ntp 服务

# python 性能分析
(http://python.jobbole.com/87621/)

# 机器学习教程
[斯坦福大学 CS231n 卷积神经网络与图像识别](http://cs231n.stanford.edu/)
[吴恩达 Deep Learning Specialization](https://www.coursera.org/specializations/deep-learning)
[Udacity 免费深度学习课程](https://www.udacity.com/course/deep-learning—ud730)
[Geoffrey Hinton 的 Neural Networks For Machine Learning](https://www.coursera.org/learn/neural-networks)
[斯坦福大学 CS224d 自然语言处理深度学习](http://cs224d.stanford.edu/)
[Ian Goodfellow 的 DeepLearning 书籍](https://exacity.github.io/deeplearningbook-chinese/)
[良心 GitHub 项目：各种机器学习任务的顶级结果（论文）汇总）](https://github.com//RedditSota/state-of-the-art-result-for-machine-learning-problems)

# apt-get 非正常退出后，出现 dpkg –configure -a 时，暴力解决
rm /var/lib/dpkg/updates/*

# latex
如果你只用 latex 画图的话，可以只看 pgfmanual 这个宏包就行了，安装完 texlive，文档都会一起安装了
[安装](https://liam0205.me/texlive/)
[在线体验](https://www.sharelatex.com/project)
《102 分钟学会 latex》


[「 Neural Networks and Deep Learning 」中文翻译（连载完毕）](https://hit-scir.gitbooks.io/neural-networks-and-deep-learning-zh_cn/content/)

# ubuntu 执行 mount 报错
ubuntu 下如果 mount 的是 window 的共享目录，会出现以下错误：
```
# mount -t cifs -o XXX_PATH LOCAL_PATH
mount: XXX_PATH is write-protected, mounting read-only
mount: cannot mount XXX_PATH read-only
```
执行以下命令即可：
```
apt-get install -y cifs-utils
```

# Flask 单元测试
[官方网站](https://pythonhosted.org/Flask-Testing/)

官方给出的例子如下：
```
#coding=utf8
from flask import Flask,jsonify
from flask_testing import TestCase
import unittest

app = Flask(__name__)

@app.route("/ajax/")
def some_json():
    return jsonify(success=True)

class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_some_json(self):
        response = self.client.get("/ajax/")
        '''''
               判断还回的 JSON 对像是不是{'success':True}
        '''
        self.assertEqual(response.json, dict(success=True))

if  __name__ =='__main__':
    unittest.main()
```

# Structuring Your TensorFlow Models
https://github.com/tensorflow/models/blob/master/tutorials/rnn/ptb/ptb_word_lm.py
存在的问题：整个 Graph 都定义在 PTBModel 的 init 函数中，可读性和重用性不太好

https://github.com/tensorflow/models/blob/master/tutorials/embedding/word2vec_optimized.py
存在的问题：直接将整个 init 函数拆分成了多份，但是整个计算图依然在 build_graph 一个函数中实现，正常的看代码的顺序是 main——train——self._train_thread_body——self._train——train——build_graph——__init__
较为冗长的调用关系，重复的命名，无法直观的看出 train 就是我们计算图中关键的节点。根本原因是 build_graph 中集合了整张图的描述。

按照我们的正常思维，计算图会有输入、预测函数、损失函数、优化函数、输出，如果按照以上部分将计算图分割，将能提高重用性和可读性
http://danijar.com/structuring-your-tensorflow-models/
弄两张 Scopes 对比，没有添加 Scopes 时的调试信息

# 数组名退化
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


# 二分查找
```c
int bin_find(int* nums, int numsSize, int target) {
    int hi = numsSize - 1;
    int low = 0;
    int mid;
    while (hi >= low) {
        mid = low + (hi - low) / 2;
        if (target == nums[mid]) {
            return mid;
        }
        else if (target > nums[mid]) {
            low = mid + 1;
        }
        else {
            hi = mid - 1;
        }
    }
    return -1;

}
```
# 双向链表
```c
#include <stdio.h>

#define prefetch(X) X
#define offset_of(type, member) ((size_t)&((type *)0)->member)
#define container_of(ptr, type, member) ((type *)((unsigned char *)ptr - offset_of(type,member)))

/* XXX list 结构体定义 */
struct list_head {
    struct list_head *next, *prev;
};

#define LIST_HEAD_INIT(name) { &(name), &(name) }

/* XXX 局部、全局 list 初始化接口 */
#define LIST_HEAD(name) struct list_head name = LIST_HEAD_INIT(name)

/* XXX 初始化已经存在的 list 头节点对象 */
static inline void INIT_LIST_HEAD(struct list_head *list)
{
    list->next = list;
    list->prev = list;
}

/* 插入元素的内部实现 */
static inline void __list_add(struct list_head *nnew,
        struct list_head *prev,
        struct list_head *next)
{
    next->prev = nnew;
    nnew->next = next;
    nnew->prev = prev;
    prev->next =nnew;
}

/* XXX 将元素插入链表头部 */
static inline void list_add(struct list_head *nnew, struct list_head *head)
{
    __list_add(nnew, head, head->next);
}

/* XXX 将元素插入链表尾部 */
static inline void list_add_tail(struct list_head *nnew, struct list_head *head)
{
    __list_add(nnew, head->prev, head);
}

/* 删除元素的内部实现 */
static inline void __list_del(struct list_head * prev, struct list_head * next)
{
    next->prev = prev;
    prev->next = next;
}

/* XXX 删除指定元素 */
static inline void list_del(struct list_head *entry)
{
    __list_del(entry->prev, entry->next);
}

/* XXX 判断该节点是否为尾节点 */
static inline int list_is_last(const struct list_head *list,
        const struct list_head *head)
{
    return list->next == head;
}

/* XXX 判断链表是否为空，仅检查后向指针 */
static inline int list_empty(const struct list_head *head)
{
    return head->next == head;
}

/* XXX 判断链表中是否仅有一个元素 */
static inline int list_is_singular(const struct list_head *head)
{
    return !list_empty(head) && (head->next == head->prev);
}

#define list_entry(ptr, type, member) container_of(ptr, type, member)

#define list_first_entry(ptr, type, member) list_entry((ptr)->next, type, member)

#define list_last_entry(ptr, type, member) list_entry((ptr)->prev, type, member)

#define list_for_each_entry(type_pos, pos, head, member)                  \
    for (pos = list_entry((head)->next, type_pos, member);                \
            &pos->member != (head);                                       \
            pos = list_entry(pos->member.next, type_pos, member))

#define list_for_each_entry_safe(type_pos, pos, ptr, head, member)        \
    for (pos = list_entry((head)->next, type_pos, member),                \
            ptr = list_entry(pos->member.next, type_pos, member);         \
            &pos->member != (head);                                       \
            pos = ptr, ptr = list_entry(ptr->member.next, type_pos, member))

#define list_for_each_entry_reverse(type_pos, pos, head, member)          \
        for (pos = list_entry((head)->prev, type_pos, member);            \
                &pos->member != (head);                                   \
                pos = list_entry(pos->member.prev, type_pos, member))

#define list_for_each_entry_safe_reverse(type_pos, pos, n, head, member)  \
    for (pos = list_entry((head)->prev, type_pos, member),                \
            n = list_entry(pos->member.prev, type_pos, member);           \
            &pos->member != (head);                                       \
            pos = n, n = list_entry(n->member.prev, type_pos, member))

/* 示例 */
#include <stdlib.h>

typedef struct _list_demo_t{
    int value;
    struct list_head node;
} list_demo_t;

int main()
{
    LIST_HEAD (local_list);
    printf("list_empty [%d]\n", list_empty(&local_list));

    list_demo_t* list_node_1 = (list_demo_t*)malloc(sizeof(list_demo_t));
    list_node_1->value = 1;
    list_demo_t* list_node_2 = (list_demo_t*)malloc(sizeof(list_demo_t));
    list_node_2->value = 2;
    list_demo_t* list_node_3 = (list_demo_t*)malloc(sizeof(list_demo_t));
    list_node_3->value = 3;
    list_demo_t* list_node_4 = (list_demo_t*)malloc(sizeof(list_demo_t));
    list_node_4->value = 4;
    list_demo_t* list_node_5 = (list_demo_t*)malloc(sizeof(list_demo_t));
    list_node_5->value = 5;
    list_demo_t* list_node_6 = (list_demo_t*)malloc(sizeof(list_demo_t));
    list_node_6->value = 6;
    list_add(&list_node_1->node, &local_list);
    list_add(&list_node_2->node, &local_list);
    list_add(&list_node_3->node, &local_list);
    list_add_tail(&list_node_4->node, &local_list);
    list_add_tail(&list_node_5->node, &local_list);
    list_add_tail(&list_node_6->node, &local_list);
    printf("list_empty [%d]\n", list_empty(&local_list));

    list_demo_t* tmp;
    list_demo_t* for_safe;
    printf("list_for_each_entry\n");
    list_for_each_entry(list_demo_t, tmp, &local_list, node)
    {
        printf("[%d]\n", tmp->value);
    }

    printf("list_first_entry [%d]\n", list_first_entry(&local_list, list_demo_t, node)->value);
    list_del(&list_first_entry(&local_list, list_demo_t, node)->node);
    printf("list_first_entry [%d]\n", list_first_entry(&local_list, list_demo_t, node)->value);
    printf("list_last_entry [%d]\n", list_last_entry(&local_list, list_demo_t, node)->value);
    list_del(&list_last_entry(&local_list, list_demo_t, node)->node);
    printf("list_last_entry [%d]\n", list_last_entry(&local_list, list_demo_t, node)->value);

    printf("list_for_each_entry_safe\n");
    list_for_each_entry_safe(list_demo_t, tmp, for_safe, &local_list, node)
    {
        printf("[%d]\n", tmp->value);
    }
    printf("list_for_each_entry_safe_reverse\n");
    list_for_each_entry_safe_reverse(list_demo_t, tmp, for_safe, &local_list, node)
    {
        list_del(&tmp->node);
        printf("[%d]\n", tmp->value);
        free(tmp);
    }
    printf("list_for_each_entry_reverse\n");
    list_for_each_entry_reverse(list_demo_t, tmp, &local_list, node)
    {
        printf("[%d]\n", tmp->value);
    }
}
```

# 单向链表

```c
#include "stdafx.h"
#include "stdio.h"
#include "stdlib.h"
#include "string.h"

typedef int elemType;

struct Node{
    elemType element;
    Node *next;
};

// 1. 初始化线性表，即置单链表的表头指针为空
void initList(Node *pNode)
{
    pNode = NULL;
    printf("initList 函数执行，初始化成功、n");
}

//2. 创建线性表，此函数输入负数终止读取数据
Node *createList()
{
    Node *p1,*p2,*pNode;
    p1=p2=pNode=(Node *)malloc(sizeof(Node));
    memset(p1,0,sizeof(Node));

    scanf("%d",&p1->element);
    p1->next = NULL;  //
    while(p1->element > 0)
    {
        if(NULL == pNode)
        {
            pNode = p1;
        }
        else
        {
            p2->next = p1;
        }

        p2=p1;

        p1=(Node *)malloc(sizeof(Node));
        memset(p1,0,sizeof(Node));

        scanf("%d",&p1->element);
        p1->next = NULL;  //
    }

    return pNode;
}

//3. 打印链表，链表的遍历
void printList(Node *pNode)
{
    if(NULL == pNode)
    {
        printf("PrintList 函数执行，链表为空、n");
    }
    else
    {
        while(NULL != pNode)
        {
            printf("%d\t", pNode->element);
            pNode = pNode->next;
        }
    }
    printf("\n");
}

// 4. 清除线性表 L 中的所有元素，即释放单链表 L 中所有的结点，使之成为一个空表
int clearList(Node *pNode)
{
    Node *pNext;

    while(NULL != pNode)
    {
        pNext = pNode->next;
        free(pNode);
        pNode = pNext;
    }

    return 1;
    //printf("清空链表成功！\n");
}

// 5. 返回单链表的长度
int sizeList(Node *pNode)
{
    int i=0;

    while(NULL != pNode)
    {
        i++;
        pNode = pNode->next;
    }

    return i;
}

// 6. 检查单链表是否为空，若为空则返回 1，否则返回 0
int isEmptyList(Node *pHead)
{
    if(pHead == NULL)
    {
        printf("isEmptyList 函数执行，链表为空、n");
        return 1;
    }
    printf("isEmptyList 函数执行，链表非空、n");

    return 0;
}

//7. 返回单链表中第 pos 个结点中的元素，若 pos 超出范围，则停止程序运行
elemType getElement(Node *pNode,int pos)
{
    int i=0;

    if(pos < 1)
    {
        printf("getElement 函数执行，pos 值非法、n");
        return 0;
    }
    if(pNode == NULL)
    {
        printf("getElement 函数执行，链表为空、n");
        return 0;
    }

    while(pNode!= NULL)
    {
        i++;
        if(i == pos)
            return pNode->element;
        pNode = pNode->next;
    }
    // 上面的 while 循环也可用 for 循环来代替


    if(i < pos)                  // 链表长度不足则退出
    {
        printf("getElement 函数执行，pos 值超出链表长度、n");
    }
    return 0;
}

// 8. 从单链表中查找具有给定值 x 的第一个元素，若查找成功则返回该结点 data 域的存储地址，否则返回 NULL
elemType *getElemAddr(Node *pNode,elemType elemValue)
{
    if(elemValue <= 0)
    {
        printf("getElemAddr 函数执行，给定值不合法、n");
        return NULL;
    }
    if(pNode == NULL)
    {
        printf("getElemAddr 函数执行，链表为空、n");
        return NULL;
    }

    while(pNode!= NULL)
    {
        if(pNode->element == elemValue)
        {
            printf("getElemAddr 函数执行，元素 %d 的地址为 0x%x\n",elemValue,&(pNode->element));
            return &(pNode->element);   // 如果不直接 return 的话，一定记得用 break 跳出循环
        }
        pNode = pNode->next;
    }

    printf("getElemAddr 函数执行，在链表中未找到 %d 值、n",elemValue);

    return NULL;
}

//9. 把单链表中第 pos 个结点的值修改为 elemValue 的值，若修改成功返回 1，否则返回 0
int modifyElem(Node *pNode,int pos, elemType elemValue)
{
    printf("modifyElem 函数执行，即将把链表的第 %d 个元素的值改为 %d\n",pos,elemValue);
    if(NULL == pNode)
    {
        printf("modifyElem 函数执行，链表为空、n");
    }
    if(pos < 1)
    {
        printf("modifyElem 函数执行，pos 值非法、n");
        return 0;
    }
    if(elemValue < 1)
    {
        printf("modifyElem 函数执行，elemValue 值非法、n");
        return 0;
    }

    int i=0;
    while(pNode != NULL)
    {
        i++;
        if(i == pos)
        {
            pNode->element = elemValue;
            return 1;
        }
        pNode = pNode->next;
    }

    if(i < pos)                  // 链表长度不足则退出
    {
        printf("modifyElem 函数执行，pos 值超出链表长度、n");
        return 0;
    }

    return 0;
}

//10. 向单链表的表头插入一个元素
int insertHeadList(Node **pNode,elemType elemInserted)
{
    if(NULL == *pNode)
    {
        printf("insertHeadList 函数执行，链表为空、n");
        return 0;
    }
    if(elemInserted < 1)
    {
        printf("insertHeadList 函数执行，elemInserted 值非法、n");
        return 0;
    }

    Node *pHead,*pLast;
    pLast = *pNode;

    pHead = (Node *)malloc(sizeof(Node));
    memset(pHead,0,sizeof(Node));
    pHead->element = elemInserted;
    pHead->next = pLast;

    *pNode = pHead;
    return 1;
}

// 11. 向单链表的末尾添加一个元素
int insertLastList(Node **pNode,elemType elemInserted)
{
    if(NULL == *pNode)
    {
        printf("insertLastList 函数执行，链表为空、n");
        return 0;
    }
    if(elemInserted < 1)
    {
        printf("insertLastList 函数执行，elemInserted 值非法、n");
        return 0;
    }

    Node *pLast,*pTemp;
    pTemp = *pNode;   // 把*pNode 先赋值给 pTemp，后面的操作（例如循环链表到最后一个节点）主要是对 pTemp 进行操作，否则返回*pNode 的时候，将返回链表*pNode 在当前指针后面的部分，而不是整个链表。
    // 因为 pTemp 与*pNode 指向同一个链表，所以对 pTemp 进行节点改动即是对*pNode 作改动

    pLast = (Node *)malloc(sizeof(Node));
    memset(pLast,0,sizeof(Node));
    pLast->element = elemInserted;
    pLast->next = NULL;

    // 循环链表至最后一个节点
    while(pTemp->next != NULL)
    {
        pTemp = pTemp->next;
    }
    // 把新增节点加入到链表中
    pTemp->next = pLast;

    return 1;
}

//12. 向单链表中第 pos 个结点位置插入元素为 x 的结点，若插入成功返回 1，否则返回 0
int insertList(Node **pNode, int pos, elemType elemInserted)
{
    if(NULL == *pNode)
    {
        printf("insertList 函数执行，链表为空、n");
        return 0;
    }
    if(elemInserted < 1)
    {
        printf("insertList 函数执行，elemInserted 值非法、n");
        return 0;
    }
    if(pos < 1)
    {
        printf("insertList 函数执行，pos 值非法、n");
        return 0;
    }

    Node *pInserted,*pTemp, *pLast;
    pTemp = *pNode;   // 把*pNode 先赋值给 pTemp，后面的操作（例如循环链表到最后一个节点）主要是对 pTemp 进行操作，否则返回*pNode 的时候，将返回链表*pNode 在当前指针后面的部分，而不是整个链表。
    // 因为 pTemp 与*pNode 指向同一个链表，所以对 pTemp 进行节点改动即是对*pNode 作改动

    pInserted = (Node *)malloc(sizeof(Node));
    memset(pInserted,0,sizeof(Node));
    pInserted->element = elemInserted;
    pInserted->next = NULL;  // 先赋值为 null

    // 循环链表至 pos 节点
    int i = 0;
    while(pTemp->next != NULL)
    {
        i = i + 1;
        if(i == pos)
        {
            pLast->next = pInserted;  // 让上一个节点的 next 指向插入节点
            pInserted->next = pTemp;  // 让插入节点的 next 指向下一节点
            break;
        }
        pLast = pTemp;  // 记住上一个节点的位置
        pTemp = pTemp->next;
    }

    return 1;
}

//13. 从单链表中删除表头结点，并把该结点的值返回，若删除失败则停止程序运行
int deleteHeadList(Node **pNode)
{
    int currVal;
    Node *pTemp;

    if(NULL == *pNode)
    {
        printf("DeleteHeadList 函数执行，链表为空、n");
        return 0;
    }

    pTemp = *pNode;
    currVal = (*pNode)->element;
    *pNode = (*pNode)->next;

    pTemp->next = NULL;  // 将头节点的 next 指针置为 NULL
    free(pTemp);

    return currVal;
}

//14. 从单链表中删除表尾结点并返回它的值，若删除失败则停止程序运行
int deleteLastList(Node **pNode)
{
    int currVal;
    Node *pTemp,*pLast;

    if(NULL == *pNode)
    {
        printf("DeleteLastList 函数执行，链表为空、n");
        return 0;
    }

    pTemp = *pNode;
    while(pTemp->next != NULL)
    {
        pLast = pTemp;
        pTemp = pTemp->next;
    }

    pLast->next = NULL;
    currVal = pTemp->element;

    free(pTemp);

    return currVal;
}
//15. 从单链表中删除第 pos 个结点并返回它的值，若删除失败则停止程序运行
int deleteList(Node **pNode, int pos)
{
    int currVal, i;
    Node *pTemp,*pLast,*pNext;

    if(NULL == *pNode)
    {
        printf("DeleteLastList 函数执行，链表为空、n");
        return 0;
    }
    if(pos < 1)
    {
        printf("DeleteList 函数执行，pos 值非法、n");
        return 0;
    }

    pTemp = *pNode;
    i = 0;
    while(pTemp != NULL)
    {
        i = i + 1;
        if(i == pos)
        {
            break;
        }
        pLast = pTemp;
        pTemp = pTemp->next;
    }
    pNext = pTemp;
    pNext = pNext->next;
    pLast->next = pNext;
    currVal = pTemp->element;

    free(pTemp);

    return currVal;
}

//16. 从单链表中删除值为 x 的第一个结点，若删除成功则返回 1, 否则返回 0
int deleteXList(Node **pNode, elemType elemVal)
{
    Node *pTemp,*pLast,*pNext;

    if(NULL == *pNode)
    {
        printf("DeleteXList 函数执行，链表为空、n");
        return 0;
    }
    if(elemVal < 1)
    {
        printf("DeleteXList 函数执行，elemVal 值非法、n");
        return 0;
    }

    pTemp = *pNode;
    int i = 0;
    while(pTemp != NULL)
    {
        if(pTemp->element == elemVal)
        {
            i = 1;
            break;
        }
        pLast = pTemp;
        pTemp = pTemp->next;
    }
    if(i == 0)
    {
        printf("DeleteXList 函数执行，链表中没有值为 %d 的节点、n",elemVal);
        return 0;
    }
    pNext = pTemp;
    pNext = pNext->next;
    pLast->next = pNext;

    free(pTemp);

    return 1;
}

//17. 交换 2 个元素的位置
int exchangeList(Node **pNode, int pos1, int pos2)
{
    if(NULL == *pNode)
    {
        printf("exchangeList 函数执行，链表为空、n");
        return 0;
    }
    if(pos1 < 1 || pos2 < 1)
    {
        printf("exchangeList 函数执行，pos 值非法、n");
        return 0;
    }

    Node *pTemp, *pFirst, *pSecond;
    pTemp = *pNode;
    int i = 0;
    while(pTemp != NULL)
    {
        i++;
        if(i == pos1)
            pFirst = pTemp;
        else if(i == pos2)
            pSecond = pTemp;

        pTemp = pTemp->next;
    }

    int p;
    p = pFirst->element;
    pFirst->element = pSecond->element;
    pSecond->element = p;
}

//18. 将单链表进行排序
int sortList(Node **pNode)
{
    if(NULL == *pNode)
    {
        printf("sortList 函数执行，链表为空、n");
        return 0;
    }

    Node *pTemp;
    pTemp = *pNode;

    int Listsize = sizeList(*pNode);

    // 循环：用 for 循环来取代指针循环，因为指针循环一次后，下次起始的指针将自动转到下一节点，而我们还想从第一个元素开始
    for(int i=0; i < Listsize; i++)
    {
        Node *pCurr, *pLast;
        pCurr = pLast = pTemp;

        for(int k=0; k < Listsize-i; k++)
        {
            int p = 0;

            if(pLast->element < pCurr->element)
            {
                p = pLast->element;
                pLast->element = pCurr->element;
                pCurr->element = p;
            }
            pLast = pCurr;
            pCurr = pCurr->next;
        }
    }
}

//19. 向有序单链表中插入元素 x 结点，使得插入后仍然有序 , 假设现在已知一个升序的单链表
int insertXList(Node **pNode, elemType elemInserted)
{
    if(NULL == *pNode)
    {
        printf("insertList 函数执行，链表为空、n");
        return 0;
    }
    if(elemInserted < 1)
    {
        printf("insertList 函数执行，elemInserted 值非法、n");
        return 0;
    }

    Node *pInserted,*pTemp, *pLast;
    pTemp = *pNode;   // 把*pNode 先赋值给 pTemp，后面的操作（例如循环链表到最后一个节点）主要是对 pTemp 进行操作，否则返回*pNode 的时候，将返回链表*pNode 在当前指针后面的部分，而不是整个链表。
    // 因为 pTemp 与*pNode 指向同一个链表，所以对 pTemp 进行节点改动即是对*pNode 作改动

    pInserted = (Node *)malloc(sizeof(Node));
    memset(pInserted,0,sizeof(Node));
    pInserted->element = elemInserted;
    pInserted->next = NULL;  // 先赋值为 null

    // 寻找该插入的节点
    while(pTemp->next != NULL)
    {
        if(pTemp->element > elemInserted)
        {
            pLast->next = pInserted;  // 让上一个节点的 next 指向插入节点，注意：如果该节点是第一节点，没有上一个节点呢？
            pInserted->next = pTemp;  // 让插入节点的 next 指向下一节点
            break;
        }
        pLast = pTemp;  // 记住上一个节点的位置
        pTemp = pTemp->next;
    }

    return 1;
}

void main()
{
    Node *pList=NULL;
    int length = 0;

    initList(pList);       // 链表初始化
    printList(pList);       // 遍历链表，打印链表

    pList=createList(); // 创建链表
    printList(pList);

    sizeList(pList);        // 链表的长度

    isEmptyList(pList);     // 判断链表是否为空链表

    elemType posElem;
    posElem = getElement(pList,3);  // 获取第三个元素，如果元素不足 3 个，则返回 0
    printf("getElement 函数执行，位置 3 中的元素为 %d\n",posElem);
    printList(pList);

    getElemAddr(pList,5);   // 获得元素 5 的地址

    modifyElem(pList,4,1);  // 将链表中位置 4 上的元素修改为 1
    printList(pList);

    insertHeadList(&pList,12);   // 表头插入元素 12
    printList(pList);

    insertLastList(&pList,10);  // 表尾插入元素 10
    printList(pList);

    insertList(&pList,2,11);  // 第 2 个节点插入元素 11
    printList(pList);

    deleteHeadList(&pList);  // 删除表头节点
    printList(pList);

    deleteLastList(&pList);  // 删除表尾节点
    printList(pList);

    deleteList(&pList,2);  // 删除第 2 个节点
    printList(pList);

    deleteXList(&pList,3);  // 删除值为 3 的第一个节点
    printList(pList);

    exchangeList(&pList,2,3);  // 第 2 个节点与第 3 个节点的值进行交换
    printList(pList);

    sortList(&pList);  // 对单链表进行冒泡排序
    printList(pList);

    insertXList(&pList,11);  // 向有序链表中插入一个元素 11，使得插入后的链表仍然有序
    printList(pList);

    clearList(pList);       // 清空链表
    //system("pause");
}
```
