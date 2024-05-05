---
title: TroubleShooting
auther: zvozve
comments: false
categories:
  - Language
  - C
tags:
  - C
date: 2024-04-29 19:05:00
---
# Windows下编译报错解决方案

## 错误代码

```shell
undefined reference to` std::ios_base::Init::~Init()
```
## 出现场景

CMD
```shell
gcc bye.cpp -o bye.exe
```
## 解决方案

CMD
```C
gcc bye.cpp -lstdc++
```
