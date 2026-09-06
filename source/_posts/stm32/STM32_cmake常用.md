---
title: STM32_cmake常用
author: zvozve
comments: false
categories:
- stm32
tags:
- stm32
date: 2026-09-06 13:37:34
---

### 包含文件

直接替换
	target_sources(${CMAKE_PROJECT_NAME} PRIVATE
	target_include_directories(${CMAKE_PROJECT_NAME} PRIVATE

```cmake
# ===========================
# User 源代码
# ===========================
file(GLOB_RECURSE USER_SOURCES 
    "User/App/Src/*.c"
    "User/BSP/bsp_dwt/Src/*.c"
    "User/BSP/bsp_uart/Src/*.c"
    "User/Hardware/heart_beat/Src/*.c"
    "User/Middleware/SEGGER_RTT/Src/*.c"
    "User/Protocols/modbus/Src/*.c"
    "User/Tasks/Src/*.c"
)

# ===========================
# 添加到可执行文件
# ===========================
target_sources(${CMAKE_PROJECT_NAME} PRIVATE
    ${USER_SOURCES}
)

# ===========================
# 头文件路径
# ===========================
target_include_directories(${CMAKE_PROJECT_NAME} PRIVATE
    # App
    User/App/Inc
    
    # BSP
    User/BSP/bsp_dwt/Inc
    User/BSP/bsp_uart/Inc
    
    # Hardware
    User/Hardware/heart_beat/Inc
    
    # Middleware
    User/Middleware/SEGGER_RTT/Inc
    
    # Protocols
    User/Protocols/modbus/Inc
    
    # Tasks
    User/Tasks/Inc
)
```

### 自动生成bin文件

放最后

```cmake
# 编译后自动生成 .hex 和 .bin 文件
add_custom_command(TARGET ${CMAKE_PROJECT_NAME} POST_BUILD
    COMMAND ${CMAKE_OBJCOPY} -O ihex $<TARGET_FILE:${CMAKE_PROJECT_NAME}> $<TARGET_FILE_DIR:${CMAKE_PROJECT_NAME}>/${CMAKE_PROJECT_NAME}.hex
    COMMAND ${CMAKE_OBJCOPY} -O binary $<TARGET_FILE:${CMAKE_PROJECT_NAME}> $<TARGET_FILE_DIR:${CMAKE_PROJECT_NAME}>/${CMAKE_PROJECT_NAME}.bin
    COMMENT "Generating HEX and BIN firmware"
)

```
