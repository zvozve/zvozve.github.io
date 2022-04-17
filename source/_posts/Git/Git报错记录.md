---
title: Git报错记录
comments: false
date: 2022-04-17 13:23:25
categories:
- Git
tags:
- Git
---

# Git报错

## 443

```
git config --global --unset http.proxy
git config --global --unset https.proxy
```

## 10054

[参考](https://blog.csdn.net/weixin_43945983/article/details/110882074)

打开Git命令页面，执行git命令脚本：修改设置，解除ssl验证

```
git config --global http.sslverify "false"
```

## command not found

[参考](https://www.cnblogs.com/chy18883701161/p/12759564.html)

此种情况常出现在复制、粘贴命令时，命令开头往往会有多余的空格。

检查命令中是否有多余的空格，去除多余的空格即可。

## No configured push destination.

[参考](https://www.cnblogs.com/nayek/p/12238801.html)

在git仓库创建新的仓库然后复制仓库URL链接：

```
git remote add origin [https:*//github.com/xxxxx/xxxxx.git*](https://github.com/xxxxx/xxxxx.git) 

git push -u origin master
```

## unable to get local issuer certificate

这个是由于Git默认开启了[SSL](https://so.csdn.net/so/search?q=SSL&spm=1001.2101.3001.7020)验证，关闭即可；

解决方式：

```javascript
git config --global http.sslVerify false
```

执行以上git命令，关闭ssl验证。

## git branch 不显示的原因

[参考](https://blog.csdn.net/angduozu7316/article/details/101489304?spm=1001.2101.3001.6650.1&amp;utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1.pc_relevant_paycolumn_v3&amp;depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1.pc_relevant_paycolumn_v3&amp;utm_relevant_index=2 )

必须使用git init命令创建仓库，执行git add . 和git [commit](https://so.csdn.net/so/search?q=commit&spm=1001.2101.3001.7020)（提交成功后）,再使用git branch命令，才显示出本地分支。
