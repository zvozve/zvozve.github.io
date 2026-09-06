---
title: 使用Docker部署Gitea
author: zvozve
comments: false
categories:
- gitea
tags:
- gitea
date: 2026-03-06 17:37:56
---


## 1. 部署

约定 **项目根目录**：`C:\Gitea`（放 `docker-compose.yml` 与数据卷）。

### 1.1 准备工作

- 确认 Docker Desktop 已安装并运行
- 建议启用 WSL 2 后端

### 1.2 创建目录

```powershell
mkdir C:\Gitea
cd C:\Gitea
mkdir data backups
```

### 1.3 docker-compose.yml（基础版，SQLite）

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

### 1.4 docker-compose.yml（MySQL 增强版，可选）

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

### 1.5 启动

```powershell
cd C:\Gitea
docker-compose up -d
docker-compose ps
docker-compose logs -f gitea
```

### 1.6 Windows 注意事项

**路径权限**

```powershell
icacls "C:\Gitea" /grant "Everyone:(OI)(CI)F"
```

**防火墙**

```powershell
New-NetFirewallRule -DisplayName "Gitea Web" -Direction Inbound -Protocol TCP -LocalPort 3000 -Action Allow
New-NetFirewallRule -DisplayName "Gitea SSH" -Direction Inbound -Protocol TCP -LocalPort 222  -Action Allow
```

### 1.7 首次访问

浏览器打开 `http://localhost:3000`，按向导完成数据库、站点标题、域名、SSH 端口（`222`）、管理员账户配置。

### 1.8 维护脚本

`backup.ps1`：

```powershell
$BackupDir = "C:\Gitea\backups"
$DataDir   = "C:\Gitea\data"
$Date      = Get-Date -Format "yyyyMMdd_HHmmss"

docker-compose down
Compress-Archive -Path $DataDir -DestinationPath "$BackupDir\gitea-backup-$Date.zip"
docker-compose up -d

# 仅保留最近 7 天
Get-ChildItem $BackupDir -Filter "gitea-backup-*.zip" |
    Where-Object { $_.LastWriteTime -lt (Get-Date).AddDays(-7) } |
    Remove-Item
```

`start.ps1`：

```powershell
cd "C:\Gitea"
docker-compose up -d
Write-Host "Gitea 服务已启动: http://localhost:3000"
```

`stop.ps1`：

```powershell
cd "C:\Gitea"
docker-compose down
Write-Host "Gitea 服务已停止"
```

### 1.9 日常命令

```powershell
cd C:\Gitea

docker-compose up -d          # 启动
docker-compose down           # 停止
docker-compose logs gitea     # 日志
docker exec -it gitea bash    # 进容器

# 升级
docker-compose pull
docker-compose up -d
```

---

## 2. 完全卸载

### 2.1 停止并删除容器

```powershell
cd C:\Gitea
docker-compose down -v        # -v 同步删除卷
```

### 2.2 删除镜像

```powershell
docker images
docker rmi gitea/gitea:latest
docker rmi mysql:8.0
docker rmi -f gitea/gitea:latest   # 强制
```

### 2.3 清理 Docker 资源

```powershell
docker system df
docker system prune
docker system prune -a --volumes   # 含卷的彻底清理
```

### 2.4 删除项目文件

彻底删除（含数据、配置、备份）：

```powershell
Remove-Item -Recurse -Force C:\Gitea
```

保留备份再删除：

```powershell
cd C:\Gitea
Copy-Item -Recurse data backups\data-backup-$(Get-Date -Format "yyyyMMdd")
Remove-Item -Recurse -Force C:\Gitea
```

### 2.5 一键卸载脚本 `uninstall.ps1`

```powershell
Write-Host "开始卸载 Gitea..." -ForegroundColor Yellow
Set-Location "C:\Gitea"

Write-Host "停止并删除容器..." -ForegroundColor Cyan
docker-compose down -v

Write-Host "删除镜像..." -ForegroundColor Cyan
docker rmi gitea/gitea:latest -f 2>$null
docker rmi mysql:8.0         -f 2>$null

Write-Host "清理 Docker 资源..." -ForegroundColor Cyan
docker system prune -f

$confirm = Read-Host "是否删除所有数据文件？(y/n)"
if ($confirm -eq 'y' -or $confirm -eq 'Y') {
    Write-Host "删除数据文件..." -ForegroundColor Red
    Remove-Item -Recurse -Force "C:\Gitea"
    Write-Host "Gitea 已完全卸载" -ForegroundColor Green
} else {
    Write-Host "数据文件保留在 C:\Gitea" -ForegroundColor Yellow
}
Write-Host "卸载完成！" -ForegroundColor Green
```

### 2.6 验证卸载

```powershell
docker ps -a   | findstr "gitea"
docker images  | findstr "gitea"
docker volume ls | findstr "gitea"
```

以上命令应全部无输出。

### 2.7 分阶段卸载

**完全卸载（测试环境推荐）**

```powershell
cd C:\Gitea
docker-compose down -v
docker rmi gitea/gitea:latest -f
Remove-Item -Recurse -Force C:\Gitea
```

**保留数据（便于重装）**

```powershell
cd C:\Gitea
docker-compose down
# 数据保留在 C:\Gitea\data，重装只需 docker-compose up -d
```

**备份后卸载**

```powershell
$BackupDir = "C:\Backups\Gitea-$(Get-Date -Format 'yyyyMMdd_HHmmss')"
New-Item -ItemType Directory -Path $BackupDir -Force
Copy-Item -Recurse C:\Gitea\data           $BackupDir
Copy-Item           C:\Gitea\docker-compose.yml $BackupDir

docker-compose down -v
Remove-Item -Recurse -Force C:\Gitea
```

---

## 3. 迁移

> 四种方案由浅入深，推荐 **方案一**。

### 方案一：完整迁移（推荐）

源服务器：

```bash
cd /path/to/gitea
docker-compose down
tar -czf gitea-full-backup-$(date +%Y%m%d).tar.gz ./
# 仅备份数据目录也行
tar -czf gitea-data-backup-$(date +%Y%m%d).tar.gz ./data/
```

传输到新服务器（任选其一）：

```bash
# SCP
scp gitea-full-backup-$(date +%Y%m%d).tar.gz user@new-server:/tmp/

# Rsync（带宽允许时）
rsync -avz ./data/ user@new-server:/tmp/gitea-data/
```

新服务器：

```bash
mkdir -p /opt/gitea
cd /opt/gitea
tar -xzf /tmp/gitea-full-backup-$(date +%Y%m%d).tar.gz
chown -R 1000:1000 ./data
docker-compose up -d
```

### 方案二：内置 `dump` / `restore`

源服务器：

```bash
docker exec -it gitea bash
gitea dump -c /data/gitea/conf/app.ini --file /tmp/gitea-dump.zip
exit

# 或一步完成
docker exec gitea gitea dump -c /data/gitea/conf/app.ini

# 把备份复制到主机
docker cp gitea:/data/gitea/dump.zip ./gitea-dump.zip
```

新服务器：

```bash
mkdir -p /opt/gitea && cd /opt/gitea

# 部署一个空白 Gitea（先启动一次生成目录结构，再停掉）
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

docker-compose up -d
docker-compose down
```

恢复：

```bash
cp gitea-dump.zip ./data/
docker run --rm \
    -v /opt/gitea/data:/data \
    gitea/gitea:latest \
    gitea restore --config /data/gitea/conf/app.ini --temp-dir /tmp --from /data/gitea-dump.zip

chown -R 1000:1000 ./data
docker-compose up -d
```

### 方案三：仅迁移仓库数据

源服务器：

```bash
tar -czf gitea-repos-backup.tar.gz ./data/gitea/repositories/
cp ./data/gitea.db ./gitea.db.backup
```

新服务器（部署全新 Gitea 后）：

```bash
tar -xzf gitea-repos-backup.tar.gz -C ./data/
cp gitea.db.backup ./data/gitea.db
chown -R 1000:1000 ./data
docker-compose up -d
```

### 方案四：Windows → Linux 互迁

**Windows 端备份**

```powershell
cd C:\Gitea
docker-compose down
Compress-Archive -Path .\data -DestinationPath .\backups\gitea-windows-backup.zip
```

**Linux 端恢复**

```bash
mkdir -p /opt/gitea && cd /opt/gitea
unzip gitea-windows-backup.zip -d ./
chown -R 1000:1000 ./data
find ./data -type d -exec chmod 755 {} \;
find ./data -type f -exec chmod 644 {} \;
docker-compose up -d
```

### 迁移后的配置调整

```bash
vi ./data/gitea/conf/app.ini
```

```ini
[server]
DOMAIN     = 新域名或 IP
SSH_DOMAIN = 新域名或 IP
ROOT_URL   = http://新域名或IP:3000/

[database]
PATH = /data/gitea/gitea.db
```

验证：

```bash
docker-compose ps
docker-compose logs gitea
curl http://localhost:3000
```

### 注意事项

1. **版本一致**：新旧服务器 Gitea 版本号要一致
2. **权限**：Linux 上注意 `1000:1000` 用户
3. **数据库切换**：更换数据库类型需要额外步骤
4. **远程 URL**：迁移后需要更新所有客户端仓库的远程地址
5. **定时任务**：原服务器上的备份 cron / Task Scheduler 需要重新配置

### 迁移检查清单

- [ ] 停止源服务器 Gitea 服务
- [ ] 创建完整备份
- [ ] 传输备份到新服务器
- [ ] 新服务器部署相同版本的 Gitea
- [ ] 恢复备份数据
- [ ] 更新配置文件中的域名/IP
- [ ] 启动新服务器服务
- [ ] 测试所有功能正常
- [ ] 更新 DNS 或客户端远程地址