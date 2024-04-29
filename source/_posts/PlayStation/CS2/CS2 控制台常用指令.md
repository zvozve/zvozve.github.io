---
title: CS2 控制台常用指令
auther: zvozve
comments: false
categories:
  - PlayStation
  - CS2
tags:
  - CS2
date: 2024-04-28 19:04:35
---
# 在STEAM/CS2右键属性

![](/images/20240429163621.png)
# 启动选项中输入

```shell
-console
```

![](/images/20240429163847.png)

# 启动游戏后按“~”打开控制台

根据需求输入以下指令并回车

打B5时一键发刀

```
bind F5 "say_team !drop" 
```

打B5和5E时一键发起暂停投票

```
bind F6 "say_team !pause"  
```

打B5和5E时一键发起取消暂停投票

```
bind F7 "say_team !unpause"
```

一键丢掉雷包。

```
bind "6" "use weapon_c4;drop"
```

两种一键切换左右手写法。

```
bind "L" "toggle cl_righthand 0 1" 
```

消音器单独绑定为鼠标侧键

```
bind mouse2 "+zoom"; 

bind mouse4 "+attack2";
```



