---
title: 常用快捷键汇总
categories: 工具使用
tags:
  - 快捷键
---

{% note default %}
日常使用的快捷键太多，分散存储不易查找，得益于 Next 主题优秀的目录导航，可以将所有的快捷键统一记录
{% endnote %}

<!--more-->

---

# Item2
{% note default %}
Mac 下的 Item2 真心好用
{% endnote %}
## 标签
新建标签：``command + t``
关闭标签：``command + w``
关闭标签：``command + z``
切换标签：``command + 数字 ``
选择标签：``command + 左右方向键`` 或者 ``command + { 或 command + }``

## 窗口
垂直分屏：``command + d``
水平分屏：``command + shift + d``
最大化当前分屏：``command + shift + Enter``
切换屏幕：``command + option + 方向键`` 或者 ``command + [ 或 command + ]``
预览所有窗口 + 搜索：``command + option + e``

## 历史
查看命令历史：``command + ;``
查看剪贴板历史：``command + shift + h``

## 其他
切换全屏：``command + enter``
查找：``command + f``
高亮光标：``command + /``
标记：``command + shift + m``
跳转：``command + shift + j``

---

# Chrome

{% note default %}
通常只需要查看帮助 [?] 即可，不过自己写的东西理解起来还是要容易些
{% endnote %}

## 滚动
向下滚动：``j``
向上滚动：``k``
向左滚动：``h``
向右滚动：``l``
滚动到最上方：``gg``
滚动到最下方：``G``
滚动到最左方：``zH``
滚动到最右方：``zL``
向下滚动半页：``d``
向上滚动半页：``u``

## 常用
后退：``H``
前进：``L``
刷新：``r``
查找：``/``
下一个匹配：``n``
上一个匹配：``N``
选中地址栏：``command/Ctrl + l``
隐藏标签栏：``Ctrl + Shift + B``

## URL 相关操作
拷贝当前 URL:                                                         ``yy``
拷贝指定 URL:                                                        ``yf *相当于鼠标右键 ->复制链接*``
打开上一级 URL:                                                      ``gu``
打开最上级 URL:                                                      ``gU``
在当前标签打开链接：``f *最常用的键，相当于鼠标左键*``
在新建标签打开链接：``F``
在当前标签页中打开剪切板中的 URL:                                    ``p``
在新建标签页中打开剪切板中的 URL:                                    ``P``

## 输入
进入编辑模式：``i *比如说要在 jupyter 中编辑的时候，要先切换至编辑模式，否则快捷键均被覆盖*``
选择输入框：``gi *相当于鼠标左键点击输入框*``
选择下一个 frame:                                                     ``gf *很多页面只有一个 frame 所以不常用*``
选择上一个 frame:                                                     ``gF``

## 快速检索
打开快速检索窗口，搜索书签 / 历史记录：``o``
打开快速检索窗口，搜索书签 / 历史记录，在新建标签中打开链接：``O``
打开快速检索窗口，搜索书签：``b``
打开快速检索窗口，搜索书签，在新建标签中打开链接：``B``
打开快速检索窗口，将当前 URL 自动填入便于编辑：``ge``
打开快速检索窗口，将当前 URL 自动填入便于编辑，在新建标签中打开链接：``gE``
打开快速检索窗口，搜索 Tab 标签：``T *在 Tab 页很多的时候很好用*``

## Tab 页
新建 Tab 页：``t``
关闭当前标签页：``x``
打开最近关闭的标签页：``X``
选择上一个 Tab 页：``J/gT *经常遇到不能使用 vimium 的网页只能使用 Tab 键替代*``
选择下一个 Tab 页：``K/gt *经常遇到不能使用 vimium 的网页只能使用 Shift Tab 键替代*``
选择最近浏览的 Tab 页：``^``
选择第一个 Tab 页：``g0``
选择最后一个 Tab 页：``g$``
将当前标签页向左移动：``<<``
将当前标签页向右移动：``>>``
在新建页中打开当前页面：``yt *很常用，相当于 yy 复制当前链接，P 打开新的链接*``
将当前标签移至新窗口：``W *相当于鼠标拖拽标签页至窗口外*``

## 其他
帮助：``?``
查看网页源码：``gs``

## 不知道能干什么...
Open multiple links in a new tab:                                    ``< a-f >``
Enter visual mode:                                                   ``v``
Enter visual line mode:                                              ``V``
Follow the link labeled previous or <:                               ``[[``
Follow the link labeled next or >:                                   ``]]``
Create a new mark:                                                   ``m``
Go to a mark:                                                        `` ` ``
Pin or unpin current tab:                                            ``< a-p >``
Mute or unmute current tab:                                          ``< a-m >``

---

# Vim
{% note default %}
vim 需要记得太多了，用了几年有些都还不知道，汇总一下实用的，不常用的就不罗列了
{% endnote %}

## 普通模式

### 折叠
zi 在 vim 中取消、生效折叠

### 移动

#### 左右

左移：``h``
右移：``l``
行尾：``$``
行首：``0``
非空行首：``^``
前向行内查找：``f{char}``
后向行内查找：``F{char}``
前向行内查找，目标字符前一个位置：``t{char}``
后向行内查找，目标字符后一个位置：``T{char}``
重复行内查找：``;``
反向重复行内查找：``,``

#### 上下
上移：``k``
下移：``j``
至尾行：``G``
至首行：``gg``
至第 n 尾行：``nG``
至全文件 %n 处：``n%``

#### 文本对象

向右 N 个单词：``w``
向右 N 个单词，停在词尾：``e``
向右 N 个空白隔开的单词：``W``
向右 N 个空白隔开的单词，停在词尾：``E``

向左 N 个单词：``b``
向左 N 个单词，停在词尾：``ge``
向左 N 个空白隔开的单词：``B``
向左 N 个空白隔开的单词，停在词尾：``gE``

向前 N 个句子：``)``
向后 N 个句子：``(``
向前 N 个段落：``}``
向后 N 个段落：``{``

### 查找

向前查找``{``: ``]]``
向后查找``{``: ``[[``
向前查找``}``: ``][``
向后查找``}``: ``[]``
``第一个 [ 表示方向，重复的找 {, 不同的找 }``

向前查找``)``: ``])``
向后查找``(``: ``[(``
向前查找``}``: ``]}``
向后查找``{``: ``[{``

向前查找 ``#else`` 或 ``#endif``: ``]#``
向后查找 ``#if`` 或 ``#else``: ``[#``
向前查找 ``*/``: ``]*``
向后查找 ``/*``: ``[*``

查找：``/``
反向查找：``?``
重复查找：``n``
反向重复查找：``N``
``可以使用正则表达式``

按光标下的单词查找：``*``
按光标下的单词反向查找：``#``
查找高亮的文本：``{visual} *``
反向查找高亮的文本：``{visual} #``

查找光标下的局部变量：``gd``
查找光标下的全局变量：``gD``

### 标记与跳转

标记：``m{a-zA-Z}``
文件内跳转：``'{a-z}``
全局跳转：``'{A-Z}``

跳转至文件最后被改动的位置：``'.``
列出活动的位置标记：``:marks``

向后跳转：``Ctrl + o``
向前跳转：``Ctrl + i``
列出跳转列表：``:ju``

转到当前光标下标签的定义：``Ctrl + ]``
跳转至本行中``{ ( [``等的对称位置：``%``

窗口顶部：``H``
窗口底部：``L``
窗口中部：``M``

### 滚动

向下滚动一行：``Ctrl + e``
向上滚动一行：``Ctrl + y``
向左滚动一列：``zh``
向右滚动一列：``zl``

向下滚动半屏：``Ctrl + d``
向上滚动半屏：``Ctrl + u``
向左滚动半屏：``zH``
向右滚动半屏：``zL``

当前行置为窗口顶部：``zt``
当前行置为窗口中部：``zz``
当前行置为窗口底部：``zb``

### 编辑

删除整行：``dd``
复制整行：``yy``
删除行内容：``D``
连接行：``J``
连接行，但不插入空格：``gJ``

粘贴至光标后：``p``
粘贴至光标前：``P``
粘贴至光标后，缩进与光标所在行一致：``]p``
粘贴至光标前，缩进与光标所在行一致：``]P``
粘贴至光标后，光标停留在粘贴文本后：``gp``
粘贴至光标前，光标停留在粘贴文本后：``gP``
交换当前光标及下一个字符：``xp``
交换当前光标及上一个字符：``Xp``
替换字符：``r``
替换字符并不影响布局：``gr``

将光标之上或之后的数值增加 N: ``CTRL-A``
将光标之上或之后的数值减少 N: ``CTRL-X``

### 进入 visual 模式

以字符方式开始高亮：``v``
使用上一次的可视区域开始高亮：``gv``
以行方式开始高亮：``V``
以列块方式开始高亮：``CTRL-V``

选择一个单词：``aw``
选择一个单词，不包括词尾空格：``iw``
选择一段不包含空白符的字串：``aW``
选择一段不包含空白符的字串，不包含词尾空格：``iW``

### 进入编辑模式

光标前插入：``i``
光标后插入：``a``
行首非空插入：``I``
行首插入：``gI``
行末插入：``A``

当前行下方插入新行：``o``
当前行上方插入新行：``O``

插入光标下方的字符：``Ctrl + e``
插入光标上方的字符：``Ctrl + y``

进入替换模式：``R``
进入替换模式，但不影响布局：``gR``
删除行，并进入插入模式：``cc``
删除字符，并进入插入模式：``s``

翻转大小写并前进光标：``~``





## 编辑模式

### 快捷键

补全路径：``Ctrl + x Ctrl + f``
向前删除单词：``Ctrl + w``
删除一段时间内输入的字符：``Ctrl + u``
增加缩进：``Ctrl + t``
减少当前行的缩进：``Ctrl + d``




## visual 模式

删除高亮的文本：``d``
删除高亮的文本，进入编辑模式：``c``
删除高亮的行，进入编辑模式：``C``
复制高亮的文本：``y``
替换高亮的文本：``r``

连接高亮行：``J``
连接高亮行，但不插入空格：``gJ``

翻转高亮文本的大小写：``~``
改高亮的文本为小写：``u``
改高亮的文本为大写：``U``
交换高亮区域的开始处和光标位置：``o``

选择 "一个句子" (sentence): ``as``
选择 "内含句子": ``is``
选择 "一个段落" (paragraph): ``ap``
选择 "内含段落": ``ip``
选择 "一个块" （从 "[(" 至 "])") (block): ``ab``
选择 "内含块" （从 "[(" 到 "])"): ``ib``
选择 "一个大块" （从 "[{" 到 "]}") (Block): ``aB``
选择 "内含大块" （从 "[{" 到 "]}"): ``iB``
选择 "一个 <> 块": ``a>``
选择 "内含 <> 块": ``i>``
选择 "一个标签块" （从 <aaa> 到 </aaa>) (tag): ``at``
选择 "内含标签块" （从 <aaa> 到 </aaa>): ``it``
选择 "一个单引号字符串": ``a'``
选择 "内含单引号字符串": ``i'``
选择 "一个双引号字符串": ``a"``
选择 "内含双引号字符串": ``i"``
选择 "一个反引号字符串": ``a```
选择 "内含反引号字符串": ``i```




## 命令行

将文件的内容插入到下一行：``:r {file}``
将命令结果插入到下一行：``:r {file}``
显示寄存器的内容：``:reg``







## motion

删除动作 {motion} 覆盖的文本，并进入插入模式：``c{motion}``
将动作 {motion} 覆盖的文本翻转大小写：``g~{motion}``
将动作 {motion} 覆盖的文本改为小写：``gu{motion}``
将动作 {motion} 覆盖的文本改为大写：``gU{motion}``

---

```






改变文本
重复最近一次改动 （将计数改为 N): ``.``
记录键入的字符，存入寄存器 {a-z}: ``q{a-z}``
记录键入的字符，添加进寄存器 {a-z}: ``q{A-Z}``
终止记录：``q``
执行寄存器 {a-z} 的内容 (N 次）: ``@{a-z}``
重复上次的 @{a-z} 操作 (N 次）: ``@@``
将寄存器 {a-z} 的内容当作 Ex 命令来执行：``:@{a-z}``
重复上次的 :@{a-z} 操作：``:@@``
撤销最近的 N 此改动：``u``
重做最近的 N 个被撤销的改动：``CTRL-r``
恢复最近被改动的行：``U``
执行 shell 命令：``:!{command}``
查看光标下的标识符的 man 帮助：``K``
显示第 [nr] 个错误 （缺省为同一错误）: ``:cc [nr]``
显示下一个错误：``:cn``
显示上一个错误：``:cp``
列出所有错误：``:cl``
显示 quickfix 窗口：``:cw``
以十进制、十六进制和八进制显示当前光标下的字符：``ga``
重新载入当前文件：``:e``
编辑第 N 个轮换文件名：``CTRL-^``
显示所有的轮换文件名：``:files``
编辑光标下的文件名对应的文件：``gf``
显示当前目录名：``:pwd``
切换当前目录到 [path]: ``:cd [path]``
回到上一次当前目录：``:cd -``
将当前文件目录设置为工作目录：``,cd``
置光标于第 [num] 行 （缺省：末行）: ``+[num]``
置光标于第一次出现 {pat} 的地方：``+/{pat} {file} ..``
写入当前文件改动，并退出：``ZZ``
放弃当前文件修改退出：``ZQ``
挂起 vim: ``CTRL-z``
回复 vim: ``fg``
写入所有改动的缓冲区并退出：``:xa``
退出 Vim，放弃所有改动：``:qa!``
快速保存：``,w``
分隔窗口并在其中一个编辑 {file}: ``:split {file}``
同上，但垂直分割：``:vsplit {file}``
分割窗口并跳转到光标下的标签：``CTRL-W ]``
分割窗口并编辑光标下的文件名 (file): ``CTRL-W f``
分割窗口并编辑轮换文件：``CTRL-W ^``
创建新空白窗口              (new): ``CTRL-W n``
退出编辑并关闭窗口          (quit): ``CTRL-W q``
隐藏当前缓冲区并关闭窗口    (close): ``CTRL-W c``
使当前窗口成为唯一窗口      (only): ``CTRL-W o``
跳转到下方窗口：``CTRL-j``
跳转到上方窗口：``CTRL-k``
跳转到左方窗口：``CTRL-h``
跳转到右方窗口：``CTRL-l``
跳转到顶端窗口              (top): ``CTRL-W t``
跳转到底端窗口              (bottom): ``CTRL-W b``
跳转到上一次激活的窗口      (previous): ``CTRL-W p``
向下旋转窗口                (rotate): ``CTRL-W r``
向上旋转窗口                (Rotate): ``CTRL-W R``
将当前窗口与下一个窗口对调  (eXchange): ``CTRL-W x``
使所有窗口等高：``CTRL-W =``
减少当前窗口高度：``CTRL-W -``
增加当前窗口高度：``CTRL-W +``
设置当前窗口高度 （缺省：很高）: ``CTRL-W _``
将当前窗口移动到右侧：``Ctrl + w L``
将当前窗口移动到左侧：``Ctrl + w H``
将当前窗口移动到下面：``Ctrl + w J``
将当前窗口移动到上面：``Ctrl + w K``




折叠
删除光标下的一个折叠        (delete)

zd

折叠
删除光标下的所有折叠        (Delete)

zD

折叠
打开光标下的折叠            (open)

zo

折叠
打开光标下的所有折叠        (Open)

zO

折叠
关闭光标下的一个折叠        (close)

zc

折叠
关闭光标下的所有折叠        (Close)

zC

折叠
折起更多：减少 'foldlevel'  (more)

zm

折叠
关闭所有折叠：置 'foldlevel' 为 0

zM

折叠
减少折叠：增加 'foldlevel'  (reduce)

zr

折叠
打开所有折叠：置 'foldlevel' 为最大

zR

折叠
不折叠：复位 'foldenable'   (none)

zn

折叠
正常折叠：置位 'foldenable' (Normal)

zN

折叠
反转 'foldenable'           (invert)

zi

MRU
打开最近访问的文件

，f

MRU
在当前窗口打开

Enter

MRU
在新建水平窗口打开该文件

o

MRU
在新建垂直打开该文件

O

MRU
只读打开

v

MRU
在新的 tab 打开

t

MRU
在新的 tab 打开错误


修改 mru.vim 中对应行  exe 'tabnew ' . a:esc_fname
Ctrlp
打开文件模糊搜索

Ctrl + F

ctrlp
设置 ctrlp 垂直分割打开窗口，防止和粘贴重复


let g:ctrlp_prompt_mappings = { 'AcceptSelection("v")': ['<c-g>'] }
ctrlp
查看基本操作帮助

:cs

NERD Tree
NERDTreeToggle

，nn

NERD Tree
NERDTreeFromBookmark

，nb

NERD Tree
NERDTreeFind

，nf

NERD Tree
打开 / 关闭帮助

?

tab
新建一个标签页

，tn

tab
关闭其他标签

，to

tab
关闭标签

，tc

tab
移动便签至指定标签之后

，tm

tab
打开指定标签

，t，

tab
打开最近访问的标签

，tl

tab
打开新的标签页，新页的内容与当前页一致

，te

tab
打开上一标签

gT

tab
打开下一标签

gt

buffers
关闭当前 buffer

，bd

buffers
关闭所有 buffer

，ba

buffers
显示当前所有 buffers

，o

Ag
快速搜索

，g

Ag
选取模式下，搜索选中的内容

gv

Ag
选取模式下，搜索并替换选中的内容

，r

Ag
在新建窗口中显示结果

，cc

Ag
在新建窗口显示下一个搜索结果

，n

Ag
在新建窗口显示上一个搜索结果

，p

Ag
帮助信息

:h ag-mappings

basic.vim
取消高亮

，<cr>

Goyo
开启 goyo 模式

，z

option
设置查找时忽略大小写

:set ignorecase

option
设置查找时大小写敏感

:set noignorecase

surround
可视模式下，添加 ()

1

surround
可视模式下，添加 []

2

surround
可视模式下，添加 {}

3

surround
可视模式下，添加 ""

$$

surround
可视模式下，添加 ''

$q

命令组合
搜索并将 int 替换为 s32_t

/int
cws32_t<esc>
n
.

cscope
find all references to the token under cursor

CTRL-\ s

cscope
global: find global definition(s) of the token under cursor

CTRL-\ g

cscope
calls:  find all calls to the function name under cursor

CTRL-\ c

cscope
text:   find all instances of the text under cursor

CTRL-\ t

cscope
calls:  find all calls to the function name under cursor

CTRL-\ e

cscope
egrep:  egrep search for the word under cursor

CTRL-\ f

cscope
includes: find files that include the filename under cursor

CTRL-\ i

cscope
called: find functions that function under cursor calls

CTRL-\ d

cscope
在新建水平窗口打开

CTRL-\ ss

cscope
在新建垂直窗口打开

CTRL-\ CTRL-\ s

cscope
设置 cscope 从右边打开新建垂直窗口

:set splitright

cscope
设置结果显示至 quickfix 窗口

h cscopequickfix

man
快速打开 man 帮助

:source $VIMRUNTIME/ftplugin/man.vim
:nmap K :Man <c-r><c-w><cr>
:echo $VIMRUNTIME 修改 man.vim 中的 new 为 vnew

YankRing
在插入模式下选择上一个粘贴的内容

CTRL-p

YankRing
在插入模式下选择下一个粘贴的内容

CTRL-n

YankRing
显示所有剪切内容

:YRShow

BufExplorer
查看帮助

F1

commentary
注释 / 反注释单行

gcc

commentary
注释 / 反注释高亮部分

{visual} gc

SnipMate
打开可选的补全列表 / 选择可选的补全列表

<Tab>

SnipMate
选择上一个可选项

Ctrl - p

SnipMate
选择下一个可选项

Ctrl - n

MRU	打开最近访问的文件		，f
MRU	在当前窗口打开		Enter
MRU	在新建水平窗口打开该文件		o
MRU	在新建垂直打开该文件		o
MRU	只读打开		v
MRU	在新的 tab 打开		t
Ctrlp	打开文件模糊搜索		Ctrl + F
NERD Tree	NERDTreeToggle		，nn
NERD Tree	NERDTreeFromBookmark		，nb
NERD Tree	NERDTreeFind		，nf
tab	新建一个标签页		，tn
tab	关闭其他标签		，to
tab	关闭标签		，tc
tab	移动便签至指定标签之后		，tm
tab	打开指定标签		，t，
tab	打开最近访问的标签		，tl
tab	打开新的标签页，新页的内容与当前页一致		，te
tab	打开上一标签		gT
tab	打开下一标签		gt
windows	切换至左边窗口		Ctrl + h
windows	切换至下边窗口		Ctrl + j
windows	切换至上边窗口		Ctrl + k
windows	切换至右边窗口		Ctrl + l
windows	打开水平窗口		sp
windows	打开垂直窗口		vs
windows	关闭非激活窗口		only
windows	将当前窗口移动到右侧		Ctrl + w L
windows	将当前窗口移动到左侧		Ctrl + w H
windows	将当前窗口移动到下面		Ctrl + w J
windows	将当前窗口移动到上面		Ctrl + w K
windows	关闭所有窗口		:qa
windows	保存所有窗口		:wa
windows	保存并关闭所有窗口		:wqa
windows	放弃保存并关闭所有窗口		:qa!
buffers	关闭当前 buffer		，bd
buffers	关闭所有 buffer		，ba
buffers	显示当前所有 buffers		，o
Ack	暂时不知道 ACK 怎么指定搜索路径，可以在 Vim 中通过 cd 命令进入指定目录再搜索	　
Ag	快速搜索		，g
Ag	选取模式下，搜索选中的内容		gv
Ag	选取模式下，搜索并替换选中的内容		，r
Ag	在新建窗口中显示结果		，cc
Ag	未知		，co
Ag	在新建窗口显示下一个搜索结果		，n
Ag	在新建窗口显示上一个搜索结果		，p
basic.vim	取消高亮		，<cr>
basic.vim	将工作目录指定为当前标签的路径		，cd
basic.vim	前向搜索		space
basic.vim	前向搜索光标所在单词		*
basic.vim	后向搜索光标所在单词		#
合并行		J
撤销		u
重做		Ctrl + r
代码补全		Ctrl + N/P
保存文件并退出 vi		ZZ
放弃更改并退出 vi		:q!
Goyo	开启 goyo 模式		，z
挂起 vim		Ctrl + z
恢复 vim		fg
执行 shell 命令		！
　
动作：文本对象	光标向前移动到下一个单词的词首		w
动作：文本对象	光标向后移动到上一个单词的词首		b
动作：文本对象	光标向前移动到下一个单词的词末		e
动作：文本对象	光标向后移动到上一个单词的词末		ge
动作：文本对象	光标向前移动到下一个字串的词首		W
动作：文本对象	光标向后移动到上一个字串的词首		B
动作：文本对象	光标向前移动到下一个字串的词末		E
动作：文本对象	光标向后移动到上一个字串的词末		gE
动作：左右	至当前行（加上 N-1 后续行）的行尾	N	$
动作：左右	至屏幕行（加上 N-1 后续行）的行尾	N	g$
动作：左右	至当前行的第一个非空字符		^
动作：左右	至屏幕行的第一个非空字符		g^
动作：左右	至当前行的第一个字符		0
动作：左右	至屏幕行的第一个字符		g0
动作：左右	至屏幕行的中点		gm
动作：左右	至第 N 列	N	|
动作：左右	至右边第 N 次出现 {char} 之处——find	N	f{char}
动作：左右	至左边第 N 次出现 {char} 之处——Find	N	F{char}
动作：左右	至右边第 N 次出现 {char} 之前——till	N	t{char}
动作：左右	至左边第 N 次出现 {char} 之前——Till	N	T{char}
动作：左右	重复上次 f、t、F、T 命令 N 次	N	;
动作：左右	反方向重复上次 f、t、F、T 命令 N 次	N	,
移动到匹配的括号上		%
移动到第 n 行		nG
移动到第一行		gg
移动到最后一行		G
移动到视野中接近上方的行		H
移动到视野中中部的行		M
移动到视野中接近下方的行		L
向下滚动一行		Ctrl + y
向上滚动一行		Ctrl + e
向下滚动一屏		Ctrl + f
向上滚动一屏		Ctrl + b
向下滚动半屏		Ctrl + d
向上滚动半屏		Ctrl + u
滚动屏幕使当前行成为靠上的行		zt
滚动屏幕使当前行成为靠下的行		zb
滚动屏幕使当前行成为靠中的行		zz
前向查找字符串		/
反向查找字符串		?
重复前一次查找		n
反方向重复前一次查找		N
设置查找时忽略大小写		:set ignorecase
设置查找时大小写敏感		:set noignorecase
查找上一次字符串		/<up>
查找上一次以 a 开头的字符串		/a<up>
向前查找光标下的单词		*
向后查找光标下的单词		#
查找整个单词 the，其中 \<、\> 分别匹配单词的开头和结尾		/\<the\>
查找处于行尾的 the		/the$
查找处于行首的 the		/^the
查找 com 或者 cam		/c.m
查找 .com		/\.com
在两个位置间跳转，跳转指的是移动到本行以外的命令，但是不包括 j、k 命令		''
跳转至函数定义		Ctrl + ]
跳转至一个较新的位置		Ctrl + o
跳转至一个较旧的位置		Ctrl + i
输出可以跳往的位置		:jumps
增加书签，参数可以选择 26 个字母，所以最多可以设置 26 个书签		ma
跳转至书签		'a
跳转至最近编辑的光标位置		,"
跳转至最近修改的开始位置		,[
跳转至最近修改的结束位置		,]
删除一整行		dd
删除 4 个单词		d4w
从当前位置一直删除到本行末尾		d$
删除一个单词并切换到插入模式		cw
修改一整行		cc
删除当前光标下的字符，表示 dl		x
删除光标左边的字符，表示 dh		X
删除当前位置到行尾，表示 d$		D
修改当前位置到行尾，表示 c$		C
修改一个字符，表示 c1		s
修改一整行，表示 cc		S
替换一个字符		r
修改光标下字符的大小写，并移动到下一个字符		~
使多个字符被同一个字符 x 替换		5rx
重复同一个修改		.
将 int 型替换为 s32_t		/int
　	cws32_t<esc>
　	n
　	.
切换至可视模式		v
切换至可视模式，按行选择		V
切换至可视模式，按列选择		Ctrl + V
可视模式下，进行批量插入，编辑完后<ESC><CR>可完成批量修改		I
可视模式下，移动光标至对角上		o
可视模式下，移动光标至同一行的另一个角上		O
切换至插入模式，在光标前插入字符		i
切换至插入模式，在当前行的第一个非空字符处插入		I
切换至插入模式，在当前行的末尾插入字符		A
切换至插入模式，在光标下方建立一个新的空行		o
切换至插入模式，在光标上方建立一个新行		O
切换至替换模式		R
在插入模式和替换模式间切换		<Insert>
在替换模式下，取消上一个替换的字符		<BS>
可视模式下，添加 ()		1
可视模式下，添加 []		2
可视模式下，添加 {}		3
可视模式下，添加 ""		$$
可视模式下，添加 ''		$q
粘贴至光标前，如果拷贝内容为一行则表示粘贴至前一行		P
粘贴至光标后，如果拷贝内容为一行则表示粘贴至后一行		p
交换当前光标及下一个字符		xp
交换当前光标及下一个字符		Xp
拷贝一整行		Y/yy
拷贝单词及其后面的空白符		yw
拷贝单词不包含后面的空白符		ye
拷贝光标所在单词		yaw
拷贝光标所在单词，不包含单词后的空格		yiw
拷贝光标所在的 () 内的部分		ya(
拷贝光标所在的 () 内的部分，不包含括号		yi(
拷贝光标所在的 [] 内的部分		ya[
拷贝光标所在的 [] 内的部分，不包含括号		yi[
拷贝光标所在的 {} 内的部分		ya{
拷贝光标所在的 {} 内的部分，不包含括号		yi{
cscope	find all references to the token under cursor		CTRL-\ s
cscope	global: find global definition(s) of the token under cursor		CTRL-\ g
cscope	calls:  find all calls to the function name under cursor		CTRL-\ c
cscope	text:   find all instances of the text under cursor		CTRL-\ t
cscope	calls:  find all calls to the function name under cursor		CTRL-\ e
cscope	egrep:  egrep search for the word under cursor		CTRL-\ f
cscope	includes: find files that include the filename under cursor		CTRL-\ i
cscope	called: find functions that function under cursor calls		CTRL-\ d
cscope	在新建水平窗口打开		CTRL-\ hs
cscope	在新建垂直窗口打开		CTRL-\ vs
cscope	设置 cscope 从右边打开新建垂直窗口		:set splitright
cscope	设置结果显示至 quickfix 窗口		h cscopequickfix
ctrlp	设置 ctrlp 垂直分割打开窗口，防止和粘贴重复		let g:ctrlp_prompt_mappings = { 'AcceptSelection("v")': ['<c-g>'] }
ctrlp	查看基本操作帮助		:h ctrlp-mappings
打开命令行窗口		q:
保存上一次会话		https://github.com/tmuxinator/tmuxinator
man	快速打开 man 帮助		:source $VIMRUNTIME/ftplugin/man.vim
:nmap K :Man <c-r><c-w><cr>
:echo $VIMRUNTIME 修改 man.vim 中的 new 为 vnew
```

---

# Tumx
{% note default %}
从 window 连接 Ubuntu, 实在不喜欢太多窗口，只能用 Tmux 了
{% endnote %}
* 参考
<http://www.cnblogs.com/congbo/archive/2012/08/30/2649420.html>

---

# Jupyter

帮助：``h``

---

# Windows

激活任务栏第 N 个任务：``Win + 数字`` *极其常用*

---

# Mac

## 常用
删除：``command + del``
打开强制退出窗口：``Command + Option + esc``
切换：``Command + Tab``

## 截图
截取全屏至文件：``Command + Shift + 3``
截取全屏到剪贴板：``Command + Shift + Control + 3``
截取所选屏幕区域到文件，或按空格键截取窗口：``Command + Shift + 4``
截取所选屏幕区域到剪贴板，或按空格键截取窗口：``Command + Shift + Control + 4``

## Finder
新建文件夹：``Command + Shift + N``
调出直达窗口：``Command + Shift + G``
重命名文件：``Enter``
进入文件：``Command + O``
剪切：``Command + Option + V ``
进入上级目录：``Command + 上箭头``
删除：``Command + Delete``
清倒废纸篓：``Command + Shift + Delete``
预览：``空格``

## chrome
光标直接跳至地址栏：``Command + l``
转向下一个标签页：``Control + Tab``
转向上一个标签页：``Control + Shift + Tab``
放大页面：``Command + 加号或等号``
缩小页面：``Command + 减号``

---

# zsh

{% note default %}
说实在的行编辑功能不如 shell, 比如删除单词、向前向后按单词移动
{% endnote %}

## 移动
移动到行首：``ctrl + a``
移动到行尾：``ctrl + e``
移动到前一个字符：``ctrl + f``
移动到前一个字符：``ctrl + b``

## 编辑
剪切当前光标的字符：``ctrl + d``
剪切光标之前的字符：``ctrl + h``
剪切光标之前的单词：``ctrl + w``
剪切整行：``ctrl + u （本来 ctrl + u 是删至命令行首，但 iterm 中是删掉整行）``
剪切至行末尾：``ctrl + k``
粘贴至光标后：``ctrl + y``
交换光标处文本：``ctrl + t``

## 历史
上一条命令历史：``ctrl + p``
下一条命令历史：``ctrl + n``
搜索命令历史：``ctrl + r``

## 其他
清屏：``ctrl + l``

---
