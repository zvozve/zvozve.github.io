---
title: WSL 常用指令速查手册
author: zvozve
comments: false
categories:
- wsl
tags:
- wsl
date: 2026-09-04 16:21:53
---
# WSL 常用指令速查手册

---

## 一、基础管理

| 命令 | 用途 |
|---|---|
| `wsl` | 进入默认 WSL 系统 |
| `wsl -d <发行版名>` | 进入指定发行版 |
| `wsl -l -v` | 查看已安装的发行版及版本 |
| `wsl --list --online` | 查看可在线安装的发行版列表 |
| `wsl --set-default <发行版名>` | 设置默认发行版 |
| `wsl --shutdown` | 关闭所有 WSL 实例 |
| `wsl -t <发行版名>` | 关闭指定发行版 |
| `wsl --status` | 查看 WSL 状态 |

---

## 二、安装与卸载

| 命令 | 用途 |
|---|---|
| `wsl --install` | 一键安装 WSL（默认 Ubuntu） |
| `wsl --install -d <发行版名>` | 安装指定发行版 |
| `wsl --unregister <发行版名>` | 卸载指定发行版（⚠️ 数据全丢） |
| `wsl --export <发行版名> <路径>` | 导出发行版为 tar 文件 |
| `wsl --import <发行版名> <安装路径> <tar文件>` | 导入 tar 文件为发行版 |

---

## 三、版本管理

| 命令 | 用途 |
|---|---|
| `wsl --set-version <发行版名> 1/2` | 切换 WSL 版本（1/2） |
| `wsl --set-default-version 1/2` | 设置默认 WSL 版本 |
| `wsl --update` | 更新 WSL 内核 |

---

## 四、常用组合

```bash
# 查看当前所有发行版
wsl -l -v

# 安装 Ubuntu 22.04
wsl --install -d Ubuntu-22.04

# 设置 Ubuntu-22.04 为默认
wsl --set-default Ubuntu-22.04

# 迁移发行版到 D 盘（导出→注销→导入）
wsl --export Ubuntu D:\ubuntu.tar
wsl --unregister Ubuntu
wsl --import Ubuntu D:\WSL\Ubuntu D:\ubuntu.tar --version 2

# 完全重启 WSL（解决资源占用问题）
wsl --shutdown
wsl
```

---

## 五、WSL 配置文件

### `.wslconfig`（Windows 下，全局配置）

路径：`C:\Users\<用户名>\.wslconfig`

```ini
[wsl2]
memory=8GB
processors=4
swap=4GB
localhostForwarding=true
```

修改后执行 `wsl --shutdown` 重启生效。

### `wsl.conf`（WSL 内，发行版配置）

路径：`/etc/wsl.conf`

```ini
[boot]
systemd=true

[network]
generateHosts=true
generateResolvConf=true
```

---

## 六、文件系统互通

| 操作 | 方法 |
|---|---|
| Windows 访问 WSL 文件 | 资源管理器输入 `\\wsl$\Ubuntu\home\用户名` |
| WSL 访问 Windows 文件 | `/mnt/c/`（C盘）`/mnt/d/`（D盘） |
| 当前目录打开 Windows 资源管理器 | `explorer.exe .` |

---

## 七、常用问题排查

| 问题 | 解决方法 |
|---|---|
| WSL 启动慢 | `wsl --shutdown` 后重进 |
| 内存占用高 | 配置 `.wslconfig` 限制内存 |
| DNS 解析失败 | `/etc/resolv.conf` 配置 nameserver |
| 代理不通 | WSL2 NAT 模式需手动配置代理 |
| 跨系统文件读写慢 | 把项目文件放在 WSL 内部（`/home/...`） |

---

## 八、进入 WSL 后的常用 Linux 命令

```bash
# 系统信息
uname -a                # 查看内核版本
cat /etc/os-release     # 查看发行版版本
lsb_release -a          # 查看 Ubuntu 版本

# 用户管理
passwd                  # 修改当前用户密码
sudo passwd <用户名>     # 修改指定用户密码

# 包管理（Ubuntu/Debian）
sudo apt update && sudo apt upgrade -y  # 更新系统
sudo apt install <包名>                 # 安装软件
sudo apt remove <包名>                  # 卸载软件

# 查看资源
free -h                 # 查看内存
df -h                   # 查看磁盘
htop                    # 查看进程（需安装）

# 文件操作
pwd                     # 查看当前路径
ls -la                  # 列出文件（含隐藏）
cd ~                    # 回到家目录
mkdir -p <目录>         # 创建目录
cp -r <源> <目标>       # 复制（递归）
rm -rf <目录>           # 删除目录（⚠️ 慎用）
```
