# A simple tool for Clang-Format directories

----

[TOC]

----

【[中文版本](README_EN.md)】

## Description

A simple tool to clang-format your coding directories with a `.clang-format` file. So far, it only support to format `['.h', '.cpp', '.cu', '.cuh', '.hpp', '.cc']`.

## Usage

- `clang_format_dir.py` has two required arguments:
  - `-b [CLANG_FORMAT_EXE]`: specify the executable file `CLANG_FORMAT_EXE` of clang-format
  - `-dir [TARGET_DIR]`: specify the target directory `TARGET_DIR` to be formatted.

## Quick Start

- Install `clang-format` and `Python`.

```bash
clang-format --version
```

- Use `clang_format_dir.py`. 
  - Step 1: Copy `clang_format_dir.py` into your working directory `working_dir`.
  - Step 2: Copy your expected `.clang-format` file into your working directory `working_dir`.
  - Step 3: Run `clang_format_dir.py` with required arguments (see [Usage](#usage)).

### Example

- The working directory is as follows:

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

- If we need to format the directory `src`, then:

```bash
python3 clang_format_dir.py -b $(which clang-format) -dir src
```

- If we need to format the whole working directory `.`, then:

```bash
python3 clang_format_dir.py -b $(which clang-format) -dir .
```

#### Windows

- Find the executable file of clang-format: `clang-format.exe`. Assume that we get the path to the executable file `CF_PATH=c:\\clang-format.exe`.

- If we need to format the directory `src`, then:

```bash
python3 clang_format_dir.py -b %CF_PATH% -dir src
```

- If we need to format the whole working directory `.`, then:

```bash
python3 clang_format_dir.py -b %CF_PATH% -dir .
```
