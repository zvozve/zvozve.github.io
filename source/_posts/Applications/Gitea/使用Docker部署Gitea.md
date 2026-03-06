---
title: 使用Docker部署Gitea
comments: false
categories:
  - Applications
  - Gitea
tags:
  - Gitea
  - Git
date: 2026-03-06 17:37:56
---

# 1.部署

在 Windows 上使用 Docker 部署 Gitea 到 `C:\Container\Library\Docker\Gitea`，以下是完整部署方案：

## 1. 准备工作

### 确保 Docker 运行
- 确认 Docker Desktop 已安装并运行
- 建议使用 WSL 2 后端以获得更好性能

## 2. 创建目录结构

```bash
# 在 PowerShell 或 CMD 中执行
mkdir C:\Container\Library\Docker\Gitea
cd C:\Container\Library\Docker\Gitea
mkdir data backups
```

### 最终目录结构：
```
C:\Container\Library\Docker\Gitea\
├── docker-compose.yml
├── data\          # Gitea 数据目录
└── backups\       # 备份目录
```

## 3. 创建 Docker Compose 文件

在 `C:\Container\Library\Docker\Gitea\docker-compose.yml`：

```yaml
version: "3.8"

services:
  gitea:
    image: gitea/gitea:latest
    container_name: gitea
    environment:
      - USER_UID=1000
      - USER_GID=1000
      - GITEA__database__DB_TYPE=sqlite3
    restart: unless-stopped
    volumes:
      - ./data:/data
      - /etc/timezone:/etc/timezone:ro
      - /etc/localtime:/etc/localtime:ro
    ports:
      - "3000:3000"
      - "222:22"
    networks:
      - gitea-network

networks:
  gitea-network:
    driver: bridge
```

## 4. 使用 MySQL 的增强版本（可选）

如果需要 MySQL，使用这个版本：

```yaml
version: "3.8"

services:
  gitea:
    image: gitea/gitea:latest
    container_name: gitea
    environment:
      - USER_UID=1000
      - USER_GID=1000
      - GITEA__database__DB_TYPE=mysql
      - GITEA__database__HOST=db:3306
      - GITEA__database__NAME=gitea
      - GITEA__database__USER=gitea
      - GITEA__database__PASSWD=gitea123
    restart: unless-stopped
    volumes:
      - ./data:/data
    ports:
      - "3000:3000"
      - "222:22"
    depends_on:
      - db
    networks:
      - gitea-network

  db:
    image: mysql:8.0
    container_name: gitea_db
    environment:
      - MYSQL_ROOT_PASSWORD=root123
      - MYSQL_USER=gitea
      - MYSQL_PASSWORD=gitea123
      - MYSQL_DATABASE=gitea
    restart: unless-stopped
    volumes:
      - ./mysql_data:/var/lib/mysql
    command:
      - --default-authentication-plugin=mysql_native_password
      - --character-set-server=utf8mb4
      - --collation-server=utf8mb4_unicode_ci
    networks:
      - gitea-network

networks:
  gitea-network:
    driver: bridge
```

## 5. 部署和启动

### 在 PowerShell 中执行：
```powershell
# 切换到目录
cd C:\Container\Library\Docker\Gitea

# 启动服务
docker-compose up -d

# 查看状态
docker-compose ps

# 查看日志
docker-compose logs -f gitea
```

## 6. Windows 特定的注意事项

### 路径权限问题
如果遇到权限问题，在 PowerShell 中运行：
```powershell
# 给 Docker 服务授权访问目录
icacls "C:\Container\Library\Docker\Gitea" /grant "Everyone:(OI)(CI)F"
```

### 防火墙设置
```powershell
# 开放端口（如果需要）
New-NetFirewallRule -DisplayName "Gitea Web" -Direction Inbound -Protocol TCP -LocalPort 3000 -Action Allow
New-NetFirewallRule -DisplayName "Gitea SSH" -Direction Inbound -Protocol TCP -LocalPort 222 -Action Allow
```

## 7. 初始访问和配置

1. **打开浏览器访问**：`http://localhost:3000`
2. **首次安装配置**：
   - 数据库类型：SQLite3（如果使用基础版本）
   - 站点标题：你的 Gitea 名称
   - 服务器域名：`localhost`（或你的本机 IP）
   - SSH 服务器端口：`222`
   - 创建管理员账户

## 8. 管理和维护脚本

### 创建备份脚本 `backup.ps1`：
```powershell
# C:\Container\Library\Docker\Gitea\backup.ps1
$BackupDir = "C:\Container\Library\Docker\Gitea\backups"
$DataDir = "C:\Container\Library\Docker\Gitea\data"
$Date = Get-Date -Format "yyyyMMdd_HHmmss"

# 停止服务
docker-compose down

# 创建备份
Compress-Archive -Path $DataDir -DestinationPath "$BackupDir\gitea-backup-$Date.zip"

# 启动服务
docker-compose up -d

# 删除7天前的备份
Get-ChildItem $BackupDir -Filter "gitea-backup-*.zip" | Where-Object { $_.LastWriteTime -lt (Get-Date).AddDays(-7) } | Remove-Item
```

### 创建启动脚本 `start.ps1`：
```powershell
# C:\Container\Library\Docker\Gitea\start.ps1
cd "C:\Container\Library\Docker\Gitea"
docker-compose up -d
Write-Host "Gitea 服务已启动，访问: http://localhost:3000"
```

### 创建停止脚本 `stop.ps1`：
```powershell
# C:\Container\Library\Docker\Gitea\stop.ps1
cd "C:\Container\Library\Docker\Gitea"
docker-compose down
Write-Host "Gitea 服务已停止"
```

## 9. 日常使用命令

```powershell
# 进入目录
cd C:\Container\Library\Docker\Gitea

# 启动服务
docker-compose up -d

# 停止服务
docker-compose down

# 查看日志
docker-compose logs gitea

# 进入容器
docker exec -it gitea bash

# 升级 Gitea
docker-compose pull
docker-compose up -d
```

## 10. 最终目录结构

```
C:\Container\Library\Docker\Gitea\
├── docker-compose.yml
├── backup.ps1
├── start.ps1
├── stop.ps1
├── data\                  # Gitea 数据
│   ├── gitea\
│   │   ├── conf\
│   │   ├── repositories\  # Git 仓库
│   │   └── log\
│   └── gitea.db          # SQLite 数据库
├── mysql_data\           # MySQL 数据（如果使用）
└── backups\              # 备份文件
```

这样部署后，你的所有 Gitea 相关文件都会整齐地组织在 `C:\Container\Library\Docker\Gitea` 目录下，便于管理和备份。

# 2.完全卸载已部署的 Gitea 的步骤

以下是完全卸载已部署的 Gitea 的步骤：

## 1. 停止并删除容器

### 进入项目目录：
```powershell
cd C:\Container\Library\Docker\Gitea
```

### 停止并删除容器：
```powershell
# 停止并删除容器、网络
docker-compose down

# 或者使用更彻底的删除
docker-compose down -v
```

## 2. 删除 Docker 镜像

### 查看现有镜像：
```powershell
docker images
```

### 删除 Gitea 相关镜像：
```powershell
# 删除 Gitea 镜像
docker rmi gitea/gitea:latest

# 如果使用了 MySQL，也删除它
docker rmi mysql:8.0

# 强制删除（如果有容器依赖）
docker rmi -f gitea/gitea:latest
```

## 3. 清理 Docker 资源

### 查看所有 Docker 资源：
```powershell
docker system df
```

### 清理未使用的资源：
```powershell
# 删除所有未使用的容器、网络、镜像
docker system prune

# 更彻底的清理（包括卷）
docker system prune -a --volumes
```

## 4. 删除项目文件

### 删除整个 Gitea 目录：
```powershell
# 删除整个目录（包括数据、配置、备份）
Remove-Item -Recurse -Force C:\Container\Library\Docker\Gitea
```

### 或者选择性保留备份：
```powershell
# 如果只想删除运行文件，保留数据备份
cd C:\Container\Library\Docker\Gitea

# 备份重要数据
Copy-Item -Recurse data backups\data-backup-$(Get-Date -Format "yyyyMMdd")

# 然后删除目录
Remove-Item -Recurse -Force C:\Container\Library\Docker\Gitea
```

## 5. 完整的卸载脚本

创建 `uninstall.ps1` 脚本：

```powershell
# C:\Container\Library\Docker\Gitea\uninstall.ps1
Write-Host "开始卸载 Gitea..." -ForegroundColor Yellow

# 1. 进入目录
Set-Location "C:\Container\Library\Docker\Gitea"

# 2. 停止并删除容器
Write-Host "停止并删除容器..." -ForegroundColor Cyan
docker-compose down -v

# 3. 删除镜像
Write-Host "删除 Docker 镜像..." -ForegroundColor Cyan
docker rmi gitea/gitea:latest -f 2>$null
docker rmi mysql:8.0 -f 2>$null

# 4. 清理 Docker 资源
Write-Host "清理 Docker 资源..." -ForegroundColor Cyan
docker system prune -f

# 5. 确认删除文件
$confirm = Read-Host "是否删除所有数据文件？(y/n)"
if ($confirm -eq 'y' -or $confirm -eq 'Y') {
    Write-Host "删除数据文件..." -ForegroundColor Red
    Remove-Item -Recurse -Force "C:\Container\Library\Docker\Gitea"
    Write-Host "Gitea 已完全卸载" -ForegroundColor Green
} else {
    Write-Host "数据文件保留在 C:\Container\Library\Docker\Gitea" -ForegroundColor Yellow
}

Write-Host "卸载完成！" -ForegroundColor Green
```

## 6. 验证卸载

### 检查是否完全清理：
```powershell
# 检查容器
docker ps -a | findstr "gitea"

# 检查镜像
docker images | findstr "gitea"

# 检查卷
docker volume ls | findstr "gitea"
```

所有命令都应该返回空结果。

## 7. 分阶段卸载选项

### 选项 A：完全卸载（推荐用于测试环境）
```powershell
# 一键完全卸载
cd C:\Container\Library\Docker\Gitea
docker-compose down -v
docker rmi gitea/gitea:latest -f
Remove-Item -Recurse -Force C:\Container\Library\Docker\Gitea
```

### 选项 B：保留数据（用于重新安装）
```powershell
# 只删除容器，保留数据
cd C:\Container\Library\Docker\Gitea
docker-compose down

# 数据保留在 C:\Container\Library\Docker\Gitea\data
# 以后可以重新运行 docker-compose up -d
```

### 选项 C：备份后卸载
```powershell
# 备份重要数据后卸载
cd C:\Container\Library\Docker\Gitea

# 备份数据
$BackupDir = "C:\Backups\Gitea-$(Get-Date -Format 'yyyyMMdd_HHmmss')"
New-Item -ItemType Directory -Path $BackupDir -Force
Copy-Item -Recurse data $BackupDir
Copy-Item docker-compose.yml $BackupDir

# 然后卸载
docker-compose down -v
Remove-Item -Recurse -Force C:\Container\Library\Docker\Gitea
```

## 8. 重新安装

如果需要重新安装，只需：
```powershell
# 重新创建目录
mkdir C:\Container\Library\Docker\Gitea
cd C:\Container\Library\Docker\Gitea

# 重新创建 docker-compose.yml
# 然后启动
docker-compose up -d
```

## 重要提醒

1. **备份重要数据**：卸载前确保已备份仓库数据
2. **确认卸载范围**：决定是否保留数据文件
3. **检查依赖**：确保没有其他服务依赖这些容器
4. **清理端口**：3000 和 222 端口会被释放

按照这些步骤，你可以完全清理 Gitea 的 Docker 部署。

# 3.迁移

迁移 Gitea 仓库分为几种情况，以下是详细的迁移方案：

## 📦 方案一：完整迁移（推荐）

### 1. 源服务器备份

**在旧服务器上执行：**
```bash
# 进入 Gitea 目录
cd /path/to/gitea

# 停止 Gitea 服务
docker-compose down

# 创建完整备份
tar -czf gitea-full-backup-$(date +%Y%m%d).tar.gz ./

# 或者只备份数据目录
tar -czf gitea-data-backup-$(date +%Y%m%d).tar.gz ./data/
```

### 2. 传输备份文件

**方法一：SCP 传输**
```bash
# 从旧服务器传到新服务器
scp gitea-full-backup-$(date +%Y%m%d).tar.gz user@new-server:/tmp/
```

**方法二：Rsync（如果网络好）**
```bash
rsync -avz ./data/ user@new-server:/tmp/gitea-data/
```

**方法三：手动下载上传**
如果服务器间无法直连，先下载到本地再上传。

### 3. 新服务器恢复

**在新服务器上执行：**
```bash
# 创建目录
mkdir -p /opt/gitea
cd /opt/gitea

# 解压备份文件
tar -xzf /tmp/gitea-full-backup-$(date +%Y%m%d).tar.gz

# 修改权限
chown -R 1000:1000 ./data

# 启动服务
docker-compose up -d
```

## 🔄 方案二：使用 Gitea 内置备份

### 1. 源服务器备份

```bash
# 进入容器
docker exec -it gitea bash

# 在容器内执行备份
gitea dump -c /data/gitea/conf/app.ini --file /tmp/gitea-dump.zip

# 或者直接执行
docker exec gitea gitea dump -c /data/gitea/conf/app.ini

# 将备份文件复制到主机
docker cp gitea:/data/gitea/dump.zip ./gitea-dump.zip
```

### 2. 新服务器部署

```bash
# 1. 在新服务器部署全新的 Gitea
mkdir -p /opt/gitea
cd /opt/gitea

# 创建 docker-compose.yml（与源服务器相同配置）
cat > docker-compose.yml << EOF
version: "3"
services:
  gitea:
    image: gitea/gitea:latest
    container_name: gitea
    environment:
      - USER_UID=1000
      - USER_GID=1000
    volumes:
      - ./data:/data
    ports:
      - "3000:3000"
      - "222:22"
    restart: unless-stopped
EOF

# 2. 启动空白的 Gitea
docker-compose up -d

# 等待启动完成后停止
docker-compose down
```

### 3. 恢复备份

```bash
# 复制备份文件到数据目录
cp gitea-dump.zip ./data/

# 进入容器恢复
docker run --rm -v /opt/gitea/data:/data gitea/gitea:latest gitea restore --config /data/gitea/conf/app.ini --temp-dir /tmp --from /data/gitea-dump.zip

# 修改权限
chown -R 1000:1000 ./data

# 启动服务
docker-compose up -d
```

## 🗂️ 方案三：仅迁移仓库数据

### 1. 备份仓库数据

```bash
# 只备份仓库目录
tar -czf gitea-repos-backup.tar.gz ./data/gitea/repositories/

# 备份数据库
cp ./data/gitea.db ./gitea.db.backup
```

### 2. 新服务器部署

```bash
# 新服务器部署全新 Gitea
mkdir -p /opt/gitea
cd /opt/gitea

# 创建 docker-compose.yml
# 启动服务完成初始配置
docker-compose up -d

# 访问 http://新服务器IP:3000 完成初始设置
# 然后停止服务
docker-compose down
```

### 3. 恢复数据

```bash
# 解压仓库数据
tar -xzf gitea-repos-backup.tar.gz -C ./data/

# 复制数据库（如果使用 SQLite）
cp gitea.db.backup ./data/gitea.db

# 修改权限
chown -R 1000:1000 ./data

# 启动服务
docker-compose up -d
```

## 🌐 方案四：Windows 到 Linux 迁移

### 1. Windows 备份

```powershell
# 在 Windows PowerShell 中
cd C:\Container\Library\Docker\Gitea

# 停止服务
docker-compose down

# 备份数据
Compress-Archive -Path .\data -DestinationPath .\backups\gitea-windows-backup.zip
```

### 2. Linux 恢复

```bash
# 在 Linux 服务器上
mkdir -p /opt/gitea
cd /opt/gitea

# 解压 Windows 备份（可能需要安装 unzip）
unzip gitea-windows-backup.zip -d ./

# 修复权限
chown -R 1000:1000 ./data
find ./data -type d -exec chmod 755 {} \;
find ./data -type f -exec chmod 644 {} \;

# 部署并启动
# 创建 docker-compose.yml
docker-compose up -d
```

## ⚙️ 迁移后的配置调整

### 修改应用配置
```bash
# 编辑 app.ini 更新域名和路径
docker exec -it gitea cat /data/gitea/conf/app.ini

# 或者直接修改主机上的文件
vi ./data/gitea/conf/app.ini
```

**需要修改的配置项：**
```ini
[server]
DOMAIN = 新服务器IP或域名
SSH_DOMAIN = 新服务器IP或域名
ROOT_URL = http://新服务器IP或域名:3000/

[database]
# 如果数据库路径变化需要调整
PATH = /data/gitea/gitea.db
```

### 验证迁移
```bash
# 检查服务状态
docker-compose ps

# 查看日志
docker-compose logs gitea

# 测试访问
curl http://localhost:3000
```

## 🚨 注意事项

1. **版本一致性**：确保新旧服务器 Gitea 版本相同
2. **权限问题**：Linux 上注意文件权限，特别是 1000:1000
3. **数据库类型**：如果更换数据库类型需要额外步骤
4. **域名更新**：更新所有仓库中的远程 URL
5. **定时任务**：如果有备份定时任务需要重新配置

## 📋 迁移检查清单

- [ ] 停止源服务器 Gitea 服务
- [ ] 创建完整备份
- [ ] 传输备份到新服务器
- [ ] 新服务器部署相同版本的 Gitea
- [ ] 恢复备份数据
- [ ] 更新配置文件中的域名/IP
- [ ] 启动新服务器服务
- [ ] 测试所有功能正常
- [ ] 更新 DNS 或客户端配置

**推荐使用方案一（完整迁移）**，最简单可靠，几乎不会出错。