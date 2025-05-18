---
comments: true
# icon: material/emoticon-happy 
# status: new
title: pathlib 和 os.path
subtitle: 文件操作
---

:material-pen-plus: `本文创建于2025-4-18`

[:simple-python: os.path官方文档](https://docs.python.org/zh-cn/3/library/os.path.html){ .md-button .md-button--primary }
[:simple-python: pathlib官方文档](https://docs.python.org/zh-cn/3/library/pathlib.html){ .md-button }

## 第一步：导入pathlib和os.path

    from pathlib import Path
    import os.path

## 第二步：创建Path对象

Path类：

`Path(*pathsegments)` 传入文件路径或路径片段，路径之间使用逗号分隔，默认值是当前目录

## 第二步：对Path对象进行操作

### 2.1 path对象路径常用属性和方法

- `parts` 将路径拆分，返回路径片段的元组
- `drive` 返回盘符
- `parents` 返回祖先路径
- `parent` 返回父路径，相当于 `os.path.dirname()`函数
- `name` 返回最末尾的路径（文件名或文件夹名），相当于 `os.path.basename()` 函数
- `suffix` 返回文件后缀名（文件扩展名），相当于 `os.path.splitext()` 函数
- `suffixes` 返回文件扩展名列表，主要针对文件后缀名中有多个 `.` 的后缀名
- `stem` 返回去除后缀名的最末尾路径（不包含后缀名的文件名或文件夹名），相当于 `os.path.splitext()` 函数
- `as_posix()` 返回使用 `/` 的文件路径，主要用于将windows路径的 `\\` 路径转换为 `/` 路径
- `is_absolute()` 判断是否是绝对路径，相当于 `os.path.isabs()` 函数
- `is_relative_to(other)` 判断此路径是否是相对于 other 的路径
- `joinpath(*pathsegments)` 将传入的路径片段与path对象的路径组和，相当于 `os.path.join()` 函数
- `with_name(name)` 返回一个新的路径并修改 name。如果原本路径没有 name，ValueError 被抛出
- `with_stem(stem)` 返回一个带有修改后 stem 的新路径。 如果原路径没有名称，则会引发 ValueError
- `with_suffix(suffix)` 返回一个新的路径并修改 suffix。如果原本的路径没有后缀，新的 suffix 则被追加以代替。如果 suffix 是空字符串，则原本的后缀被移除
- `absolute()` 改为绝对路径，不会执行正规化或解析符号链接。 返回一个新的路径对象
- `exists(*, follow_symlinks=True)`
判断路径是否存在，此方法通常会跟随符号链接；要检查符号链接是否存在，请添加参数 follow_symlinks=False，相当于 `os.path.exists()` 函数
- `is_file(*, follow_symlinks=True)` 判断路径是否指向普通文件（不是文件夹），路径不存在时也返回False，相当于 `os.path.isfile()` 函数
- `is_dir(*, follow_symlinks=True)` 同上，判断路劲是否指向文件夹，相当于 `os.path.isdir()` 函数
- `iterdir()` 当路径指向一个目录时，产生该路径下的对象的路径，用于for循环
  
### 2.2 常用函数

以下函数不需要创建path对象就可以直接使用：

- `Path.home()` 返回当前用户的用户文件夹路径
- `Path.cwd()` 返回一个新的表示当前工作目录的路径对象，相当于 `os.getcwd()` 函数

### 2.3 创建、删除、重命名

- `touch(mode=0o666, exist_ok=True)` 使用给定的路径创建文件。 如果给出了 mode，它将与进程的 umask 值合并以确定文件模式和访问旗标。 如果文件已存在，则当 exist_ok 为真值时函数将成功执行（并且其修改时间将更新为当前时间），在其他情况下则会引发 FileExistsError。
- `mkdir(mode=0o777, parents=False, exist_ok=False)` 同上，创建文件夹，相当于`os.mkdir()` 和 `os.makedirs()` 函数
- `rename(target)` 将此文件或目录重命名为给定的 target，并返回一个新的指向 target 的 Path 实例。相当于 `os.rename()` 函数
- `replace(target)` 将此文件或目录重命名为给定的 target，并返回一个新的指向 target 的 Path 实例。 如果 target 指向一个现有文件或空目录，则它将被无条件地替换。相当于 `os.replace()` 函数
- `rmdir()` 移除此目录。此目录必须为空的。相当于 `os.rmdir()` 函数

### 2.3 读写文件操作

path对象常用的文件读写操作方法：

- `open(mode='r', buffering=-1, encoding=None, errors=None, newline=None)` 方法 打开路径指向的文件，和内置函数`open()`用法类似。Path.open()和open()相比，减少了文件路径file参数，因为创建path对象时就已经传入了文件路径。建议使用 `with path.open() as f` 语句读写文件参数说明如下：
    - mode 文件打开模式，可选值如下
        - 'r'或'rt' 读取文件（默认）
        - 'w' 写入，若文件已存在则将其清空
        - 'x' 排它性创建，如果文件已存在则失败 
        - 'a' 打开文件用于写入，如果文件存在则在末尾追加
        - 'b' 二进制模式（配合前面的参数使用）
        - 't' 文本模式（默认）（配合前面的参数使用）
        - '+' 打开用于更新（读取与写入）（配合前面的参数使用）
    - encoding 设置编码格式，常用 utf_8
    - newline 设置换行模式
    - buffering 用于设置缓冲策略
    - errors 处理错误
- `read_text(encoding=None, errors=None, newline=None)` 方法 读取文件内容，返回字符串。以字符串形式返回路径指向的文件的解码后文本内容。
- `read_bytes()` 方法 以字节对象的形式返回路径指向的文件的二进制内容
- `write_text(data, encoding=None, errors=None, newline=None)` 写入文件，同名的现有文件会被覆盖。
- `write_bytes(data)` 将文件以二进制模式打开，写入 data 并关闭，同名的现存文件将被覆盖。

