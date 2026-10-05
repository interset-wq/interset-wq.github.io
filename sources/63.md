# DAY 1 背景介绍

用户图形化界面（GUI）是Windows的最大特点

名词解释：

- 64位操作系统 x64
- 32位操作系统 x86
- 图形化powershell集成脚本环境，即ISE

反引号`之后不要随意添加空格等空白字符

## 检查powershell版本

``` powershell
PS C:\Users\86183> $PSVersionTable

Name                           Value
----                           -----
PSVersion                      5.1.26100.4202
PSEdition                      Desktop
PSCompatibleVersions           {1.0, 2.0, 3.0, 4.0...}
BuildVersion                   10.0.26100.4202
CLRVersion                     4.0.30319.42000
WSManStackVersion              3.0
PSRemotingProtocolVersion      2.3
SerializationVersion           1.1.0.1
```

## PowerShell的两个组件

- 基于文本的标准控制台powershell.exe，即终端命令行
- 集成了命令行环境的图形化界面powershell_ise.exe，即ISE


