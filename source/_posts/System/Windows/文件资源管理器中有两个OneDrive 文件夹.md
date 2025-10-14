---
title: 文件资源管理器中有两个OneDrive 文件夹
auther: zvozve
comments: false
categories:
  - System
  - Windows
tags:
  - Windows
  - OneDrive
date: 2025-10-14 21:09:47
---

文件资源管理器中有两个OneDrive 文件夹 - 删除多余的OneDrive图标

https://www.youtube.com/watch?v=igcPJtu-AYE

1. WINDOWS + R, 输入regedit
2. 找到这条路径： HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Desktop\NameSpace
3. 找到其中包含 *OneDrive* 条目的文件夹，记录文件夹名称
4. 进入HKEY_CLASSES_ROOT\CLSID\
5. 找到步骤3同名文件夹
6. 打开此文件夹，双击右边窗格System.IsPinnedtoNameSpaceTree文件，把值改为“0”；