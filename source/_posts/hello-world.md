---
title: Markdown 语法示例
date: 2017-11-11 11:11:11
categories: 工具使用
tags:
  - markdown
photos:
  - http://bruce.u.qiniudn.com/2013/11/27/reading/photos-0.jpg
  - http://bruce.u.qiniudn.com/2013/11/27/reading/photos-1.jpg
---

<!-- 文章开头都用它了，整齐才好看 -->
{% note default %}
本篇博文不仅仅包含 Markdown 基础语法，也有 Hexo 定义的一些标签，主要是自己 copy 起来方便，所有的章节一定是语法 + 示例，不用怀疑
{% endnote %}

<!--more-->

---

# 标题

markdown 标题语法，``#`` 号个数代表标题级别

```
## 二级标题示例
### 三级标题示例
#### 四级标题示例
##### 五级标题示例
###### 六级标题示例
```

## 二级标题示例
### 三级标题示例
#### 四级标题示例
##### 五级标题示例
###### 六级标题示例

<!-- 注释 -->

---

# 列表

## 无序列表

懒得记，无序列表我只用 ``*`` 开头

```
* 一级无序列表
    * 二级无序列表
        * 三级无序列表
            * 四级无序列表
* 一级无序列表
```

* 一级无序列表
    * 二级无序列表
        * 三级无序列表
            * 四级无序列表
* 一级无序列表

## 有序列表

有序列表以 ``1. 2. 3.`` 开头，注意第四行，真实显示的需要是自动生成的

```
1. 一级有序列表
    1. 二级有序列表
    2. 三级有序列表
        4. 注意序号是自动生成的
2. 有序列表
```

1. 一级有序列表
    1. 二级有序列表
    2. 二级有序列表
        4. 注意序号是自动生成的
2. 有序列表

## 待办列表

语法应该就是 - [x] 开头的行

```
- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> are supported
    - [x] list syntax is required (any unordered or ordered list supported)
        - [x] this is a complete item
        - [ ] this is an incomplete item
```

- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> are supported
    - [x] list syntax is required (any unordered or ordered list supported)
        - [x] this is a complete item
        - [ ] this is an incomplete item

---

# 引用

## 标准引用

引用以一个或多个 ``>`` 开头，注意第四行的空行，如果没有空行第五行也会是三级引用
```
> 这是一级引用
>> 这是二级引用
>>> 这是三级引用

> 这是一级引用
```
> 这是一级引用
>> 这是二级引用
>>> 这是三级引用

> 这是一级引用

## centerquote 标签

非常适合单行的引用，比较好看
```
{% cq %} blah blah blah {% endcq %}
```
<!-- 引号包围，居中 -->
{% cq %} blah blah blah {% endcq %}

## blockquote 标签

```
{% blockquote Seth Godin http://sethgodin.typepad.com/seths_blog/2009/07/welcome-to-island-marketing.html Welcome to Island Marketing %}
Every interaction is both precious and an opportunity to delight.
{% endblockquote %}
```
{% blockquote Seth Godin http://sethgodin.typepad.com/seths_blog/2009/07/welcome-to-island-marketing.html Welcome to Island Marketing %}
Every interaction is both precious and an opportunity to delight.
{% endblockquote %}

## note 标签
```
{% note class_name %} Content (md partial supported) {% endnote %}
```
其中，class_name 可以是以下列表中的一个值：
* default
* primary
* success
* info
* warning
* danger

```
{% note warning %}
举个例子
{% endnote %}
```
{% note warning %}
举个例子
{% endnote %}

---

# 代码块

用 \`\`\` 包围起来的就是代码块，这个没法演示，这里展示使用标签的方式，下面是代码标签的语法

```
{% codeblock [title] [lang:language] [url] [link text] %}
code snippet
{% endcodeblock %}
```

举两个例子：

1. 最简单的例子
```
{% codeblock %}
print('Hello World!');
{% endcodeblock %}
```

    * 效果如下：
    {% codeblock %}
    print('Hello World!');
    {% endcodeblock %}

2. 附加说明和网址，其中 [title] 是 ``compact``, [lang:language] 是 ``lang:objc``, [url] 是 ``http://underscorejs.org/#compact``  [link text] 是 ``Underscore.js``
```
{% codeblock lang:objc compact http://underscorejs.org/#compact Underscore.js %}
[rectangle setX: 10 y: 10 width: 20 height: 20];
{% endcodeblock %}
```

    * 效果如下：
    {% codeblock compact lang:objc  http://underscorejs.org/#compact Underscore.js %}
    [rectangle setX: 10 y: 10 width: 20 height: 20];
    {% endcodeblock %}

---

# 链接

## 行内式链接

行内式链接的语法结构为 ``[链接的描述](link "鼠标放到链接上后的提示")``

```
这就是行内链接：[李阿昀的简书](http://www.jianshu.com "李阿昀的简书")
```

这就是行内链接：[李阿昀的简书](http://www.jianshu.com "李阿昀的简书")

## 参考式链接

```
1. [李阿昀的简书][1]
2. [Hexo 中文文档][2]
[1]: <http://www.jianshu.com/p/250e36bb5690#fn_lemma_footer>
[2]: <https://hexo.io/zh-cn/docs/tag-plugins.html>
```

1. [李阿昀的简书][1]
2. [Hexo 中文文档][2]

## 自动链接

用 ``<>`` 包围的就是自动链接，没有 http 就不会显示

```
<http://example.com/>
<example.com/>
```

<http://example.com/>
<example.com/>

## 博客内部链接

```
{% post_link "Hash_implement" %}
```

<!-- 博客内部跳转 -->
{% post_link "Hash_implement" %}

```
{% post_link "hello-world" "Deploy to remote sites" %}
```

<!-- 博客内部跳转 -->
{% post_link "hello-world" "Deploy to remote sites" %}

## 锚点

点击位置
```
[点击跳转](#jump)
```
目标位置
```
<span id="jump">跳转到的地方</span>
```
可以看到 ``jump`` 关联了点击位置和目标位置

[点击跳转](#jump)

---

# 图片

插入图片与插入链接的语法很像，区别在一个！号，而且也有行内式和参考式两种。

## 行内式图片

行内式优势在于简单，图片语法为：``![无法显示图片时的说明](图片地址或者链接 "鼠标悬停提示")``

* 显示链接图片
```
![图灵社区](http://bruce.u.qiniudn.com/2013/11/27/reading/photos-1.jpg)
```
![图灵社区](http://bruce.u.qiniudn.com/2013/11/27/reading/photos-1.jpg)

* 显示失效链接图片
```
![图灵社区](http://bruce.u.qiniudn.com/2013/11/27/reading/photos-1.jpg1)
```
![图灵社区](http://bruce.u.qiniudn.com/2013/11/27/reading/photos-1.jpg1)

* 显示本地图片
```
![github](/images/github-page.png)
```
![github](/images/github-page.png)

## 参考式图片

参考式优势在于可以多次引用网址，类似声明 Constant 变量，参考式图片我没有找到使用本地图片的办法
```
![链接图片][3]
[3]: http://bruce.u.qiniudn.com/2013/11/27/reading/photos-1.jpg
```
![链接图片][3]

## 标签显示图片

标签显示图片的语法
```
{% img [class names] /path/to/image [width] [height] [title text [alt text]] %}
```

* 基础应用
```
{% img  '/images/github-page.png' %}
```
<!-- 显示本地图片 -->
{% img  '/images/github-page.png' %}

## 标签放大显示图片

优势是可以强调图片显示

```
{% fi '/images/github-page.png', alt, title %}
```
<!-- 以 120% 的尺寸显示图片 -->
{% fi '/images/github-page.png', alt, title %}

---

# 字体 / 行内代码 / 删除线

使用``**``表示粗体，使用``*``表示斜体。符号和文字间不能有空格
使用 \`\` 包围表示行内代码
使用 ``~~`` 包围表示删除线

```
**粗体**
*斜体*
~~删除线~~
*~~斜体删除线~~*
``行内代码``
普通字体
```

**粗体**
*斜体*
~~删除线~~
*~~斜体删除线~~*
``行内代码``
普通字体

---

# 表格

用|表示表格纵向边界，表头和表内容用 - 隔开，并可用：进行对齐设置，两边都有：则表示居中，若不加：则默认左对齐。
详细说明：
``----:``为右对齐
``:----``为左对齐
``:---:``为居中对齐
``-----``为默认左对齐

## 正常的表格
```
dog | bird | cat
----|------|----
foo | foo  | foo
bar | bar  | bar
baz | baz  | baz
```

dog | bird | cat
----|------|----
foo | foo  | foo
bar | bar  | bar
baz | baz  | baz

## 复杂的表格
```
| 序号 | 交易名 | 交易说明 | 备注 |
| ---: | :----: | :------- | ---- |
|   1  | prfcfg | 菜单配置 | 可以通过此交易查询到所有交易码和菜单的对应关系 |
|   2  | gentmo | 编译所有交易 |  |
|   100000  | sysdba | 数据库表模型汇总 |  |
```

| 序号 | 交易名 | 交易说明 | 备注 |
| ---: | :----: | :------- | ---- |
|   1  | prfcfg | 菜单配置 | 可以通过此交易查询到所有交易码和菜单的对应关系 |
|   2  | gentmo | 编译所有交易 |  |
|   100000  | sysdba | 数据库表模型汇总 |  |

## 表格中插入 | 和代码块
```
语法                      | 说明
-----                     | -----
`a += x;`                 | 表格中插入代码
a &#124;= y;              | 表格中插入 &#124;
<code>a &#124;= y;</code> | 表格代码中插入 &#124;
```

语法                      | 说明
-----                     | -----
`a += x;`                 | 表格中插入代码
a &#124;= y;              | 表格中插入 &#124;
<code>a &#124;= y;</code> | 表格代码中插入 &#124;

# 设置表格宽度
```
<style>
table th:nth-of-type(1) {
    width: 100px;
}
table th:nth-of-type(2) {
    width: 300px;
}
table th {
    font-weight: bold; /*加粗*/
    font-size: 12pt;
    text-align: center !important; /*内容居中，加上 !important 避免被 Markdown 样式覆盖*/
    background: rgba(158,188,226,0.2); /*背景色*/
}
</style>

|别名                | 命令                                                                                                                               |
|--------------      |---------------------               |
|g                   | git                                |
|ga                  | git add                            |
|gaa                 | git add --all                      |
|gapa                | git add --patch                    |

```

<style>
table th:nth-of-type(1) {
    width: 100px;
}
table th:nth-of-type(2) {
    width: 300px;
}
table th {
    font-weight: bold; /*加粗*/
    font-size: 12pt;
    text-align: center !important; /*内容居中，加上 !important 避免被 Markdown 样式覆盖*/
    background: rgba(158,188,226,0.2); /*背景色*/
}
</style>

|别名                | 命令                                                                                                                               |
|--------------      |---------------------               |
|g                   | git                                |
|ga                  | git add                            |
|gaa                 | git add --all                      |
|gapa                | git add --patch                    |


---

# 分割线

使用``---``表示分割线，其他形式不管

```
---
```

---

---

# LaTeX 公式

## 行内公式

$ 表示行内公式
```
质能方程 $E=mc^2$
```
质能方程 $E=mc^2$

## 整行公式

$$ 表示整行公式
```
$$\sum_{i=1}^n a_i=0$$
```
$$\sum_{i=1}^n a_i=0$$

访问 [MathJax](http://meta.math.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference) 参考更多使用方法。

---

# 暂不使用的高级特性
1. 内嵌图标，更多的图标和玩法可以参看 [font-awesome](http://fortawesome.github.io/Font-Awesome/3.2.1/icons/) 官方网站。

2. 定义型列表

3. 注脚

4. 流程图，更多语法参考：[流程图语法参考](http://adrai.github.io/flowchart.js/)

5. 序列图，更多语法参考：[序列图语法参考](http://bramp.github.io/js-sequence-diagrams/)

---


# 参考

<span id="jump">跳转到的地方</span>

1. [李阿昀的简书][1]
2. [Hexo 中文文档][2]
3. [Github Page 官方帮助][4]
4. [作业部落][5]
[1]: http://www.jianshu.com/p/250e36bb5690#fn_lemma_footer
[2]: https://hexo.io/zh-cn/docs/tag-plugins.html
[3]: http://bruce.u.qiniudn.com/2013/11/27/reading/photos-1.jpg
[4]: https://help.github.com/categories/writing-on-github/
[5]: https://www.zybuluo.com/mdeditor#371834

---
