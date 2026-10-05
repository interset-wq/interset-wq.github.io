# 管道：连接命令

## 通过管道连接命令

powershell通过管道 `|` 连接命令。管道通过传输一个命令，把其输出作为另一个cmdlet的输入，使第二个命令可以通过第一个的结果作为输入并联合起来运行。

``` powershell
PS C:\Desktop> Dir | More


    目录: C:\Desktop


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         2025/7/29     19:13                新建文件夹
-a----         2025/7/10     10:12            601 FinalShell.lnk
-a----         2025/7/31     10:24       20130571 progit.pdf
-a----         2025/7/24     17:43            670 ShareX.lnk
-a----         2025/6/17     19:47            820 Visual Studio Code.lnk
-a----         2025/2/16     22:21            684 XMind 8 Update 9.lnk
```

上面的例子就是把 `dir` 的输出结果作为 `More` 的输入。

## 输出结果到CSV或XML文件

### CSV表格

``` powershell
PS C:\Desktop> Get-Process | Export-Csv procs.csv
```

将 `Get-Process` 的输出结果写入 `procs.csv` 文件，并保存到桌面

这个csv表格的第一行是 `#TYPE System.Diagnostics.Process`，这是一个注释 （`#`用来注释），代表文件中包含的信息类型。这个csv文件中显示的内容比控制台显示的内容更详细，因为控制台只输出一些比较重要的信息

在控制台导入csv文件，查看其内容：

``` powershell
PS C:\Desktop> Import-Csv procs.csv
```

### XML

`Export-clixml` 命令，用于创建常规的命令行界面可扩展标记语言文件 generic command-line interface (CLI) extensible makeup language (XML)。`clixml` 是powershell专用的，但是任何可以解析xml文件的程序都能够读取它。还有 `Import-clixml` 命令，所有的以 `import` 和 `export` 开头的cmdlet都需要传入文件名参数。

### 对比文件

`Compare-Object` 用于对比文件的差异，它的别名是 `Diff`。建议使用 `diff` 别名

``` powershell
> Get-Process | Export-Clixml reference.xml
> diff -ReferenceObject (Import-Clixml .\reference.xml) -DifferenceObject (Get-Process) -Property name

name               SideIndicator
----               -------------
ai                 =>
backgroundTaskHost =>
chrome             =>
chrome             =>
chrome             =>
chrome             =>
chrome             =>
chrome             =>
chrome             =>
chrome             =>
conhost            =>
msedgewebview2     =>
msedgewebview2     =>
msedgewebview2     =>
msedgewebview2     =>
msedgewebview2     =>
msedgewebview2     =>
msedgewebview2     =>
mspaint            =>
olk                =>
RuntimeBroker      =>
RuntimeBroker      =>
tasklist           =>
WINWORD            =>
audiodg            <=
ChsIME             <=
MSPCManagerCore    <=
rundll32           <=
smartscreen        <=
svchost            <=
```

通过 `Get-Process | Export-Clixml reference.xml` 导出xml文件之后，又打开了一些应用程序，通过 `diff`命令可以比对前后数据的差异。`=>` 代表只存在与 `-DifferenceObject` 的内容， `<=` 代表只存在与 `-ReferenceObject` 中的内容，二者都有的内容不会出现在输出结果中。 `()` 可以提高命令执行的优先级

## 管道传输到文件或打印机

powershell的输出一般是在控制台上面，但是可以修改它输入内容的位置，使其可以保存到文件中或是通过打印机打印到纸上。

``` powershell
> dir > DirectoryList.txt
> dir | Out-File DirectoryList2.txt
```

以上两个命令结果是相同的，都是将 `dir` 的输出结果保存到txt文件中，但是第一种通过 `>` 写法是兼容cmd的写法，第二种是powershell的写法

`Out-File` 提供了一些参数让你定制替代的字符编码（如UTF8或Unicode）、追加内容到现有文件等功能。默认情况下，用“Out-File”创建的文件有80列宽，这种默认的80列宽可能会导致一些内容原本的排版格式被破坏，使可读性变差。

PowerShell有很多 `out` 开头的cmdlet，其中一个叫 `out-default`

``` powershell
> dir
> dir | Out-Default | Out-Host
```

当你运行 `dir` 时，实际上是在运行 `Dir | Out-Default | Out-Host` 而“Out-Host”是显示结果到显示器中。

- `out-printer` 用于将输出结果打印到打印机，没有打印机是输出为pdf
- `out-gridview` 用于将输出结果显示在网格视图中，通过powershell ise显示

## 转换成html

只需要通过管道将结果传递给“ConvertTo-HTML”命令即可。该命令可以生成结构良好的、通用的HTML数据，并可以在任何Web浏览器中打开。但是这只是原始数据，如果需要美观，需要引用CSS（Cascading Style Sheet）文件定制样式。

``` powershell
> Get-Service | ConvertTo-Html
```

该命令不需要文件名，直接在控制台输出这个html文件的内容。

``` powershell
> Get-Service | ConvertTo-Html | Out-File services.html
```

输出为html文件。

PowerShell附带其他`ConvertTo`开头的cmdlet，包括“ConvertTo-CSV”和“ConvertTo-XML”等。正如“ConvertTo-HTML”一样，这些命令都不在磁盘上创建文件，只是把命令的输出结果分别转换成CSV或XML。你需要用管道把它们和“Out-File”连接起来以便存储到磁盘上，和使用“Export-CSV”或“Export-CliXML”效果类似。另外，它们能既转换又存储。

## 使用cmdlet修改系统：终止进程和停止服务

> [!WARNING]
> 不要运行下面这个命令，否则电脑会蓝屏死机

``` powershell
> Get-Process | Stop-Process
```

这个命令会关闭所有的进程，会导致电脑死机。带有相同名词（本例中的进程Process）的Cmdlets可以在彼此之间互传信息。通常情况下，你最好带上特定进程名称而不是终止全部进程：

``` powershell
> Get-Process -Name Notepad | Stop-Process
```

上面的代码结束Windows记事本notepad的进程，会关闭记事本。

服务也是类似的，“Get-Service”命令的输出结果能和其他Cmdlets（如Stop-Service、Start-Service、Set-Service等）一起被管道传输。

类似于 “Stop-Service”和“Stop-Process” 的 Cmdlets以某些方式修改系统，并且有一个内部定义的影响级别（impact level）。Cmdlet的创建者已经设定了这些影响级别，并且不允许修改。而Shell有一个相应的“$ConfirmPreference”设置，默认为“High”。可以通过下面的命令查看你的Shell的设置：

``` powershell
> $ConfirmPreference
High
```

工作原理：当Cmdlet的内部影响级别大于等于Shell的“$ConfirmPreference”设置时，不管Cmdlet正准备做什么，Shell都会自动询问是否进行此操作。当Cmdlet的内部影响级别小于Shell的“$ConfirmPreference”设置时，不会自动弹出这个提示。也就是说，如果权限较高的cmdlet在执行修改系统的操作时，不会提示用户是否进行此操作。

在末尾添加 `-confirm`参数，对于某些被支持的用于修改系统的Cmdlet，会弹出提示，并对这些被支持的Cmdlet显示对应的帮助文档。或者使用 `-whatif` 参数，也可以达成类似的效果。

## 读取文件

`Get-Content` 用于读取文件内容。它的别名是 `cat` `type`

`Import`开头的cmdlet会关注文件中的内容，尝试解析它们，然后创建一个比原始命令看上去更加顺眼的输出结果。如果你使用“Export-CSV”创建文件，可以使用“Import-CSV”命令来读取它们。如果使用“Export-CliXML”命令创建文件，通常建议使用“Import-CliXML”命令读取。使用这些配套命令可以得到更好的结果。仅在从一个文本文件中读取内容并且不需要PowerShell解析数据时，才使用“Get-Content”命令，也就是你仅需要原始内容。