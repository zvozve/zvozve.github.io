---
title: STM32_UTF-8文件编码
author: zvozve
comments: false
categories:
- stm32
tags:
- stm32
date: 2026-09-06 13:37:34
---

# 1. 在Keil中默认使用UTF-8编码显示内容

1. 编辑，配置
2. 编码格式选择UTF-8
3. 顺便统一TAB为4个空格

![|325](https://raw.githubusercontent.com/zvozve/image-bed/main/pic/99A7080471D05F5ED3A3AB9E078E3740.png)

![](https://raw.githubusercontent.com/zvozve/image-bed/main/pic/36A6382A883DD11D00A40974FA037834.png)


# 2. Keil中转换GB2312为UTF-8工具

#### 0. 环境依赖：

1. 需要安装 python 环境，
2. 并且为 python 安装 charset_normalizer

```cmd
pip install chardet
```

#### 1. 准备脚本文件并拷贝到指定目录


文件名： translate_to_utf8.py
放置路径：X: ...\Keil_v5\UV4\customize_tools\translate_to_utf8.py
内容如下：
```py
# translate_to_utf8.py

# -*- coding: UTF-8 -*-
# 强行将 GBK 转换为 UTF-8 的安全脚本（不进行不靠谱的自动检测）
import sys
import os

if len(sys.argv) > 1:
    file_path = sys.argv[1]
    
    # 1. 尝试以 GBK 模式读取
    try:
        with open(file_path, 'r', encoding='gbk') as f:
            content = f.read()
    except UnicodeDecodeError:
        # 如果用 GBK 读都报错，说明它本来就已经是 UTF-8 或者其他编码了，直接退出不破坏文件
        print("File is not GBK encoding. Advanced skip.")
        sys.exit(0)
        
    # 2. 安全写入备份，成功后再替换
    bak_path = file_path + ".tmp"
    try:
        with open(bak_path, 'w', encoding='utf-8') as f:
            f.write(content)
        os.replace(bak_path, file_path)
        print("Successfully converted from GBK to UTF-8.")
    except Exception as e:
        if os.path.exists(bak_path):
            os.remove(bak_path)
        print(f"Error during save: {e}")
```


#### 2. 自定义外部工具

打开 keil(MDK) ,选择 Tools->Customize Tools Menu，自定义外部工具菜单

![261](https://raw.githubusercontent.com/zvozve/image-bed/main/pic/AE2BBDB2A8804561A6852A310E6677E7.png)

点击新建按钮，

输入插件工具名称：
Convert2UTF-8，

![411](https://raw.githubusercontent.com/zvozve/image-bed/main/pic/C9F61A9A47B79683148EDDDC9D374724.png)

Command指令
```cmd
py D:\Keil_v5\UV4\customize_tools\translate_to_utf8.py
```

  Argument选项：要转换的文件,#E代表当前编辑文件

```cmd
#E
```

#### 3. 定义一个快捷键来执行代码的快速格式化

点击工具栏最右边的配置图标，
切换到 Shortcut Keys 选项，
选择 Tools:Convert2UTF-8，
点击 Create Shortcut 创建新的快捷键(此处以 CTRL+U 为例)，
在弹出的窗口按下你要设置的快捷键，然后保存退出就可以了，
下次需要使用的时候，只要按下相对应的快捷键，就可以一键将当前文件编码格式转换为 UTF-8。

![](https://raw.githubusercontent.com/zvozve/image-bed/main/pic/E7F2CE4D4FDCC1C0805C7E1FB0AC5E73.png)

# 3. 使用CubeMX生成代码默认UFT-8格式

添加环境变量

```cpp
// 变量名
JAVA_TOOL_OPTIONS
// 内容
-Dfile.encoding=UTF-8
```

![458](https://raw.githubusercontent.com/zvozve/image-bed/main/pic/CAB6A2871BDE88ED52B9F9AD2475C98F.png)


![401](https://raw.githubusercontent.com/zvozve/image-bed/main/pic/6935F63F5B2F63BBC83C00D8E71442AA.png)
