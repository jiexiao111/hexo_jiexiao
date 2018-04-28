---
title: git 使用
date: 2017-12-31 10:46:55
categories: 操作系统
tags:
  - linux
---

<!-- 文章开头都用它了，整齐才好看 -->
{% note default %}
经常在使用 git，但是使用的命令都是那几个，有时候想达到特殊目的时都要查半天，所以决定整理一下，如果安装了 oh-my-zsh，则快捷命令均能生效
{% endnote %}

<style>
table th:nth-of-type(1) {
    width: 100px;
}
table th:nth-of-type(2) {
    width: 500px;
}
table th {
    font-weight: bold; /*加粗*/
    font-size: 12pt;
    text-align: center !important; /*内容居中，加上 !important 避免被 Markdown 样式覆盖*/
    background: rgba(158,188,226,0.2); /*背景色*/
}
</style>


<!--more-->

# git 基础功能

## git clone 克隆版本库

开始一个项目时，第一步就是将远程代码 clone 到本地
```
gcl https://github.com/jiexiao111/hexo_jiexiao.git
```

| Alias                | Brief                                                                                      | CMD
| --------------       | ----                                                                                       | ------------------------
| gcl                  | 递归的 clone                                                                               | ``git clone --recursive``

## git config 配置环境
可以通过 ``gcf`` 查看已经配置的环境变量

| Alias                | Brief                                                                                      | CMD
| --------------       | ----                                                                                       | ------------------------
| gcf                  | 查看 ``git`` 的配置                                                                        | ``git config --list``

## git clean 清理工作目录
如果想要放弃工作区中所有变更，可以使用 ``git clean``
```
gclean
```

| Alias                | Brief                                                                                      | CMD
| --------------       | ----                                                                                       | ------------------------
| gclean               | 删除当前目录下没有 ``git add`` 的文件                                                      | ``git clean -df``

## git status 状态概览
如果需要查看当前目录下文件的状态则需要使用 ``git status`` 命令
```
gss
```

| Alias                | Brief                                                                                      | CMD
| --------------       | ----                                                                                       | ------------------------
| gst                  | 显示工作区状态                                                                             | ``git status``
| gss                  | 简洁的显示工作区状态                                                                       | ``git status -s``
| gsb                  | 简洁的显示工作区状态，同时展示分支状态                                                     | ``git status -sb``

## git add 保存至暂存区
git 在 commit 时，仅会提交暂存区中的变更，所以新增或删除文件时，可以使用 ``git add`` 将修改保存至暂存区
```
gaa
```

| Alias                | Brief                                                                                      | CMD
| --------------       | ----                                                                                       | ------------------------
| ga                   | 添加指定修改至暂存区                                                                       | ``git add``
| gaa                  | 添加所有修改至暂存区                                                                       | ``git add --all``
| gapa                 | 添加指定修改至暂存区，但是可以对提交结果进行编辑                                           | ``git add --patch``

## git commit 提交至仓库

使用 ``git commit`` 将暂存区的变更提交
```
gcam
```

| Alias                | Brief                                                                                      | CMD
| --------------       | ----                                                                                       | ------------------------
| gcmsg                | 提交暂存区指定文件到仓库区                                                                 | ``git commit -m``
| gcam                 | 提交暂存区所有修改到仓库区                                                                 | ``git commit -a -m``
| gca                  | 提交暂存区所有修改到仓库区，通过 ``vi`` 查看修改详情，并添加提交备注                       | ``git commit -v -a``
| gc!                  | 通过 ``vi`` 查看上一次修改详情，并添加提交备注                                             | ``git commit -v --amend``
| gca!                 | 提交暂存区所有修改到仓库区，与上一次 commit 合并，通过 ``vi`` 查看修改详情，并添加提交备注 | ``git commit -v -a --amend``
| gcan!                | 提交暂存区所有修改到仓库区，与上一次 commit 合并                                           | ``git commit -v -a -s --no-edit --amend``

## git diff 差异比较
经常需要查看修改的详情，如果是需要查看未执行 ``gaa`` 的变更，则使用 ``gd``, 如果需要查看已经执行 ``gaa`` 的变更，则需要执行 ``gdca``

| Alias                | Brief                                                                                      | CMD
| --------------       | ----                                                                                       | ------------------------
| gd                   | 查看未暂存的修改                                                                           | ``git diff``
| gdw                  | 查看未暂存的修改，以单词的维度，很适合长句中修改了个别单词的对比                           | ``git diff --word-diff``
| gdca                 | 查看已暂存的修改                                                                           | ``git diff --cached``

# git blame 查看某个文件的提交历史
| Alias                | Brief                                                                                      | CMD
| --------------       | ----                                                                                       | ------------------------
| gbl                  | 查看某个文件的提交历史                                                                     | ``git blame -b -w``
| gdt                  | 查看某次提交修改了哪些文件                                                                 | ``git diff-tree --no-commit-id --name-only -r``
| gsps                 | 查看某次提交的详情，通常配合 ``gbl`` 使用                                                  | ``git show --pretty=short --show-signature``
| gwch                 | 查看某一个文件的变更记录                                                                   | ``git whatchanged -p --abbrev-commit --pretty = medium``

# git log 查看提交历史
| Alias                | Brief                                                                                      | CMD
| --------------       | ----                                                                                       | ------------------------
| glg                  | 查看提交日志，显示提交代码量的统计信息                                                     | ``git log --stat --color``
| glgg                 | 查看提交日志，以简单图形的方式显示                                                         | ``git log --graph --color``
| glgga                | 同上，显示所有 branch                                                                      | ``git log --graph --decorate --all``
| glgm                 | 查看提交日志，最多显示 10 条                                                               | ``git log --graph --max-count = 10``
| glgp                 | 查看提交日志，同时查看变更详情                                                             | ``git log --stat --color -p``
| glo                  | 查看提交日志，在一行内显示                                                                 | ``git log --oneline --decorate --color``
| glog                 | 查看提交日志，在一行内显示，以简单图形的方式显示                                           | ``git log --oneline --decorate --color --graph``
| glol                 | 查看提交日志，在一行内显示，以简单图形的方式显示，显示提交日期和提交人                     | [见 glol 章节](#glol)
| glola                | 同上，显示所有 branch                                                                      | [见 glola 章节](#glola)
| gcount               | 统计每个人提交的次数                                                                       | ``git shortlog -sn``

# git reset 撤销
| Alias                | Brief                                                                                      | CMD
| --------------       | ----                                                                                       | ------------------------
| gru                  | 不知道与 ``grh`` 的区别                                                                    | ``git reset --``
| grh                  | 放弃暂存区的修改                                                                           | ``git reset HEAD``
| grhh                 | 放弃暂存区的修改，同时放弃工作区中已经暂存的修改                                           | ``git reset HEAD --hard``
| gpristine            | 放弃暂存区的修改，同时放弃工作区的全部修改                                                 | ``git reset --hard && git clean -dfx``

# git bisect 错误提交定位

当你需要找出某次提交引入的错误时，就需要使用``git bisect``做二分查找
首先，进入 ``bisect`` 模型，然后标记一个有问题的版本和一个没问题的版本
```python
gbss
gbsb      # 当前版本是有问题的
gbsg v2.6 # 2.6 版本是没有问题的
```
此时，版本已经切换到中间的某个版本了，我们可以验证这个版本是否正常，如果正常，则使用
```
gbsg
```
此时，版本又切换到某个中间版本，继续验证，如果有问题，则使用
```
gbsb
```
最终肯定能找到出现问题的提交记录，最后使用 ``gbsr`` 切换至输入 ``gbss`` 前的版本

| Alias                | Brief                                                                                      | CMD
| --------------       | ----                                                                                       | ------------------------
| gbs                  | NA                                                                                         | ``git bisect``
| gbsb                 | 标记为有问题提交                                                                           | ``git bisect bad``
| gbsg                 | 标记为无问题提交                                                                           | ``git bisect good``
| gbsr                 | 回到``gbss``前的状态                                                                       | ``git bisect reset``
| gbss                 | 开始定位提交错误                                                                           | ``git bisect start``

# git remote 远程仓库管理
运行 ``git remote add <shortname> <url>`` 添加一个新的远程 Git 仓库，同时指定一个你可以轻松引用的简写：
```
$ git remote
origin
$ git remote add pb https://github.com/paulboone/ticgit
$ git remote -v
origin	https://github.com/schacon/ticgit (fetch)
origin	https://github.com/schacon/ticgit (push)
pb	https://github.com/paulboone/ticgit (fetch)
pb	https://github.com/paulboone/ticgit (push)
```

| Alias                | Brief                                                                                      | CMD
| --------------       | ----                                                                                       | ------------------------
| gr                   | 查看远程仓库                                                                               | ``git remote``
| grv                  | 查看远程仓库及其对应的 URL                                                                 | ``git remote -v``
| gra                  | 添加远程仓库                                                                               | ``git remote add``
| grmv                 | 重命名远程仓库                                                                             | ``git remote rename``
| grrm                 | 删除远程仓库                                                                               | ``git remote remove``
| grset                | 修改远程仓库的 URL                                                                         | ``git remote set-url``
| grup                 |                                                                                            | ``git remote update``

# git fetch 拉取远程分支
| Alias                | Brief                                                                                      | CMD
| --------------       | ----                                                                                       | ------------------------
| gf                   |                                                                                            | ``git fetch``
| gfa                  |                                                                                            | ``git fetch --all --prune``
| gfo                  |                                                                                            | ``git fetch origin``

# git checkout 分支创建与切换
如果想放弃工作区的某个文件的修改可以使用 ``git checkout -- filename``
``
gco -- filename
``

| Alias                | Brief                                                                                      | CMD
| --------------       | ----                                                                                       | ------------------------
| gco                  | 切换至指定分支                                                                             | ``git checkout``
| gcb                  | 创建并切换至分支                                                                           | ``git checkout -b``
| gcm                  | 切换至 ``master`` 分支                                                                     | ``git checkout master``
| gcd                  | 切换至 ``develop`` 分支                                                                    | ``git checkout develop``

# git branch 分支查询与删除
| Alias                | Brief                                                                                      | CMD
| --------------       | ----                                                                                       | ------------------------
| gb                   | 查看本地分支，如果指定``branch name``则新建分支，但停留在当前分支                          | ``git branch``
| gbr                  | 查看远程分支                                                                               | ``git branch --remote``
| gba                  | 查看本地及远程分支                                                                         | ``git branch -a``
| gbnm                 | 查看未 merge 的分支                                                                        | ``git branch --no-merged``
| gbd                  | 删除``branch name``分支                                                                    | ``git branch -d``
| gbda                 | 删除已经 merge 的分支，不包括：当前分支、master/develop/dev 分支                           | [见 gbda 章节](#gbda)
| ggsup                | 建立本地分支和远端分支的关系                                                               | ``git branch --set-upstream-to=origin/$(git_current_branch)``

# git merge 合并分支
| Alias                | Brief                                                                                      | CMD
| --------------       | ----                                                                                       | ------------------------
| gm                   | 合并指定分支至当前分支                                                                     | ``git merge``
| gmom                 | 合并 origin 分支至当前分支                                                                 | ``git merge origin/master``
| gmum                 | 合并 upstream 分支至当前分支                                                               | ``git merge upstream/master``
| gmt                  |                                                                                            | ``git mergetool --no-prompt``
| gmtvim               |                                                                                            | ``git mergetool --no-prompt --tool = vimdiff``

# 忽略文件
| Alias                | Brief                                                                                      | CMD
| --------------       | ----                                                                                       | ------------------------
| gignore              | 忽略文件                                                                                   | ``git update-index --assume-unchanged``
| gunignore            | 取消忽略文件                                                                               | ``git update-index --no-assume-unchanged``
| gignored             | 查看忽略的文件                                                                             | ``git ls-files -v grep "^[[:lower:]]"``

# git submodule 子模块
| Alias                | Brief                                                                                      | CMD
| --------------       | ----                                                                                       | ------------------------
| gsi                  |                                                                                            | git submodule init
| gsu                  |                                                                                            | git submodule update

# git stash 保存工作进度
| Alias                | Brief                                                                                      | CMD
| --------------       | ----                                                                                       | ------------------------
| gsta                 |                                                                                            | git stash save
| gstaa                |                                                                                            | git stash apply
| gstd                 |                                                                                            | git stash drop
| gstl                 |                                                                                            | git stash list
| gstp                 |                                                                                            | git stash pop
| gstc                 |                                                                                            | git stash clear
| gsts                 |                                                                                            | git stash show --text
| gwip                 |                                                                                            | [见 gwip 章节](#gwip)
| gunwip               |                                                                                            | [见 gunwip 章节](#gunwip)

# git push 推送至远程仓库
| Alias                | Brief                                                                                      | CMD
| --------------       | ----                                                                                       | ------------------------
| ggp                  |                                                                                            | [见 ggp 章节](#ggp)
| gp                   |                                                                                            | git push
| gpd                  |                                                                                            | git push --dry-run
| gpoat                |                                                                                            | git push origin --all && git push origin --tags
| gpu                  |                                                                                            | git push upstream
| gpv                  |                                                                                            | git push -v
| ggf                  |                                                                                            | git push --force origin $(current_branch)
| gpsup                |                                                                                            | git push --set-upstream origin $(current_branch)

# git pull 拉取远程仓库
| Alias                | Brief                                                                                      | CMD
| --------------       | ----                                                                                       | ------------------------
| ggl                  | 将 ``origin`` 的变更更新至指定分支，若未指定则默认当前分支                                 | [见 ggl 章节](#ggl)
| gl                   |                                                                                            | git pull
| gup                  |                                                                                            | git pull --rebase
| gupv                 |                                                                                            | git pull --rebase -v
| glum                 |                                                                                            | git pull upstream master
| ggu                  |                                                                                            | [见 ggu 章节](#ggu)

# git rebase 合并
| Alias                | Brief                                                                                      | CMD
| --------------       | ----                                                                                       | ------------------------
| grb                  |                                                                                            | git rebase
| grba                 |                                                                                            | git rebase --abort
| grbc                 |                                                                                            | git rebase --continue
| grbi                 |                                                                                            | git rebase -i
| grbm                 |                                                                                            | git rebase master
| grbs                 |                                                                                            | git rebase --skip

# git cherry-pick 选择某次 commit 再次提交
git cherry-pick 可以选择某一个分支中的一个或几个 commit(s) 来进行操作。例如，假设我们有个稳定版本的分支，叫 v2.0，另外还有个开发版本的分支 v3.0，我们不能直接把两个分支合并，这样会导致稳定版本混乱，但是又想增加一个 v3.0 中的功能到 v2.0 中，这里就可以使用 cherry-pick 了，其实也就是对已经存在的 commit 进行再次提交。

| Alias                | Brief                                                                                      | CMD
| --------------       | ----                                                                                       | ------------------------
| gcp                  | git cherry-pick <commit id> 再次提交 commit                                                | git cherry-pick
| gcpa                 |                                                                                            | git cherry-pick --abort
| gcpc                 |                                                                                            | git cherry-pick --continue

# 杂项
| Alias                | Brief                                                                                      | CMD
| --------------       | ----                                                                                       | ------------------------
| grt                  | 进入 ``git`` 仓库的根路径                                                                  | ``cd $(git rev-parse --show-toplevel)``
| ghh                  | 帮助                                                                                       | ``git help``


# git svn 通过 git 管理 svn
| Alias                | Brief                                                                                      | CMD
| --------------       | ----                                                                                       | ------------------------
| git-svn-dcommit-push |                                                                                            | ``git svn dcommit && git push github master:svntrunk``
| gsd                  |                                                                                            | ``git svn dcommit``
| gsr                  |                                                                                            | ``git svn rebase``

# 长命令说明
* <span id='gbda'>gbda</spn>
    ```
    git branch --no-color --merged | command grep -vE "^(\*|\s*(master|develop|dev)\s*$)" | command xargs -n 1 git branch -d
    ```
* <span id='glol'>glol</spn>
    ```
    git log --graph --pretty='%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit
    ```
* <span id='glola'>glola</spn>
    ```
    git log --graph --pretty='%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --all
    ```
* <span id='gwip'>gwip</spn>
    ```
    git add -A; git rm $(git ls-files --deleted) 2> /dev/null; git commit --no-verify -m "--wip-- [skip ci]"
    ```
* <span id='gunwip'>gunwip</spn>
    ```
    git log -n 1 | grep -q -c "\-\-wip\-\-" && git reset HEAD~1
    ```

# git
## 修改默认编辑器为 vim
git config --global core.editor vim

## 保存提交密码
* 更好的方式是使用秘钥
```shell
git config --global credential.helper store
```

## 生成秘钥
* [git 官方帮助](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/) 描述的非常清楚，如果是 Linux 系统，首先通过命令生成秘钥，注意下面命令中的 jiexiao111@gmail.com 是你注册 github 时的邮箱
```python
ssh-keygen -t rsa -C jiexiao111@gmail.com
```

* 想办法把下面这个文件的内容拷贝出来
```shell
~/.ssh/id_rsa.pub
```

* 然后打开你的 github 主页，依次点击 Settings->SSH and GPG keys->New SSH key, 然后 Title 随便取个名字，再把 ``~/.ssh/id_rsa.pub`` 中的内容拷贝到 Key 中，Add SSH key 完成添加
{% img  '/images/add_ssh.png' %}
-

## 解决 git 中文乱码
```python
git config --global core.quotepath false
```

## 撤销 commit 但是保留修改
```shell
git reset --soft [commit_id] 就可以回滚到某一个 commit，然后保留下修改的内容
```

## 比较文件
<https://gist.github.com/jhjguxin/3271961>

## git clone 时 Resolving deltas 后卡住
具体原因不清楚，最后的解决方案是：
* 将其他环境已经 ``git clone`` 的目录拷贝至当前环境
* 执行 ``git fsck``
* 执行 ggl

---

# FAQ
## git clone 时显示 Filename too long
```
git config --global core.longpaths true
```

# 参考
[oh-my-zsh:Plugin:Git](https://github.com/robbyrussell/oh-my-zsh/wiki/Plugin:git)
[Git 常用命令速查表](http://www.jb51.net/article/55442.htm)
[Gitbook](https://git-scm.com/book/zh/v2)
[Git 最常用功能，这一篇就够了！（结合开发场景） ](http://blog.csdn.net/h247263402/article/details/74849182)
