---
title: git 使用
date: 2017-12-31 10:46:55
categories: 操作系统
tags:
  - linux
---

<!-- 文章开头都用它了，整齐才好看 -->
{% note default %}
经常在使用 git，但是使用的命令都是那几个，有时候想达到特殊目的时都要查半天，所以决定整理一下
{% endnote %}

<!--more-->

# git 命令别名
如果安装了 oh-my-zsh，则以下快捷命令均能生效
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

| Alias                | Brief                                                            | CMD
| --------------       | ----                                                             | ------------------------
| g                    | NA                                                               | ``git``
| ga                   | 添加指定修改至缓存区                                             | ``git add``
| gaa                  | 添加所有修改至缓存区                                             | ``git add --all``
| gapa                 | 添加指定修改至缓存区，但是可以对提交结果进行编辑，[见 gapa 章节](#gapa)                                 | ``git add --patch``
| gb                   | 查看本地分支                                                     | ``git branch``
| gba                  | 查看本地及远程分支                                                                | ``git branch -a``
| gbda                 | 删除已经 merge 的分支，不包括：当前分支、master/develop/dev 分支 | [见 gbda 章节](#gbda)
| gbl                  |                                                                  | git blame -b -w
| gbnm                 |                                                                  | git branch --no-merged
| gbr                  |                                                                  | git branch --remote
| gbs                  |                                                                  | git bisect
| gbsb                 |                                                                  | git bisect bad
| gbsg                 |                                                                  | git bisect good

| Alias                | Brief                                                            | CMD
| --------------       | ----                                                             | ------------------------
| gbsr                 |                                                                  | git bisect reset
| gbss                 |                                                                  | git bisect start
| gc                   |                                                                  | git commit -v
| gc!                  |                                                                  | git commit -v --amend
| gca                  |                                                                  | git commit -v -a
| gcam                 |                                                                  | git commit -a -m
| gca!                 |                                                                  | git commit -v -a --amend
| gcan!                |                                                                  | git commit -v -a -s --no-edit --amend
| gcb                  | 创建并切换至分支                                                 | git checkout -b
| gcf                  |                                                                  | git config --list
| gcl                  |                                                                  | git clone --recursive
| gclean               |                                                                  | git clean -df
| gcm                  |                                                                  | git checkout master
| gcd                  |                                                                  | git checkout develop
| gcmsg                |                                                                  | git commit -m
| gco                  |                                                                  | git checkout
| gcount               |                                                                  | git shortlog -sn
| gcp                  |                                                                  | git cherry-pick
| gcpa                 |                                                                  | git cherry-pick --abort
| gcpc                 |                                                                  | git cherry-pick --continue
| gcs                  |                                                                  | git commit -S
| gd                   |                                                                  | git diff
| gdca                 |                                                                  | git diff --cached
| gdt                  |                                                                  | git diff-tree --no-commit-id --name-only -r
| gdw                  |                                                                  | git diff --word-diff
| gf                   |                                                                  | git fetch
| gfa                  |                                                                  | git fetch --all --prune
| gfo                  |                                                                  | git fetch origin
| gg                   |                                                                  | git gui citool
| gga                  |                                                                  | git gui citool --amend
| ggf                  |                                                                  | git push --force origin $(current_branch)
| ghh                  |                                                                  | git help
| ggpull               |                                                                  | ggl
| ggpur                |                                                                  | ggu
| ggpush               |                                                                  | ggp
| ggsup                |                                                                  | git branch --set-upstream-to = origin/$(current_branch)
| gpsup                |                                                                  | git push --set-upstream origin $(current_branch)
| gignore              |                                                                  | git update-index --assume-unchanged
| gignored             |                                                                  | git ls-files -v &#124; grep "^:lower:"
| git-svn-dcommit-push |                                                                  | git svn dcommit && git push github master:svntrunk
| gk                   |                                                                  | \gitk --all --branches
| gke                  |                                                                  | \gitk --all $(git log -g --pretty = format:%h)
| gl                   |                                                                  | git pull
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
| gm                   | 合并指定分支至当前分支                                           | git merge
| gmom                 |                                                                  | git merge origin/master
| gmt                  |                                                                  | git mergetool --no-prompt
| gmtvim               |                                                                  | git mergetool --no-prompt --tool = vimdiff
| gmum                 |                                                                  | git merge upstream/master
| gp                   |                                                                  | git push
| gpd                  |                                                                  | git push --dry-run
| gpoat                |                                                                  | git push origin --all && git push origin --tags
| gpristine            |                                                                  | git reset --hard && git clean -dfx
| gpu                  |                                                                  | git push upstream
| gpv                  |                                                                  | git push -v
| gr                   |                                                                  | git remote
| gra                  |                                                                  | git remote add
| grb                  |                                                                  | git rebase
| grba                 |                                                                  | git rebase --abort
| grbc                 |                                                                  | git rebase --continue
| grbi                 |                                                                  | git rebase -i
| grbm                 |                                                                  | git rebase master
| grbs                 |                                                                  | git rebase --skip
| grh                  |                                                                  | git reset HEAD
| grhh                 |                                                                  | git reset HEAD --hard
| grmv                 |                                                                  | git remote rename
| grrm                 |                                                                  | git remote remove
| grset                |                                                                  | git remote set-url
| grt                  |                                                                  | cd $(git rev-parse --show-toplevel &#124;&#124; echo ".")
| gru                  |                                                                  | git reset --
| grup                 |                                                                  | git remote update
| grv                  |                                                                  | git remote -v
| gsb                  |                                                                  | git status -sb
| gsd                  |                                                                  | git svn dcommit
| gsi                  |                                                                  | git submodule init
| gsps                 |                                                                  | git show --pretty = short --show-signature
| gsr                  |                                                                  | git svn rebase
| gss                  |                                                                  | git status -s
| gst                  |                                                                  | git status
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
| gunwip               |                                                                  | git log -n 1 &#124; grep -q -c "--wip--" && git reset HEAD~1
| gup                  |                                                                  | git pull --rebase
| gupv                 |                                                                  | git pull --rebase -v
| glum                 |                                                                  | git pull upstream master
| gvt                  |                                                                  | git verify-tag
| gwch                 |                                                                  | git whatchanged -p --abbrev-commit --pretty = medium
| gwip                 |                                                                  | git add -A; git rm $(git ls-files --deleted) 2> /dev/null; git commit -m "--wip--"

# 部分命令详细说明

## <span id='gapa'>gapa</spn>
http://nuclearsquid.com/writings/git-add/

## <span id='gbda'>gbda</spn>
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
