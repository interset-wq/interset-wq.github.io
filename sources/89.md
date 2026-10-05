# sys 和 argparse

## sys 

### 命令行参数

一般的工具脚本常常需要处理命令行参数。 这些参数以列表形式存储在 sys 模块的 argv 属性中。

### 错误输出重定向和程序终止

sys 模块还具有 stdin ， stdout 和 stderr 的属性。后者对于发出警告和错误消息非常有用，即使在 stdout 被重定向后也可以看到它们

终止脚本的最直接方法是使用 sys.exit()

## argparse 命令行参数

argparse 模块提供了一种更复杂的机制来处理命令行参数。