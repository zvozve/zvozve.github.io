---
title: Hackintosh Installation tutorial_UDisk
auther: zvozve
comments: false
categories:
  - System
  - Hackintosh
tags:
  - Hackintosh
date: 2023-01-14 19:04:35
---
# 1.准备：

## 1.1.镜像

公众号：黑果小兵，打赏对应文章后获取下载链接

## 1.2.EFI

本群大佬发的群文件

## 1.3.工具

### win用：

DiskGenius （硬盘分区、替换EFI文件）、

balenaEtcher（写U盘镜像）、

EasyUEFI（更换开机启动项）

双系统时间同步补丁.reg （百度搜，同步双系统时间用）

### mac用：

OCAT （挂载硬盘，编辑配置文件）

OpenCore Configurator （挂载硬盘，编辑配置文件）

PlistEdit_Pro（编辑配置文件）

## 1.4.备份网卡的MAC地址

打开cmd，输入ipconfig /all

全文复制保存为txt备用

# 2.硬盘分区：

DiskGenius给硬盘分区，格式化为APFS格式，

或者使用win自带的“创建并格式化硬盘分区”，不要格式化，不要加载盘符

# 3．U盘写入镜像：

直接用balenaEtcher加载镜像写入U盘分区

打开DiskGenius，找到U盘的EFI文件夹，删除OC文件夹，把大佬EFI文件里的OC文件夹丢进去

（后续不开机或者报错就再找EFI替换这个文件）

———这之前都在win下完成———

# 4．安装macOS：

开机按F9进入启动项选择，选择你U盘的macOS

进去后先不要安装，使用mac的磁盘工具看一下分区情况，没有分区就创建然后退出磁盘工具，进入安装界面

选择你创建的macOS安装位置，安装，

中间会重启两三次，第一次重启后选择继续安装的图标

# 5．洗白：

进入macOS，

先设置账户密码啥的，不要联网！！！

安装或者解压OCAT、OpenCore Configurator、PlistEdit＿Pro

进入系统后用OpenCore Configurator 挂载硬盘，访达里打开加载的EFI文件夹

找到config.plist，备份一份，然后右键用OCAT打开，然后看这个[洗白教程](https://blog.csdn.net/KGD_Judy/article/details/118943312)，修改完保存重启，启动项里选择清理NVRAM

开机后就可以联网玩了

mac／win系统时间有问题的话，用这个“双系统时间同步补丁.reg”

# 6．启动项：

重启到win，

用DiskGenius把修改后的OC文件夹放到MBR分区的EFI里面，

用EasyUEFI添加macOS的启动项，选择你放OC文件夹里面的启动项目，大功告成！！！

# 优化

### 1．连接鼠标时禁用Mac触控板设置

路径：设置，辅助功能

### 2．屏蔽独显

用PlistEdit Pro打开config，搜索找到boot-args，添加-wegnoegpu参数，之后保存重启即可

### 3．开机跑码

升级OC，使用OCAT更新

## 4．修饰键

设置，辅助功能