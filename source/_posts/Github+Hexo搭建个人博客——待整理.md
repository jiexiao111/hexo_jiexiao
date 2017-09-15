---
title: 使用 Github + Hexo 搭建个人博客
categories: 个人博客
tags:
  - hexo
  - 博客
---

{% cq %} 
Github 让个人技术博客的创建变得异常简单，Hexo 框架 + Next 主题提供了高度定制且美观的个人博客，本文记录了搭建过程 
{% endcq %}

<!--more-->

# Hexo 与 jekyll 框架的选择
{% note default %}
经过两天的折腾，彻底放弃jekyll搭建自己的Blog，究其原因就是目录、sitemap无法自动生成，一个没有前端开发经验的我最终发现Hexo。
{% endnote %}

Hexo能够满足我对Blog的所有想法：
1、我只负责写内容，至于文章的按标签分类还是按日期归档我都不关心，但是我需要使用这些功能
2、文章要有一个漂亮的内容导航栏，开发做多了，对始终能在一屏内了解当前文件的整体结构有着某种偏执
3、sitemap、文章目录最好能够复用网页位置，以便留出更多的位置显示正文，尽量少的翻页绝对能提升生产效率

# 个人博客搭建
{% note default %}
依次安装 git、node.js、hexo、next主题
{% endnote %}

## 安装 git
[官网](https://git-scm.com/book/zh/v1/%E8%B5%B7%E6%AD%A5-%E5%AE%89%E8%A3%85-Git)描述的很清楚
我最常用的是Ubuntu，只需要执行以下命令即可:
```shell
apt-get install git
```

## 安装 node.js
一开始，我以为使用的 Ubuntu-16.04LTS 已经很新了，所以就直接使用 apt-get 安装了，结果在安装 hexo 时出现错误。网上整了一堆高级方法都没能解决。
最终参考(node.js 官网)[https://nodejs.org/en/]，直接download官方的首页的最新的LTS版本 *node-v6.11.3-linux-x64.tar.xz*，解压至 /usr 目录
```python
tar -vxf node-v6.11.3-linux-x64.tar.xz -C /usr/
```

默认 hexo 安装的位置与 npm 一致，所以如果没有把 npm 所在路径加入环境变量，则安装 hexo 后发现无法找到 hexo 命令，所以建议将 node.js 解压路径加入 ~/.bashrc
```python
echo 'export PATH="/usr/node-v6.11.3-linux-x64/bin:$PATH' >> ~/.bashrc
```

如果你和我一样使用 zsh，就放到 ~/.zshrc 中
```python
echo 'export PATH="/usr/node-v6.11.3-linux-x64/bin:$PATH' >> ~/.zshrc
```

添加环境变量后记得 source 
```python
source ~/.bashrc
source ~/.zshrc
```

## 安装 hexo
创建一个目录——这里是*hexo_dir*——用于安装 hexo，通过 npm 命令安装 hexo
```python
mkdir hexo_dir
cd hexo_dir
npm install -g hexo-cli
```

## 安装 next 主题
hexo 的安装路径下有一个 themes 目录，hexo 默认会使用该目录下的主题，所以一定要在 hexo 安装目录下执行
```python
git clone https://github.com/iissnan/hexo-theme-next themes/next
```

如果你想能够更新 next 主题，且又想通过 github 管理你的主题定制信息，那么需要麻烦一些

# 站点配置文件修改
{% note default %}
在 hexo 安装目录下可以找到 _config.yml 文件, 这个文件就是站点配置文件, 修改站点配置文件后，需要重起 hexo 服务，才能生效
{% endnote %}
```python
hexo s
```

## 启用 next 主题
编辑站点配置文件
```python
theme: next
```

验证next主题，在 hexo 安装目录下执行 hexo s --debug，如果未出现错误，则在浏览器中访问以下位置
```python
http://localhost:4000/
```

## 修改默认标题、子标题、描述、作者、字符集
编辑站点配置文件
```python
 # Site
 title: JieXiao's Blog
 subtitle:
 description:
 author: JIE XIAO
 language: zh-Hans
```

# 主题配置文件修改
{% note default %}
hexo 目录下的 themes/next/ 子目录中也有一个 _config.yml 文件, 这个文件就是主题配置文件，修改主题配置文件后立即生效，无需重启 hexo 服务
{% endnote %}

## 修改 Next 主题风格
个人偏向于在一屏内显示更多的内容所以选择了 Mist 风格
```python
# Schemes
# scheme: Muse
scheme: Mist
# scheme: Pisces
# scheme: Gemini
```

## 设置侧边栏
Next 主题的文章目录导航和作者介绍复用了侧边栏，非常不错
```python
 sidebar:
   position: left
   display: always
```
## 修改字体
```python
font:
  enable: true

  # 外链字体库地址，例如 //fonts.googleapis.com (默认值)
  host:

  # 全局字体，应用在 body 元素上
  global:
    external: true
    family: Monda

  # 标题字体 (h1, h2, h3, h4, h5, h6)
  headings:
    external: true
    family: Roboto Slab

  # 文章字体
  posts:
    external: true
    family:

  # Logo 字体
  logo:
    external: true
    family: Lobster Two
    size: 24

  # 代码字体，应用于 code 以及代码块
  codes:
    external: true
    family: PT Mono
```

## 修改代码风格
```python
 highlight_theme: night
```

## 侧边栏中增加社交信息
```python
social:
  GitHub: https://github.com/jiexiao111
  E-Mail: mailto:jiexiao111@gmail.com
social_icons:
   GitHub: github
   E-Mail: email
```

## 开启背景动画
```python
canvas_nest: true
```

# 创建分类和标签
{% note default %}
为了方便日后查阅，分类和标签目录还是需要配置的
{% endnote %}

## 增加标签和分类目录
在 hexo 安装目录下执行以下
```python
hexo new page tags
hexo new page categories
```

## 修改标签和分类目录的配置信息
在生成的文件中分别写入以下信息
```python
cat > source/tags/index.md 
---
title: tags
date: 2017-09-10 12:21:49
type: "tags"
---

cat > source/categories/index.md
---
title: categories
date: 2017-09-10 12:25:38
type: "categories"
---
```

# 增加搜索第三方服务，
{% note default %}
考虑到博文多了以后方便自己查阅，搜索功能必不可少
{% endnote %}

## 安装 searchdb
```python
npm install hexo-generator-searchdb --save
```

## 修改主题配置文件
```python
# Local search
local_search:
  enable: true
```

## 修改站点配置文件
```python
search:
  path: search.xml
  field: post
  format: html
  limit: 10000
```

# Hexo 框架及 Next 主题相关文档链接
[Hexo 的官方文档](https://hexo.io/zh-cn/docs/)，满满的诚意
[next 官方文档](http://theme-next.iissnan.com/getting-started.html)，进去就充满了好感 
从 jekyll 转换到 hexo 多亏了下面这篇[文章](https://www.ezlippi.com/blog/2016/02/jekyll-to-hexo.html)

开启公式显示
```python
mathjax:
  enable: true
```

开启访问统计
```python
busuanzi_count:
   # count values only if the other configs are false
   enable: true
   # custom uv span for the whole site
   site_uv: true
   site_uv_header: <i class="fa fa-user"></i> 访问
   site_uv_footer: 人
   # custom pv span for the whole site
   site_pv: true
   site_pv_header: <i class="fa fa-eye"></i> 浏览
   site_pv_footer: 次
   # custom pv span for one page only
   page_pv: true
   page_pv_header: <i class="fa fa-file-o"></i> 阅读
   page_pv_footer:
```

git部署插件，1安装
```python
npm install hexo-deployer-git --save
```

git部署插件，2配置
```python
deploy:
	type: git
	repository: git@github.com:jiexiao111/jiexiao111.github.io.git
	branch: master
```

git部署插件，3使用
```python
hexo deploy
```

设置页面宽度，编辑hexo_dir/themes/next/source/css/_variables/custom.styl
```python
 // 修改成你期望的宽度
 $content-desktop = 1000px

 // 当视窗超过 1600px 后的宽度
 $content-desktop-large = 1400px
```

生成秘钥
```python
ssh-keygen -t rsa -C jiexiao111@gmail.com
```

参考以下网页完成秘钥添加


```python
https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/
```

hexo环境仅将以下几个文件/目录同步至 git@github.com:jiexiao111/hexo_jiexiao.git
README.md    
_config.yml
_ipynb
package.json
scaffolds   
source       
themes
在新的环境上更新博客


```python
git clone git@github.com:jiexiao111/hexo_jiexiao.git
cd hexo_jiexiao
npm install  
hexo d -g
```

尴尬的是出错了，themes中使用的next并不在我的仓库中，所以，我必须先fork一个next主题，然后把我修改的配置合入，然后还需要能够更新获取next的最新修改，于是参考了 这篇blog[https://gaohaoyang.github.io/2015/04/12/Syncing-a-fork/] 以及 官方帮助[https://help.github.com/articles/syncing-a-fork/]

第一步fork主题，在刚刚clone好的hexo_jiexiao目录，然后clone到本地


```python
git clone git@github.com:jiexiao111/hexo-theme-next.git themes/next
```

第二步进入themes/next，增加上游仓库


```python
cd themes/next
git remote add upstream https://github.com/iissnan/hexo-theme-next.git
```

第三步通过git remote -v确认执行结果正确


```python
$ git remote -v
origin	git@github.com:jiexiao111/hexo-theme-next.git (fetch)
origin	git@github.com:jiexiao111/hexo-theme-next.git (push)
upstream	https://github.com/iissnan/hexo-theme-next.git (fetch)
upstream	https://github.com/iissnan/hexo-theme-next.git (push)
```

第四步，获取变更（获取next主题最新的修改），切换到master（一般不需要切换，可以通过git branch看到大多数时候都处于 master 分支），合并更改(获取next主题主线版本的最新修改)，最后把修改推送到fork的分支里


```python
git fetch upstream
git checkout master
git merge upstream/master
git push origin master
```

处理标签个数错误


```python
rm db.json
hexo clean
hexo g
hexo s
```

mac+chrome检查网页打开速度快慢


```python
鼠标右键->检查->performance->start
```
