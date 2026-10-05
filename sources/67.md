# DAY 5 使用提供程序

## 提供程序PSProvider

一个PowerShell的提供程序，即PSProvider，本质上是一个适配器。它可以接受某些数据存储。

查看当前shell中已存在的提供程序：

``` powershell
> Get-PSProvider

Name                 Capabilities   Drives
----                 ------------   ------
Registry             ShouldProce... {HKLM, HKCU}
Alias                ShouldProcess  {Alias}
Environment          ShouldProcess  {Env}
FileSystem           Filter, Sho... {C, D, E, F}
Function             ShouldProcess  {Function}
Variable             ShouldProcess  {Variable}
```

- `ShouldProcess` 这部分提供程序支持 `-WhatIf` 参数和 `-Confirm` 参数，保证我们在正式执行这部分脚本之前可以对他们进行测试
- `Filter` 在cmdlet中操作提供程序的数据时，支持 `-Filter` 参数
- `Credentials` 提供程序支持 `-Credentials` 参数，用于指定访问数据存储的凭据
- `Transactions` 提供程序支持事务

也可以通过某个提供程序创建一个 `PSDrive`。`PSDriver` 可以通过一个特定的提供程序链接到存储某些数据的介质。类似于Windows文件资源管理器。

查看当前已连接的驱动器：

``` powershell
> Get-PSDrive

Name           Used (GB)     Free (GB) Provider
----           ---------     --------- --------
Alias                                  Alias
C                 138.38         27.16 FileSy...
Cert                                   Certif...
D                 103.07         96.93 FileSy...
E                  18.83         81.17 FileSy...
Env                                    Enviro...
F                   8.08          1.92 FileSy...
Function                               Function
HKCU                                   Registry
HKLM                                   Registry
Variable                               Variable
WSMan                                  WSMan
```

大多数情况下，操作 `PSDrive` 的cmdlet名词部分都会包含 'item'：

``` powershell
> Get-Command -Noun *item*

CommandType     Name
-----------     ----
Function        Get-DAEntryPointTableItem
Function        Get-TestDriveItem
Function        New-DAEntryPointTableItem
Function        Remove-DAEntryPointTableItem
Function        Rename-DAEntryPointTableItem
Function        Reset-DAEntryPointTableItem
Function        Set-DAEntryPointTableItem
Cmdlet          Clear-Item
Cmdlet          Clear-ItemProperty
Cmdlet          Copy-Item
Cmdlet          Copy-ItemProperty
Cmdlet          Get-ChildItem
Cmdlet          Get-ControlPanelItem
Cmdlet          Get-Item
Cmdlet          Get-ItemProperty
Cmdlet          Get-ItemPropertyValue
Cmdlet          Get-WebItemState
Cmdlet          Invoke-Item
Cmdlet          Move-Item
Cmdlet          Move-ItemProperty
Cmdlet          New-Item
Cmdlet          New-ItemProperty
Cmdlet          Remove-Item
Cmdlet          Remove-ItemProperty
Cmdlet          Rename-Item
Cmdlet          Rename-ItemProperty
Cmdlet          Restart-WebItem
Cmdlet          Set-Item
Cmdlet          Set-ItemProperty
Cmdlet          Show-ControlPanelItem
Cmdlet          Start-WebItem
Cmdlet          Stop-WebItem
```

我们可以通过以上cmdlet命令或者它们的别名来调用提供程序。

## FileSystem的结构

Windows/MacOS/Linux文件系统主要由3种对象组成：磁盘驱动器，文件和目录（文件夹）

- 磁盘驱动器是最上层的对象，包含文件夹和文件
- 文件夹是一种容器对象，可以包含文件和其他文件夹
- 文件不是一种容器对象，它处于层级的末尾

PSDrive可能不指向某个文件系统，比如PSDrive可以映射到注册表（注册表不属于文件系统）。在powershell中，文件和文件夹都叫做项item，尽管二者本质上是两种不同的项。

每个项基本上都会存在对应的属性。如：文件项可能有最后写入时间，是否只读等属性，文件夹项可能包含子项。

- `Clear` `Copy` `Get` `Move` `New` `Remove` `Rename` `Set`等动词可以应用于文件项或文件夹项以及它们对应的属性
- `Item` 名词对应的是单独对象，如文件或文件夹
- `ItemProperty` 名词对应的是项的属性，如文件的最后写入时间等。
- `ChildItem` 名词对应的是项的子项，如文件夹的文件或子文件夹。

文件系统驱动器下的cmdlet中的命令都不支持 `UseTransaction` 参数。注册表驱动器下的cmdlet中的命令都不支持 `Filter` 参数。`Environment`这个PSProvider主要用来构造powershell中可用的ENV（类型驱动器，如Env:\PSModulePath），该驱动器主要用于访问Windows中的环境变量，它没有对应的项属性：

``` powershell
> Get-ItemProperty -Path Env:\PSModulePath
Get-ItemProperty : 无法使用接口。此提供程序不支
持 IPropertyCmdletProvider 接口。
所在位置 行:1 字符: 1
+ Get-ItemProperty -Path Env:\PSModulePath
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotImplemented: (
   :) [Get-ItemProperty], PSNotSupportedExcept
  ion
    + FullyQualifiedErrorId : NotSupported,Micr
   osoft.PowerShell.Commands.GetItemPropertyCo
  mmand
```

## 文件系统与其他数据存储的类似之处

文件系统可以算作其他数据存储的模板。如：注册表与文件系统有相同的分层结构

## 使用文件系统

### 切换目录Set-Location

类似于cmd中的 `cd` 命令，用于切换当前目录。在powershell中 `cd` 是 `Set-Location` 的别名。

``` powershell
PS C:\Users\86183> cd c:\windows
PS C:\windows> Set-Location -Path c:\desktop
PS C:\desktop>
```

### 创建项New-Item

`New-Item` 用于创建项。可以创建文件或文件夹。

`New-Item [-Path] <string[]> -ItemType Directory` 或 `New-Item [-Path] <string[]> -Type Directory` 创建文件夹，相当于`mkdir`

``` powershell
PS C:\desktop> New-Item test -ItemType Directory


    目录: C:\desktop


Mode                 LastWriteTime        Length
----                 -------------        ------
d-----         2025/7/31      8:18

PS C:\desktop> mkdir test2


    目录: C:\desktop


Mode                 LastWriteTime        Length
----                 -------------        ------
d-----         2025/7/31      8:22
```

不传入 `-ItemType` 参数时，默认创建文件。

## 使用通配符和字面路径

大部分项的cmdlet都包含 `-Path` 属性，默认情况下，该属性支持使用通配符。如果想禁用通配符，用 `-LiteralPath` 参数替代 `-Path` 参数

### 通配符

- `*` 0个或多个字符
- `?` 1个字符

这就是为什么Windows文件名中禁止使用 `*` 和 `?` 这两个字符。

在大部分其他类型的数据存储中，`*` 和 `?` 都可以出现在项item的名称中，如注册表

### 列出子项Get-ChildItem

`Get-ChildItem` 用于列出子项。可以列出文件或文件夹。`Dir` 是它的别名。

``` powershell
PS C:\windows> Get-ChildItem *.exe


    目录: C:\windows


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----         2025/6/12      8:14         122880 bfsvc.exe
-a----         2025/6/12      8:14        2943472 explorer.exe
-a----         2025/6/12      8:14        1081344 HelpPane.exe
-a----         2025/3/13     12:50          40960 hh.exe
-a----         2025/4/10     16:30         360448 notepad.exe
-a----         2023/12/7     22:20         765208 py.exe
-a----         2023/12/7     22:20         763672 pyw.exe
-a----         2025/6/12      8:14         622592 regedit.exe
-a----         2025/2/13     18:40         591432 RtkBtManServ.exe
-a----         2025/6/12      8:14         245760 splwow64.exe
-a----         2025/6/12      8:15          12288 winhlp32.exe


PS C:\windows> dir *.exe


    目录: C:\windows


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----         2025/6/12      8:14         122880 bfsvc.exe
-a----         2025/6/12      8:14        2943472 explorer.exe
-a----         2025/6/12      8:14        1081344 HelpPane.exe
-a----         2025/3/13     12:50          40960 hh.exe
-a----         2025/4/10     16:30         360448 notepad.exe
-a----         2023/12/7     22:20         765208 py.exe
-a----         2023/12/7     22:20         763672 pyw.exe
-a----         2025/6/12      8:14         622592 regedit.exe
-a----         2025/2/13     18:40         591432 RtkBtManServ.exe
-a----         2025/6/12      8:14         245760 splwow64.exe
-a----         2025/6/12      8:15          12288 winhlp32.exe
```

## 注册表提供程序

切换目录到注册表：

``` powershell
PS C:\desktop> Set-Location -Path HKCU:
PS HKCU:\> Set-Location -Path software
PS HKCU:\software> Set-Location -Path microsoft
PS HKCU:\software\microsoft> Set-Location -Path .\Windows\
PS HKCU:\software\microsoft\Windows\> Get-ChildItem


    Hive: HKEY_CURRENT_USER\software\microsoft\Windows


Name                           Property
----                           --------
AssignedAccessConfiguration
CurrentVersion
DWM                            Composition                  : 1
                               ColorPrevalence              : 0
                               ColorizationColor            : 3288365268
                               EnableAeroPeek               : 1
                               AccentColor                  : 4292114432
                               ColorizationColorBalance     : 89
                               ColorizationAfterglow        : 3288365268
                               ColorizationAfterglowBalance : 10
                               ColorizationBlurBalance      : 1
                               EnableWindowColorization     : 1
                               ColorizationGlassAttribute   : 1
MiracastDiscovery              NotificationCount   : 6
                               DisableNotification : 1
                               LastNotifiedTime    : {233, 7, 7, 0...}
RemoteSystemIntegration
Roaming
Shell
TabletPC
Windows Error Reporting        LastRateLimitedDumpGenerationTime : 133972848573425409
Winlogon


PS HKCU:\software\microsoft\Windows\> Set-ItemProperty -Path .\DWM\ -PSProperty EnableWindowColorization -Value 0
```

HKEY_CURRENT_USER目录，在powershell中显示为 `HKCU:` 驱动器，这个过程将 `EnableWindowColorization     : 1` 改为了 `EnableWindowColorization     : 0`。







