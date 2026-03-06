---
title: Windows x64 手动安装 Gitea 教程
comments: false
categories:
  - Applications
  - Gitea
tags:
  - Gitea
  - Git
date: 2026-03-06 17:37:56
---


## 📋 系统要求
- Windows 7/8/10/11 或 Windows Server 2012+
- 64位操作系统
- 建议 2GB+ 内存
- 1GB+ 可用磁盘空间

## 📥 下载 Gitea

### 方法 1：从官网下载
1. 访问 [Gitea 下载页面](https://dl.gitea.io/gitea/)
2. 选择最新版本
3. 下载 `gitea-[version]-windows-amd64.exe`

### 方法 2：使用 PowerShell 下载
```powershell
# 创建安装目录
mkdir C:\Gitea
cd C:\Gitea

# 下载最新稳定版
$url = "https://dl.gitea.io/gitea/latest/gitea-latest-windows-amd64.exe"
Invoke-WebRequest -Uri $url -OutFile "gitea.exe"
```

## 🔧 安装步骤

### 步骤 1：准备目录结构
```powershell
# 以管理员身份打开 PowerShell
# 创建必要目录
mkdir C:\Gitea
mkdir C:\Gitea\data
mkdir C:\Gitea\custom
mkdir C:\Gitea\log
mkdir C:\Gitea\repositories
```

### 步骤 2：创建配置文件 `C:\Gitea\custom\conf\app.ini`
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
ROOT = C:/Gitea/repositories

[log]
ROOT_PATH = C:/Gitea/log
MODE      = console
LEVEL     = Info

[session]
PROVIDER = file
PROVIDER_CONFIG = C:/Gitea/data/sessions

[picture]
AVATAR_UPLOAD_PATH = C:/Gitea/data/avatars
```

### 步骤 3：安装为 Windows 服务（推荐）
```powershell
# 安装 Windows 服务
.\gitea.exe install --config C:\Gitea\custom\conf\app.ini

# 设置服务描述
sc.exe description gitea "Gitea - Git with a cup of tea"

# 设置服务启动类型
sc.exe config gitea start= auto

# 启动服务
net start gitea

# 或使用 PowerShell
Start-Service gitea
```

### 步骤 4：使用 NSSM（替代方案，更稳定）
如果内置服务安装有问题，使用 NSSM：

```powershell
# 下载 NSSM
$nssmUrl = "https://nssm.cc/release/nssm-2.24.zip"
Invoke-WebRequest -Uri $nssmUrl -OutFile "nssm.zip"
Expand-Archive -Path "nssm.zip" -DestinationPath "."

# 安装服务（使用 x64 版本）
.\nssm-2.24\win64\nssm.exe install Gitea "C:\Gitea\gitea.exe"
# 在弹窗中设置参数：
# Path: C:\Gitea\gitea.exe
# Startup directory: C:\Gitea
# Arguments: web --config C:\Gitea\custom\conf\app.ini

# 启动服务
Start-Service Gitea
```

## 🗄️ 配置数据库（可选）

### 使用 SQLite（默认，适合小规模）
无需额外配置，已在上面的 app.ini 中设置。

### 使用 MySQL
```ini
[database]
DB_TYPE  = mysql
HOST     = 127.0.0.1:3306
NAME     = gitea
USER     = gitea
PASSWD   = your_password
```

### 使用 PostgreSQL
```ini
[database]
DB_TYPE  = postgres
HOST     = 127.0.0.1:5432
NAME     = gitea
USER     = gitea
PASSWD   = your_password
```

## 🔧 首次运行配置

1. **访问 Gitea**：
   - 打开浏览器访问 `http://localhost:3000`
   - 如果是远程访问，使用 `http://服务器IP:3000`

2. **初始设置**：
   - 数据库设置（如果使用内置 SQLite 则已自动配置）
   - 管理员账户设置
   - 服务器域名和基础 URL
   - 邮件服务器配置（可选）

3. **保存配置**：
   - 点击 "立即安装"
   - 系统会自动重启并应用配置

## ⚙️ 高级配置

### 修改端口（如果需要）
编辑 `app.ini`：
```ini
[server]
HTTP_PORT = 8080
ROOT_URL = http://your-domain:8080/
```

### 启用 SSH 支持
```powershell
# 生成 SSH 密钥（如果没有）
ssh-keygen -t rsa -b 4096 -C "gitea@localhost"

# 配置 SSH
[server]
START_SSH_SERVER = true
SSH_PORT         = 22
SSH_LISTEN_PORT  = 22
```

### 使用反向代理（IIS）
```xml
<!-- web.config 文件 -->
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

### 使用反向代理（Nginx）
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

## 🔄 维护命令

```powershell
# 服务管理
net stop gitea      # 停止服务
net start gitea     # 启动服务
sc query gitea      # 检查服务状态

# 手动运行（调试）
cd C:\Gitea
.\gitea.exe web --config custom\conf\app.ini

# 备份
.\gitea.exe dump -c custom\conf\app.ini -o backup.zip

# 恢复
.\gitea.exe restore --from backup.zip
```

## 📁 目录结构说明
```
C:\Gitea\
├── gitea.exe              # 主程序
├── custom\
│   └── conf\
│       └── app.ini       # 配置文件
├── data\                  # 数据库和上传文件
├── log\                   # 日志文件
├── repositories\          # Git 仓库
└── public\                # 静态资源
```

## 🚨 常见问题解决

### 1. 端口被占用
```powershell
# 查看占用端口的进程
netstat -ano | findstr :3000

# 终止进程（如果需要）
taskkill /PID [PID] /F
```

### 2. 权限问题
```powershell
# 给 Gitea 目录设置权限
icacls "C:\Gitea" /grant "SYSTEM:(OI)(CI)F" /T
icacls "C:\Gitea" /grant "Users:(OI)(CI)RX" /T
```

### 3. 防火墙设置
```powershell
# 开放端口
New-NetFirewallRule -DisplayName "Gitea HTTP" -Direction Inbound -Protocol TCP -LocalPort 3000 -Action Allow
New-NetFirewallRule -DisplayName "Gitea SSH" -Direction Inbound -Protocol TCP -LocalPort 22 -Action Allow
```

### 4. 服务启动失败
检查日志：`C:\Gitea\log\gitea.log`

## 🔄 更新 Gitea
```powershell
# 1. 停止服务
net stop gitea

# 2. 备份当前版本
copy gitea.exe gitea.exe.backup

# 3. 下载新版本
$url = "https://dl.gitea.io/gitea/latest/gitea-latest-windows-amd64.exe"
Invoke-WebRequest -Uri $url -OutFile "gitea.exe"

# 4. 启动服务
net start gitea
```

## 📚 更多资源
- [Gitea 官方文档](https://docs.gitea.io/)
- [Windows 服务配置指南](https://docs.gitea.io/en-us/windows-service/)
- [配置示例](https://github.com/go-gitea/gitea/tree/main/custom/conf)

安装完成后，你可以通过浏览器访问 `http://localhost:3000` 来使用 Gitea！