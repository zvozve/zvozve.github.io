---
title: Hackintosh
auther: zvozve
comments: false
date: 2022-04-10 11:28:51
categories:
- Hackintosh
tags:
- Hackintosh
---

# 硬盘安装黑苹果

参考链接

> [硬盘安装黑苹果](https://www.bilibili.com/video/BV1Vb411U735)
>
> [2020年AMD R52600最新黑苹果教程，无需u盘直接硬盘安装，看了不会别找我](https://www.bilibili.com/video/BV1ba4y1L7CV)



## 下载镜像和efi文件

工具🔧：迅雷或者各家云盘

镜像：黑果小兵的公众号

efi：github或者加交流群（自己找）

## 准备容器（硬盘）

工具🔧：DiskGenius

**目标盘**

> 目标盘要有esp分区且分区格式为guid

将硬盘分出来一个区（50g左右）

分配盘符后**不要格式化**

**安装工具盘**

将硬盘分出来一个区（20g左右）

分配盘符后**不要格式化**

## 处理镜像

工具🔧：软碟通、7z、leadra

1.利用软碟通把黑苹果dmg 镜像转换为iso格式

2.改后缀名为cdr

3.用7zip提取镜像中的hfsx文件用于制作安装盘

4.用leadra工具把提取的hfsx文件写入到安装工具盘

**取消底下三个勾选**

5.以**管理员**打开CMD

选择镜像所在磁盘分区

```c
diskpart
list disk
select disk 1（指定硬盘号）
list partition
select partition 2（指定分区号）
set id=48465300-0000-11AA-AA11-00306543ECAC
```

## 安装

# 洗白

工具🔧：OC Auxiliary Tools、PlistEdit Pro

[洗白教程](https://blog.csdn.net/KGD_Judy/article/details/118943312)

在Win下查看MAC地址

# 优化

1.**俩系统时间不一致**

Win下安装“双系统时间同步补丁.reg”

2.**连接鼠标时禁用Mac触控板**

在辅助功能里设置

3.**屏蔽独显**

用PlistEdit Pro打开config，搜索找到boot-args,添加-wegnoegpu参数，之后保存重启即可

4.**开机跑码**

升级OC，使用OCAT更新

5.修饰键

| macOS          | Fn        | ⌃ Control | ⌥ Option  | ⌘ Command | Space | ⌘ Command | ⌥ Option  |
| -------------- | --------- | --------- | --------- | --------- | ----- | --------- | --------- |
| 正常Hackintosh | ⌃ Control | Fn        | ⌘ Command | ⌥ Option  | Space | ⌥ Option  | ⌃ Control |
| 我的Hackintosh | ⌥ Option  | Fn        | ⌘ Command | ⌃ Control | Space | ⌃ Control | ⌥ Option  |
| 修改后         | ⌥ Option  | Fn        | ⌃ Control | ⌘ Command | Space | ⌘ Command | ⌥ Option  |
| Windows        | Ctrl      | Fn        | ❖Windows  | Alt       | Space | Alt       | Ctrl      |
