---
title: VSCode终端中文乱码问题
auther: zvozve
comments: false
categories:
  - Applications
  - VSCode
tags:
  - VSCode
date: 2024-04-29 19:20:45
---
打开VSCode
打开“文件”--“首选项”--“设置”
然后在setting.json中设置
把下面三行复制到里面

```c
{
    "editor.fontSize": 18,
    "terminal.integrated.shellArgs.windows": ["/K chcp 65001 >nul"],
    "terminal.integrated.fontFamily": "Lucida Console",
}
```