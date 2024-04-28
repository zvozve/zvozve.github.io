---
title: FFMPEG常用指令
auther: zvozve
comments: false
date: 2022-03-18 17:54:54
categories: FFMPEG
tags: FFMPEG
---

## XXX2MP4

**flv 2 MP4**

```
ffmpeg -i filename.flv -c:v libx264 -crf 19 -strict experimental filename.mp4
```

 

**mkv 2 mp4**

```
ffmpeg -i filename.mkv -vcodec copy -acodec copy filename.mp4
```

 

**rm 2 mp4**

```
ffmpeg -i filename.rmvb -c:v libx264 -strict -2 filename.mp4
```

 

**ts 2 mp4**

```
ffmpeg -i filename.ts -c copy -map 0:v -map 0:a -bsf:a aac_adtstoasc filename.mp4
```

 

**wmv 2 MP4**

```
ffmpeg -i filename.wmv filename.mp4
```

 

## 其他

**合并音视频**

```
ffmpeg -i filename.mp4 -i filename.m4a -c:v copy -c:a aac -strict experimental filename.mp4
```

 

**提取MP3**

```
ffmpeg -i filename.mp4 -f mp3 -vn filename.mp3
```



**修复MP4**

```
ffmpeg -i filename.mp4 -codec copy filename.mp4
```

 

**剪视频**

```
ffmpeg -i filename.mp4 -ss 00:10:02 -to 00:41:39 filename1.mp4
```

