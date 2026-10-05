# os 操作系统接口

提供用于与操作系统交互的函数

## 导入

    import os

一定要使用 import os 而不是 from os import * 。这将避免内建的 open() 函数被 os.open() 隐式替换掉，因为它们的使用方式大不相同

## 常用函数

- os.getcwd() 返回当前工作目录
- os.chdir(path) 切换当前工作目录
- os.system(command) 在系统终端运行命令