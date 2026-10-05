# DAY 10 格式化及如何正确使用

PowerShell Cmdlets可以用于生成对象，并且这些对象通常含有比PowerShell默认所显示的属性多。使用“Gm”命令可以获取一个对象的所有属性，使用“Select-Object”自定义想看到的属性。

## 默认格式

现在运行一下我们熟悉的命令“Get-Process”，然后注意结果的列头部分。可以看到，报表列头部分的名称与属性名称并不完全相符。每个列头都有固定的宽度、别名等。这些结果来自于某些配置文件。你可
以在安装PowerShell的路径下找到其中一个名为“.format.pslxml”的文件。其中进程对象的格式化目录在“DotNetTypes.format.pslxml”中。

下面我们先修改PowerShell的安装目录，并且打开
“DotNetType.format.pslxml”文件。注意，不要保存对该文件的任何变更。该文件带有数字签名，即使一个简单的回车或者空格，都会影响签名并阻止PowerShell从中获取信息。下面的命令适合于powershell5

```
PS C:\Users\86183> cd $PSHOME
PS C:\Windows\System32\WindowsPowerShell\v1.0> notepad dotnettypes.format.ps1xml
```

然后从中找出准确的类型并返回给Get-Process”。

```
> get-process | gm
```

