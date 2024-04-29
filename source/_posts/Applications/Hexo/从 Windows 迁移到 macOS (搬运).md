---
title: 从 Windows 迁移到 macOS (搬运)
comments: false
categories:
  - Applications
  - Hexo
tags:
  - Hexo
  - Git
date: 2024-04-28 19:17:56
auther:
---
[原文链接](https://juejin.cn/post/7016661862448103460)
## 一、Mac 环境配置

### 1. 在 Mac 安装 git 和 node.js

使用 brew 进行安装

```shell
brew install git
brew install node
```

### 2. 安装 hexo

```shell
npm install hexo g
```

这条命令不行（用的时候会出现 `hexo: COMMAND NOT FOUND` 问题）就执行下面这条：

```shell
npm install hexo-cli -g
```

### 3. 初始化 hexo 目录

```shell
mkdir blog
cd blog
```

### 4. 新建 hexo 服务

```shell
hexo init
hexo s
```

打开 `localhost:4000` 查看是否成功。

### 5. 生成 SSH 密钥

先查看本地的 SSH Key：

```shell
cd ~/.ssh
```

如果没有，生成一个SSH Key：

```shell
ssh-keygen -t rsa -C "example@example.com"
```

最后那个是注册邮箱。

### 6. 关联 GitHub

进入 .ssh 文件夹：

```shell
cd ~/.ssh
```

然后打开里面的 `id_rsa.pub` 文件，里面的内容就是 SSH key，复制全部内容。

网页打开 GitHub 的设置：Settings -> SSH and GPG keys，点击绿色的按钮New SSH key，然后在输入框中输入刚才复制的内容。保存后，GitHub 可能会向你的邮箱发送一个验证链接（如果有记得去邮箱验证，不然之后的 hexo 部署会一直不成功的）。

测试一下是否成功：`ssh git@github.com`

看到下面的即成功：

```shell
PTY allocation request failed on channel 0Hi gjincai! You've successfully authenticated, but GitHub does not provide shell access.Connection to github.com closed.
```

## 二、配置文件转移

先找到 Windows 下的博客根目录 hexo，复制该目录下的：`_config.yml`、`scaffolds`、`source`、`themes`、`public`。 再找到 Mac 下的博客根目录 hexo，把刚才复制的内容，直接覆盖替换相同的文件以及文件夹。

## 三、设置个人信息

```shell
git config --global user.name "yourname”git config --global user.email youremail@example.com
```

## 四、发布文章

运行以下命令，查看是否可以成功发布博客：

```shell
hexo d -g
```

发现报错：

```shell
ERROR Deployer not found: git
```

只需要安装：

```shell
npm install hexo-deployer-git --save
```

![https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc26b287680f434f8fa15a63b82473b7~tplv-k3u1fbpfcp-jj-mark:3024:0:0:0:q75.awebp](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc26b287680f434f8fa15a63b82473b7~tplv-k3u1fbpfcp-jj-mark:3024:0:0:0:q75.awebp)

之后就可以正常发布博客了。

## 五、参考

[hexo+github博客迁移（Windows迁移到Mac）](https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fqq_39153421%2Farticle%2Fdetails%2F89362432)

[将Hexo从Windows迁移到Mac上的踩坑教学](https://link.juejin.cn/?target=https%3A%2F%2Fcoldwave96.github.io%2F2020%2F05%2F01%2FWintoMac%2F%23%25E5%25AE%2589%25E8%25A3%2585hexo)
