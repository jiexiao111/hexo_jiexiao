---
title: C 程序调试
date: 2018-01-02 10:32:53
categories: 编程语言
tags:
  - C
---

<!-- 文章开头都用它了，整齐才好看 -->
{% note default %}
调试 C 语言多年，简单总结一下自己的心得
{% endnote %}

<!--more-->

---
# 一些想法
作为开发人员，我们每天大部分的时间都在进行调试，只有清晰的认识我们的工具才能更高效的进行工作。一般来说，我们遇到的大部分问题都是业务流程出现了问题，这里的业务流程不仅仅指的是报文收发，也包括引用计数器的操作，对象成员的读写等等，这类问题的特点是，各个函数实现本身没有问题，但是以某种特殊的序列执行后就引入了问题，通常来说充满各种回调的模块我们通过代码可能无法预见到所有的调用顺序。

GDB 脚本
开销：2ms 每次命中
优势：GDB 脚本是调试最高效的办法，我们无需修改和编译代码就能够掌握程序的动态信息。
劣势：GDB 断点命中后，会触发中断、进程切换、系统调用、文件读写等一系列高消耗的操作，所以高频率的命中会占用很高的 CPU，在 Microkernel 中很可能导致定时器紊乱、用户无法发起等异常。
适用场景：断点命中频率小于每秒 100 次（断点命中占用 CPU 20%），或者更本不在乎 CPU 是否过载的场景。通常开发在进行功能自验证时或者走读陌生模块的代码时，这种方式是最为实用的。

日志打印
开销： 2us 每行日志
优势： 流程相关的问题，日志基本上是万能的方法
劣势： 通常需要反复增加日志进行问题复现，反复的进行修改代码——编译 —— 复现，定位效率并不高 。另外，日志打印的信息占用的硬盘空间大，3M 行日志差不多需要占用 1G 的硬盘空间。
适用场景： 日志打印速率小于 100K 行的场景（打印日志占用 CPU 20%）

流程信息保存至内存
开销： 平均 20ns 每写入 8 字节
优势： 极其高效的记录速率，在定位 Microkernel 中状态机、Socket 相关问题时非常有效
劣势： 依赖于良好的代码实现，否则需要进行较多调整
适用场景： 每秒写入流程信息小于 10M 条的场景，如，高频读写的对象出现异常

GDB 脚本和日志打印较为常用，不再累述，主要通过定位 Microkernel 状态跃迁异常的问题来说明一下如何将流程信息保存至内存。
我们 NTE 的执行的大致流程为：1、平台调用协议的接口执行 action，协议执行完成后向平台发送 event；2、平台遍历 event 链表，修改 event 对应的 FSM 的状态；3、平台遍历 fsm 链表，根据 fsm 的状态确定下一个动作，然后调用协议的执行接口执行下一个 action。如果在第三步中协议发现平台调用了错误的 action，我们只能知道 FSM 的状态出现了错误，但是如何出错的已经无法知晓，因为在第二步遍历 event 链表后，该链表的资源已经被完全清空。定位这个问题，我们至少需要打印每一个 FSM 的每一次状态跃迁以及每一个 FSM 收到的每一个 event，此时问题就来了，FSM 的状态切换和 event 的触发都是极其频繁的调用，打印日志导致 CPU 负载进一步升高，很容易导致其他异常，另外，如果用户使用自动化运行测试，很可能出现日志被覆盖的情况。我计算过打印一条日志大致需要 2us，现在需要进一步减少记录流程的消耗，只有考虑把日志写入内存了，一般来说 8 字节写入 L1cache 小于 1ns, L2 cache 小于 10ns， L3 cache 小于 50ns，写入主存小于 100ns，高频度的写入，意味着高的 Cache 命中率，所以写入内存的时间期望在 20ns 左右，相较日志打印提升了 100 倍性能。以 1W 用户在线，每个用户每秒需要记录 20 次信息为例，每秒打印日志需要消耗 1W * 20 * 2us = 400ms，即 40% CPU，如果场景本身消耗的 CPU 超过 50% 则会出现 CPU 过载等异常。可以看出就必须把流程信息保存至内存。现在有两个问题：1、保存在哪； 2、保存哪些信息。
第一个问题：我们可以看到问题的重点为 FSM 对象，所以，这些信息我们保存至 FSM 对象的结构体中，以每个 FSM 保存 640 字节信息来算，20K 在线用户仅需要消耗 13M 空间
第二个问题：需要保存触发 FSM 状态跃迁和 event 触发的位置，通常这些位置处于公共接口，所以还需要打印上几层调用栈所在的位置，通常我们只需要保存 5 层栈信息就足够了（每个栈指针 8 字节）。历史栈信息我们只需要保存最近 16 次的信息即可。所以只需要 5 * 8 * 16 *  20K 就能够记录所有用户最近二十次重要的修改记录，如果出现问题，只需要打印指定的 FSM 中保存的信息即可。
 
其他需要将流程信息保存至内存场景举例：
协议栈中 Socket 引用计数器发生错误。我们按照典型场景 1024 包长打满 10Gpbs 流量进行估算，每个 Microkernel 需要达到 10Gpbs / 1024 / 3 = 3Mpps，这种高负载场景，GDB 脚本就不要想了，我们假设每发送一个报文打印一条日志，3M / 50K * 20% = 1200% ，显然通过 Microkernel 日志接口打印信息也是不现实的。即使 CPU 不是瓶颈，3M 行日志大致要占用 1G 的空间，也就是说 10s 就会打印 10G 的日志，这个大小的文件打开和操作已经非常慢了，如果定位问题需要打印超过 10s 日志就更加艰难了，而我们最常见的问题通常复现时间是几分钟或者几个小时，这种情况下，通过将流程信息保存至 Socket 结构体中就很很好的定位。

