---
title: STM32_GDB + J-Link调试说明
author: zvozve
comments: false
categories:
- stm32
tags:
- stm32
date: 2026-09-06 13:37:34
---

根据我们之前的调试过程，我为你整理了一份完整的 **GDB + J-Link 单片机调试使用说明**，包含从环境搭建到常用命令的全流程。

---

# GDB + J-Link 单片机调试使用说明

## 一、环境准备

### 1.1 硬件准备
- J-Link 调试器（V9 或更高版本）
- 目标单片机（如 STM32F407ZG）
- SWD/JTAG 连接线
- 目标板供电

### 1.2 软件准备
- **ARM GDB**：`arm-none-eabi-gdb`（Arm GNU Toolchain）
- **J-Link GDB Server**：SEGGER 官方工具
- **带调试信息的固件**：编译时需添加 `-g` 选项生成的 `.elf` 文件

---

## 二、启动调试服务

### 2.1 启动 J-Link GDB Server

**图形界面方式**：
1. 打开 J-Link GDB Server GUI
2. 配置参数：
   - Device: `STM32F407ZG`（根据实际芯片修改）
   - Interface: `SWD`
   - Speed: `4000 kHz`
3. 点击 `Start`，等待显示 `Waiting for GDB connection...`

**命令行方式**：
```bash
JLinkGDBServer -device STM32F407ZG -if SWD -speed 4000
```

### 2.2 启动 GDB 客户端

在另一个终端中：
```bash
arm-none-eabi-gdb -q "路径/项目名.elf"
```

参数说明：
- `-q`：静默模式，跳过版权信息
- `"路径/项目名.elf"`：带调试信息的固件文件

---

## 三、连接与基础调试

### 3.1 连接到 GDB Server
```gdb
(gdb) target extended-remote :2331
```
默认端口为 `2331`，可在 J-Link GDB Server 日志中确认。

### 3.2 下载程序
```gdb
(gdb) load
```
将 `.elf` 文件烧录到单片机 Flash。

### 3.3 复位与运行
```gdb
(gdb) monitor reset      # 复位芯片
(gdb) monitor reset halt # 复位并暂停
(gdb) continue           # 继续运行
```

### 3.4 设置断点
```gdb
(gdb) break main         # 在 main 函数设置断点
(gdb) break 42           # 在当前文件的第 42 行设置断点
(gdb) break 文件名.c:100 # 在指定文件的指定行设置断点
```

---

## 四、常用调试命令大全

### 4.1 程序控制命令

| 命令 | 缩写 | 作用 |
|------|------|------|
| `continue` | `c` | 继续运行程序 |
| `next` | `n` | 单步跳过（不进入函数内部） |
| `step` | `s` | 单步进入（进入函数内部） |
| `finish` | `fin` | 执行完当前函数并返回 |
| `until` | `u` | 持续运行直到指定位置 |
| `quit` | `q` | 退出 GDB |

### 4.2 查看信息命令

| 命令 | 缩写 | 作用 |
|------|------|------|
| `print 变量名` | `p 变量名` | 打印变量值 |
| `print /x 变量名` | - | 以十六进制打印 |
| `print /t 变量名` | - | 以二进制打印 |
| `info locals` | `i lo` | 查看当前函数所有局部变量 |
| `info registers` | `i r` | 查看所有 CPU 寄存器 |
| `info breakpoints` | `i b` | 查看所有断点 |
| `backtrace` | `bt` | 查看调用栈 |
| `list` | `l` | 查看当前位置源代码 |
| `disassemble` | `disas` | 反汇编当前函数 |

### 4.3 内存查看命令
```gdb
(gdb) x/4xw 0x20000000   # 查看地址 0x20000000 开始的 4 个字（十六进制）
(gdb) x/10xb 0x20000000  # 查看 10 个字节（十六进制）
(gdb) x/20xw 0x8000000   # 查看 Flash 起始地址的 20 个字
```

格式说明：`x/[数量][格式][大小] 地址`
- 数量：要显示的单位个数
- 格式：`x`(十六进制)、`d`(十进制)、`t`(二进制)、`c`(字符)、`s`(字符串)
- 大小：`b`(字节)、`h`(半字)、`w`(字)、`g`(双字)

### 4.4 寄存器操作
```gdb
(gdb) print $r0           # 查看 R0 寄存器的值
(gdb) set $r0 = 0x10      # 设置 R0 寄存器为 0x10
(gdb) monitor reg r0      # 通过 monitor 命令查看寄存器
```

### 4.5 Monitor 扩展命令
J-Link GDB Server 提供的专用命令：

| 命令 | 作用 |
|------|------|
| `monitor reset` | 复位目标板 |
| `monitor halt` | 暂停 CPU |
| `monitor regs` | 查看所有寄存器 |
| `monitor reg 寄存器名` | 查看指定寄存器 |
| `monitor flash erase` | 擦除 Flash |
| `monitor help` | 查看所有 monitor 命令 |
| `monitor speed 速度` | 设置调试速度 |

---

## 五、断点管理

### 5.1 设置与查看断点
```gdb
(gdb) break main          # 设置断点
(gdb) info breakpoints    # 查看所有断点（含编号）
(gdb) info b              # 简写
```

### 5.2 删除与禁用断点
```gdb
(gdb) delete 2            # 删除编号为 2 的断点
(gdb) delete              # 删除所有断点
(gdb) disable 2           # 禁用编号为 2 的断点
(gdb) enable 2            # 启用编号为 2 的断点
```

### 5.3 条件断点
```gdb
(gdb) break main if count > 10   # 当 count > 10 时才触发断点
```

---

## 六、进阶技巧

### 6.1 使用 `.gdbinit` 自动化

在 `.elf` 文件同目录下创建 `.gdbinit` 文件：
```
target extended-remote :2331
monitor reset
break main
```

这样每次启动 GDB 时会自动执行这些命令，省去手动输入。

### 6.2 查看宏定义
```gdb
(gdb) info macro 宏名     # 查看宏定义
(gdb) macro expand 表达式 # 展开宏
```
（需要编译时加 `-g3` 参数）

### 6.3 FreeRTOS 调试
```gdb
(gdb) info threads        # 查看所有任务（需配置支持）
(gdb) thread 任务号       # 切换到指定任务
```

### 6.4 常用启动命令组合
```bash
arm-none-eabi-gdb -q -ex "target extended-remote :2331" -ex "monitor reset" -ex "break main" SmartHome.elf
```
一条命令完成连接、复位、设置断点的全部操作。

---

## 七、常见问题与解决

| 问题现象 | 可能原因 | 解决方法 |
|----------|----------|----------|
| `connection refused` | GDB Server 未启动或端口错误 | 检查 J-Link GDB Server 是否运行，端口是否为 2331 |
| `Load failed` | 芯片未进入调试模式 | 先执行 `monitor reset halt` 再 `load` |
| `No symbol table loaded` | `.elf` 编译时未加 `-g` | 重新编译时添加 `-g` 选项 |
| `Cannot access memory` | 芯片休眠或写保护 | 按住复位键执行 `load`，或检查芯片型号 |
| `Remote connection closed` | GDB Server 被关闭 | 检查服务器窗口是否还在运行 |
| 中文/编码警告 | 字符编码问题 | 忽略即可，不影响调试 |

---

## 八、快速参考卡片

```bash
# 启动 J-Link GDB Server
JLinkGDBServer -device STM32F407ZG -if SWD -speed 4000

# 启动 GDB 并连接
arm-none-eabi-gdb -q SmartHome.elf
(gdb) target extended-remote :2331
(gdb) load
(gdb) monitor reset
(gdb) break main
(gdb) continue

# 常用命令速记
(gdb) c          # 继续运行
(gdb) n          # 单步跳过
(gdb) s          # 单步进入
(gdb) p 变量     # 打印变量
(gdb) i r        # 查看寄存器
(gdb) bt         # 查看调用栈
(gdb) q          # 退出
```

---

以上就是 GDB + J-Link 调试的完整使用说明。调试过程中遇到任何问题，欢迎随时交流！ 🚀
