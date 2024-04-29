---
title: Hexo写作
comments: false
categories:
  - Applications
  - Hexo
tags:
  - Hexo
  - Git
date: 2024-04-28 19:17:56
---
# 新建目录

Hexo 项目并没有 categories（分类）、tags（标签）、about（关于）、links（友链）等页面，需要自己手动创建。创建「 about（关于）」页面，在 Hexo 项目根目录下执行命令，即可在 `source` 目录下生成 about 文件夹。

```shell
hexo new page about
```

# 新建文章

格式（Hexo根目录/Sourse/文件夹下）

分类文件夹/自定义文件夹/文件名 “标题名”

```shell
hexo new page --path _posts/Hexo/hexo建站 "Hexo建站"
```

# 自动生成目录

```shell
npm install hexo-auto-category --save
```