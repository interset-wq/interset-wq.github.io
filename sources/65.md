# DAY 3 使用帮助系统

命令行接口，即CLIs(command-line interfaces)

RTFM(Read The Friendly Manual)帮助文档

Cmdlet，即powershell独有的概念，绝大多数powershell命令都可以看作是cmdlet

## 通过help查看某条命令的帮助文档

``` powershell
PS C:\Users\86183> help Get-Service

名称
    Get-Service

语法
    Get-Service [[-Name] <string[]>]  [<CommonParameters>]

    Get-Service  [<CommonParameters>]

    Get-Service  [<CommonParameters>]


别名
    gsv


备注
    Get-Help 在此计算机上找不到该 cmdlet 的帮助文件。它仅显示部分帮助。
        -- 若要下载并安装包含此 cmdlet 的模块的帮助文件，请使用 Update-Help。
        -- 若要联机查看此 cmdlet 的帮助主题，请键入: "Get-Help Get-Service -Online" 或
           转到 https://go.microsoft.com/fwlink/?LinkID=113332。
```

## 更新帮助文档

``` powershell
PS C:\Users\86183> Update-Help
```

> [!IMPORTANT]
> 在管理员身份下使用。此命令会自动下载最新的powershell官方文档

指定下载帮助文档的url

``` powershell
PS C:\Users\86183> Update-Help -SourcePath http://github.com/powershell
```

从指定的url下载帮助文档

## 将帮助文档保存到本地

``` powershell
PS C:\Users\86183> Save-Help C:\Desktop\new  
```

将帮助文档下载到桌面上的new目录中

## 获取帮助

使用cmdlet命令 `Get-Help` 可以获取帮助。使用 `Help` 或 `Man` 也可以获取帮助，它们二者都是对cmdlet命令封装后的函数。只不过 `Get-Help` 是一次性显示，`Help` 和 `Man` 是分页显示，使用空格键翻页，`Man` 是 `Help` 的别名。在控制台中CTRL+C组合键是返回，并不是复制

### Help分页显示帮助文档

``` powershell
PS C:\Users\86183> Help Get-Content

名称
    Get-Content

语法
    Get-Content [-Path] <string[]>  [<CommonParameters>]

    Get-Content  [<CommonParameters>]


别名
    gc
    cat
    type


备注
    Get-Help 在此计算机上找不到该 cmdlet 的帮助文件。它仅显示部分帮助。
        -- 若要下载并安装包含此 cmdlet 的模块的帮助文件，请使用 Update-Help。
        -- 若要联机查看此 cmdlet 的帮助主题，请键入: "Get-Help Get-Content -Online" 或
           转到 https://go.microsoft.com/fwlink/?LinkID=113310。
-- More  --
```

### Get-Help一次性显示帮助文档

```powershell

PS C:\Users\86183> Get-Help Get-Content

名称
    Get-Content

语法
    Get-Content [-Path] <string[]>  [<CommonParameters>]

    Get-Content  [<CommonParameters>]


别名
    gc
    cat
    type


备注
    Get-Help 在此计算机上找不到该 cmdlet 的帮助文件。它仅显示部分帮助。
        -- 若要下载并安装包含此 cmdlet 的模块的帮助文件，请使用 Update-Help。
        -- 若要联机查看此 cmdlet 的帮助主题，请键入: "Get-Help Get-Content -Online" 或
           转到 https://go.microsoft.com/fwlink/?LinkID=113310。
```

### Get-Help使用分页显示模式

``` powershell
PS C:\Users\86183> Get-Help Get-Content | More

名称
    Get-Content

语法
    Get-Content [-Path] <string[]>  [<CommonParameters>]

    Get-Content  [<CommonParameters>]


别名
    gc
    cat
    type


备注
    Get-Help 在此计算机上找不到该 cmdlet 的帮助文件。它仅显示部分帮助。
        -- 若要下载并安装包含此 cmdlet 的模块的帮助文件，请使用 Update-Help。
        -- 若要联机查看此 cmdlet 的帮助主题，请键入: "Get-Help Get-Content -Online" 或
           转到 https://go.microsoft.com/fwlink/?LinkID=113310。
-- More  --
```

## 查找命令

`Get-Help` 的 `-Name` 参数可以用来查找命令，这个参数是一个位置参数，使用时用需要查找的命令替换 Name，支持使用通配符

``` powershell
PS C:\Users\86183> Help *event*

Name                              Category  Module                    Synopsis
----                              --------  ------                    --------
Clear-EventLog                    Cmdlet    Microsoft.PowerShell.M... ...
Get-EventLog                      Cmdlet    Microsoft.PowerShell.M... ...
Limit-EventLog                    Cmdlet    Microsoft.PowerShell.M... ...
New-EventLog                      Cmdlet    Microsoft.PowerShell.M... ...
Register-WmiEvent                 Cmdlet    Microsoft.PowerShell.M... ...
Remove-EventLog                   Cmdlet    Microsoft.PowerShell.M... ...
Show-EventLog                     Cmdlet    Microsoft.PowerShell.M... ...
Write-EventLog                    Cmdlet    Microsoft.PowerShell.M... ...
Get-Event                         Cmdlet    Microsoft.PowerShell.U... ...
Get-EventSubscriber               Cmdlet    Microsoft.PowerShell.U... ...
New-Event                         Cmdlet    Microsoft.PowerShell.U... ...
Register-EngineEvent              Cmdlet    Microsoft.PowerShell.U... ...
Register-ObjectEvent              Cmdlet    Microsoft.PowerShell.U... ...
Remove-Event                      Cmdlet    Microsoft.PowerShell.U... ...
Unregister-Event                  Cmdlet    Microsoft.PowerShell.U... ...
Wait-Event                        Cmdlet    Microsoft.PowerShell.U... ...
Register-CimIndicationEvent       Cmdlet    CimCmdlets                Register-CimIndicationEvent...
Get-WinEvent                      Cmdlet    Microsoft.PowerShell.D... Get-WinEvent...
-- More  --
```

查找和事件日志有关的命令。`Help` 本质上是搜索帮助主题，并不是搜索cmdlet命令，因为每个cmdlet都有一个帮助文件，这就使 `Help` 可以实现查找命令。

可以直接使用 `Get-Command` 来查找cmdlet命令，它的别名是 `Gcm`，用法与 `Help` 类似。

- `Get-Command -noum *event*` 返回一个关于event命令的列表
- `Get-Command -verb Get` 返回一个具有Get的命令列表
- `Get-Command *log* -type Cmdlet` 返回一个所有Cmdlet命令名称包含log的列表

## 帮助详解

``` powershell
PS C:\Users\86183> Get-Help Get-EventLog

名称
    Get-EventLog

语法
    Get-EventLog [-LogName] <string> [[-InstanceId] <long[]>]  [<CommonParameters>]

    Get-EventLog  [<CommonParameters>]
```

- 通用参数 `[<CommonParameters>]` 每个cmdlet命令的参数结尾都有 `[<CommonParameters>]`，反之每个cmdlet命令都是使用的一组包含8个参数的集合
- 可选参数 用方括号包裹的参数是可选的，这种情况才是可选参数，例如 `[<CommonParameters>]`是可选参数， `[[-InstanceId] <long[]>]`是可选位置参数
- 位置参数 只有参数名被方括号包裹的参数，例如 `[-LogName] <string>` 这是个位置参数，必选参数。因为它的参数名 `[-LogName]` 被方括号包裹，参数值类型 `<string>` 不被方括号包裹

### 查看更详细的帮助文档

`Help` 的 `-full` 选项可以更详细的显示帮助文档

``` powershell
PS C:\Users\86183> Help Get-Event -full

名称
    Get-Event

语法
    Get-Event [[-SourceIdentifier] <string>]  [<CommonParameters>]

    Get-Event [-EventIdentifier] <int>  [<CommonParameters>]


参数
    -EventIdentifier <int>

        是否必需?                    True
        位置?                        0
        是否接受管道输入?            True (ByPropertyName)
        参数集名称          ById
        别名                     Id
        动态?                    false

    -SourceIdentifier <string>

        是否必需?                    False
        位置?                        0
        是否接受管道输入?            True (ByPropertyName)
        参数集名称          BySource
        别名                     无
        动态?                    false

    <CommonParameters>
        此 Cmdlet 支持常见参数: Verbose、Debug、
        ErrorAction、ErrorVariable、WarningAction、WarningVariable、
        OutBuffer、PipelineVariable 和 OutVariable。有关详细信息，请参阅
        about_CommonParameters (https:/go.microsoft.com/fwlink/?LinkID=113216)。


输入
    System.String
    System.Int32


输出
    System.Management.Automation.PSEventArgs


别名
    无
```

常用输入类型：

- `string` 字符串，如果字符串中有空格等空白字符时，需要使用引号包裹，单引号和双引号都可以，推荐使用单引号
    - `string[]` 字符串列表，字符串集合，表示可以传入多个字符串，使用逗号分隔。如果需要传入的值有很多，可以使用文本文档`.txt`，每行写一个值，然后把这个文档传入对应的参数中。也可以每输入一个参数回车一次，确认传参完毕之后，再次回车
- `Int` `Int32` `Int64` 整型
- `DateTime` 日期，日期的表示格式受电脑所在的时区的影响

圆括号 `()` 的作用与数学运算类似，可以提高命令执行的优先级，被圆括号包裹的命令先执行

### 查看帮助文档用法举例

和 `-full` 参数用法类似，在命令某位添加 `-example`即可

## 访问 about 主题

背景主题又叫关于主题，它们都以 `about_` 开头

## 在线帮助文档

类似于 `-full` 和 `-example` 选项，`-online`选项会自动打开浏览器查看帮助文档