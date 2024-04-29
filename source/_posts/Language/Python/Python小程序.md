---
title: Python小程序
auther: zvozve
comments: false
categories:
  - Language
  - Python
tags: Python
date: 2022-03-19 16:17:53
---

## 回文年

```python
import datetime
sdate = datetime.datetime.strptime('2021.12.1','%Y.%m.%d') 
for i in range(1,100000):
    delta1 = datetime.timedelta (days=i) 
    edate = sdate + delta1
    curYear = int(edate.strftime("%Y"))
    curMon = int(edate.strftime("%m"))
    curDay = int(edate.strftime("%d"))
    firLoc = int(curDay % 10) * 1000
    secLoc = int(curDay / 10) * 100
    thrLoc = int(curMon % 10) * 10
    ForLoc = int(curMon / 10)
    newYear = int(firLoc + secLoc + thrLoc + ForLoc)
    #print (i)
    #print (curYear)
    #print (curMon)
    #print (curDay)
    #print (newYear)
    if (newYear == curYear):
        print (edate)
    i = i + 1

```

## 小猪佩奇

```python
# coding:utf-8
import turtle as t
 
t.screensize(400, 300, "blue")
t.pensize(4) # 设置画笔的大小
t.colormode(255) # 设置GBK颜色范围为0-255
t.color((255,155,192),"pink") # 设置画笔颜色和填充颜色(pink)
t.setup(840,500) # 设置主窗口的大小为840*500
t.speed(10) # 设置画笔速度为10
#鼻子
t.pu() # 提笔
t.goto(-100,100) # 画笔前往坐标(-100,100)
t.pd() # 下笔
t.seth(-30) # 笔的角度为-30°
t.begin_fill() # 外形填充的开始标志
a=0.4
for i in range(120):
   if 0<=i<30 or 60<=i<90:
       a=a+0.08
       t.lt(3) #向左转3度
       t.fd(a) #向前走a的步长
   else:
       a=a-0.08
       t.lt(3)
       t.fd(a)
t.end_fill() # 依据轮廓填充
t.pu() # 提笔
t.seth(90) # 笔的角度为90度
t.fd(25) # 向前移动25
t.seth(0) # 转换画笔的角度为0
t.fd(10)
t.pd()
t.pencolor(255,155,192) # 设置画笔颜色
t.seth(10)
t.begin_fill()
t.circle(5) # 画一个半径为5的圆
t.color(160,82,45) # 设置画笔和填充颜色
t.end_fill()
t.pu()
t.seth(0)
t.fd(20)
t.pd()
t.pencolor(255,155,192)
t.seth(10)
t.begin_fill()
t.circle(5)
t.color(160,82,45)
t.end_fill()
#头
t.color((255,155,192),"pink")
t.pu()
t.seth(90)
t.fd(41)
t.seth(0)
t.fd(0)
t.pd()
t.begin_fill()
t.seth(180)
t.circle(300,-30) # 顺时针画一个半径为300,圆心角为30°的园
t.circle(100,-60)
t.circle(80,-100)
t.circle(150,-20)
t.circle(60,-95)
t.seth(161)
t.circle(-300,15)
t.pu()
t.goto(-100,100)
t.pd()
t.seth(-30)
a=0.4
for i in range(60):
   if 0<=i<30 or 60<=i<90:
       a=a+0.08
       t.lt(3) #向左转3度
       t.fd(a) #向前走a的步长
   else:
       a=a-0.08
       t.lt(3)
       t.fd(a)
t.end_fill()
#耳朵
t.color((255,155,192),"pink")
t.pu()
t.seth(90)
t.fd(-7)
t.seth(0)
t.fd(70)
t.pd()
t.begin_fill()
t.seth(100)
t.circle(-50,50)
t.circle(-10,120)
t.circle(-50,54)
t.end_fill()
t.pu()
t.seth(90)
t.fd(-12)
t.seth(0)
t.fd(30)
t.pd()
t.begin_fill()
t.seth(100)
t.circle(-50,50)
t.circle(-10,120)
t.circle(-50,56)
t.end_fill()
#眼睛
t.color((255,155,192),"white")
t.pu()
t.seth(90)
t.fd(-20)
t.seth(0)
t.fd(-95)
t.pd()
t.begin_fill()
t.circle(15)
t.end_fill()
t.color("black")
t.pu()
t.seth(90)
t.fd(12)
t.seth(0)
t.fd(-3)
t.pd()
t.begin_fill()
t.circle(3)
t.end_fill()
t.color((255,155,192),"white")
t.pu()
t.seth(90)
t.fd(-25)
t.seth(0)
t.fd(40)
t.pd()
t.begin_fill()
t.circle(15)
t.end_fill()
t.color("black")
t.pu()
t.seth(90)
t.fd(12)
t.seth(0)
t.fd(-3)
t.pd()
t.begin_fill()
t.circle(3)
t.end_fill()
#腮
t.color((255,155,192))
t.pu()
t.seth(90)
t.fd(-95)
t.seth(0)
t.fd(65)
t.pd()
t.begin_fill()
t.circle(30)
t.end_fill()
#嘴
t.color(239,69,19)
t.pu()
t.seth(90)
t.fd(15)
t.seth(0)
t.fd(-100)
t.pd()
t.seth(-80)
t.circle(30,40)
t.circle(40,80)
#身体
t.color("red",(255,99,71))
t.pu()
t.seth(90)
t.fd(-20)
t.seth(0)
t.fd(-78)
t.pd()
t.begin_fill()
t.seth(-130)
t.circle(100,10)
t.circle(300,30)
t.seth(0)
t.fd(230)
t.seth(90)
t.circle(300,30)
t.circle(100,3)
t.color((255,155,192),(255,100,100))
t.seth(-135)
t.circle(-80,63)
t.circle(-150,24)
t.end_fill()
#手
t.color((255,155,192))
t.pu()
t.seth(90)
t.fd(-40)
t.seth(0)
t.fd(-27)
t.pd()
t.seth(-160)
t.circle(300,15)
t.pu()
t.seth(90)
t.fd(15)
t.seth(0)
t.fd(0)
t.pd()
t.seth(-10)
t.circle(-20,90)
t.pu()
t.seth(90)
t.fd(30)
t.seth(0)
t.fd(237)
t.pd()
t.seth(-20)
t.circle(-300,15)
t.pu()
t.seth(90)
t.fd(20)
t.seth(0)
t.fd(0)
t.pd()
t.seth(-170)
t.circle(20,90)
#脚
t.pensize(10)
t.color((240,128,128))
t.pu()
t.seth(90)
t.fd(-75)
t.seth(0)
t.fd(-180)
t.pd()
t.seth(-90)
t.fd(40)
t.seth(-180)
t.color("black")
t.pensize(15)
t.fd(20)
t.pensize(10)
t.color((240,128,128))
t.pu()
t.seth(90)
t.fd(40)
t.seth(0)
t.fd(90)
t.pd()
t.seth(-90)
t.fd(40)
t.seth(-180)
t.color("black")
t.pensize(15)
t.fd(20)
#尾巴
t.pensize(4)
t.color((255,155,192))
t.pu()
t.seth(90)
t.fd(70)
t.seth(0)
t.fd(95)
t.pd()
t.seth(0)
t.circle(70,20)
t.circle(10,330)
t.circle(70,30)
t.done()
```

## 二进制转十进制

```python
# 小数的二进制显示

# 运算数（十进制）
cntNum = 0.114514
# 用于存储结果的数组初始化
cont = {}
i = 0
# 程序主体
while cntNum != 1:
    if cntNum < 1:
        cntNum = cntNum * 2
        cont[i] = "0"
    elif cntNum > 1:
        cntNum = cntNum - 1
        cntNum = cntNum * 2
        cont[i] = "1"
    i = i + 1
    # 打印过程数字
    # print(cntNum)
cont[i] = "1"
cont[0] = "0."
# 打印结果
for i in cont:
    print(cont[i], end="")  # 同行显示
print('\n')
# 打印小数位数
print(len(cont)-1)
```

## FileName2FileTime

```python
# 读取文件名并以其命名
# 末尾添加4位随机字母防止重复

import os
import time
import datetime
import re
import random
import win32_setfiletime
import exifread


# 自动补齐信息
def addInfo(inputMainName):
    yearPart = chr(0000)
    monPart = 00
    dayPart = 00
    if 13 == len(inputMainName):
        outputMainName = inputMainName[0:10]
    else:
        if len(inputMainName) < 13:
            if 8 <= len(inputMainName) <= 10:
                yearPart = inputMainName[0:4]
                monPart = inputMainName[4:6]
                dayPart = inputMainName[6:8]
            elif 6 <= len(inputMainName) <= 7:
                yearPart = inputMainName[0:4]
                monPart = inputMainName[4:6]
                dayPart = '%02d' % random.randint(1, 28)
            elif 4 == len(inputMainName):
                yearPart = inputMainName[0:4]
                monPart = '%02d' % random.randint(1, 12)
                dayPart = '%02d' % random.randint(1, 28)
            hourPart = '%02d' % random.randint(1, 24)
            minPart = '%02d' % random.randint(1, 60)
            secPart = '%02d' % random.randint(1, 60)
        else:
            yearPart = inputMainName[0:4]
            monPart = inputMainName[4:6]
            dayPart = inputMainName[6:8]
            hourPart = inputMainName[9:11]
            minPart = inputMainName[11:13]
            secPart = inputMainName[13:15]
        outputMainName = (yearPart + '-' + monPart + '-' + dayPart + ' ' + hourPart + ':' + minPart + ':' + secPart)
    return outputMainName


# 时间戳转时间
# 正确10位长度的时间戳可精确到秒，11-14位长度则是包含了毫秒
def intTodatetime(intValue):
    if len(str(intValue)) == 10:
        # 精确到秒
        timeValue = time.localtime(intValue)
        tempDate = time.strftime("%Y-%m-%d %H:%M:%S", timeValue)
        datetimeValue = datetime.datetime.strptime(tempDate, "%Y-%m-%d %H:%M:%S")
    elif 10 < len(str(intValue)) < 15:
        # 精确到毫秒
        k = len(str(intValue)) - 10
        timetamp = datetime.datetime.fromtimestamp(intValue / (1 * 10 ** k))
        datetimeValue = timetamp.strftime("%Y-%m-%d %H:%M:%S.%f")
    else:
        return -1
    return datetimeValue


# 替换字符
def replaceChar(inputFileName):
    outputFileName = re.sub(r':', '', str(inputFileName))  # 时间串转字符串
    try:
        outputFileName = re.sub(r'-', '', str(outputFileName))  # 时间串转字符串
    except:
        pass
    outputFileName = re.sub(r' ', '-', str(outputFileName))  # 时间串转字符串
    return outputFileName


# 读取文件创建时间并以其创建时间命名
if __name__ == '__main__':
    loadPath = r"C:\Users\ZOZE\Desktop\新建文件夹"  # 文件夹目录
    path = re.sub(r"\\", "/", str(loadPath))  # 时间串转字符串
    files = os.listdir(path)  # 得到文件夹下的所有文件名称
    for file in files:  # 遍历文件夹
        if not os.path.isdir(file):  # 判断是否是文件夹
            oldFilePath = path + '/' + file  # 旧路径和文件
            mainName = os.path.splitext(file)[0]  # 获取文件名
            suffixName = os.path.splitext(file)[-1]  # 获取文件扩展名
            newInfo = addInfo(mainName)
            if len(newInfo) == 10:
                timeStamp = float("%.1f" % int(newInfo))
                timeStamp = timeStamp - 102468214
                print(type(timeStamp))
                print('a')
            else:
                format = "%Y-%m-%d %H:%M:%S"
                timeStamp = time.mktime(time.strptime(newInfo, format))  # 转为时间戳
                print(type(timeStamp))
                print('b')
            win32_setfiletime.setctime(oldFilePath, timeStamp)  # 修改创建时间
            win32_setfiletime.setmtime(oldFilePath, timeStamp)  # 修改修改时间
            # win32_setfiletime.setatime(oldFilePath, timeStamp)  # 修改访问时间
            print('c')
            createTime = os.path.getctime(oldFilePath)  # 获取时间戳
            fileTime = intTodatetime(int(createTime))  # 将时间戳整形化，并转换为时间

            newFileTime = replaceChar(fileTime)  # 简化格式

            randomNumberList = ''
            if len(suffixName) > 0:
                for i in range(0, 4):
                    randomNumber = chr(random.randint(64 + 1, 64 + 26))  # 生成随机数
                    randomNumberList = randomNumberList + randomNumber
                newFilePath = path + '/' + newFileTime + '-' + randomNumberList + suffixName  # 新路径和文件
                os.rename(oldFilePath, newFilePath)  # 替换文件名
            print("success!")
            # else:
            # realCreateTime = realCreateTime[0:8]
            # newFilePath = path + '/' + realCreateTime  # 新路径和文件
```

## FileTime2FileName

```python
# 读取文件创建时间并以其创建时间命名
# 末尾添加4位随机字母防止重复

import os
import time
import datetime
import re
import random
import exifread


# 时间戳转时间
# 正确10位长度的时间戳可精确到秒，11-14位长度则是包含了毫秒
def intTodatetime(intValue):
    if len(str(intValue)) == 10:
        # 精确到秒
        timeValue = time.localtime(intValue)
        tempDate = time.strftime("%Y-%m-%d %H:%M:%S", timeValue)
        datetimeValue = datetime.datetime.strptime(tempDate, "%Y-%m-%d %H:%M:%S")
    elif 10 < len(str(intValue)) < 15:
        # 精确到毫秒
        k = len(str(intValue)) - 10
        timetamp = datetime.datetime.fromtimestamp(intValue / (1 * 10 ** k))
        datetimeValue = timetamp.strftime("%Y-%m-%d %H:%M:%S.%f")
    else:
        return -1
    return datetimeValue


# 替换字符
def replaceChar(inputFileName):
    outputFileName = re.sub(r':', '', str(inputFileName))  # 时间串转字符串
    try:
        outputFileName = re.sub(r'-', '', str(outputFileName))  # 时间串转字符串
    except:
        pass
    outputFileName = re.sub(r' ', '-', str(outputFileName))  # 时间串转字符串
    return outputFileName


# 读取文件创建时间并以其创建时间命名
loadPath = r"C:\Users\ZOZE\Desktop\新建文件夹"  # 文件夹目录
path = re.sub(r"\\", "/", str(loadPath))  # 时间串转字符串
files = os.listdir(path)  # 得到文件夹下的所有文件名称
for file in files:  # 遍历文件夹
    if not os.path.isdir(file):  # 判断是否是文件夹
        oldFilePath = path + '/' + file  # 旧路径和文件
        suffixName = os.path.splitext(file)[-1]  # 获取文件扩展名
        try:  # 尝试打开文件读取拍摄信息
            openFile = open(oldFilePath, 'rb')
            tags = exifread.process_file(openFile)
            fileTime = tags['EXIF DateTimeOriginal']  # 获取拍摄时间
            openFile.close()
            print("shot time")
        except:  # 获取创建日期，不等于拍摄日期
            createTime = os.path.getctime(oldFilePath)  # 获取时间戳
            fileTime = intTodatetime(int(createTime))  # 将时间戳整形化，并转换为时间
            print("create time")
        try:
            newFileTime = replaceChar(fileTime)  # 简化格式
            print(newFileTime)
            randomNumberList = ''
            if len(suffixName) > 0:
                for i in range(0, 4):
                    randomNumber = chr(random.randint(64 + 1, 64 + 26))  # 生成随机数
                    randomNumberList = randomNumberList + randomNumber
                newFilePath = path + '/' + newFileTime + '-' + randomNumberList + suffixName  # 新路径和文件
                os.rename(oldFilePath, newFilePath)  # 替换文件名
                print("success!")
        except:
            pass
        # else:
        # realCreateTime = realCreateTime[0:8]
        # newFilePath = path + '/' + realCreateTime  # 新路径和文件


```

