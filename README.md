# 一个辅助 Clang-Format 整个目录的简单工具

----

[TOC]

----

【[English Version](README_EN.md)】

## 描述

一个利用 `.clang-format` 文件来 Clang-Format 整个目录的简单工具. 该工具支持递归目录进行格式化的功能，支持的文件类型为： `['.h', '.cpp', '.cu', '.cuh', '.hpp', '.cc']`.

## 使用说明

- `clang_format_dir.py` 有两个必要参数:
  - `-b [CLANG_FORMAT_EXE]`: 用于声明可执行的 clang-format 文件路径`CLANG_FORMAT_EXE`.
  - `-dir [TARGET_DIR]`: 用于声明想要格式化代码的目录 `TARGET_DIR`.

## 快速上手

- 安装 `clang-format` 和 `Python`.

```bash
clang-format --version
```

- 使用 `clang_format_dir.py` 脚本格式化代码.
  - Step 1: 拷贝 `clang_format_dir.py` 到你的工作目录 `working_dir`.
  - Step 2: 拷贝你自定义的 `.clang-format` 配置文件到你的工作目录 `working_dir`.
  - Step 3: 执行脚本 `clang_format_dir.py` (参考上述使用说明 [使用说明](#使用说明)).

### 案例

- 当前案例的工作目录如下:

```bash
---- working_dir
|
---- src
    |
    -- hello_world.cc
    |
    -- hello_world.h
|
---- util
    |
    -- util.cc
    |
    -- util.h
|
-- BUILD
|
-- WORKSPACE
```

#### Linux

- 若我们想要格式化目录 `src` 下的所有代码, 执行:

```bash
python3 clang_format_dir.py -b $(which clang-format) -dir src
```

- 若我们想要格式化当前整个工作目录下 `.` 的所有代码文件, 执行:

```bash
python3 clang_format_dir.py -b $(which clang-format) -dir .
```

#### Windows

- 找到所安装的 clang-format 的执行文件路径: `clang-format.exe`. 假设我们已知执行文件路径为 `CF_PATH=c:\\clang-format.exe`.

- 若我们想要格式化目录 `src` 下的所有代码, 执行:

```bash
python3 clang_format_dir.py -b %CF_PATH% -dir src
```

- 若我们想要格式化当前整个工作目录下 `.` 的所有代码文件, 执行:

```bash
python3 clang_format_dir.py -b %CF_PATH% -dir .
```
