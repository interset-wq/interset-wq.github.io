# DAY 9 深入理解管道

这些命令（比如`Get-Process | Sort VM-desc | ConvertTo-HTML | Out-File process.html`）的功能非常强大。如果采用其他脚本语言实现相同功能，可能需要编写多行代码，但是利用PowerShell，仅需要单行命令即可。

## 管道：更少的输入，更强大的功能

单行的PowerShell命令功能如此强大，主要在于PowerShell管道的工作机制。

## PowerShell如何传输数据给管道

当将两条命令串联在一起时，PowerShell必须搞清楚怎样将第一条命令的输出作为第二条命令的输入。在下面的示例中，我们将第一条命令称为命令A，这条命令会产生某些结果。第二条命令称为命令B，它会接收命令A产生的结果集，然后完成自己的工作。

``` powershell
> CommandA | CommandB
```

你可能希望将这部分计算机名称作为某些命令的传入数据，以便该命令会在这些计算机上被运行，比如下面的例子。

PS C:\> Get-Content .\computers.txt | Get-Service
当运行Get-Content命令时，它会将文本文件中的计算机名称放入管道中。之后PowerShell再决定如何将该数据传递给Get-Service命令。但PowerShell一次只能使用单个参数接收传入数据。也就是说，PowerShell必须决定由Get-Service的哪个参数接收Get-Content的输出结果。这个决定的过程就称为管道参数绑定（Pipeline parameter binding）。PowerShell使用两种方法将Get-Content的输出结果传入给Get-Service的某个参数。该Shell尝试使用的第一种方法称为ByValue；如果这种方法行不通，它将会尝试ByPropertyName。