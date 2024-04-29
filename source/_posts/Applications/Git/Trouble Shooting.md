---
title: Trouble Shooting
comments: false
categories:
  - Applications
  - Git
tags:
  - Git
date: 2024-04-28 19:17:56
---
# 443

```shell
git config --global --unset http.proxy
git config --global --unset https.proxy
```

# 10054

> Open the Git command page and execute the git command script
> Modify settings and disable SSL verification

```shell
git config --global http.sslverify "false"
```
# command not found

> This situation often occurs when copying and pasting commands. 
> There are often extra spaces at the beginning of the command.
> Check whether there are any extra spaces in the command and remove them.

# No configured push destination.

> Create a new repository in git and copy the repository URL link：

```shell
git remote add origin [https:*//github.com/xxxxx/xxxxx.git*](https://github.com/xxxxx/xxxxx.git) 

git push -u origin master
```

# unable to get local issuer certificate

> Since Git turns on SSL verification by default, just turn it off;

```shell
git config --global http.sslVerify false
```

# Do not show local branches

```shell
git init
git add .
git commit
git branch
```
# Reference

[OpenSSL SSL_read: Connection was reset, errno 10054 错误解决](https://blog.csdn.net/weixin_43945983/article/details/110882074)
[解决使用Git时报错"bash: $'\302\226git': command not found"](https://www.cnblogs.com/chy18883701161/p/12759564.html "发布于 2020-04-24 09:31")
[git报错：fatal: No configured push destination](https://www.cnblogs.com/nayek/p/12238801.html "发布于 2020-01-28 20:17")
[git branch 不显示的原因](https://blog.csdn.net/angduozu7316/article/details/101489304)
