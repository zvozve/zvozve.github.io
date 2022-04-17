---
title: 本地项目同步到Github
comments: false
date: 2022-04-17 13:28:51
categories:
- Git
tags:
- Git
---

# 本地项目同步到Github

## 安装软件

首先在本地安装[git](https://git-scm.com/downloads)



## 建立Github仓库

复制地址（http连接）

```
git clone https://github.com/用户名/仓库名.git
```



## 生成SSH key

生成密钥（Git Bash中操作）

```c
ssh-keygen -t rsa -C "邮箱"
//接下来直接全部回车
```

将生成密钥：id_rsa.pud 中的密钥设置到github中

将密钥写入key中，title可以不用写，只是一个标题

 

## 配置登录信息

同步信息

> 将自己在Github上的注册的用户名和邮箱写入本地git的配置文件中

```
git config --global user.email "zvozve@gmail.com"
git config --global user.name "ZvoZve"
```

连接远程仓库

```
git clone https://github.com/用户名/仓库名.git
```

## 推送

初始化

```
git init
```

将工作区文件提交到缓存区中

```c
git status //查看有多少文件未提交到仓库中
git add . 
git status
git commit -m ‘提交描述’
git push --set-upstream origin master //初次配置
git push -u origin master
```

推送到Github

```
git push
```
