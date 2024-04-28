---
title: 本地项目同步到Github
comments: false
date: 2022-04-17 13:28:51
categories:
- Git
tags:
- Git
---
# 首次推送

## 云端建立Github仓库

## 安装软件[git](https://git-scm.com/downloads)

## 生成SSH key并设置到github中
  
>Git Bash / CMD中操作
>将生成密钥：id_rsa.pud 中的密钥设置到github中   
>将密钥写入key中，title可以不用写，只是一个标题
  
```shell   
ssh-keygen -t rsa -C "邮箱"   
//接下来直接全部回车   
```
## 配置登录信息   
  
> 将自己在Github上的注册的用户名和邮箱写入本地git的配置文件中   
  
```shell
git config --global user.email "zheng.zhao@hi-uside.com"   
git config --global user.name "zheng.zhao"   
```
## Git拉取和推送
  
```c
// 目录初始化
git init

// 建立并切换到分支
git checkout -b dev

// 连接仓库
git remote add origin [ProjectURL]

// 选择并下载远程分支
git fetch origin
git merge origin/[branchName]

// 更新内容并推送
git add .
git status
git commit -m '[updateCommit]' 
git push origin [branchName]

// 或者
git status //查看有多少文件未提交到仓库中   
git add .   
git status   
git commit -m '[updateCommit]' 
git push --set-upstream origin [branchName] //初次配置   
git push -u origin [branchName] 
```
# 非首次推送   

```c
// 更新内容并推送
git add .
git status
git commit -m '[updateCommit]' 
git push
```
