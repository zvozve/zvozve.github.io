---
title: Github分支管理
comments: false
date: 2022-04-17 13:22:10
categories:
- Git
tags:
- Git
---



# Github 分支管理

[参考](https://blog.csdn.net/top_code/article/details/51931916)

## 创建/切换分支

创建分支的同时切换到该分支上，命令如下：

```
git checkout -b [branch name]
```

效果相当于以下两步操作：

本地创建分支

```
git branch [branch name]
```

切换到分支

```
git checkout [branch name]
```

## 删除分支

### 删除本地分支

```
git branch -d [branch name]
```

### 删除远程分支

```
git push origin :[branch name]
```

## 查看分支

### 查看本地分支

```c
$ git branch
* master
// * 标识的是你当前所在的分支。
```

### 查看远程分支

```
git branch -r
```

### 查看所有分支

```
git branch -a
```

## 推送分支

```
git push origin [branch name]
```
