---
title: UWP App bypasses system proxy
auther: zvozve
comments: false
categories:
  - System
  - Windows
tags:
  - Windows
  - UWP
date: 2022-03-18 17:50:47
---
# Registry path

```
HKEY_CURRENT_USER\Software\Classes\Local Settings\Software\Microsoft\Windows\CurrentVersion\AppContainer\Mappings
```

# CMD Part

```
CheckNetIsolation.exe loopbackexempt -a -p=
```

# CMD Full

```c

// Microsoft Store
CheckNetIsolation.exe loopbackexempt -a -p=S-1-15-2-1609473798-1231923017-684268153-4268514328-882773646-2760585773-1760938157

// OneDrive
CheckNetIsolation.exe loopbackexempt -a -p=S-1-15-2-4273547510-4115876375-966110897-1700121547-3167824608-1571544438-2504093867

// outlook
CheckNetIsolation.exe loopbackexempt -a -p=S-1-15-2-58910866-3222973021-3644791724-2336003105-2142029753-2093886826-3648459896

// OneNote
CheckNetIsolation.exe loopbackexempt -a -p=S-1-15-2-3445883232-1224167743-206467785-1580939083-2750001491-3097792036-3019341970

// To Do
CheckNetIsolation.exe loopbackexempt -a -p=S-1-15-2-2537927067-2140208811-1083047336-3825492100-1188134376-3459723148-3131426163

// Stickynote
CheckNetIsolation.exe loopbackexempt -a -p=S-1-15-2-3539788797-2700867667-1432428195-1581642-2885308443-3834444517-2495346167

// Weather
CheckNetIsolation.exe loopbackexempt -a -p=S-1-15-2-2040986369-264322980-3882385089-1970153872-3662121739-3363227934-2464603330

// Map
CheckNetIsolation.exe loopbackexempt -a -p=S-1-15-2-1239072475-3687740317-1842961305-3395936705-4023953123-1525404051-2779347315

// phone
CheckNetIsolation.exe loopbackexempt -a -p=S-1-15-2-2226957697-3030467180-2301525-4248967783-2024719031-2325529081-2915787518

// your phone
CheckNetIsolation.exe loopbackexempt -a -p=S-1-15-2-1726375552-1729233799-74693324-3851689839-2151781990-3623637752-3611872497

// iCloud
CheckNetIsolation.exe loopbackexempt -a -p=S-1-15-2-577278596-3063659431-1612091346-1109771266-600305798-4280066548-3535389673

// apple music
CheckNetIsolation.exe loopbackexempt -a -p=S-1-15-2-1055287963-2136560721-558446762-482033650-1886948555-2417497247-349453271

// Intel Union
CheckNetIsolation.exe loopbackexempt -a -p=S-1-15-2-2979296028-3263479262-1425011945-1249768886-2352407162-3367022568-1368475839

// QQ Music
CheckNetIsolation.exe loopbackexempt -a -p=S-1-15-2-1971894009-4117020779-3514498563-3192240937-1419126668-1560270856-676699529

// Bilibili
CheckNetIsolation.exe loopbackexempt -a -p=S-1-15-2-4091843776-1243804748-1367707030-686088537-118659545-1271627824-1744311777

// Baidu Netdisk
CheckNetIsolation.exe loopbackexempt -a -p=S-1-15-2-1975623427-2939646708-607648744-3861755161-2409147266-1152891593-3234113407
```
