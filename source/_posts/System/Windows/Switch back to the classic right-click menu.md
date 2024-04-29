---
title: Switch back to the classic right-click menu
auther: zvozve
comments: false
categories:
  - System
  - Windows
tags:
  - Windows
date: 2022-03-18 17:50:47
---
# Switch back to the classic

> Open Windows powershell（Admin）

```c
reg add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f /ve
```

# Recovery New

> Open Windows powershell（Admin）

```c
reg delete "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}" /f
```

# Reference

[【Win11】完美解决Win11烦人的右键菜单&任务栏问题](https://blog.csdn.net/p2003722/article/details/120769690)
