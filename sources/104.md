## 单项选择题

1. 下面的网络协议中，面向连接的的协议是：（ ）
   - [x] A 传输控制协议
   - [ ] B 用户数据报协议
   - [ ] C 网际协议
   - [ ] D 网际控制报文协议
   答案：A

2. 在/etc/fstab文件中指定的文件系统加载参数中，（ ）参数一般用于CD-ROM等移动设备。
   - [ ] A defaults
   - [ ] B sw
   - [ ] C rw 和ro
   - [x] D noauto
   答案：D

3. Linux文件权限一共10位长度，分成四段，第三段表示的内容是（ ）
   - [ ] A 文件类型
   - [ ] B 文件所有者的权限
   - [x] C 文件所有者所在组的权限
   - [ ] D 其他用户的权限
   答案：C

4. 终止一个前台进程可能用到的命令和操作（ ）
   - [ ] A kill
   - [x] B Ctrl+C
   - [ ] C shut down
   - [ ] D halt
   答案：B

5. 在使用mkdir命令创建新的目录时，在其父目录不存在时先创建父目录的选项是（ ）
   - [ ] A -m
   - [ ] B -d
   - [ ] C -f
   - [x] D -p
   答案：D

6. 下面关于i节点描述错误的是（ ）
   - [x] A i节点和文件是一一对应的
   - [ ] B i节点能描述文件占用的块数
   - [ ] C i节点描述了文件大小和指向数据块的指针
   - [ ] D 通过i节点实现文件的逻辑结构和物理结构的转换
   答案：A

7. 一个文件名字为rr.Z，可以用来解压缩的命令是：（ ）
   - [ ] A tar
   - [ ] B gzip
   - [ ] C compress
   - [x] D uncompress
   答案：D

8. 具有很多C语言的功能，又称过滤器的是（ ）
   - [ ] A csh
   - [ ] B tcsh
   - [x] C awk
   - [ ] D sed
   答案：C

9. 一台主机要实现通过局域网与另一个局域网通信，需要做的工作是（ ）
   - [ ] A 配置域名服务器
   - [ ] B 定义一条本机指向所在网络的路由
   - [x] C 定义一条本机指向所在网络网关的路由
   - [ ] D 定义一条本机指向目标网络网关的路由
   答案：C

10. 建立动态路由需要用到的文件有（ ）
    - [ ] A /etc/hosts
    - [ ] B /etc/HOSTNAME
    - [ ] C /etc/resolv.conf
    - [x] D /etc/gateways
    答案：D

11. 局域网的网络地址192.168.1.0/24，局域网络连接其它网络的网关地址是192.168.1.1。主机192.168.1.20访问172.16.1.0/24网络时，其路由设置正确的是（ ）
    - [ ] A route add –net 192.168.1.0 gw 192.168.1.1 netmask 255.255.255.0 metric 1
    - [x] B route add –net 172.16.1.0 gw 192.168.1.1 netmask 255.255.255.255 metric 1
    - [ ] C route add –net 172.16.1.0 gw 172.16.1.1 netmask 255.255.255.0 metric 1
    - [ ] D route add default 192.168.1.0 netmask 172.168.1.1 metric 1
    答案：B

12. 下列提法中，不属于ifconfig命令作用范围的是（ ）
    - [ ] A 配置本地回环地址
    - [ ] B 配置网卡的IP地址
    - [ ] C 激活网络适配器
    - [x] D 加载网卡到内核中
    答案：D

13. 下列关于链接描述，错误的是（ ）
    - [ ] A 硬链接就是让链接文件的i节点号指向被链接文件的i节点
    - [x] B 硬链接和符号连接都是产生一个新的i节点
    - [ ] C 链接分为硬链接和符号链接
    - [ ] D 硬连接不能链接目录文件
    答案：B

14. 在局域网络内的某台主机用ping命令测试网络连接时发现网络内部的主机都可以连同，而不能与公网连通，问题可能是（ ）
    - [ ] A 主机IP设置有误
    - [ ] B 没有设置连接局域网的网关
    - [x] C 局域网的网关或主机的网关设置有误
    - [ ] D 局域网DNS服务器设置有误
    答案：C

15. 下列文件中，包含了主机名到IP地址的映射关系的文件是：（ ）
    - [ ] A /etc/HOSTNAME
    - [x] B /etc/hosts
    - [ ] C /etc/resolv.conf
    - [ ] D /etc/networks
    答案：B

16. 不需要编译内核的情况是（ ）
    - [ ] A 删除系统不用的设备驱动程序时
    - [ ] B 升级内核时
    - [ ] C 添加新硬件时
    - [x] D 将网卡激活
    答案：D

17. 在shell中变量的赋值有四种方法，其中，采用name=12的方法称（ ）
    - [x] A 直接赋值
    - [ ] B 使用read命令
    - [ ] C 使用命令行参数
    - [ ] D 使用命令的输出
    答案：A

18. （ ）命令可以从文本文件的每一行中截取指定内容的数据。
    - [ ] A cp
    - [ ] B dd
    - [ ] C fmt
    - [x] D cut
    答案：D

19. 下列不是Linux系统进程类型的是（ ）
    - [ ] A 交互进程
    - [ ] B 批处理进程
    - [ ] C 守护进程
    - [x] D 就绪进程
    答案：D

20. 配置Apache 1.3.19服务器需要修改的配置文件为（ ）
    - [x] A httpd.conf
    - [ ] B access.conf
    - [ ] C srm.conf
    - [ ] D named.conf
    答案：A

21. 内核不包括的子系统是（ ）
    - [ ] A 进程管理系统
    - [ ] B 内存管理系统
    - [ ] C I/O管理系统
    - [x] D 硬件管理系统
    答案：D

22. 在日常管理中，通常CPU会影响系统性能的情况是：（ ）
    - [x] A CPU已满负荷地运转
    - [ ] B CPU的运行效率为30%
    - [ ] C CPU的运行效率为50%
    - [ ] D CPU的运行效率为80%
    答案：A

23. 若一台计算机的内存为128MB，则交换分区的大小通常是（ ）
    - [ ] A 64MB
    - [ ] B 128MB
    - [x] C 256MB
    - [ ] D 512MB
    答案：C

24. 在安装Linux的过程中的第五步是让用户选择安装方式，如果用户希望安装部分组件（软件程序），并在选择好后让系统自动安装，应该选择的选项是（ ）
    - [ ] A full
    - [ ] B expert
    - [ ] C newbie
    - [x] D menu
    答案：D

25. Linux有三个查看文件的命令，若希望在查看文件内容过程中可以用光标上下移动来查看文件内容，应使用（ ）命令。
    - [ ] A cat
    - [ ] B more
    - [x] C less
    - [ ] D menu
    答案：C

26. 下列信息是某系统用ps –ef命令列出的正在运行的进程，（ ）进程是运行Internet超级服务器，它负责监听Internet sockets上的连接，并调用合适的服务器来处理接收的信息。
    - [ ] A root 1 4.0 0.0 344 204? S 17:09 0:00 init
    - [ ] B root 2 0.0 0.1 2916 1520? S 17:09 0:00 /sbin/getty
    - [ ] C root 3 0.0 0.2 1364 632? S 17:09 0:00 /usr/sbin/syslogd
    - [x] D root 4 0.0 1344 1204? S 17:09 0:10 /usr/sbin/inetd
    答案：D

27. 在TCP/IP模型中，应用层包含了所有的高层协议，在下列的一些应用协议中，（ ）是能够实现本地与远程主机之间的文件传输工作。
    - [ ] A telnet
    - [x] B FTP
    - [ ] C SNMP
    - [ ] D NFS
    答案：B

28. 当我们与某远程网络连接不上时，就需要跟踪路由查看，以便了解在网络的什么位置出现了问题，满足该目的的命令是（ ）
    - [ ] A ping
    - [ ] B ifconfig
    - [x] C traceroute
    - [ ] D netstat
    答案：C

29. 对名为fido的文件用chmod 551 fido进行了修改，则它的许可权是（ ）
    - [ ] A -rwxr-xr-x
    - [ ] B -rwxr--r--
    - [ ] C -r--r--r--
    - [x] D -r-xr-x-x
    答案：D

30. 在i节点表中的磁盘地址表中，若一个文件的长度是从磁盘地址表的第1块到第11块，则该文件共占有（ ）块号。
    - [ ] A 256
    - [x] B 266
    - [ ] C 11
    - [ ] D 256×10
    答案：B

31. 用ls –al命令列出下面的文件列表，（ ）文件是符号连接文件。
    - [ ] A -rw-rw-rw- 2 hel-s users 56 Sep 09 11:05 hello
    - [ ] B -rwxrwxrwx 2 hel-s users 56 Sep 09 11:05 goodbey
    - [ ] C drwxr--r-- 1 hel users 1024 Sep 10 08:10 zhang
    - [x] D lrwxr--r-- 1 hel users 2024 Sep 12 08:12 cheng
    答案：D

32. DNS域名系统主要负责主机名和（ ）之间的解析。
    - [x] A IP地址
    - [ ] B MAC地址
    - [ ] C 网络地址
    - [ ] D 主机别名
    答案：A

33. WWW服务器是在Internet上使用最为广泛，它采用的是（ ）结构。
    - [ ] A 服务器/工作站
    - [x] B B/S
    - [ ] C 集中式
    - [ ] D 分布式
    答案：B

34. Linux系统通过（ ）命令给其他用户发消息。
    - [ ] A less
    - [ ] B mesg y
    - [x] C write
    - [ ] D echo to
    答案：C

35. NFS是（ ）系统。
    - [ ] A 文件
    - [ ] B 磁盘
    - [x] C 网络文件
    - [ ] D 操作
    答案：C

36. （ ）命令可以在Linux的安全系统中完成文件向磁带备份的工作。
    - [ ] A cp
    - [ ] B tr
    - [ ] C dir
    - [x] D cpio
    答案：D

37. Linux文件系统的文件都按其作用分门别类地放在相关的目录中，对于外部设备文件，一般应将其放在（ ）目录中。
    - [ ] A /bin
    - [ ] B /etc
    - [x] C /dev
    - [ ] D /lib
    答案：C

38. 在重新启动Linux系统的同时把内存中的信息写入硬盘，应使用（ ）命令实现。
    - [ ] A # reboot
    - [ ] B # halt
    - [ ] C # reboot
    - [x] D # shutdown –r now
    答案：D

39. 网络管理具备以下几大功能：配置管理、（ ）、性能管理、安全管理和计费管理等。
    - [x] A 故障管理
    - [ ] B 日常备份管理
    - [ ] C 升级管理
    - [ ] D 发送邮件
    答案：A

40. 关于代理服务器的论述，正确的是（ ）
    - [x] A 使用internet上已有的公开代理服务器，只需配置客户端。
    - [ ] B 代理服务器只能代理客户端http的请求。
    - [ ] C 设置好的代理服务器可以被网络上任何主机使用。
    - [ ] D 使用代理服务器的客户端没有自己的ip地址。
    答案：A

41. 关闭linux系统（不重新启动）可使用命令（ ）
    - [ ] A Ctrl+Alt+Del
    - [x] B halt
    - [ ] C shutdown -r now
    - [ ] D reboot
    答案：B

42. 实现从IP地址到以太网MAC地址转换的命令为：（ ）
    - [ ] A ping
    - [ ] B ifconfig
    - [x] C arp
    - [ ] D traceroute
    答案：C

43. 在vi编辑器中的命令模式下，键入（ ）可在光标当前所在行下添加一新行。
    - [ ] A <a>
    - [x] B <o>
    - [ ] C <I>
    - [ ] D 
    答案：B

44. 在vi编辑器中的命令模式下，删除当前光标处的字符使用（ ）命令。
    - [x] A <x>
    - [ ] B <d><w>
    - [ ] C <D>
    - [ ] D <d><d>
    答案：A

45. 在vi编辑器中的命令模式下，重复上一次对编辑的文本进行的操作，可使用（ ）命令
    - [ ] A 上箭头
    - [ ] B 下箭头
    - [x] C <.>
    - [ ] D <*>
    答案：C

46. 用命令ls -al显示出文件ff的描述如下所示，由此可知文件ff的类型为（ ）
    -rwxr-xr-- 1 root root 599 Cec 10 17:12 ff
    - [x] A 普通文件
    - [ ] B 硬链接
    - [ ] C 目录
    - [ ] D 符号链接
    答案：A

47. 删除文件命令为：（ ）
    - [ ] A mkdir
    - [ ] B rmdir
    - [ ] C mv
    - [x] D rm
    答案：D

48. 在下列的名称中，不属于DNS服务器类型的是：（ ）
    - [ ] A Primary Master Server
    - [ ] B Secondary Master Server
    - [x] C samba
    - [ ] D Cache_only Server
    答案：C

49. 网络管理员对WWW服务器进行访问、控制存取和运行等控制，这些控制可在（ ）文件中体现。
    - [x] A httpd.conf
    - [ ] B lilo.conf
    - [ ] C inetd.conf
    - [ ] D resolv.conf
    答案：A

50. 邮件转发代理也称邮件转发服务器，它可以使用SMTP协议，也可以使用（ ）协议。
    - [ ] A FTP
    - [ ] B TCP
    - [x] C UUCP
    - [ ] D POP
    答案：C

51. 启动samba服务器进程，可以有两种方式：独立启动方式和父进程启动方式，其中前者是在（ ）文件中以独立进程方式启动。
    - [ ] A /usr/sbin/smbd
    - [ ] B /usr/sbin/nmbd
    - [x] C rc.samba
    - [ ] D /etc/inetd.conf
    答案：C

52. DHCP是动态主机配置协议的简称，其作用是可以使网络管理员通过一台服务器来管理一个网络系统，自动地为一个网络中的主机分配（ ）地址。
    - [ ] A 网络
    - [ ] B MAC
    - [ ] C TCP
    - [x] D IP
    答案：D

53. 为了保证在启动服务器时自动启动DHCP进程，应将（ ）文件中的dhcpd=no改为dhcpd=yes。
    - [x] A rc.inet1
    - [ ] B lilo.conf
    - [ ] C inetd.conf
    - [ ] D httpd.conf
    答案：A

54. 对文件进行归档的命令为（ ）
    - [ ] A dd
    - [ ] B cpio
    - [ ] C gzip
    - [x] D tar
    答案：D

55. 改变文件所有者的命令为（ ）
    - [ ] A chmod
    - [ ] B touch
    - [x] C chown
    - [ ] D cat
    答案：C

56. 在给定文件中查找与设定条件相符字符串的命令为：（ ）
    - [x] A grep
    - [ ] B gzip
    - [ ] C find
    - [ ] D sort
    答案：A

57. 建立一个新文件可以使用的命令为（ ）
    - [ ] A chmod
    - [ ] B more
    - [ ] C cp
    - [x] D touch
    答案：D

58. 在下列命令中，不能显示文本文件内容的命令是：（ ）
    - [ ] A more
    - [ ] B less
    - [ ] C tail
    - [x] D join
    答案：D

59. 在使用匿名登录ftp时，用户名为（ ）
    - [ ] A users
    - [x] B anonymous
    - [ ] C root
    - [ ] D guest
    答案：B

60. 在实际操作中，想了解命令logname的用法，可以键入（ ）得到帮助。
    - [ ] A logname --man
    - [ ] B logname/?
    - [ ] C help logname
    - [x] D logname --help
    答案：D

61. 如果LILO被安装在MBR，使用（ ）命令即可卸载LILO。
    - [x] A lilo –u
    - [ ] B lilo –c
    - [ ] C lilo –v
    - [ ] D lilo -V
    答案：A

62. 当用命令ls –al查看文件和目录时，欲观看卷过屏幕的内容，应使用组合键（ ）
    - [ ] A Shift+Home
    - [ ] B Ctrl+ PgUp
    - [ ] C Alt+ PgDn
    - [x] D Shift+ PgUp
    答案：D

63. mc是UNIX风格操作系统的（ ）
    - [ ] A 文件编辑器/程序编译器
    - [ ] B 配置网络的窗口工具
    - [x] C 目录浏览器/文件管理器
    - [ ] D Samba服务器管理工具
    答案：C

64. i节点是一个（ ）长的表，表中包含了文件的相关信息。
    - [ ] A 8字节
    - [ ] B 16字节
    - [ ] C 32字节
    - [x] D 64字节
    答案：D

65. 文件权限读、写、执行的三种标志符号依次是（ ）
    - [x] A rwx
    - [ ] B xrw
    - [ ] C rdx
    - [ ] D srw
    答案：A

66. Linux文件名的长度不得超过（ ）个字符。
    - [ ] A 64
    - [ ] B 128
    - [x] C 256
    - [ ] D 512
    答案：C

67. 进程有三种状态：（ ）
    - [ ] A 准备态、执行态和退出态
    - [ ] B 精确态、模糊态和随机态
    - [x] C 运行态、就绪态和等待态
    - [ ] D 手工态、自动态和自由态
    答案：C

68. 从后台启动进程，应在命令的结尾加上符号（ ）
    - [x] A &
    - [ ] B @
    - [ ] C #
    - [ ] D $
    答案：A

69. （ ）不是邮件系统的组成部分。
    - [ ] A 用户代理
    - [x] B 代理服务器
    - [ ] C 传输代理
    - [ ] D 投递代理
    答案：B

70. 在Shell脚本中，用来读取文件内各个域的内容并将其赋值给Shell变量的命令是（ ）
    - [ ] A fold
    - [ ] B join
    - [ ] C tr
    - [x] D read
    答案：D

71. crontab文件由六个域组成，每个域之间用空格分割，其排列如下：（ ）
    - [ ] A MIN HOUR DAY MONTH YEAR COMMAND
    - [x] B MIN HOUR DAY MONTH DAYOFWEEK COMMAND
    - [ ] C COMMAND HOUR DAY MONTH DAYOFWEEK
    - [ ] D COMMAND YEAR MONTH DAY HOUR MIN
    答案：B

72. 用ftp进行文件传输时，有两种模式：（ ）
    - [ ] A Word 和binary
    - [ ] B .txt 和Word Document
    - [x] C ASCII 和binary
    - [ ] D ASCII 和Rich Text Format
    答案：C

73. 某文件的组外成员的权限为只读；所有者有全部权限；组内的权限为读与写，则该文件的权限为（ ）
    - [ ] A 467
    - [ ] B 674
    - [ ] C 476
    - [x] D 764
    答案：D

74. 在DNS系统测试时，设named进程号是53，命令（ ）通知进程重读配置文件。
    - [ ] A kill –USR2 53
    - [ ] B kill –USR1 53
    - [ ] C kill -INT 63
    - [x] D kill –HUP 53
    答案：D

75. Apache服务器默认的接听连接端口号是（ ）
    - [ ] A 1024
    - [ ] B 800
    - [x] C 80
    - [ ] D 8
    答案：C

76. PHP和MySQL的联合使用解决了（ ）
    - [ ] A 在Proxy上处理数据库的访问问题
    - [ ] B 在WWW服务器上处理黑客的非法访问问题
    - [x] C 在WWW服务器上处理数据库的访问问题
    - [ ] D 在Sendmail邮件系统上处理数据库的访问问题
    答案：C

77. OpenSSL是一个（ ）
    - [x] A 加密软件
    - [ ] B 邮件系统
    - [ ] C 数据库管理系统
    - [ ] D 嵌入式脚本编程语言
    答案：A

78. Samba服务器的配置文件是（ ）
    - [ ] A httpd.conf
    - [ ] B inetd.conf
    - [ ] C rc.samba
    - [x] D smb.conf
    答案：D

79. 关于DNS服务器，叙述正确的是（ ）
    - [ ] A DNS服务器配置不需要配置客户端
    - [ ] B 建立某个分区的DNS服务器时只需要建立一个主DNS服务器
    - [ ] C 主DNS服务器需要启动named进程，而辅DNS服务器不需要
    - [x] D DNS服务器的root.cache文件包含了根名字服务器的有关信息
    答案：D

80. 退出交互模式的shell，应键入（ ）
    - [ ] A ;
    - [ ] B ^q
    - [x] C exit
    - [ ] D quit
    答案：C