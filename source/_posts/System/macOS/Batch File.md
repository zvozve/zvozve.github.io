---
title: Batch File
auther: zvozve
comments: false
categories:
  - System
  - macOS
tags: 
date: 2024-04-29 17:20:21
---
# 新建一个文本文件

> 命名为test.command。
> 注意一定要以command为结尾。
# 打开『**终端**』程序

> 给test.command加上可执行权限。命令为

```shell
chmod +x test.command.
```
# 用编辑器打开文本文件

> 输入可以在终端执行的指令。**例如ls**

# 将文件保存到桌面上。然后双击打开

> 这里有一个问题。就是批处理执行完了。弹出的那个命令行不会自动关闭。
> 为了解决这个问题。在批处理文件的最后加上代码：

```shell
osascript -e 'tell application"Terminal" to close (every window whose name contains".command")' &exit
```
