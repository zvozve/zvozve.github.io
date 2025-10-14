---
title: Obsidian链接Todoist
auther: zvozve
comments: false
categories:
  - Applications
  - Obsidian
tags: 
date: 2025-08-20 21:20:06
---
# 规则

1. 安装Todoist并注册账户
2. Obsidian插件商店安装“Todoist Sync”
3. 在Todoist Sync配置界面填写Todoist的API
4. 新建md文件，填写以下内容 （参考todoist.md）
	[todoist规则说明](https://www.todoist.com/help/articles/introduction-to-filters-V98wIH?locale=en&articleId=introduction-to-filters-V98wIH&utm_source=chatgpt.com)
5. 在Obsidian或Todoist中新建任务，可以使用以下格式

```c
[显示文件名](md文件名.md)
```

说明：在Obsidian中用ctrl+p也可以新建任务，会加入当前打开文件的地址，需要注意

```c
[显示文件名](md文件名.md)(当前打开的文件名.md)
```

# todoist.md

---


```todoist  
name: "Overdue"  
filter: "overdue"  
sorting:  
- date  
- priority
show:  
- due  
- project
autorefresh: 60
```

---

```todoist  
name: "Today"  
filter: "today"  
sorting:  
- date  
- priority
show:  
- due  
- project
autorefresh: 60
```

---

```todoist  
name: "Tomorrow"  
filter: "tomorrow"
sorting:  
- date  
- priority
show:  
- due  
- project
autorefresh: 60
```

---

```todoist  
name: "Later"  
filter: "date after: tomorrow"  
sorting:  
- date  
- priority
show:  
- due  
- project
autorefresh: 60
```

---

```todoist  
name: "NoDate"  
filter: "no date" 
sorting:  
- priority
show:  
- due  
- project
autorefresh: 60
```


---
