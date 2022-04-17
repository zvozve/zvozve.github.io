---
title: MySQL配置
auther: zvozve
comments: false
date: 2022-03-19 16:22:06
categories: MySQL
tags: MySQL
---

目录：  

```
cd D:\Applications\mysql-8.0.22\bin
```

安装mysql：  

```
mysqld install
```

安装pymysql：  

```
pip install pymysql
```

开机：  

```
net start mysql
```

关机：  

```
net stop mysql
```

登录：  

```
mysql -u root -p
```

初始密码：   

重置密码：  

```
use mysql;  
UPDATE user SET Password=PASSWORD('123456') where USER='root';
FLUSH PRIVILEGES;
quit

mysql> SET PASSWORD = PASSWORD('123456');

ALTER USER 'root'@'localhost' IDENTIFIED BY '123456';
```
