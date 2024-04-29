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
mkdir 19.串口 20.IWDG 21.WWDG 22.TIMER 23.OLED 24.MPU 25.FSMC_FMC 26.LTDC 27.USMART 28.RTC 29.RNG 30.LOW POWER 31.DMA 32.ADC 33.DAC 34.IIC 35.SPI_QSPI 36.RS485 37.CAN 38.TOUCH 39.REMOTE 40.游戏手柄 41.单总线 42.无线通信 43.FLASH模拟EEPROM 44.摄像头 45.内存管理 46.SD卡 47.FATFS 48.汉字显示 49.图片编解码 50.音频编解码 51.FPU 52.DSP 55.IAP 56.USB
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
