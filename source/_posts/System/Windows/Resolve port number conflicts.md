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

![](https://raw.githubusercontent.com/zvozve/image-bed/main/pic/20250810211002810.png)

# 查找占用端口号的进程

> 如图所示，此进程编号（pid）为16524

```shell
netstat -ano|findstr "1085"
```

![](https://raw.githubusercontent.com/zvozve/image-bed/main/pic/20250810211022115.png)

# 杀死进程，解放端口

```shell
taskkill /pid 16524 -t -f
```

![](https://raw.githubusercontent.com/zvozve/image-bed/main/pic/20250810211031878.png)

# Reference

[windows解决端口号冲突](https://blog.csdn.net/qq_36251958/article/details/79346299)

