---
title: Homebrew下载换源
auther: zvozve
comments: false
categories:
  - Applications
  - HomeBrew
date: 2024-04-28 19:17:56
tags:
---
[https://developer.aliyun.com/article/1119808](https://developer.aliyun.com/article/1119808)

# **修改dns(方案一)**

系统偏好设置=>网络=>高级=>DNS

这里要添加两个dns

`8.8.8.8 114.114.114.114`

# **换源(方案二)**

**1.使用国内源（建议清华大学源）**

`/bin/zsh -c "$(curl -fsSL <https://gitee.com/cunkai/HomebrewCN/raw/master/Homebrew.sh>)"`

**2.安装成功测试**

`brew search redis #搜索包信息`

**3.Homebrew安装上了，但是有些软件无法安装，可以考虑使用阿里镜像**

替换 / 还原 brew.git 仓库地址

替换成阿里巴巴的 brew.git 仓库地址:

`cd "$(brew --repo)" git remote set-url origin <https://mirrors.aliyun.com/homebrew/brew.git`>

还原为官方提供的 brew.git 仓库地址

`cd "$(brew --repo)" git remote set-url origin <https://github.com/Homebrew/brew.git`>

替换 / 还原 homebrew-core.git 仓库地址

替换成阿里巴巴的 homebrew-core.git 仓库地址:

`cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core" git remote set-url origin <https://mirrors.aliyun.com/homebrew/homebrew-core.git`>

还原为官方提供的 homebrew-core.git 仓库地址

`cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core" git remote set-url origin <https://github.com/Homebrew/homebrew-core.git`>