---
title: 安装Homebrew
auther: zvozve
comments: false
categories:
  - Applications
  - HomeBrew
tags:
  - HomeBrew
date: 2024-04-28 19:17:56
---
[https://developer.aliyun.com/article/1291277](https://developer.aliyun.com/article/1291277)

[Homebrew](https://brew.sh/index_zh-cn?spm=a2c6h.12873639.article-detail.7.4f9243d45TDi01) 是一款Mac OS平台下的软件包管理工具，拥有安装、卸载、更新、查看、搜索等很多实用的功能。简单的一条指令，就可以实现包管理，而不用你关心各种依赖和文件路径的情况，十分方便快捷。

### **一、[Homebrew](https://brew.sh/index_zh-cn?spm=a2c6h.12873639.article-detail.8.4f9243d45TDi01) 安装与卸载**

- 安装方式一`(推荐)`：（使用[科大源](https://mirrors.ustc.edu.cn/help/?spm=a2c6h.12873639.article-detail.9.4f9243d45TDi01)进行安装）
- 安装

`$ /bin/bash -c "$(curl -fsSL <https://gitee.com/ineo6/homebrew-install/raw/master/install.sh>)"`

- 卸载

`$ /bin/bash -c "$(curl -fsSL <https://gitee.com/ineo6/homebrew-install/raw/master/uninstall.sh>)"`

- 如果报错 `Error: No similarly named formulae found.`，则更换一下 `homebrew-core` 文件即可，如果 `git clone` 的方式慢，也可以直接打开链接进行下载，将下载的文件夹改成 `homebrew-core` 替换掉之前的 `homebrew-core` 文件即可。

`$ cd /usr/local/Homebrew/Library/Taps/homebrew/ $ rm -rf homebrew-core $ git clone <https://github.com/Homebrew/homebrew-core.git`>

- 安装方式二：（完全纯官方安装，但是需要配置 `host`，`githubusercontent` 国内访问不了）

`$ /bin/bash -c "$(curl -fsSL <https://raw.githubusercontent.com/Homebrew/install/master/install.sh>)"`

- 安装报错这个，试试连接梯子:

`curl: (7) Failed to connect to raw.githubusercontent.com port 443: Connection reset by peer`

- 卸载

`$ /bin/bash -c "$(curl -fsSL <https://raw.githubusercontent.com/Homebrew/install/master/uninstall.sh>)"`

- 卸载过程中根据提示进行操作

`dengzemiaodeMacBook-Pro:~ dengzemiao$ /bin/bash -c "$(curl -fsSL <https://raw.githubusercontent.com/Homebrew/install/master/uninstall.sh>)" Warning: This script will remove: /Users/dengzemiao/Library/Caches/Homebrew/ /usr/local/Caskroom/ /usr/local/Cellar/ /usr/local/bin/brew -> /usr/local/bin/brew Are you sure you want to uninstall Homebrew? This will remove your installed packages! [y/N] ......`

### **二、[Homebrew](https://brew.sh/index_zh-cn?spm=a2c6h.12873639.article-detail.10.4f9243d45TDi01) 使用**

- 安装包

`$ brew install 包名`

- 示例：

`$ brew install node`

- 卸载包

`$ brew uninstall 包名`

- 示例：

`$ brew uninstall node`

- 查询可用包

`$ brew search 包名`

- 更新包

`# 更新全部包 $ brew upgrade

# 更新指定包

$ brew upgrade 包名`

- 查看已安装包列表

`$ brew list`

- 查看任意包信息

`$ brew info 包名`

- 清理包

`# 查看哪些软件包要被清除 $ brew cleanup -n

# 清除指定软件包的所有老版本

$ brew cleanup 软件名

# 清除所有软件包的所有老版本

$ brew cleanup`

- 查看版本

`$ brew -v`

- 升级 `Homebrew` 自身

`$ brew update`

- `Homebrew` 帮助信息

`$ brew -h`

### **三、[Homebrew](https://brew.sh/index_zh-cn?spm=a2c6h.12873639.article-detail.11.4f9243d45TDi01) 常见问题**

- [brew update 长时间没反应（或卡在 Updating Homebrew…）](https://blog.csdn.net/zz00008888/article/details/113880633?spm=a2c6h.12873639.article-detail.12.4f9243d45TDi01)
- [Mac 下镜像飞速安装 Homebrew 教程](https://zhuanlan.zhihu.com/p/90508170?spm=a2c6h.12873639.article-detail.13.4f9243d45TDi01)
- 注意事项：在 `Mac OS X 10.11` 系统以后，`/usr/local/` 等系统目录下的[文件读写](https://so.csdn.net/so/search?spm=a2c6h.12873639.article-detail.14.4f9243d45TDi01&q=%E6%96%87%E4%BB%B6%E8%AF%BB%E5%86%99)是需要系统 `root` 权限的，以往的 `Homebrew` 安装如果没有指定安装路径，会默认安装在这些需要系统 `root` 用户读写权限的目录下，导致有些指令需要添加 `sudo` 前缀来执行，比如升级 `Homebrew` 需要：

`$ sudo brew update`

- 报错 `echo 'export HOMEBREW_GITHUB_API_TOKEN=your_token_here' >> ~/.bash_profile`

`dengzemiaodeMacBook-Pro:~ dengzemiao$ brew search nginx Warning: Error searching on GitHub: GitHub Bad credentials:The GitHub credentials in the macOS keychain may be invalid. Clear them with: printf "protocol=https\\nhost=github.com\\n" | git credential-osxkeychain erase Or create a personal access token: <https://github.com/settings/tokens/new?scopes=gist,public_repo&description=Homebrew> echo 'export HOMEBREW_GITHUB_API_TOKEN=your_token_here' >> ~/.bash_profile ==> Formulae nginx`

- 解决方式：1、点击错误中的链接，就会打开 `github` 页面，进入页面之后直接滚到底部点击 `Generate token` 按钮，然后拷贝得到的 `token`：

`https://github.com/settings/tokens/new?scopes=gist,public_repo&description=Homebrew`

```
!<https://ucc.alicdn.com/pic/developer-ecology/mi5buufzsvd3q_311f61f049664392a89cd195250eb4c3.png>

!<https://ucc.alicdn.com/pic/developer-ecology/mi5buufzsvd3q_c1dae4f8555442f3988a6fdf0b20496c.png>
```

2、打开命令行，输入下面命令，回车之后就行了，然后就正常使用：

`$ export HOMEBREW_GITHUB_API_TOKEN=填入你刚才得到的Token 例如： $ export HOMEBREW_GITHUB_API_TOKEN=465832bc2dd057a2c556f...`