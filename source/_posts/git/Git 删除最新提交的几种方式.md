---
title: Git 删除最新提交的几种方式
author: zvozve
comments: false
categories:
- git
tags:
- git
date: 2026-09-06 11:49:40
---

根据你的需求，选择合适的方式：

---

## 1. `git reset` — 撤销提交（推荐）

### 保留修改内容（soft）

```bash
# 撤销提交，但保留所有修改在暂存区
git reset --soft HEAD~1
```

### 保留修改但不暂存（mixed，默认）

```bash
# 撤销提交，修改保留在工作区（未暂存）
git reset HEAD~1
# 或
git reset --mixed HEAD~1
```

### 完全删除（hard）

```bash
# ⚠️ 危险！彻底删除提交和所有修改
git reset --hard HEAD~1
```

---

## 2. `git revert` — 安全撤销（保留历史）

```bash
# 创建一个新提交来撤销最新提交
git revert HEAD

# 撤销指定提交
git revert <commit-hash>
```

**特点：** 保留原始提交历史，适合团队协作。

---

## 3. 各种方式对比

| 方式 | 提交历史 | 修改内容 | 适用场景 |
|------|---------|---------|---------|
| `reset --soft HEAD~1` | ❌ 删除 | ✅ 保留（暂存区） | 想重新提交 |
| `reset --mixed HEAD~1` | ❌ 删除 | ✅ 保留（工作区） | 想修改后再提交 |
| `reset --hard HEAD~1` | ❌ 删除 | ❌ 彻底删除 | 完全不想要了 |
| `revert HEAD` | ✅ 保留（新增撤销提交） | ✅ 保留 | 团队协作，安全撤销 |

---

## 4. 根据你的场景

你在各个 worktree 中有独立的提交，比如：

```bash
cd ../doc
echo "# 文档目录" > README.md
git add README.md
git commit -m "doc: 初始化文档分支"
```

### 想撤销 doc 的最新提交

```bash
cd ../doc

# 方式一：保留修改，重新编辑
git reset --soft HEAD~1
# 修改文件后重新提交
git add .
git commit -m "doc: 修正文档内容"

# 方式二：完全删除提交和修改
git reset --hard HEAD~1

# 方式三：安全撤销（推荐用于已推送的提交）
git revert HEAD
```

---

## 5. 已推送到远程的提交

**千万不要用 `reset`！** 用 `revert`：

```bash
# 创建一个撤销提交
git revert HEAD
git push origin doc
```

---

## 6. 快速参考

| 你想做什么 | 命令 |
|-----------|------|
| 撤销最新提交，保留修改 | `git reset --soft HEAD~1` |
| 撤销最新提交，修改放工作区 | `git reset HEAD~1` |
| 彻底删除最新提交 | `git reset --hard HEAD~1` |
| 安全撤销（保留历史） | `git revert HEAD` |
| 撤销最近 N 个提交 | `git reset --hard HEAD~N` |
| 撤销到指定提交 | `git reset --hard <commit-hash>` |

---

## 警告 ⚠️

- `git reset --hard` 会**永久丢失**未提交的修改
- 已推送的提交用 `revert`，不要用 `reset`
- 不确定时先用 `git log` 查看提交历史

```bash
# 查看提交历史
git log --oneline

# 查看最新提交的修改
git show HEAD
```
