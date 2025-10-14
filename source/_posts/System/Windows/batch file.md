---
title: batch file
auther: zvozve
comments: false
categories:
  - System
  - Windows
tags:
  - Scripts
date: 2024-04-29 15:41:34
---
# App

## Kill the software background：Acrobat

```c
taskkill /F /IM Acrobat.exe
taskkill /F /IM acrotray.exe
taskkill /F /IM AdobeCollabSync.exe
taskkill /F /IM AcroCEF.exe
```

## Kill the software background：iCloud

```c
taskkill /F /IM APSDaemon.exe
taskkill /F /IM secd.exe
taskkill /F /IM ApplePhotoStreams.exe
taskkill /F /IM iCloudServices.exe
taskkill /F /IM iCloudDrive.exe
taskkill /F /IM iCloudPhotos.exe
```

## Kill the software background：RockStar Club

```c
taskkill /F /IM SocialClubHelper.exe
taskkill /F /IM Launcher.exe
taskkill /F /IM LauncherPatcher.exe
taskkill /F /IM RockstarService.exe
taskkill /F /IM RockstarErrorHandler.exe
taskkill /F /IM PlayGTAV.exe
```

## Launch software

```c
//start /d"Path" AppName
start /d"C:\Program Files\Tencent\QQNT" QQ.exe
```

# File

## Create folders in batches

```c
@echo off
chcp 65001 > nul
mkdir A B C D
```

## Create folders in batches named by file

> Name the folder after the file name and then move the file to the folder

```c
for %%i in (*.png) do (
mkdir "%%~ni"
move "%%i" "%%~ni"
)
pause
```

## Delete all empty folders

```c
@echo off
for /f "tokens=*" %%i in ('dir/s/b/ad^|sort /r') do rd "%%i"
```
