---
title: Hexo部署
comments: false
categories:
  - Applications
  - Hexo
tags:
  - Hexo
  - Git
date: 2024-06-18 15:46:56
---
# 新建Github仓库

**替换为自己的**

> abc.github.io

#  安装软件

## 安装git node.js

## 安装hexo

```
npm install hexo-cli -g
```

验证软件版本

```
git --version
node -v
npm -v
```

# 本地部署

初始化Hexo文件夹（选择空文件夹）

```
hexo init
```

安装npm

```
npm install
```

安装插件

```
npm install hexo-deployer-git --save
```

开启本地访问（http://localhost:4000）

ctrl c退出

```
hexo s
```
# 同步到Github

修改根目录下_config.yal文件

```
deploy:
  type: git
  repo: 
        repository: https://github.com/abc/abc.github.io.git
  branch: master
```

登录信息

```
git config --global user.email "abc@xxx.com"
git config --global user.name "abc"
```

推送到github

```
hexo g -d
```
# 更换主题（可选）

> [hexo主题](http://www.hexo.io)
>
> [主题"keep"配置](https://keep-docs.xpoet.cn/usage-tutorial/configuration-guide.html#menu)

克隆主题

```
git clone https://github.com/sanjinhub/hexo-theme-geek.git geek 
```

修改_config.yal文件中使用的主题名

删除.deploy_git文件夹和public文件夹

执行以下代码刷新

```
hexo clean
hexo deploy
```

重新生成index

```
npm install hexo-deployer-git --save
npm install hexo-generator-index --save
```
# 备份

1. 创建新分支，命名为：hexo

   ```
   git checkout -b hexo
   ```

2. 对于日常修改博客的时候，应该首先用将内容保存至github中，然后再部署博客

   ```
   git add . 
   git commit -m “…”
   git push origin hexo　
   hexo g -d
   ```

# 恢复

1. 将仓库克隆到本地

   ```
   git clone -b hexo [git@github.com](mailto:git@github.com): …
   ```

2. 然后在文件夹下执行 

   ```
   npm install hexo 
   npm install 
   npm install hexo-deployer-git 
   (不需要hexo init)
   ```

# 参考

[blog+github备份和恢复]( https://jinzequn.github.io/2018/01/24/github-hexo/ )
