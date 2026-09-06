---
title: 在VS Code中配置Python(Windows)
author: zvozve
comments: false
categories:
  - python
tags:
  - python
date: 2024-04-29 19:18:03
---
# 安装软件

> **VSCode**
> **Python**
# vscode中安装Python插件

# 将Python.exe和Scripts文件夹添加到环境变量

```shell
%LOCALAPPDATA%\Programs\Python\Python312\python.exe
%LOCALAPPDATA%\Programs\Python\Python312\Scripts
```
# 配置launch.json文件

```c
{
    // 使用 IntelliSense 了解相关属性。 
    // 悬停以查看现有属性的描述。
    // 欲了解更多信息，请访问: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python:Flask",
            "type": "python",
            "request": "launch",
            "module": "flask",
            "env":{
                "FLASK_APP": "app.py",
                "FLASK_ENV": "development",
                "FLASL_DEBUG": "0"
            },
            "args":[
                "run",
                "--no-debugger"
            ],  
            "jinja": true
        }
    ]
}
```