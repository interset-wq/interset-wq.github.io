# Linux 常用操作

## 一、快捷键

这些快捷键绝大多数在Windows中也同样适用

### 1.1 ctrl+c 强制停止

Linux某些程序的运行，如果想要强制停止它，可以使用快捷键 `ctrl`+`c`

命令输入错误，也可以通过快捷键 `ctrl`+`c` ，退出当前输入，重新输入

`ctrl`+`c` 强制结束某个命令，和Windows中的用法类似

### 1.2 ctrl+d 退出和登出

可以通过快捷键：`ctrl`+`d` ，退出账户的登录，类似于exit命令，退出Linux用户

或者退出某些特定程序的专属页面，例如退出python命令行，类似于exit()命令

不能用于退出vi/vim

### 1.3 ctrl r 搜索历史命令

可以通过快捷键：`ctrl`+`r` ，输入内容去匹配历史命令

如果搜索到的内容是你需要的，那么：回车键可以直接执行。键盘左右键，移动光标修改，也可以得到此命令（不执行）

### 1.4 光标移动快捷键

- `ctrl`+`a` ，跳到命令开头
- `ctrl`+`e` ，跳到命令结尾
- `ctrl`+`left` ，向左跳一个单词
- `ctrl`+`right` ，向右跳一个单词

### 1.5 ctrl l 清空终端

通过快捷键 `ctrl`+`l` ，可以清空终端内容。或通过命令 `clear` 得到同样效果

## 二、历史命令

### 2.1 通过history命令查看历史命令

可以通过 `history` 命令，查看历史输入过的命令。此时，控制台将会列出所有最近使用的命令

### 2.2 通过 `!` 快速调用历史命令

可以通过：`!`命令前缀，自动执行上一次匹配前缀的命令

例如：比较近的历史命令中曾使用过 `python` 命令开启python命令行，可以直接通过 `!p` 快速搜索以字母`p`开头的命令，从而快速调用 `python` 命令

## 三、联网安装软件

操作系统安装软件有许多种方式，一般分为：

- 下载安装包自行安装。如win系统使用exe文件、msi文件等，如mac系统使用dmg文件、pkg文件等
- 系统的应用商店内安装。如win系统有Microsoft Store商店，如mac系统有AppStore商店

Linux系统同样支持这两种方式，我们首先，先来学习使用：Linux命令行内的“应用商店”，`yum`命令安装软件。前面学习的各类Linux命令，都是通用的。 但是软件安装，CentOS系统和Ubuntu是使用不同的包管理器。CentOS使用yum管理器，Ubuntu使用apt管理器

### 3.1 CentOS

CentOS系统使用： `yum [-y] [install remove search] 软件名称`

- `install` 安装
- `remove` 卸载
- `search` 搜索
- `-y`，自动确认

例如：

- `yum [-y] install wget`， 通过yum命令安装wget程序
- `yum [-y] remove wget`，通过yum命令卸载wget命令
- `yum search wget`，通过yum命令，搜索是否有wget安装包


### 3.2 Ubuntu

Ubuntu系统使用 `apt [-y] [install remove search] 软件名称`

- `install` 安装
- `remove` 卸载
- `search` 搜索
- `-y`，自动确认

> yum 和 apt 均需要root权限

## 四、systemctl控制系统服务

功能：控制系统服务的启动关闭等

Linux系统很多软件（内置或第三方）均支持使用systemctl命令控制：启动、停止、开机自启
能够被systemctl管理的软件，一般也称之为：服务

系统内置的服务比较多，比如：

- NetworkManager，主网络服务
- network，副网络服务
- firewalld，防火墙服务
- sshd，ssh服务（FinalShell远程登录Linux使用的就是这个服务）

语法：`systemctl start | stop | restart | disable | enable | status 服务名`

- start，启动
- stop，停止
- status，查看状态
- disable，关闭开机自启
- enable，开启开机自启
- restart，重启

除了内置的服务以外，部分第三方软件安装后也可以以`systemctl`进行控制。

`yum install -y ntp`，安装ntp软件。可以通过ntpd服务名，配合systemctl进行控制

`yum install -y httpd`，安装apache服务器软件。可以通过httpd服务名，配合systemctl进行控制

部分软件安装后没有自动集成到systemctl中，我们可以手动添加。

## 五、软链接

功能：创建文件、文件夹软链接（快捷方式）

语法：`ln -s 参数1 参数2`

- 参数1：被链接的
- 参数2：要链接去的地方（快捷方式的名称和存放位置）

例如：

- `ln -s /etc/yum.conf ~/yum.conf`
- `ln -s /etc/yum ~/yum`

## 六、日期和时间

### 6.1 日期

语法：`date [-d] [+格式化字符串]`

- `-d` 按照给定的字符串显示日期，一般用于日期计算。其中支持的时间标记为：
    - year年
    - month月
    - day天
    - hour小时
    - minute分钟
    - second秒
- 格式化字符串：通过特定的字符串标记，来控制显示的日期格式，如果格式化字符串中有空格，需要使用双引号包裹
    - %Y   年（类似于2025的四位数年份）
    - %y   年份后两位数字 (00-99)
    - %m   月份 (01-12)
    - %d   日 (01-31)
    - %H   小时 (00-23)
    - %M   分钟 (00-59)
    - %S   秒 (00-60)
    - %s   时间戳，自 1970-01-01 00:00:00 UTC 到现在的秒数


例如：

- `date` 以 `2025年 07月 22日 星期二 19:29:29 PDT` 格式显示当前时间
- `date +%Y-%m-%d` 以 `2025-07-22` 格式显示当前时间
- `date "+%Y-%m-%d %H:%M:%S"` 以 `2025-07-22 19:34:04` 格式显示当前时间

通过 `-d` 进行日期的计算，例如：

- `date -d "+1 day"` 当前时间的明天的时间

### 6.2 时区

通过date查看的日期时间是不准确的，这是因为：系统默认时区并不是中国时区。

使用root权限，执行如下命令，修改时区为东八区时区CST

```
# rm -f /etc/localtime
# ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
# date
Wed Jul 23 10:51:41 CST 2025
```

将系统自带的localtime文件删除，并将`/usr/share/zoneinfo/Asia/Shanghai`文件链接为`localtime`文件即可

### 6.3 使用ntp联网同步时间

功能：同步时间

安装：`yum install -y ntp`

启动管理：`systemctl start | stop | restart | status | disable | enable ntpd`

手动校准时间：`ntpdate -u ntp.aliyun.com`


## 七、ip地址和主机名

### 7.1 ip地址

每一台联网的电脑都会有一个地址，用于和其它计算机进行通讯。IP地址主要有2个版本，V4版本和V6版本（V6很少用）

IPv4版本的地址格式是：`a.b.c.d`，其中abcd表示0~255的数字，如`192.168.88.101`就是一个标准的IP地址

可以通过命令：`ifconfig`，查看本机的ip地址，如无法使用ifconfig命令，CentOS可以安装：`yum -y install net-tools`

``` bash
$ ifconfig
Command 'ifconfig' not found, but can be installed with:
sudo apt install net-tools
```


### 7.2 特殊IP地址

- `127.0.0.1`，表示本机localhost
- `0.0.0.0`，特殊IP地址
    - 可以用于指代本机
    - 可以在端口绑定中用来确定绑定关系（后续讲解）
    - 在一些IP地址限制中，表示所有IP的意思，如放行规则设置为0.0.0.0，表示允许任意IP访问

### 7.3 主机名

每一台电脑除了对外联络地址（IP地址）以外，也可以有一个名字，称之为主机名。无论是Windows或Linux系统，都可以给系统设置主机名。主机名就是主机的名称，用于标识一个计算机

查看主机名：`hostname`

修改主机名：`hostnamectl set-hostname 主机名`

Linux命令提示符 `[d111kc@centos ~]$` 中的 `d111kc` 表示用户名 `@` 之后的 `centos` 表示主机名

### 7.4 域名解析（主机名映射）

IP地址实在是难以记忆，实际上，我们一直都是通过字符化的地址去访问服务器，很少指定IP地址。比如，我们在浏览器内打开：www.baidu.com，会打开百度的网址。其中，www.baidu.com，是百度的网址，我们称之为：域名。访问百度的流程如下：

![图片](https://d111kc.github.io/picx-images-hosting/linux/图片.lw11ph8rx.webp)

即：

1. 先查看本机的记录（私人地址本）
    - Windows看：`C:\Windows\System32\drivers\etc\hosts`
    - Linux看：`/etc/hosts`
2. 再联网去DNS服务器（如114.114.114.114，8.8.8.8等）询问

可以通过主机名找到对应计算机的IP地址，这就是主机名映射（域名解析）。先通过系统本地的记录去查找，如果找不到就联网去公开DNS服务器去查找

## 八、网络传输

### 8.1 使用ping命令检查服务器是否联通

可以通过ping命令，检查指定的网络服务器是否是可联通状态

语法：`ping [-c num] 参数`

- 选项：-c，用数字代替num，检查的次数，不使用-c选项，将无限次数持续检查
- 参数：ip或主机名，被检查的服务器的ip地址或主机名地址

例如 `ping baidu.com` 检查到baidu.com是否联通

### 8.2 wget命令下载文件

下载wget `yum -y install wget`

wget是非交互式的文件下载器，可以在命令行内下载网络文件。wget下载文件时，可以使用 `ctrl`+`c` 取消下载。无论是否下载完成，都会创建需要下载的文件到`~`目录中

语法： `wget [-b] url`

- 选项：-b，可选，后台下载，会将日志写入到当前工作目录的wget-log文件
- 参数：url，下载链接

例如：

- 下载apache-hadoop 3.3.0版本：`wget http://archive.apache.org/dist/hadoop/common/hadoop-3.3.0/hadoop-3.3.0.tar.gz`
- 在后台下载：`wget -b http://archive.apache.org/dist/hadoop/common/hadoop-3.3.0/hadoop-3.3.0.tar.gz`

通过tail命令可以监控后台下载进度：`tail -f wget-log`

注意：无论下载是否完成，都会生成要下载的文件，如果下载未完成，请及时清理未完成的不可用文件。

### 8.3 curl命令发送网络请求或下载文件

curl可以发送http网络请求（类似于python中的requests库），可用于：下载文件、获取信息等

- `curl url` 发送请求
- `curl -O url` 下载文件，和wget类似

### 8.4 端口

端口，是设备与外界通讯交流的出入口。端口可以分为：物理端口和虚拟端口两类

- 物理端口：又可称之为接口，是可见的端口，如USB接口，RJ45网口，HDMI端口等
- 虚拟端口：是指计算机内部的端口，是不可见的，是用来操作系统和外部进行交互使用的

计算机程序之间的通讯，通过IP只能锁定计算机，但是无法锁定具体的程序。通过端口可以锁定计算机上具体的程序，确保程序之间进行沟通。IP地址相当于小区地址，在小区内可以有许多住户（程序），而门牌号（端口）就是各个住户（程序）的联系地址

Linux系统是一个超大号小区，可以支持65535个端口，这6万多个端口分为3类进行使用：

- 公认端口：1~1023，通常用于一些系统内置或知名程序的预留使用，如SSH服务的22端口，HTTPS服务的443端口，非特殊需要，不要占用这个范围的端口
- 注册端口：1024~49151，通常可以随意使用，用于松散的绑定一些程序\服务
- 动态端口：49152~65535，通常不会固定绑定程序，而是当程序对外进行网络链接时，用于临时使用。

### 8.5 nmap查看端口占用情况

可以通过Linux命令去查看端口的占用情况

使用nmap命令，安装nmap：`yum -y install nmap`

语法：`nmap 被查看的IP地址`

例如 `nmap 127.0.0.1` 查看本机端口占用情况

### 8.6 netstat查看指定端口占用情况

可以通过netstat命令，查看指定端口的占用情况

安装netstat：`yum -y install net-tools`

语法：`netstat -anp | grep 端口号`

## 九、进程管理

### 9.1 进程

程序运行在操作系统中，是被操作系统所管理的。为管理运行的程序，每一个程序在运行的时候，便被操作系统注册为系统中的一个进程，并会为每一个进程都分配一个独有的：进程ID（进程号）

### 9.2 ps查看进程

可以通过ps命令查看Linux系统中的进程信息

语法：`ps [-e -f]`

- 选项：-e，显示出全部的进程
- 选项：-f，以完全格式化的形式展示信息（展示全部信息）

一般来说，固定用法就是： `ps -ef` 列出全部进程的全部信息，这些信息含义如下：

- UID：进程所属的用户ID
- PID：进程的进程号ID
- PPID：进程的父ID（启动此进程的其它进程）
- C：此进程的CPU占用率（百分比）
- STIME：进程的启动时间
- TTY：启动此进程的终端序号，如显示?，表示非终端启动
- TIME：进程占用CPU的时间
- CMD：进程对应的名称或启动路径或启动命令

### 9.3 查看指定进程

我们可以使用管道符配合grep来进行过滤，如：`ps -ef | grep tail`，即可准确的找到tail命令的信息

过滤不仅仅过滤名称，进程号，用户ID等等，都可以被grep过滤。如：`ps -ef | grep 30001`，过滤带有30001关键字的进程信息（一般指代过滤30001进程号）

### 9.4 kill关闭进程

在Windows系统中，可以通过任务管理器选择进程后，点击结束进程从而关闭它。同样，在Linux中，可以通过kill命令关闭进程。

语法：`kill [-9] 进程ID`

选项：-9，表示强制关闭进程。不使用此选项会向进程发送信号要求其关闭，但是否关闭看进程自身的处理机制。通过 `-9` 结束进程，命令行中输出的是`killed`已杀死。不使用 `-9` 输出的是 `terminated`已终止

## 十、主机状态

### 10.1 top命令查看资源占用

功能：查看主机运行状态

可以通过top命令查看CPU、内存使用情况，类似Windows的任务管理器。默认每5秒刷新一次，语法：直接输入top即可，按q或ctrl + c退出


语法：`top`，查看基础信息

```
$ top
top - 11:10:33 up  2:28,  5 users,  load average: 0.16, 0.19, 0.17
Tasks: 213 total,   1 running, 212 sleeping,   0 stopped,   0 zombie
%Cpu(s):  4.0 us,  6.7 sy,  0.0 ni, 89.0 id,  0.0 wa,  0.0 hi,  0.3 si,  0.0 st
KiB Mem :   995896 total,    70088 free,   563132 used,   362676 buff/cache
KiB Swap:  2098172 total,  1967100 free,   131072 used.   206980 avail Mem 
```

top命令输出内容的前五行：

- 第一行：`top - 11:10:33 up  2:28,  5 users,  load average: 0.16, 0.19, 0.17`

    `top`：命令名称，`11:10:33`：当前系统时间，up  2:28：启动了2小时28分钟，`5 users`：5个用户登录，`load average: 0.16, 0.19, 0.17`：1、5、15分钟负载分别是0.16, 0.19, 0.17

- 第二行：`Tasks: 213 total,   1 running, 212 sleeping,   0 stopped,   0 zombie`

    `Tasks: 213 total`：213个进程，`1 running`：1个进程子在运行，`212 sleeping`：212个进程睡眠，`0 stopped`: 0个停止进程，`0 zombie`: 0个僵尸进程

- 第三行：`%Cpu(s):  4.0 us,  6.7 sy,  0.0 ni, 89.0 id,  0.0 wa,  0.0 hi,  0.3 si,  0.0 st`

    %Cpu(s)：CPU使用率，us：用户CPU使用率，sy：系统CPU使用率，ni：高优先级进程占用CPU时间百分比，id：空闲CPU率，wa：IO等待CPU占用率，hi：CPU硬件中断率，si：CPU软件中断率，st：强制等待占用CPU率

- 第四行：`KiB Mem :   995896 total,    70088 free,   563132 used,   362676 buff/cache`

    Kib Mem：物理内存，total：总量，free：空闲，used：使用，buff/cache：buff和cache占用

- 第五行：`KiB Swap:  2098172 total,  1967100 free,   131072 used.   206980 avail Mem `

    KibSwap：虚拟内存（交换空间），total：总量，free：空闲，used：使用，buff/cache：buff和cache占用

top输出的主要内容及其含义：

- PID：进程id
- USER：进程所属用户
- PR：进程优先级，越小越高
- NI：负值表示高优先级，正表示低优先级
- VIRT：进程使用虚拟内存，单位KB
- RES：进程使用物理内存，单位KB
- SHR：进程使用共享内存，单位KB
- S：进程状态（S休眠，R运行，Z僵死状态，N负数优先级，I空闲状态）
- %CPU：进程占用CPU率
- %MEM：进程占用内存率
- TIME+：进程使用CPU时间总计，单位10毫秒
- COMMAND：进程的命令或名称或程序文件路径

可用选项：

![image-20221027221340729](https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2022/10/27/20221027221340.png)

交互式模式中，可用快捷键：

![image-20221027221354137](https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2022/10/27/20221027221354.png)

### 10.2 df命令查看磁盘使用情况

使用df命令，可以查看硬盘的使用情况

语法：`df [-h]`

选项：-h，以更加人性化的单位显示

### 10.3 iostat命令查看CPU、磁盘的相关信息

查看CPU、磁盘的相关信息

可以使用iostat查看CPU、磁盘的相关信息

语法：`iostat [-x] [num1] [num2]`

- 选项：-x，显示更多信息
- num1：数字，刷新间隔，num2：数字，刷新几次

tps：该设备每秒的传输次数（Indicate the number of transfers per second that were issued to the device.）。"一次传输"意思是"一次I/O请求"。多个逻辑请求可能会被合并为"一次I/O请求"。"一次传输"请求的大小是未知的。

使用iostat的-x选项，可以显示更多信息

- rrqm/s：	每秒这个设备相关的读取请求有多少被Merge了（当系统调用需要读取数据的时候，VFS将请求发到各个FS，如果FS发现不同的读取请求读取的是相同Block的数据，FS会将这个请求合并Merge, 提高IO利用率, 避免重复调用）；
- wrqm/s：	每秒这个设备相关的写入请求有多少被Merge了。
- rsec/s：	每秒读取的扇区数；sectors
- wsec/：	每秒写入的扇区数。
- rKB/s：	每秒发送到设备的读取请求数
- wKB/s：	每秒发送到设备的写入请求数
- avgrq-sz 	平均请求扇区的大小
- avgqu-sz 	平均请求队列的长度。毫无疑问，队列长度越短越好。    
- await：  	每一个IO请求的处理的平均时间（单位是微秒毫秒）。
- svctm    	表示平均每次设备I/O操作的服务时间（以毫秒为单位）
- %util： 	磁盘利用率

### 10.4 sar命令查看网络统计

可以使用sar命令查看网络的相关统计（sar命令非常复杂，这里仅简单用于统计网络）

语法：`sar -n DEV [num1 num2]`

- 选项：-n，查看网络，DEV表示查看网络接口
- num1：刷新间隔（不填就查看一次结束），num2：查看次数（不填无限次数）

输出信息：

- IFACE 本地网卡接口的名称
- rxpck/s 每秒钟接受的数据包
- txpck/s 每秒钟发送的数据包
- rxKB/S 每秒钟接受的数据包大小，单位为KB
- txKB/S 每秒钟发送的数据包大小，单位为KB
- rxcmp/s 每秒钟接受的压缩数据包
- txcmp/s 每秒钟发送的压缩包
- rxmcst/s 每秒钟接收的多播数据包

## 十一、环境变量

### 11.1 env查看系统全部环境变量

环境变量是操作系统（Windows、Linux、Mac）在运行的时候，记录的一些关键性信息，用以辅助系统运行。在Linux系统中执行：`env` 命令即可查看当前系统中记录的环境变量。环境变量是一种KeyValue型结构，即名称和值。

### 11.2 环境变量PATH

无论当前工作目录是什么，都能执行/usr/bin/cd这个程序，这个就是借助环境变量中：PATH这个项目的值来做到的。

```
$ env | grep PATH
PATH=/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/d111kc/.local/bin:/home/d111kc/bin
```

PATH记录了系统执行任何命令的搜索路径，如上面的代码记录了以下路径（路径之间以:隔开）：

```
/usr/local/bin
/usr/bin
/usr/local/sbin
/usr/sbin
/home/d111kc/.local/bin
/home/d111kc/bin
```

当执行任何命令，都会按照顺序，从上述路径中搜索要执行的程序的本体。比如执行cd命令，就从第二个目录/usr/bin中搜索到了cd命令，并执行

### 11.3 $符号

在Linux系统中，$符号被用于取”变量”的值。环境变量记录的信息，除了给操作系统自己使用外，如果我们想要取用，也可以使用。取得环境变量的值就可以通过语法：`$环境变量名`  来取得

```
$ echo $PATH
/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/d111kc/.local/bin:/home/d111kc/bin
```

使用 `$` 就可以取得PATH这个环境变量的值，并通过echo语句输出出来。

```
$ echo ${PATH}ABC
/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/d111kc/.local/bin:/home/d111kc/binABC
```

当和其它内容混合在一起的时候，可以通过{}来标注取的变量是谁

### 11.4 自行设置环境变量

Linux环境变量可以用户自行设置，其中分为：

- 临时设置，语法：`export 变量名=变量值`
- 永久生效
    - 针对当前用户生效，配置在当前用户的：配置文件	`~/.bashrc` 中，在这个文件中添加`export 变量名=变量值`来配置环境变量
    - 针对所有用户生效，配置在系统的：配置文件	`/etc/profile` 中
    - 并通过语法：`source 配置文件`，进行立刻生效，或重新登录FinalShell生效

### 11.5 自定义环境变量PATH

环境变量PATH这个项目里面记录了系统执行命令的搜索路径。这些搜索路径我们也可以自行添加到PATH中去。

例如：

1. 在当前HOME目录内创建文件夹`myenv`，在文件夹内创建文件`hello`
2. 通过vim编辑器，在`hello`文件内填入：`echo "hello world"`
3. 要使hello文件中的命令可以执行，必须要有x权限，因此需要修改文件的权限 `chmod 755 hello`
4. 此时在命令行输入这个hello文件的路径可以执行这个文件中的命令
5. 输入这个文件的绝对路径实在太复杂了，因此可以将这个目录添加到PATH中 
6. 通过前面的方法修改PATH：`export PATH=$PATH:~/myenv`，在其中添加 `myenv` 文件夹的路径，再次执行hello，无论在哪里都能执行了

## 十二、Linux虚拟机和本地电脑互相传输文件

### 12.1 FinalShell

我们可以通过FinalShell工具，方便的和虚拟机进行数据交换。在FinalShell软件的下方窗体中，提供了Linux的文件系统视图，可以方便的：浏览文件系统，找到合适的文件，右键点击下载，即可下载虚拟机中的文件到本地Windows电脑。浏览Windows文件资源管理器，将文件拖入finalshell文件视图中，即可方便的上传数据到Linux中

### 12.2 rz和sz

当然，除了通过FinalShell的下方窗体进行文件的传输以外，也可以通过rz、sz命令进行文件传输。rz、sz命令需要安装，可以通过：`yum -y install lrzsz`，即可安装。

- sz命令将Linux虚拟机上的文件下载到本地Windows的 `C:\Desktop\fsdownload`目录中，语法：`sz 要下载的文件`

- rz命令将本地Windows中的文件上传到Linux虚拟机中，语法：`rz` 此时会弹出文件资源管理器，选择文件双击即可

注意，rz、sz命令需要终端软件支持才可正常运行。FinalShell、SecureCRT、XShell等常用终端软件均支持此操作

## 十三、压缩和解压缩

解压时如果目录中有同名文件或目录会被覆写

### 13.1 常见压缩包格式

市面上有非常多的压缩格式：

- zip格式：Linux、Windows、MacOS，常用
- 7zip：Windows系统常用
- rar：Windows系统常用
- tar：Linux、MacOS常用
- gzip：Linux、MacOS常用

在Windows系统中常用的软件如：winrar、bandizip等软件，都支持各类常见的压缩格式。在Linux系统中操作：tar、gzip、zip这三种压缩格式完成文件的压缩、解压操作。

### 13.2 tar和gz格式压缩包

Linux和Mac系统常用有2种压缩格式，后缀名分别是：

- `.tar`，称之为tarball，归档文件，即简单的将文件组装到一个.tar的文件内，并没有太多文件体积的减少，仅仅是简单的封装
- `.gz`，也常见为.tar.gz，gzip格式压缩文件，即使用gzip压缩算法将文件压缩到一个文件内，可以极大的减少压缩后的体积

针对这两种格式，使用tar命令均可以进行压缩和解压缩的操作

语法： `tar [选项] 参数1 参数2 ... 参数n`

- -c，创建压缩文件，用于压缩模式
- -v，显示压缩、解压过程，用于查看进度
- -x，解压模式
- -f，要创建的文件，或要解压的文件，-f选项必须在所有选项中位置处于最后一个
- -z，gzip模式，不使用-z就是普通的tarball格式
- -C，选择解压的目的地，用于解压模式

#### 13.2.1 压缩

tar的常用组合为：

- `tar -cvf test.tar 1.txt 2.txt 3.txt` 将1.txt 2.txt 3.txt 压缩到test.tar文件内
- `tar -zcvf test.tar.gz 1.txt 2.txt 3.txt` 将1.txt 2.txt 3.txt 压缩到test.tar.gz文件内，使用gzip模式

注意：

- -z选项如果使用的话，一般处于选项位第一个
- -f选项，必须在选项位最后一个

#### 13.2.2 解压缩

常用的tar解压组合有

- `tar -xvf test.tar` 解压test.tar，将文件解压至当前目录
- `tar -xvf test.tar -C test/` 解压test.tar，将文件解压至指定目录（~/test）
- `tar -zxvf test.tar.gz -C test/` 以Gzip模式解压test.tar.gz，将文件解压至指定目录（~/test）

注意：

- -f选项，必须在选项组合体的最后一位
- -z选项，建议在开头位置
- -C选项单独使用，和解压所需的其它参数分开

### 13.3 zip格式压缩包

#### 13.3.1 压缩

可以使用zip命令，压缩文件为zip压缩包

语法：`zip [-r] 参数1 参数2 ... 参数n`

-r，被压缩的包含文件夹的时候，需要使用-r选项，和rm、cp等命令的-r效果一致

示例：

- `zip test.zip a.txt b.txt c.txt` 将a.txt b.txt c.txt 压缩到test.zip文件内
- `zip -r test.zip test hello a.txt` 将test、hello两个文件夹和a.txt文件，压缩到test.zip文件内

#### 13.3.2 解压缩

使用unzip命令，可以方便的解压zip压缩包

语法：`unzip [-d] 参数`

- -d，指定要解压去的位置，同tar的-C选项
- 参数，被解压的zip压缩包文件

示例：

- `unzip test.zip`，将test.zip解压到当前目录
- `unzip test.zip -d test/`，将test.zip解压到指定文件夹内（~/test）

