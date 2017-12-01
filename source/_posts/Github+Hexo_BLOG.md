---
title: 使用 Github + Hexo 搭建个人博客
categories: 工具使用
tags:
  - hexo
---

{% note default %}
Github 让个人技术博客的创建变得异常简单，Hexo 框架 + Next 主题提供了高度定制且美观的个人博客，本文记录了搭建过程
{% endnote %}

<!--more-->

---

# Hexo 与 jekyll 框架的选择
{% note default %}
经过两天的折腾，彻底放弃使用 jekyll 搭建自己的技术 Blog, 究其原因就是目录、sitemap 无法自动生成，一个没有前端开发经验的我最终发现 Hexo。
{% endnote %}

Hexo 能够满足我对 Blog 的所有想法：
1、我只负责写内容，至于文章的按标签分类还是按日期归档我都不关心，但是我需要使用这些功能
2、文章要有一个漂亮的内容导航栏，开发做多了，对始终能在一屏内了解当前文件的整体结构有着某种偏执
3、sitemap、文章目录最好能够复用网页位置，以便留出更多的位置显示正文，尽量少的翻页绝对能提升生产效率

---

# 个人博客搭建
{% note default %}
依次安装 git、node.js、hexo、next 主题
{% endnote %}

## 安装 git
[官网](https://git-scm.com/book/zh/v1/%E8%B5%B7%E6%AD%A5-%E5%AE%89%E8%A3%85-Git) 描述的很清楚
我最常用的是 Ubuntu，只需要执行以下命令即可：
```shell
apt-get install git
```

## 安装 node.js
一开始，我以为使用的 Ubuntu-16.04LTS 已经很新了，所以就直接使用 apt-get 安装了，结果在安装 hexo 时出现错误。网上整了一堆高级方法都没能解决。
最终参考 [node.js 官网](https://nodejs.org/en/)，直接 download 官方的首页的最新的 LTS 版本 *node-v6.11.3-linux-x64.tar.xz*，解压至 /usr 目录
```python
tar -vxf node-v6.11.3-linux-x64.tar.xz -C /usr/
```

默认 hexo 安装的位置与 npm 一致，所以如果没有把 npm 所在路径加入环境变量，则安装 hexo 后会发现无法找到 hexo 命令，所以建议将 node.js 的安装路径加入 ~/.bashrc
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
创建一个目录，比如 *hexo_dir*, 用于安装 hexo, 通过 npm 命令安装 hexo
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

如果你想能够更新 next 主题，且又想通过 github 管理你的主题定制信息，那么需要麻烦一些，可以参考下面的 *多平台共同编辑博客*

## Github 创建博客
只需要在 github 上创建 *用户名 +github.io* 的 Repo 即可
{% img  '/images/github-page.png' %}
创建成功后，就可以通过 https:// 用户名.github.io/ 访问了，比如我就是通过 https://jiexiao111.github.io/ 访问

---

# 站点配置文件修改

{% note default %}
在 hexo 安装目录下可以找到 config.yml 文件，这个文件就是站点配置文件，修改站点配置文件后，需要重起 hexo 服务，才能生效
{% endnote %}

```python
hexo s
```

## 启用 next 主题
编辑站点配置文件
```python
theme: next
```

验证 next 主题，在 hexo 安装目录下执行 hexo s --debug，如果未出现错误，则在浏览器中访问以下位置
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

---

# 主题配置文件修改
{% note default %}
hexo 目录下的 themes/next/ 子目录中也有一个  config.yml 文件，这个文件就是主题配置文件，修改主题配置文件后立即生效，无需重启 hexo 服务
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

  # 外链字体库地址，例如 //fonts.googleapis.com （默认值）
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


## 开启公式显示
```python
mathjax:
  enable: true
```

## 开启访问统计
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

---

# 第三方插件安装
{% note default %}
主要包括本地搜索服务、git 部署
{% endnote %}

## 本地搜索插件
考虑到博文多了以后方便自己查阅，搜索功能必不可少

* 安装 searchdb
```python
npm install hexo-generator-searchdb --save
```

* 修改主题配置文件
```python
# Local search
local_search:
  enable: true
```

* 修改站点配置文件
```python
search:
  path: search.xml
  field: post
  format: html
  limit: 10000
```

## git 部署插件
* 安装
```python
npm install hexo-deployer-git --save
```

* 修改站点配置文件
```python
deploy:
	type: git
	repository: git@github.com:jiexiao111/jiexiao111.github.io.git
	branch: master
```

* 部署命令使用
```python
hexo deploy
```

## 压缩网页插件
* 安装 hexo-neat
```shell
npm install hexo-neat --save
```
* 修改站点配置，增加以下信息
```shell
# hexo neat config
neat_enable: true

neat_html:
  enable: true
  exclude:

neat_css:
  enable: true
  exclude:
    - '*.min.css'

neat_js:
  enable: true
  mangle: true
  output:
  compress:
  exclude:
    - '*.min.js'
```

## 留言插件
<http://barrysite.me/2017/05/08/hexo%E7%BD%91%E7%AB%99NexT%E4%B8%BB%E9%A2%98%E5%A2%9E%E5%8A%A0%E7%95%99%E8%A8%80%E9%A1%B5/>

---

# 多平台共同编辑博客

{% note default %}
通常我们需要在多个环境下，编辑 / 发布博客
{% endnote %}

## 生成秘钥
* [git 官方帮助](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/) 描述的非常清楚，如果是 Linux 系统，首先通过命令生成秘钥，注意下面命令中的 jiexiao111@gmail.com 是你注册 github 时的邮箱
```python
ssh-keygen -t rsa -C jiexiao111@gmail.com
```

* 想办法把下面这个文件的内容拷贝出来
```shell
~/.ssh/id_rsa.pub
```

* 然后打开你的 github 主页，依次点击 Settings->SSH and GPG keys->New SSH key, 然后 Title 随便取个名字，再把 ~/.ssh/id_rsa.pub 中的内容拷贝到 Key 中，Add SSH key 完成添加
{% img  '/images/add_ssh.png' %}

## 新建 repo 用于保存站点配置
在 github 中新建 repo, 进入 hexo 安装目录，将以下文件 / 目录同步至 repo
```shell
README.md
_config.yml
package.json
scaffolds
source
themes
```

## fork Next 主题用于保存主题配置
为了能够随时更新 Next 主题，又能保存自己的主题配置及相关修改，可以参考[同步一个 fork](https://gaohaoyang.github.io/2015/04/12/Syncing-a-fork/) 或者[官方帮助](https://help.github.com/articles/syncing-a-fork/)

* 第一步，fork Next 主题
* 第二步，进入 hexo 的安装目录，将 fork 好的 Next 主题 clone 到本地，注意 hexo 目录下应该是默认存在 themes 目录的
```python
git submodule add git@github.com:jiexiao111/hexo-theme-next.git themes/next
```
* 第三步，进入 themes/next 目录，增加上游仓库
```python
cd themes/next
git remote add upstream https://github.com/iissnan/hexo-theme-next.git
```
* 第四步，通过 git remote -v 确认执行结果正确
```python
$ git remote -v
origin	git@github.com:jiexiao111/hexo-theme-next.git (fetch)
origin	git@github.com:jiexiao111/hexo-theme-next.git (push)
upstream	https://github.com/iissnan/hexo-theme-next.git (fetch)
upstream	https://github.com/iissnan/hexo-theme-next.git (push)
```
* 第五步，获取变更（获取 next 主题最新的修改），切换到 master（一般不需要切换，可以通过 git branch 看到应该是处于 master 分支），合并更改（获取 next 主题主线版本的最新修改），最后把修改推送到 fork 的分支里
```python
git fetch upstream
git checkout master
git merge upstream/master
git push origin master
```

## 在新的环境上部署
* 安装 git、node.js、hexo 后
* clone hexo 相关配置
```python
git clone --recursive git@github.com:jiexiao111/hexo_jiexiao.git
```
* 安装相关插件
```pythhon
cd hexo_jiexiao
npm install
```
* 测试新环境的部署功能
```pythhon
hexo d -g
```

---

# 其他设置及常用操作
{% note default %}
一些不好分类但是非常有用的设置及操作
{% endnote %}

## 设置正文页面宽度
编辑 hexo_dir/themes/next/source/css/_variables/custom.styl
```python
 // 修改成你期望的宽度
 $content-desktop = 1000px

 // 当视窗超过 1600px 后的宽度
 $content-desktop-large = 1400px
```

## 解决网页分类 / 标签显示错误
```python
rm db.json
hexo clean
hexo g
hexo s
```

## 创建分类和标签
在 hexo 安装目录下执行以下命令，用于增加标签和分类目录
```python
hexo new page tags
hexo new page categories
```

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

## 使用 chrome 分析网页加载速度
在 chrome 流量器中按 F12 或者单击鼠标右键 ->检查，打开调试栏 ->Network, 刷新网页就可以看到以下信息了
{% img  '/images/chrome_perf.png' %}

---

# Hexo 框架及 Next 主题相关文档链接

{% note default %}
提供一些高质量的链接，便于参考
{% endnote %}

[Hexo 的官方文档](https://hexo.io/zh-cn/docs/)，满满的诚意
[next 官方文档](http://theme-next.iissnan.com/getting-started.html)，进去就充满了好感
从 jekyll 转换到 hexo 多亏了下面这篇[文章](https://www.ezlippi.com/blog/2016/02/jekyll-to-hexo.html)

---
