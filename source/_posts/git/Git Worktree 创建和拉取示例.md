---
title: Git Worktree 创建和拉取示例
author: zvozve
comments: false
categories:
- git
tags:
- git
date: 2026-09-06 11:49:16
---

# 创建工作树
 
```shell

# 1. 创建 main 文件夹并进入
mkdir main
cd main
git init
git branch -m master main
echo "# 项目主分支" > README.md
git add README.md
git commit -m "初始化 main 分支"

# ============================================
# doc 分支
# ============================================
git checkout -b doc
git checkout main
git worktree add ../doc doc
cd ../doc
echo "# 文档目录" > README.md
git add README.md
git commit -m "doc: 初始化文档分支"
cd ../main

# ============================================
# mcu 分支
# ============================================
git checkout -b mcu
git checkout main
git worktree add ../mcu mcu
cd ../mcu
echo "# MCU 固件" > README.md
git add README.md
git commit -m "mcu: 初始化固件分支"
cd ../main

# ============================================
# hmi 分支
# ============================================
git checkout -b hmi
git checkout main
git worktree add ../hmi hmi
cd ../hmi
echo "# HMI 界面" > README.md
git add README.md
git commit -m "hmi: 初始化界面分支"
cd ../main

# ============================================
# 查看结果
# ============================================
git worktree list

```


# 拉取

```shell

# 1. 创建项目根目录并进入
mkdir project_name
cd project_name

# 2. 克隆仓库（指定克隆到 main 文件夹）
git clone http://<gitea-host>:<port>/<user>/<repo>.git main

# 3. 进入 main（Git 仓库）
cd main

# 4. 拉取所有远程分支
git fetch --all

# 5. 为每个分支创建 worktree（自动创建目录）
git worktree add ../doc doc
git worktree add ../hmi hmi
git worktree add ../mcu mcu

# 6. 查看结果
git worktree list

```

# 本地目录移动后

```shell
# 路径变更后修复 worktree 指向（示例占位路径）
git worktree repair \
  "<obsidian-vault>/<project>/doc" \
  "<obsidian-vault>/<project>/hmi"

# 多个 worktree 批量修复（示例）
git worktree repair \
  "<obsidian-vault>/<project>/doc" \
  "<obsidian-vault>/<project>/hmi" \
  "<obsidian-vault>/<project>/hmi_dev_dacai" \
  "<obsidian-vault>/<project>/mcu"

```
