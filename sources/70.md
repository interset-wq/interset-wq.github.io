# 对象：数据的另一个名称

## 对象

运行PowerShell中的`Get-Process`。可以看到一个包含多列的表格，但这些信息仅仅是关于进程的冰山一角。进程对象还包括机器名、主窗口句柄、最大工作集大小、退出代码和时间、处理器掩码信息以及其他大量信息。实际上，你可以找出超过60个与进程有关的信息。PowerShell仅仅展示少量的信息，原因非常简单，PowerShell当然可以提供屏幕上所无法容纳的更多的信息。当运行任意命令，比如Get-Process、Get-Service、Get-EventLog或其他命令时，PowerShell会在内存中完全构造用于容纳关于项的所有信息的表格。例如Get-Process，该表格由67列组成，每行对应运行在计算机中的一个进程。每一列包含一部分信息，比如说虚拟内存、CPU利用率、处理器名称、进程ID等。然后，PowerShell会检查你是否指定所需查看的列。如果你未指定想查看的列，Shell会查看由微软提供的配置文件并只显示微软认为你希望查看的列。

一种查看所有列的方式是使用ConvertTo-HTML命令：

``` powershell
Get-Process | ConvertTo-Html | Out-File processes.html
```

该命令不会过滤列，而是生成包含所有列的HTML文件。这是查看整个表的一种方式。

除去包含这些信息的列之外，表中每一行都有一些与之对应的方法。这些方法包括操作系统可以以进程为目标进行的操作。比如说，操作系统可以关闭进程、杀死进程、刷新信息，或者等待进程退出等。

每当运行一个可以产生结果的命令时，输出结果在内存中以表的形式存放。当将输出结果以管道的方式由一个命令传送给另一个命令时，比如说：

`> Get-Process | ConvertTo-HTML`

整个表通过管道进行传输。该表在传输过程中并不会过滤到只有一小部分列，而是直到所有的命令都运行后才会进行过滤。

下面是一些术语的变化。PowerShell并不会将这些内存中的表命名为“表”，而是使用下述4个术语。

- 对象——这也就是所谓的“表行”。它代表单个事物，比如说单个进程或是单个服务。
- 属性——这也就是所谓的“表列”。它代表关于对象的一部分信息，比如说进程名称、进程ID或服务状态。
- 方法——这也就是所谓的“行为”。方法与某个对象关联并使得对象完成某些任务，比如说杀死进程或启动服务。
- 集合——这是整个对象的集合，我们曾称之为“表”。

## 理解对象

powershell使用对象代表数据。

第一个原因是Windows本身就是一个面向对象的操作系统，大部分在Windows上运行的软件是面向对象的。选择以对象集合的方式组织数据非常容易，因为大多数操作系统适用这种结构的数据。

另一个使用对象的原因是这样会使事情简单，并给你提供更加强大的功能和更好的灵活性。这使得不来你的窗口调整为什么大小，都能美观的输出结果到控制台。

PowerShell使用对象消除所有的文本操作开销。由于对象的工作机制类似内存中的表，因此你无须告知PowerShell信息所在的文本位置，而是仅仅需要输入列名。无论在屏幕或文件中如何组织输出结果，PowerShell都知道去哪里获取数据，内存表总是同一个，因此你永远都不需要由于移动列而重写命令。这样的好处是你更多专注于如何实现功能，而不是这类不必要的开销。

- Linux或UNIX都是基于文本的操作系统，因此文本对这些操作系统意义重大。
- Windows并不是基于文本，而是基于API的操作系统，Windows重度依赖对象模型。因此PowerShell以更原生的方式与Windows共同工作。

## 探索对象：Get-Member

如果说对象就像内存中一个巨大的表，而PowerShell仅仅在屏幕上展示表的一部分，有些我们需要使用的属性可能并没有显示在屏幕上。

如果需要了解更多关于对象的内容，使用命令：`Get-Member`，它的别名是 `Gm`。可以在任何产生某些输出的命令之后使用Gm。

例如，运行Get-Process会在屏幕上产生一些输出，可以将这些输出通过管道传送给Gm

``` powershell
> Get-Process | gm


   TypeName:System.Diagnostics.Process

Name                       MemberType     Definition
----                       ----------     ----------
Handles                    AliasProperty  Handles = Handlecount
Name                       AliasProperty  Name = ProcessName
NPM                        AliasProperty  NPM = NonpagedSystemMemorySize64
PM                         AliasProperty  PM = PagedMemorySize64
SI                         AliasProperty  SI = SessionId
VM                         AliasProperty  VM = VirtualMemorySize64
WS                         AliasProperty  WS = WorkingSet64
Disposed                   Event          System.EventHandler Disposed(System.Object, System.EventArgs)
ErrorDataReceived          Event          System.Diagnostics.DataReceivedEventHandler ErrorDataReceived(System.Objec...
Exited                     Event          System.EventHandler Exited(System.Object, System.EventArgs)
OutputDataReceived         Event          System.Diagnostics.DataReceivedEventHandler OutputDataReceived(System.Obje...
BeginErrorReadLine         Method         void BeginErrorReadLine()
BeginOutputReadLine        Method         void BeginOutputReadLine()
CancelErrorRead            Method         void CancelErrorRead()
CancelOutputRead           Method         void CancelOutputRead()
Close                      Method         void Close()
CloseMainWindow            Method         bool CloseMainWindow()
CreateObjRef               Method         System.Runtime.Remoting.ObjRef CreateObjRef(type requestedType)
Dispose                    Method         void Dispose(), void IDisposable.Dispose()
Equals                     Method         bool Equals(System.Object obj)
GetHashCode                Method         int GetHashCode()
GetLifetimeService         Method         System.Object GetLifetimeService()
GetType                    Method         type GetType()
InitializeLifetimeService  Method         System.Object InitializeLifetimeService()
Kill                       Method         void Kill()
Refresh                    Method         void Refresh()
Start                      Method         bool Start()
ToString                   Method         string ToString()
WaitForExit                Method         bool WaitForExit(int milliseconds), void WaitForExit()
WaitForInputIdle           Method         bool WaitForInputIdle(int milliseconds), bool WaitForInputIdle()
__NounName                 NoteProperty   string __NounName=Process
BasePriority               Property       int BasePriority {get;}
Container                  Property       System.ComponentModel.IContainer Container {get;}
EnableRaisingEvents        Property       bool EnableRaisingEvents {get;set;}
ExitCode                   Property       int ExitCode {get;}
ExitTime                   Property       datetime ExitTime {get;}
Handle                     Property       System.IntPtr Handle {get;}
HandleCount                Property       int HandleCount {get;}
HasExited                  Property       bool HasExited {get;}
Id                         Property       int Id {get;}
MachineName                Property       string MachineName {get;}
MainModule                 Property       System.Diagnostics.ProcessModule MainModule {get;}
MainWindowHandle           Property       System.IntPtr MainWindowHandle {get;}
MainWindowTitle            Property       string MainWindowTitle {get;}
MaxWorkingSet              Property       System.IntPtr MaxWorkingSet {get;set;}
MinWorkingSet              Property       System.IntPtr MinWorkingSet {get;set;}
Modules                    Property       System.Diagnostics.ProcessModuleCollection Modules {get;}
NonpagedSystemMemorySize   Property       int NonpagedSystemMemorySize {get;}
NonpagedSystemMemorySize64 Property       long NonpagedSystemMemorySize64 {get;}
PagedMemorySize            Property       int PagedMemorySize {get;}
PagedMemorySize64          Property       long PagedMemorySize64 {get;}
PagedSystemMemorySize      Property       int PagedSystemMemorySize {get;}
PagedSystemMemorySize64    Property       long PagedSystemMemorySize64 {get;}
PeakPagedMemorySize        Property       int PeakPagedMemorySize {get;}
PeakPagedMemorySize64      Property       long PeakPagedMemorySize64 {get;}
PeakVirtualMemorySize      Property       int PeakVirtualMemorySize {get;}
PeakVirtualMemorySize64    Property       long PeakVirtualMemorySize64 {get;}
PeakWorkingSet             Property       int PeakWorkingSet {get;}
PeakWorkingSet64           Property       long PeakWorkingSet64 {get;}
PriorityBoostEnabled       Property       bool PriorityBoostEnabled {get;set;}
PriorityClass              Property       System.Diagnostics.ProcessPriorityClass PriorityClass {get;set;}
PrivateMemorySize          Property       int PrivateMemorySize {get;}
PrivateMemorySize64        Property       long PrivateMemorySize64 {get;}
PrivilegedProcessorTime    Property       timespan PrivilegedProcessorTime {get;}
ProcessName                Property       string ProcessName {get;}
ProcessorAffinity          Property       System.IntPtr ProcessorAffinity {get;set;}
Responding                 Property       bool Responding {get;}
SafeHandle                 Property       Microsoft.Win32.SafeHandles.SafeProcessHandle SafeHandle {get;}
SessionId                  Property       int SessionId {get;}
Site                       Property       System.ComponentModel.ISite Site {get;set;}
StandardError              Property       System.IO.StreamReader StandardError {get;}
StandardInput              Property       System.IO.StreamWriter StandardInput {get;}
StandardOutput             Property       System.IO.StreamReader StandardOutput {get;}
StartInfo                  Property       System.Diagnostics.ProcessStartInfo StartInfo {get;set;}
StartTime                  Property       datetime StartTime {get;}
SynchronizingObject        Property       System.ComponentModel.ISynchronizeInvoke SynchronizingObject {get;set;}
Threads                    Property       System.Diagnostics.ProcessThreadCollection Threads {get;}
TotalProcessorTime         Property       timespan TotalProcessorTime {get;}
UserProcessorTime          Property       timespan UserProcessorTime {get;}
VirtualMemorySize          Property       int VirtualMemorySize {get;}
VirtualMemorySize64        Property       long VirtualMemorySize64 {get;}
WorkingSet                 Property       int WorkingSet {get;}
WorkingSet64               Property       long WorkingSet64 {get;}
PSConfiguration            PropertySet    PSConfiguration {Name, Id, PriorityClass, FileVersion}
PSResources                PropertySet    PSResources {Name, Id, Handlecount, WorkingSet, NonPagedMemorySize, PagedM...
Company                    ScriptProperty System.Object Company {get=$this.Mainmodule.FileVersionInfo.CompanyName;}
CPU                        ScriptProperty System.Object CPU {get=$this.TotalProcessorTime.TotalSeconds;}
Description                ScriptProperty System.Object Description {get=$this.Mainmodule.FileVersionInfo.FileDescri...
FileVersion                ScriptProperty System.Object FileVersion {get=$this.Mainmodule.FileVersionInfo.FileVersion;}
Path                       ScriptProperty System.Object Path {get=$this.Mainmodule.FileName;}
Product                    ScriptProperty System.Object Product {get=$this.Mainmodule.FileVersionInfo.ProductName;}
ProductVersion             ScriptProperty System.Object ProductVersion {get=$this.Mainmodule.FileVersionInfo.Product...
```

当一个Cmdlet产生一个对象的集合时，就像Get-Process命令那样，整个集合直到管道末尾之前都可以被访问。直到最后一个命令运行完之前，PowerShell都不会将对象的89个标签或属性过滤掉。直到最后一个命令运行完，才会创建你所见到的文本输出结果。在上面的例子中，Gm可以完整访问进程对象的属性和方法，这是由于该命令还未被过滤用于显示。Gm会查看每一个对象并构建一个包含对象属性和方法的列表

一个对象的属性、方法以及其他附加到对象的东西都被称为成员。这也是Get-Member名称的由来：该命令获取对象成员的列表。PowerShell中的惯例是使用单数名词，所以Cmdlet的名称为Get-Member

## 使用对象标签，也就是所谓的“属性”

当你查看Gm的输出结果时，你会注意到一些不同种类的属性：脚本属性、属性、NoteProperty、别名属性。

通常来说，.Net Framework中的对象——也就是所有PowerShell对象的来源——只包含“属性”。owerShell会动态添加其他内容：ScriptProperty、NoteProperty、AliasProperty等。PowerShell有一个扩展类型系统（ETS）负责添加这些后来的属性。它使得对象具有更好的一致性，比如为原生只具有类似ProcessName属性的对象添加Name属性（这也是别名属性的作用）。还有一些情况是暴露对象中隐藏的一些信息（进程对象包含一些脚本属性完成这项工作）。

当你在PowerShell的世界中，这些属性的行为都会变得一致。但当这些属性并没有在官方文档页面中出现时，也请不要惊讶：Shell会自动添加这些额外的属性，通常会使得你的工作更加轻松。

属性总是包含一个值。例如，进程对象的ID属性可能是1234，对象的名称属性的值可能是NotePad。属性用于描述关于对象的某些方面：它的状态、它的ID、它的名称等。在PowerShell中，属性通常是只读的，意味着你无法通过给Name属性赋一个新值来改变服务的名称。但你可以通过读取Name属性获取服务的名称。

## 对象行为，也就是所谓的“方法”

很多对象都支持一个或多个方法，可以指导对象的行为。进程对象包含一个Kill方法，它会终止进程。

某些方法需要一个或多个输入参数来为某个行为提供额外的细节信息，这些方法可以和Cmdlets互相替代。

例如，如果你需要终止一个进程，可以通过3个办法实现。其中一个办法是获取对象并执行Kill方法，另一个办法是使用一系列Cmdlets：

``` powershell
> Get-Process -Name Notepad | Stop-Process
```

还可以使用单个Cmdlet完成这项任务：

``` powershell
> Stop-Process -name Notepad
```

除了属性和方法之外，对象还有一个事件。事件是以对象的方式通知你某些事情发生了。一个进程对象，举例来说，可以在进程结束时触发Exited事件。你可以将你自己的命令附加到这些事件上，比如说，当进程结束时发送一封邮件。

## 排序对象

大部分PowerShell Cmdlets以确定性的方式产生对象，这意味着每次运行命令时都会以相同的顺序产生对象。例如，服务和进程都按照字母表顺序对名称进行排序。事件日志倾向于按照事件排序。我们可以改变排序方式。

例如，假设我们希望显示一个进程列表，按照对虚拟内存（Vitrual Memory，VM）的消耗由高到低进行排列。我们将需要基于VM属性对列表进行重新排序。PowerShell提供了一个简单的Cmdlet命令 Sort-Object，就像其名称那样，可以对对象进行排序。

``` powershell
Get-Process | Sort-Object -property VM
```

该命令并不是我们最终想要的结果。它虽然以VM进行排序，但是以升序形式，最大值在列表底部。通过阅读Sort-Object，可以发现-descending参数可以反转排序。我们还注意到，-property参数是位置参数，因此无须输入参数名称。我们还告诉过你Sort-Object有一个别
名，也就是Sort

``` powershell
> Get-Process | Sort VM –desc
``

我们还将-descending简化为-desc，仍然可以得到想要的结果。-property参数接受多个值

为了防止两个进程使用的虚拟内存相同，我们还希望按照进程ID进行排序。下述命令可以实现这一点。

``` powershell
Get-Process | Sort VM, ID –desc
```

和之前一样，通过以逗号分隔列表的方式将多个值传递给任意支持多个值的参数。

## 选择所需的属性

另一个有用的Cmdlet是Select-Object。该Cmdlet从管道接受对象，你可以指定希望显示的属性。这使得你可以访问任意属性，减少返回列表，只返回你感兴趣的列，而默认情况下由PowerShell配置规则控制。这对于将对象输出到HTML的ConvertTo-HTML命令来说非常有用，因为该Cmdlet通常会创建包含所有属性的表。

比较下面两个命令的结果：

``` powershell
> Get-Process | ConvertTo-HTML | Out-File test1.html 
> Get-Process | Select-Object -property Name, ID, VM, PM | ConvertTo-HTML | Out-File test2.html
```

`test2.html` 这个文件只显示 `name` `id` `vm` `pm` 这几列。

Select-Object的别名是Select，-property参是位置参数，这意味着我们可以将上面运行的命令缩短。

``` powershell
> Get-Process | select Name, Id, vm, pm | ConvertTo-Html | Out-File test3.html
```

可以修改下述命令进行其他尝试，该命令将结果展现在屏幕上：

``` powershell
> Get-Process | select Name, id, vm, pm
```

Select-Object还拥有-First和-Last参数，这两个参数可只显示列表的前几项或后几项。

``` powershell
> Get-Process | select -First 10

Handles  NPM(K)    PM(K)      WS(K)     CPU(s)     Id  SI ProcessName
-------  ------    -----      -----     ------     --  -- -----------
    460      32     9992      26660       7.19   4240   0 AdAppMgrSvc
    188      17    26548      12988       0.97   4124   0 AdskLicensingService
    212      13     4104      16264       0.80  10996   0 AggregatorHost
    355      19     4672      26784       0.97   5104   0 AsusAppService
    278      13     2796      13508       0.23   4528   0 AsusOptimization
    336      16     3384      21096       0.23   7624   1 AsusOptimizationStartupTask
    226      18     3284      14316       0.33  13380   1 AsusOSD
     92      10     1248       6396       0.14   5096   0 AsusPTPService
    686      19     5320      25280       1.00   4140   0 AsusSoftwareManager
    615      30    40344      49428       1.03  18844   1 AsusSoftwareManagerAgent
```

将会保留前10个对象。但不能加过滤条件，比如选择特定的进程，只能选择前（或最后）10个。

Select-Object和Where-Object这两个PowerShell命令容易搞混，Select-Object用于选择所需的属性（或列），还可以选择输出行的任意子集（使用-First和-Last）。Where-object基于筛选条件从管道中移除或过滤对象。

## 在命令结束之前总是对象的形式

PowerShell管道在最后一个命令执行之前总是传递对象。在最后一个命令执行时，PowerShell将会查看管道中所包含的对象，并根据不同的配置文件决定哪一个属性被用于构建展示在屏幕上的最终结果。它还会基于一些内部规则和配置文件确定展示是表还是列表。

在一个命令行中，管道可以包含不同类型的对象。管道之后可以使用换行提交代码的可读性。换行之后命令提示符变为 `>>`

``` powershell
> Get-Process |
>> Sort-Object vm -Descending |
>> Out-File procs.txt
```

上面的代码首先运行Get-Process，该命令将进程对象放入管道。下一个命令是Sort-Object，该命令并不会改变管道中的内容，仅仅是改变对象的顺序，直到Sort-Object结束，管道仍然只包含进程。最后一个命令是Out-File。在这里，PowerShell生成输出结果，也就是管道中所包含的内容——进程对象，并根据PowerShell的内部规则将对象格式化，最终结果被存入指定文件。

``` powershell
> Get-Process |
>> Sort-Object vm -Descending |
>> Select-Object Name, Id, vm
```

该命令以同样的方式运行。Get-Process将进程对象放入管道。接下来运行Sort-Object，该命令将同样的进程对象放入管道。但Select-Object就有所不同了。进程对象总是拥有相同的成员。Select-Object并不能通过删除你不需要的属性减少属性列表。如果这样的话，结果就不再是进程对象，而是Select-Object创建一个名为PSObject的自定义对象，PowerShell使用这个对象将属性从进程对象中复制出来，结果是自定义对象被放入管道。

当PowerShell发现光标已经到达命令行结尾时，它必须知道如何对文本输出结果进行排版。这是由于管道中包含的对象不再是进程对象，PowerShell不会再将默认规则和配置应用于进程对象，而是通过查询PSObject的规则和配置，这也是当前管道中包含的配置类型。由于PSObjects用于自定义输出，微软并没有为PSObjects提供任何规则或配置。而是PowerShell将尽最大努力进行猜测并产生表。在理论上，产生的表可以容纳上述3列信息，但表并不像正常的Get-Process输出结果那样有美观的排版，这是由于Shell缺少使得表更美观的额外的配置信息。

你可以使用Gm查看管道中不同的对象。请记住，你可以在任何产生输出结果的Cmdlet之后使用Gm。

``` powershell
> Get-Process | Sort VM -descending | gm
> Get-Process | sort vm -Descending | select Name, Id, VM | gm


   TypeName:Selected.System.Diagnostics.Process

Name        MemberType   Definition
----        ----------   ----------
Equals      Method       bool Equals(System.Object obj)
GetHashCode Method       int GetHashCode()
GetType     Method       type GetType()
ToString    Method       string ToString()
Id          NoteProperty int Id=14772
Name        NoteProperty string Name=msedgewebview2
VM          NoteProperty long VM=3764506271744
```

PowerShell会展示出管道中对象的类型名称作为Gm输出结果的一部分。在第一个例子中，对象类型为System.Diagnostics.Process，但是在第二个例子中，管道里包含另一种类型的对象。这个新的“经过筛选”的对象仅包含3个指定属性——
Name、ID和VM，以及另外一些由系统生成的成员。即便Gm产生对象并将对象放入管道，在运行Gm之后，管道也不再包含进程对象或是“经过筛选”的对象，它仅包含由Gm生成的对象类型：Microsoft.PowerShell.Commands.MemberDefinition。你可以通过在管道中对Gm的输出结果再次使用Gm命令证明。

``` powershell
> Get-Process | gm | gm


   TypeName:Microsoft.PowerShell.Commands.MemberDefinition

Name        MemberType Definition
----        ---------- ----------
Equals      Method     bool Equals(System.Object obj)
GetHashCode Method     int GetHashCode()
GetType     Method     type GetType()
ToString    Method     string ToString()
Definition  Property   string Definition {get;}
MemberType  Property   System.Management.Automation.PSMemberTypes MemberType {get;}
Name        Property   string Name {get;}
TypeName    Property   string TypeName {get;}
```

首先是Get-Process命令，将进程对象放入管道。然后运行Gm，该命令分析进程对象并生成该对象的MemberDefinition对象。然后将结果再次利用管道传输给Gm，该命令将分析并产生MemberDefinition成员列表作为输出结果。
