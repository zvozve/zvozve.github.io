---
title: Obsidian插件-使用VSCode打开
author: zvozve
comments: false
categories:
- obsidian
tags:
- obsidian
date: 2026-09-06 13:29:37
---

在插件设置中，将 **"Template for executing the 'code' command"** 修改为：

```text
code "{{vaultpath}}/{{filepath}}"
```
