---
title: GTAV装MOD
auther: zvozve
comments: false
date: 2022-04-10 12:03:20
categories:
- GTAV
tags:
- GTAV
---

# 搭建环境

1.在GTAV根目录添加配置文件

单独添加有

> **1.安装ScriptHookV**
>
> 只把这2个（dinput8.dll ScriptHookV.dll）复制到GTA5游戏根目录
>
> NativeTrainer.asi 这个是修改器是英文版可以不复制。
>
> **2.安装ScriptHookVDotNet**
>
> 把文件（README.md ScriptHookVDotNet.asi ScriptHookVDotNet.dll ScriptHookVDotNet.ini ScriptHookVDotNet.xml）复制到GTA5游戏根目录
>
> 3.安装NativeUI.dll
>
> 直接复制scripts文件夹到你的GTA5.exe游戏根目录
>
> **4.安装 LUA Plugin for Script Hook V 10.1**
>
> 为以后运行LUA格式的MOD做准备。把scripts文件夹里面的文件复制进GTA5游戏目录scripts文件夹里，把LUA.asi复制进GTA5游戏根目录。
>
> 来自 <https://www.iwyv.com/youxi/2021-04-12/47711.html> 

可以下整合包

2.安装openiv

打开openiv，添加GTAV定位目录

进入软件后安装3个插件

3.打开openiv的编辑模式，在openiv中定位到Update/update.rpf/common/data，找到dlclist.xml，右键编辑，提示复制到mods目录，点击复制

4.在openiv中定位到**mods**/Update/update.rpf/common/data，替换gameconfig.xml文件

# 添加MOD

## 添加载具MOD

1.建立目录mods/Update/x64/dlcpacks，将需要添加的**mod目录**拖进去

2.在openiv中定位到mods/Update/update.rpf/common/data/dlclist.xml，右键编辑，添加mod说明文件里面的一行代码

## 添加人物MOD

下载addonpeds

1.把addonpeds的文件添加到GTAV根目录，除了dlcpacks/addonpeds

2.把addonpeds目录中dlcpacks下的“addonpeds”目录拷贝到mods/Update/x64/dlcpacks/

3.在openiv中定位目录mods/Update/x64/dlcpacks/dlc.rpf/pxx(忘了).rpf，把人物mod的四个文件拖进去

4.以管理员身份打开addonpeds.exe，添加角色，名字和mod配置文件名一样，设置性别和组合（一般是非组合）情况，点击rebuild，重建

## 添加GPS语音包

> 参考：<https://www.cnntt.com/archives/4446>

下载文件，将“Scripts”文件夹放在GTA5的根目录下，然后进入游戏就可以了。

 

游戏内修改设置:

重新读取设定文件，按键盘(~)键，输入：

"RELOADWAZE" - 重新加载 Waze.ini 文件。

"WAZECHANGEVOICE" 回车然后输入语音文件夹名称 - 换语音。

"WAZEVOLUME" 回车然后输入0-100 - 调声量。

"WAZELIVE ON/OFF" - 现场报告开关。

"WAZEUNIT METER/MILE" - 米/英里切换。
