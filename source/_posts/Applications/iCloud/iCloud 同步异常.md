---
title: iCloud 同步异常
auther: zvozve
comments: false
categories:
  - Applications
  - iCloud
tags:
  - iCloud
date: 2024-04-28 19:17:56
---
# 杀掉后台

**macOS**

```shell
killall bird
Cd ~/Library/Application\ Support
rm -rf CloudDocs
```

**Windows**
```c
taskkill /F /IM APSDaemon.exe
taskkill /F /IM secd.exe
taskkill /F /IM ApplePhotoStreams.exe
taskkill /F /IM iCloudServices.exe
taskkill /F /IM iCloudDrive.exe
taskkill /F /IM iCloudPhotos.exe
```

# 参考

[MACOS ICloud同步上传或下载卡住/失败/正在上传xx个项目/断网/断链问题的临时解决方案](https://blog.csdn.net/q753698/article/details/122198637)
