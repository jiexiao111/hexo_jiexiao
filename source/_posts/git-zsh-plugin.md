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

# 基础
| Alias          | Brief                                                                                      | CMD
| -------------- | ----                                                                                       | ------------------------
| gcl            | 递归的 clone                                                                               | ``git clone --recursive``
| gcf            | 查看 ``git`` 的配置                                                                        | ``git config --list``
| gclean         | 删除当前目录下没有 ``git add`` 的文件                                                      | ``git clean -df``
| gcount         | 统计每个人提交的次数                                                                       | ``git shortlog -sn``

# 跟踪新文件
| Alias          | Brief                                                                                      | CMD
| -------------- | ----                                                                                       | ------------------------
| ga             | 添加指定修改至暂存区                                                                       | ``git add``
| gaa            | 添加所有修改至暂存区                                                                       | ``git add --all``
| gapa           | 添加指定修改至暂存区，但是可以对提交结果进行编辑                                           | ``git add --patch``

# 暂存已经跟踪的文件
| Alias          | Brief                                                                                      | CMD
| -------------- | ----                                                                                       | ------------------------
| gcmsg          | 提交暂存区指定文件到仓库区                                                                 | ``git commit -m``
| gcam           | 提交暂存区所有修改到仓库区                                                                 | ``git commit -a -m``
| gca            | 提交暂存区所有修改到仓库区，通过 ``vi`` 查看修改详情，并添加提交备注                       | ``git commit -v -a``
| gc!            | 通过 ``vi`` 查看上一次修改详情，并添加提交备注                                             | ``git commit -v --amend``
| gca!           | 提交暂存区所有修改到仓库区，与上一次 commit 合并，通过 ``vi`` 查看修改详情，并添加提交备注 | ``git commit -v -a --amend``
| gcan!          | 提交暂存区所有修改到仓库区，与上一次 commit 合并                                           | ``git commit -v -a -s --no-edit --amend``

# 查看修改
| gd                   | 查看未暂存的修改                                                                 | git diff
| gdca                 | 查看已暂存的修改                                                                 | git diff --cached
| gdt                  |                                                                  | git diff-tree --no-commit-id --name-only -r
| gdw                  |                                                                  | git diff --word-diff

## 分支
| Alias          | Brief                                                                                      | CMD
| -------------- | ----                                                                                       | ------------------------
| gb             | 查看本地分支，如果指定``branch name``则新建分支，但停留在当前分支                          | ``git branch``
| gbr            | 查看远程分支                                                                               | ``git branch --remote``
| gba            | 查看本地及远程分支                                                                         | ``git branch -a``
| gbnm           | 查看未 merge 的分支                                                                        | ``git branch --no-merged``
| gbd            | 删除``branch name``分支                                                                    | ``git branch -d``
| gbda           | 删除已经 merge 的分支，不包括：当前分支、master/develop/dev 分支                           | [见 gbda 章节](#gbda)
| ggsup          |                                                                                            | ``git branch --set-upstream-to=origin/$(git_current_branch)``

## 状态查询
| Alias          | Brief                                                                                      | CMD
| -------------- | ----                                                                                       | ------------------------
| gbl            | 查看某个文件的变更历史                                                                     | ``git blame -b -w``
| gsps           | 查看某次提交的详情，通常配合 ``gbl`` 使用                                                  | ``git show --pretty=short --show-signature``
| gst            | 显示工作区状态                                                                             | ``git status``
| gss            | 简洁的显示工作区状态                                                                       | ``git status -s``
| gsb            | 简洁的显示工作区状态，同时展示分支状态                                                     | ``git status -sb``

## git bisect
| Alias          | Brief                                                                                      | CMD
| -------------- | ----                                                                                       | ------------------------
| gbs            |                                                                                            | ``git bisect``
| gbsb           |                                                                                            | ``git bisect bad``
| gbsg           |                                                                                            | ``git bisect good``
| gbsr           |                                                                                            | ``git bisect reset``
| gbss           |                                                                                            | ``git bisect start``

| Alias                | Brief                                                            | CMD
| --------------       | ----                                                             | ------------------------
| gcb                  | 创建并切换至分支                                                 | git checkout -b
| gcm                  |                                                                  | git checkout master
| gcd                  |                                                                  | git checkout develop
| gco                  |                                                                  | git checkout
| gcp                  |                                                                  | git cherry-pick
| gcpa                 |                                                                  | git cherry-pick --abort
| gcpc                 |                                                                  | git cherry-pick --continue
| gf                   |                                                                  | git fetch
| gfa                  |                                                                  | git fetch --all --prune
| gfo                  |                                                                  | git fetch origin
| gg                   |                                                                  | git gui citool
| gga                  |                                                                  | git gui citool --amend
| ghh                  |                                                                  | git help
| ggpull               |                                                                  | ggl
| ggpur                |                                                                  | ggu
| ggpush               |                                                                  | ggp
| gignore              |                                                                  | git update-index --assume-unchanged
| gignored             |                                                                  | git ls-files -v &#124; grep "^:lower:"
| git-svn-dcommit-push |                                                                  | git svn dcommit && git push github master:svntrunk
| gk                   |                                                                  | \gitk --all --branches
| gke                  |                                                                  | \gitk --all $(git log -g --pretty = format:%h)
| glg                  |                                                                  | git log --stat --color
| glgg                 |                                                                  | git log --graph --color
| glgga                |                                                                  | git log --graph --decorate --all
| glgm                 |                                                                  | git log --graph --max-count = 10
| glgp                 |                                                                  | git log --stat --color -p
| glo                  |                                                                  | git log --oneline --decorate --color
| glog                 |                                                                  | git log --oneline --decorate --color --graph
| glol                 |                                                                  | git log --graph --pretty = format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit
| glola                |                                                                  | git log --graph --pretty = format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit  --all
| glp                  |                                                                  | &#95;git&#95;log&#95;prettily
| gunwip               |                                                                  | git log -n 1 &#124; grep -q -c "--wip--" && git reset HEAD~1
| gm                   | 合并指定分支至当前分支                                           | git merge
| gmom                 |                                                                  | git merge origin/master
| gmum                 |                                                                  | git merge upstream/master
| gmt                  |                                                                  | git mergetool --no-prompt
| gmtvim               |                                                                  | git mergetool --no-prompt --tool = vimdiff
| gp                   |                                                                  | git push
| gpd                  |                                                                  | git push --dry-run
| gpoat                |                                                                  | git push origin --all && git push origin --tags
| gpu                  |                                                                  | git push upstream
| gpv                  |                                                                  | git push -v
| ggf                  |                                                                  | git push --force origin $(current_branch)
| gpsup                |                                                                  | git push --set-upstream origin $(current_branch)
| gr                   |                                                                  | git remote
| gra                  |                                                                  | git remote add
| grmv                 |                                                                  | git remote rename
| grrm                 |                                                                  | git remote remove
| grset                |                                                                  | git remote set-url
| grup                 |                                                                  | git remote update
| grv                  |                                                                  | git remote -v
| grb                  |                                                                  | git rebase
| grba                 |                                                                  | git rebase --abort
| grbc                 |                                                                  | git rebase --continue
| grbi                 |                                                                  | git rebase -i
| grbm                 |                                                                  | git rebase master
| grbs                 |                                                                  | git rebase --skip
| gru                  |                                                                  | git reset --
| grh                  |                                                                  | git reset HEAD
| grhh                 |                                                                  | git reset HEAD --hard
| gpristine            |                                                                  | git reset --hard && git clean -dfx
| grt                  |                                                                  | cd $(git rev-parse --show-toplevel &#124;&#124; echo ".")
| gsd                  |                                                                  | git svn dcommit
| gsi                  |                                                                  | git submodule init
| gsr                  |                                                                  | git svn rebase
| gsta                 |                                                                  | git stash save
| gstaa                |                                                                  | git stash apply
| gstd                 |                                                                  | git stash drop
| gstl                 |                                                                  | git stash list
| gstp                 |                                                                  | git stash pop
| gstc                 |                                                                  | git stash clear
| gsts                 |                                                                  | git stash show --text
| gsu                  |                                                                  | git submodule update
| gts                  |                                                                  | git tag -s
| gunignore            |                                                                  | git update-index --no-assume-unchanged
| gl                   |                                                                  | git pull
| gup                  |                                                                  | git pull --rebase
| gupv                 |                                                                  | git pull --rebase -v
| glum                 |                                                                  | git pull upstream master
| gvt                  |                                                                  | git verify-tag
| gwch                 |                                                                  | git whatchanged -p --abbrev-commit --pretty = medium
| gwip                 |                                                                  | git add -A; git rm $(git ls-files --deleted) 2> /dev/null; git commit -m "--wip--"

# 长命令说明
* <span id='gbda'>gbda</spn>
    ```
    git branch --no-color --merged | command grep -vE "^(\*|\s*(master|develop|dev)\s*$)" | command xargs -n 1 git branch -d
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

# 参考
[oh-my-zsh:Plugin:Git](https://github.com/robbyrussell/oh-my-zsh/wiki/Plugin:git)
[Git 常用命令速查表](http://www.jb51.net/article/55442.htm)
[Gitbook](https://git-scm.com/book/zh/v2)
