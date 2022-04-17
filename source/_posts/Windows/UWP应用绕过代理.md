---
title: UWP应用绕过代理
auther: zvozve
comments: false
date: 2022-03-18 17:50:47
categories: 
- Windows
tags:
- Windows
- UWP
---

## 注册表路径

```
HKEY_CURRENT_USER\Software\Classes\Local Settings\Software\Microsoft\Windows\CurrentVersion\AppContainer\Mappings
```



## CMD命令

```
CheckNetIsolation.exe loopbackexempt -a -p=
```



## 具体指令

**便签**

```
CheckNetIsolation.exe loopbackexempt -a -p=S-1-15-2-3539788797-2700867667-1432428195-1581642-2885308443-3834444517-2495346167
```

**OneNote**

```
CheckNetIsolation.exe loopbackexempt -a -p=S-1-15-2-3445883232-1224167743-206467785-1580939083-2750001491-3097792036-3019341970
```

**QQ音乐**

```
CheckNetIsolation.exe loopbackexempt -a -p=S-1-15-2-1971894009-4117020779-3514498563-3192240937-1419126668-1560270856-676699529
```

**哔哩哔哩**

```
CheckNetIsolation.exe loopbackexempt -a -p=S-1-15-2-4091843776-1243804748-1367707030-686088537-118659545-1271627824-1744311777
```



```
CheckNetIsolation.exe loopbackexempt -a -p=S-1-15-2-2537927067-2140208811-1083047336-3825492100-1188134376-3459723148-3131426163
```

 

```
CheckNetIsolation.exe loopbackexempt -a -p=S-1-15-2-2040986369-264322980-3882385089-1970153872-3662121739-3363227934-2464603330
```

 

```
CheckNetIsolation.exe loopbackexempt -a -p=S-1-15-2-1609473798-1231923017-684268153-4268514328-882773646-2760585773-1760938157
```

 

```
CheckNetIsolation.exe loopbackexempt -a -p=S-1-15-2-1239072475-3687740317-1842961305-3395936705-4023953123-1525404051-2779347315
```

 

```
CheckNetIsolation.exe loopbackexempt -a -p=S-1-15-2-466767348-3739614953-2700836392-1801644223-4227750657-1087833535-2488631167
```

 

