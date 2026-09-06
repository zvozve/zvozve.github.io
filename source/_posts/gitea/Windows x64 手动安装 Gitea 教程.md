---
title: Windows x64 手动安装 Gitea 教程
author: zvozve
comments: false
categories:
- gitea
tags:
- gitea
date: 2026-03-06 17:37:56
---


## 📋 系统要求

- Windows 7/8/10/11 或 Windows Server 2012+
- 64 位操作系统
- 建议 2GB+ 内存
- 1GB+ 可用磁盘空间

## 📥 下载 Gitea

### 从官网下载

1. 访问 [Gitea 下载页](https://dl.gitea.io/gitea/)
2. 选择最新版本
3. 下载 `gitea-[version]-windows-amd64.exe`

### 使用 PowerShell 下载

```powershell
# 创建安装目录
mkdir C:\Gitea
cd C:\Gitea

# 下载最新稳定版
$url = "https://dl.gitea.io/gitea/latest/gitea-latest-windows-amd64.exe"
Invoke-WebRequest -Uri $url -OutFile "gitea.exe"
```

## 🔧 安装步骤

约定：

- **安装目录**：`C:\Gitea`（放 `gitea.exe`）
- **数据目录**：`C:\Gitea\data`（数据库、仓库、日志等）

### 步骤 1：准备目录结构

以管理员身份打开 PowerShell：

```powershell
# 创建安装目录
mkdir C:\Gitea -Force

# 创建数据目录结构
mkdir C:\Gitea\data\custom\conf
mkdir C:\Gitea\data\repositories
mkdir C:\Gitea\data\log
mkdir C:\Gitea\data\data
```

### 步骤 2：创建配置文件 `C:\Gitea\data\custom\conf\app.ini`

```ini
APP_NAME = Gitea
RUN_USER = SYSTEM
RUN_MODE = prod

[server]
HTTP_PORT     = 3000
ROOT_URL      = http://localhost:3000/
DISABLE_SSH   = false
SSH_PORT      = 22
OFFLINE_MODE  = false

[database]
DB_TYPE  = sqlite3
PATH     = C:/Gitea/data/gitea.db

[repository]
ROOT = C:/Gitea/data/repositories

[log]
ROOT_PATH = C:/Gitea/data/log
MODE      = console
LEVEL     = Info

[session]
PROVIDER        = file
PROVIDER_CONFIG = C:/Gitea/data/sessions

[picture]
AVATAR_UPLOAD_PATH = C:/Gitea/data/avatars
```

### 步骤 3：安装为 Windows 服务

```powershell
# 进入安装目录
cd C:\Gitea

# 安装 Windows 服务
.\gitea.exe install --config C:\Gitea\data\custom\conf\app.ini

# 设置服务描述
sc.exe description gitea "Gitea - Git with a cup of tea"

# 设置服务启动类型为自动
sc.exe config gitea start= auto

# 启动服务
net start gitea
```

### 步骤 4：使用 NSSM（备选方案，如果服务安装有问题）

```powershell
# 进入安装目录
cd C:\Gitea

# 下载 NSSM
$nssmUrl = "https://nssm.cc/release/nssm-2.24.zip"
Invoke-WebRequest -Uri $nssmUrl -OutFile "nssm.zip"
Expand-Archive -Path "nssm.zip" -DestinationPath "."

# 安装服务（使用 x64 版本）
.\nssm-2.24\win64\nssm.exe install Gitea "C:\Gitea\gitea.exe"

# NSSM 弹窗中填：
#   Path: C:\Gitea\gitea.exe
#   Startup directory: C:\Gitea
#   Arguments: web --config C:\Gitea\data\custom\conf\app.ini

# 启动服务
Start-Service Gitea
```

### 最终目录结构

```
C:\Gitea\
├── gitea.exe              # 主程序
├── nssm-2.24\             # (可选) NSSM 工具
└── data\
    ├── custom\conf\app.ini
    ├── data\
    │   ├── gitea.db       # SQLite 数据库
    │   ├── sessions\
    │   └── avatars\
    ├── log\               # 日志
    └── repositories\      # Git 仓库
```

## 🗄️ 切换数据库（可选）

### MySQL

```ini
[database]
DB_TYPE  = mysql
HOST     = 127.0.0.1:3306
NAME     = gitea
USER     = gitea
PASSWD   = your_password
```

### PostgreSQL

```ini
[database]
DB_TYPE  = postgres
HOST     = 127.0.0.1:5432
NAME     = gitea
USER     = gitea
PASSWD   = your_password
```

## 🔧 首次运行配置

1. 浏览器访问 `http://localhost:3000`
2. 按向导完成数据库、管理员账户、域名、基础 URL、邮件服务器等配置
3. 点击「立即安装」，Gitea 自动重启并应用配置

## ⚙️ 高级配置

### 修改端口

编辑 `app.ini`：

```ini
[server]
HTTP_PORT = 8080
ROOT_URL = http://your-domain:8080/
```

### 启用 SSH

```powershell
# 生成 SSH 密钥（如果没有）
ssh-keygen -t rsa -b 4096 -C "gitea@localhost"
```

```ini
[server]
START_SSH_SERVER = true
SSH_PORT         = 22
SSH_LISTEN_PORT  = 22
```

### 反向代理（Nginx）

```nginx
server {
    listen 80;
    server_name git.example.com;

    location / {
        proxy_pass http://localhost:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### 反向代理（IIS）

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <system.webServer>
        <rewrite>
            <rules>
                <rule name="ReverseProxyInboundRule1" stopProcessing="true">
                    <match url="(.*)" />
                    <action type="Rewrite" url="http://localhost:3000/{R:1}" />
                </rule>
            </rules>
        </rewrite>
    </system.webServer>
</configuration>
```

## 🔄 维护命令

```powershell
# 服务管理
net stop gitea               # 停止
net start gitea              # 启动
sc query gitea               # 状态

# 手动运行（调试）
cd C:\Gitea
.\gitea.exe web --config data\custom\conf\app.ini

# 查看日志
Get-Content C:\Gitea\data\log\gitea.log -Tail 30
# 持续监控（类似 tail -f）
Get-Content C:\Gitea\data\log\gitea.log -Wait

# 备份 / 恢复
.\gitea.exe dump   -c data\custom\conf\app.ini -o backup.zip
.\gitea.exe restore --from backup.zip
```

## 🚨 常见问题

### 端口被占用

```powershell
netstat -ano | findstr :3000
taskkill /PID <PID> /F
```

### 权限问题

```powershell
icacls "C:\Gitea"      /grant "SYSTEM:(OI)(CI)F"   /T
icacls "C:\Gitea"      /grant "Users:(OI)(CI)RX"   /T
icacls "C:\Gitea\data" /grant "SYSTEM:(OI)(CI)F"   /T
```

### 防火墙

```powershell
# 放行 HTTP
New-NetFirewallRule -DisplayName "Gitea HTTP" -Direction Inbound -Protocol TCP -LocalPort 3000 -Action Allow
# 放行 SSH
New-NetFirewallRule -DisplayName "Gitea SSH"  -Direction Inbound -Protocol TCP -LocalPort 22   -Action Allow
```

## 🔄 更新 Gitea

```powershell
net stop gitea
copy gitea.exe gitea.exe.backup

$url = "https://dl.gitea.io/gitea/latest/gitea-latest-windows-amd64.exe"
Invoke-WebRequest -Uri $url -OutFile "gitea.exe"

net start gitea
```

## 📚 参考

- [Gitea 官方文档](https://docs.gitea.io/)
- [Windows 服务配置指南](https://docs.gitea.io/en-us/windows-service/)
- [配置示例](https://github.com/go-gitea/gitea/tree/main/custom/conf)