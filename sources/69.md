# 扩展命令

在 Windows 中，微软管理控制台（Microsoft Management Console，简称 MMC）是一个专门用于管理的控制台。它为 Windows 管理员提供了一个统一的、规范的管理接口和操作平台。

MMC 本身并不执行任何具体的管理操作，而是作为一个框架，允许用户加载不同的管理单元（snap - ins）来进行系统和网络管理。这些管理单元是符合 MMC 编程规范的工具，例如证书管理（certmgr.msc）、索引服务（ciadv.msc）、可移动设备管理（ntmsmgr.msc）、性能（perfmon.msc）、本地安全策略（secpol.msc）、服务（services.msc）等。

用户可以通过按下 Win + R 组合键，输入 “mmc” 后回车来打开 MMC。也可以在命令行中使用 “mmc path\filename.msc” 等命令来打开特定的控制台文件。

## 扩展：找到并添加插件

PowerShell存在两种类型的扩展：模块和管理单元。

### 管理单元

一个适合管理单元PowerShell的名字是PSSnapin，用于区别这些来自管理单元的图形MMS。PSSnapins在PowerShell v1版本的时候就已经存在。一个PSSnapin通常包含一个或多个DLL文件，同时包含配置XML文件和帮助文档。PSSnapins必须先安装和注册，然后PowerShell才能识别它的存在。

PSSnapin的概念逐步被微软移除了，将来可能会越来越少出现。在内部，微软的重点是提供扩展模块。

获取可用的管理单元列表：

``` powershell
> Get-PSSnapin -Registered


Name        : SqlServerCmdletSnapin100
PSVersion   : 5.1
Description : This is a PowerShell snap-in that includes various SQL Server cmdlets.

Name        : SqlServerProviderSnapin100
PSVersion   : 5.1
Description : SQL Server Provider
```

上面的信息说明我的机器上安装了两个可用的管理单元，但是并没有加载。

可以通过运行Get-PSSnapin命令查看已加载的列表。该列表包含所有的核心，包含PowerShell中的本机功能的自动加载管理单元：

``` powershell
> Get-PSSnapin


Name        : Microsoft.PowerShell.Core
PSVersion   : 5.1.26100.4202
Description : 此 Windows PowerShell 管理单元包含用于管理 Windows PowerShell 组件的 cmdlet。
```

通过运行Add-PSSnapin并指定管理单元名称的方式加载某一个管理单元：

``` powershell
> add-pssnapin sqlserverCmdletsnapin100
> Get-PSSnapin


Name        : Microsoft.PowerShell.Core
PSVersion   : 5.1.26100.4202
Description : 此 Windows PowerShell 管理单元包含用于管理 Windows PowerShell 组件的 cmdlet。

Name        : sqlservercmdletsnapin100
PSVersion   : 5.1
Description : This is a PowerShell snap-in that includes various SQL Server cmdlets.
```

PSSnapin可以增加Cmdlets命令、提供PSDrive，或者两者都增加。使用`Get-Command`（或者别名：`Gcm`）命令找出已增加的Cmdlets命令：

``` powershell
> gcm -PSSnapin sqlservercmdletsnapin100

CommandType     Name                                               Version    Source
-----------     ----                                               -------    ------
Cmdlet          Invoke-PolicyEvaluation                            10.0.0.0   sqlservercmdletsnapin100
Cmdlet          Invoke-Sqlcmd                                      10.0.0.0   sqlservercmdletsnapin100
```

再把添加另一个没有加载的管理单元：

``` powershell
> Add-PSSnapin SqlServerProviderSnapin100
> Get-PSSnapin


Name        : Microsoft.PowerShell.Core
PSVersion   : 5.1.26100.4202
Description : 此 Windows PowerShell 管理单元包含用于管理 Windows PowerShell 组件的 cmdlet。

Name        : sqlservercmdletsnapin100
PSVersion   : 5.1
Description : This is a PowerShell snap-in that includes various SQL Server cmdlets.

Name        : SqlServerProviderSnapin100
PSVersion   : 5.1
Description : SQL Server Provider

> Get-PSProvider

Name                 Capabilities                                      Drives
----                 ------------                                      ------
Registry             ShouldProcess, Transactions                       {HKLM, HKCU}
Alias                ShouldProcess                                     {Alias}
Environment          ShouldProcess                                     {Env}
FileSystem           Filter, ShouldProcess, Credentials                {C, D, E, F}
Function             ShouldProcess                                     {Function}
Variable             ShouldProcess                                     {Variable}
SqlServer            Credentials                                       {SQLSERVER}
```

在输出中看到了 `SqlServer` 说明sql server驱动器已被添加到shell中。由SQL Server的PSDrive提供驱动。

## 扩展：找到并添加模块

PowerShell提供的第二种扩展方式称为模块。模块被设计
得更加独立，因此更加容易分发，但是它的工作原理类似于PSSnapins。模块不需要复杂的注册。PowerShell会自动在一个特定的目录下查找模块。PSModulePath这个环境变量定义了PowerShell期望存放模块的路径：

``` powershell
> Get-Content Env:\PSModulePath
D:\Documents\WindowsPowerShell\Modules;C:\Program Files\WindowsPowerShell\Modules;C:\WINDOWS\system32\WindowsPowerShell\v1.0\Modules
```

只要知道一个模块的完整路径，你就可以从任何其他的位置添加模块。PSModulePath并不能在PowerShell中修改，它是操作系统环境变量的一部分。你可以在系统控制面板中对它进行修改，或者通过组策略修改。一些微软或第三方产品可能会修改该变量。

在PowerShell中，该路径很重要。如果你有位于其他位置的模块，你应该把模块所在的路径加入到PSModulePath这个环境变量中。

通过PSModulePath环境变量，PowerShell可以自动加载位于计算机上的所有模块。PowerShell会自动发现这些模块。它看起来好像是所有的模块都已被加载了。查看一个模块的帮助，会发现你不需要手动加载它。运行任何的命令，PowerShell都会自动加载该命令相关的模块。PowerShell的Update-Help命令同样使用PSModulePath发现已存在的任何模块，然后针对每个模块搜索需要更新的帮助文档。

即使在模块还没有显式加载到内存的情况下，PowerShell依然可以自动发现模块从而使得Shell完成命令名称自动补全、显示帮助和运行命令。该特性使得保持PSModulePath环境变量的完整和最新很有必要。

如果一个模块不在被PSModulePath引用的任何一个目录下，你应该使用Import- Module命令并指定模块的完整路径，如
C:\MyPrograms\Something\MyModule。如果在开始菜单中有一个特定产品Shell的快捷方式，比如说Share Point Server，而你却不知道该产品安装PowerShell模块的路径，打开快捷方式图标的属性，在快捷方式的目标属性中会包含使用Import-Module命令需要的模块名和路径。模块还可以添加PSDrive提供程序。运行Get-PSProvider命令可以确定有哪些新的提供程序。

## 命令冲突和移除扩展

大多数的PowerShell扩展（Exchange Server是一个明显的例外）都在它们命令名的名词部分增加了一个短的前缀，如Get-ADUser和Invoke-SqlCmd。这些前缀看起来有些多余，但是它们可以防止命令名称的冲突。

例如，假设你加载的两个模块中都包含了Get-User这个Cmdlet命令。这样两个命令名称相同，且被同时加载。你运行Get-User时，PowerShell执行最后一个加载模块的命令。但是另外一个名称相同的命令却无法再被访问。为了明确所需运行的具体命令，你需要使用看起来有点多余的命名规则，它包括管理单元名称和命令名称。如果Get-User来自一个叫作MyCoolPowerShellSnapin的模块单元，你需要使用下面的方式运行。

MyCoolPowerShellSnapin\Get-User

这需要输入很多内容，这就是为什么微软建议添加特定产品前缀，如在每个命令的名词中加入AD或者SQL。增加前缀可以防止冲突，并且使命令更容易识别和使用。

如果你已经对冲突不厌其烦，你可以随时选择删除冲突的扩展名。你需要运行Remove-PSSnapin或Remove-Module，并指定管理模块或模块命令的名称，从而卸载某个扩展

## 玩转一个新的模块

我们的目标是清除我们计算机上的DNS名称解析缓存。我们还不知道PowerShell是否能做到这一点，所以我们先要在帮助系统中寻找一些线索。

``` powershell
> Get-Help *dns*                                                                                                                                                                                                               Name                              Category  Module                    Synopsis                                          ----                              --------  ------                    --------                                          dnsn                              Alias                               Disconnect-PSSession                              Set-DnsClient                     Function  DnsClient                 ...                                               Remove-DnsClientNrptRule          Function  DnsClient                 ...                                               Get-DnsClientDohServerAddress     Function  DnsClient                 ...                                               Set-DnsClientNrptGlobal           Function  DnsClient                 ...                                               Set-DnsClientServerAddress        Function  DnsClient                 ...                                               Get-DnsClientServerAddress        Function  DnsClient                 ...                                               Add-DnsClientNrptRule             Function  DnsClient                 ...                                               Clear-DnsClientCache              Function  DnsClient                 ...                                               Get-DnsClient                     Function  DnsClient                 ...                                               Set-DnsClientDohServerAddress     Function  DnsClient                 ...                                               Add-DnsClientDohServerAddress     Function  DnsClient                 ...
Set-DnsClientNrptRule             Function  DnsClient                 ...
Get-DnsClientNrptGlobal           Function  DnsClient                 ...
Get-DnsClientNrptRule             Function  DnsClient                 ...
Set-DnsClientGlobalSetting        Function  DnsClient                 ...
Remove-DnsClientDohServerAddress  Function  DnsClient                 ...
Get-DnsClientCache                Function  DnsClient                 ...
Get-DnsClientNrptPolicy           Function  DnsClient                 ...
Resolve-DnsName                   Cmdlet    DnsClient                 Resolve-DnsName...
Get-DnsClientGlobalSetting        Function  DnsClient                 ...
Register-DnsClient                Function  DnsClient                 ...
Get-NetDnsTransitionConfiguration Function  NetworkTransition         ...
Reset-NetDnsTransitionConfigur... Function  NetworkTransition         ...
Disable-NetDnsTransitionConfig... Function  NetworkTransition         ...
Get-NetDnsTransitionMonitoring    Function  NetworkTransition         ...
Enable-NetDnsTransitionConfigu... Function  NetworkTransition         ...
Set-NetDnsTransitionConfiguration Function  NetworkTransition         ...
Add-VpnConnectionTriggerDnsCon... Function  VpnClient                 ...
Set-VpnConnectionTriggerDnsCon... Function  VpnClient                 ...
Remove-VpnConnectionTriggerDns... Function  VpnClient                 ...
```

上面显示的就是我们计算机上所有的DnsClient模块。里面并没有找到与清空DNS缓存有关的命令。为了找出该命令，我们手动加载该模块并列出所有命令。

``` powershell
> Import-Module -name DnsClient
> Get-Command -Module DnsClient

CommandType     Name                                               Version    Source
-----------     ----                                               -------    ------
Function        Add-DnsClientDohServerAddress                      1.0.0.0    DnsClient
Function        Add-DnsClientNrptRule                              1.0.0.0    DnsClient
Function        Clear-DnsClientCache                               1.0.0.0    DnsClient
Function        Get-DnsClient                                      1.0.0.0    DnsClient
Function        Get-DnsClientCache                                 1.0.0.0    DnsClient
Function        Get-DnsClientDohServerAddress                      1.0.0.0    DnsClient
Function        Get-DnsClientGlobalSetting                         1.0.0.0    DnsClient
Function        Get-DnsClientNrptGlobal                            1.0.0.0    DnsClient
Function        Get-DnsClientNrptPolicy                            1.0.0.0    DnsClient
Function        Get-DnsClientNrptRule                              1.0.0.0    DnsClient
Function        Get-DnsClientServerAddress                         1.0.0.0    DnsClient
Function        Register-DnsClient                                 1.0.0.0    DnsClient
Function        Remove-DnsClientDohServerAddress                   1.0.0.0    DnsClient
Function        Remove-DnsClientNrptRule                           1.0.0.0    DnsClient
Function        Set-DnsClient                                      1.0.0.0    DnsClient
Function        Set-DnsClientDohServerAddress                      1.0.0.0    DnsClient
Function        Set-DnsClientGlobalSetting                         1.0.0.0    DnsClient
Function        Set-DnsClientNrptGlobal                            1.0.0.0    DnsClient
Function        Set-DnsClientNrptRule                              1.0.0.0    DnsClient
Function        Set-DnsClientServerAddress                         1.0.0.0    DnsClient
Cmdlet          Resolve-DnsName                                    1.0.0.0    DnsClient
```

Clear-DnsClientCache可以清除DNS缓存

``` powershell
> Clear-DnsClientCache
> Clear-DnsClientCache -Verbose
详细信息: The specified name resolution records cached on this machine will be removed.
Subsequent name resolutions may return up-to-date information.
```

所有的命令都有-verbose开关参数，但并不是所有命令都会实现该参数。在该示例中，我们得到一个指示发生了什么事情的信息，这让我们知道这个命令已经成功运行。

## 从Internet获取模块

微软引入了一个名称为PowerShellGet的模块，这使得从在线仓库中搜索、下载、安装、升级模块变得容易了。PowerShellGet很像Linux管理员喜爱的包管理器 RPM、YUM、apt-get等。微软甚至还维护一个在线源，称为 [PowerShell Gallery](http://powershellgallery.com)

运行Register-PSRepository添加一个源的URL。http://PowerShellGallery.com 通常是默认设置，但也可以添加自用的“gallery”，并利用Register-PSRepository指向该地址。使用Find-Module在源中查找模块。你可以在名称、特定标签等列中使用通配符缩小搜索结果。找到所需的模块后，使用Install-Module下载与安装一个模块。使用Update-Module确保你的模块的副本是最新的，如果不是，下载最新版本并安装。

