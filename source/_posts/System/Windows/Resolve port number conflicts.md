---
title: Resolve port number conflicts
auther: zvozve
comments: false
categories:
  - System
  - Windows
tags:
  - Windows
date: 2024-04-29 15:48:46
---
# 查看端口号(以1085端口为例)

```shell
netstat -ano 
```

![](/images/20240425142147.png)

# 查找占用端口号的进程

> 如图所示，此进程编号（pid）为16524

```shell
netstat -ano|findstr "1085"
```

![](/images/20240425142151.png)

# 杀死进程，解放端口

```shell
taskkill /pid 16524 -t -f
```

![](/images/20240425142156.png)

# Reference

[windows解决端口号冲突](https://blog.csdn.net/qq_36251958/article/details/79346299)

