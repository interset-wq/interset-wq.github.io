# 样题

## 一、单项选择题
1. 操作系统负责管理计算机系统的______，其中包括处理机、存储器、设备和文件。
   - [ ] A 程序
   - [ ] B 文件
   - [x] C 资源
   - [ ] D 进程


2. 下面哪一个操作系统不属于Linux家族
   - [ ] A Ubuntu
   - [ ] B CentOS
   - [x] C Solaris
   - [ ] D Red Hat


3. 下列哪一个指令可以设定使用者的密码
   - [ ] A pwd
   - [ ] B newpwd
   - [x] C passwd
   - [ ] D password


4. 切换工作目录的命令是
   - [ ] A pwd
   - [x] B cd
   - [ ] C who
   - [ ] D ls


5. 已知执行ls的结果是 `chapter chapter1 chapter123 oschapter1`，那么执行`ls chapter[0-9]*`的结果是
   - [x] A chapter1 chapter123
   - [ ] B chapter chapter1 chapter123
   - [ ] C chapter1 chapter123 oschapter1
   - [ ] D chapter chapter1 chapter123 oschapter1


6. 在bash中，在一条命令后加入"2>& 1"，表示
   - [ ] A 标准错误输出重定向到标准输入
   - [ ] B 标准输入重定向到标准错误输出
   - [x] C 标准错误输出重定向到标准输出
   - [ ] D 标准输出重定向到标准输入


7. 默认情况下管理员创建了一个用户，就会在______目录下创建一个用户主目录。
   - [ ] A /usr
   - [x] B /home
   - [ ] C /root
   - [ ] D /etc


8. 下面哪个参数可以删除一个用户并同时删除用户的home目录
   - [ ] A rmuser -r
   - [ ] B deluser -r
   - [x] C userdel -r
   - [ ] D usermgr –r


9. 用ls -l命令列出下面的文件列表，______是软链接文件。
   - [ ] A -rw-rw-rw- 2 stu users 56 Sep 09 11:05 file1
   - [ ] B -rwxrwxrwx 2 stu users 56 Sep 09 11:05 ex1
   - [ ] C drwxr--r-- 1 stu users 1024 Sep 10 08:10 zhang
   - [x] D lrwxr--r-- 1 stu users 2024 Sep 12 08:12 cheng


10. 为了使文件的所有者有读和写的权限，而同组用户和其他用户只能进行只读访问，在设置文件的许可值时，应当设为
    - [ ] A 566
    - [x] B 644
    - [ ] C 655
    - [ ] D 744
 

11. 用户编写了一个文本文件file，想将该文件名称改为text，下列哪个命令可以实现
    - [ ] A cd file text
    - [ ] B echo file > text
    - [ ] C rm file text
    - [x] D cat file > text
 

12. cd ~命令的含义是
    - [ ] A 到当前目录
    - [ ] B 到根目录
    - [ ] C 到/root目录
    - [x] D 到用户的home目录
 

13. 在ps命令中，以下哪个参数是用来显示所有用户的进程的
    - [x] A a
    - [ ] B b
    - [ ] C u
    - [ ] D x
 

14. 以下哪个命令可以终止一个用户的所有进程
    - [ ] A skillall
    - [ ] B skill
    - [ ] C kill
    - [x] D killall
 

15. 在应用程序启动时，可以使用以下哪个命令设置进程的优先级
    - [ ] A priority
    - [x] B nice
    - [ ] C renice
    - [ ] D setpri
 

16. 如何从当前系统中卸载一个已装载的文件系统
    - [x] A umount
    - [ ] B dismount
    - [ ] C mount -u
    - [ ] D 从/etc/fstab中删除这个文件系统项
 

17. 哪个命令用来显示系统中各个分区中inode的使用情况
    - [x] A df -i
    - [ ] B df -H
    - [ ] C free -b
    - [ ] D du -a -c /
 

18. 为了能够把新建立的文件系统mount到系统目录中，还需要指定该文件系统的在整个目录结构中的位置，称为
    - [ ] A 子目录
    - [x] B 挂载点
    - [ ] C 新分区
    - [ ] D 目录树
 

19. 在大多数Linux发行版本中，以下哪个属于块设备(block devices)
    - [ ] A 串行口
    - [x] B 硬盘
    - [ ] C 虚拟终端
    - [ ] D 打印机
 

20. 在Linux中第一块IDE磁盘的名字为
    - [ ] A /dev/hdb
    - [ ] B /dev/hdc
    - [x] C /dev/hda
    - [ ] D /dev/hdd
 

21. 查看swap空间的使用情况该使用哪个命令
    - [ ] A df
    - [ ] B swapon
    - [x] C free
    - [ ] D fdisk
 

22. 下列哪项可能是Linux系统中以太网网络接口
    - [ ] A 10
    - [x] B eth2
    - [ ] C net0
    - [ ] D neta
 

23. 用什么命令可直接显示Linux系统当前定义的主机名
    - [ ] A ipname
    - [ ] B host
    - [ ] C ifconfig
    - [x] D hostname
 

24. 下列哪个命令可列出所有当前活跃的网络接口
    - [x] A ifconfig
    - [ ] B 1snet
    - [ ] C shownet
    - [ ] D 以上都不是
 

25. 下列哪个程序可用来确定两台机器间底层的IP连接性
    - [ ] A host
    - [ ] B netstat
    - [ ] C ifeonfig
    - [x] D ping
 

26. 在Linux终端启动Apache的命令为
    - [x] A service httpd start
    - [ ] B service start
    - [ ] C httpd start
    - [ ] D start
 

27. Linux的日志文件通常保存在
    - [x] A /var/log
    - [ ] B /usr/adm
    - [ ] C /etc/
    - [ ] D /var/run
 

28. 在VI编辑器最后一行显示“4 lines yanked”，则所输入的命令是
    - [ ] A 4yb
    - [ ] B 4p
    - [x] C 4yy
    - [ ] D 4yw
 

29. 在VI编辑器中，如果用户想在每次对文件进行编辑时都收到反馈信息，可以输入
    - [ ] A set scroll=0
    - [ ] B set shiftwidth =0
    - [ ] C set wrapmargin=0
    - [x] D set report=0
 

30. 在Emacs中，以下哪种操作可以实现打开另一个文件以替换当前打开的文件
    - [ ] A 先同时按`Ctrl`+`x`组合键，再同时按 `Ctrl`+`i`组合键。
    - [ ] B 先同时按`Ctrl`+`x`组合键，再同时按 `Ctrl`+`f`组合键。
    - [ ] C 先同时按`Ctrl`+`x`组合键，再同时按 `Ctrl`+`b`组合键。
    - [x] D 先同时按`Ctrl`+`x`组合键，再同时按 `Ctrl`+`v`组合键。
 

31. Emacs中将光标向前移动一屏的命令是
    - [x] A  `Ctrl`+`v`
    - [ ] B `Alt`+`v`
    - [ ] C  `Ctrl`+`b`
    - [ ] D `Alt`+`b`
 

32. Emacs中模式行的显示模式字段中“%%”表示
    - [ ] A 缓冲区未被编辑
    - [ ] B 缓冲区中的文本已经被修改
    - [x] C 缓冲区中的文本未被修改
    - [ ] D 只读缓冲区中的文本已经被修改
 

33. SSH是什么协议
    - [x] A 安全外壳
    - [ ] B 请求-响应
    - [ ] C 地址解析
    - [ ] D 动态主机配置
 

34. 以下协议中，为远程登录会话和其他网络服务提供安全性的协议是
    - [ ] A FTP
    - [ ] B HTTP
    - [x] C SSH
    - [ ] D ICMP
 

35. OpenSSH的默认端口号为
    - [ ] A 80
    - [ ] B 8080
    - [ ] C 21
    - [x] D 22
 

36. 使用GDB命令对查看某个变量的类型时，应使用命令
    - [ ] A set
    - [x] B whatis
    - [ ] C kill
    - [ ] D print
 

37. 在使用GCC命令式，如果想产生调试信息，需要加入以下哪个选项
    - [ ] A -w
    - [ ] B -I
    - [x] C -g
    - [ ] D –d
 

38. 下面关于make命令，说法错误的是
    - [ ] A make工具可以用来维护程序模块关系和生成可执行程序
    - [ ] B make命令是GNU的工程化编译工具，它用于编译大量互相关联的源代码
    - [x] C makefile文件中目标文件后面跟的是源文件，最后是生成源文件的命令
    - [ ] D make命令从makefile文件中获取模块之间的依赖关系
 

39. FTP是什么协议
    - [ ] A 域名系统
    - [ ] B 动态主机配置
    - [x] C 文件传输
    - [ ] D 文件解析
 

40. 下列哪个不是Web应用开发框架
    - [ ] A Spring
    - [x] B Unity
    - [ ] C Struts2
    - [ ] D MyBatis
 

## 二、填空题
41. 按照冯诺依曼体系结构，传统的单核CPU由运算器和 **控制器** 这两个主要部件组成。
42. Linux下的软件包可细分为两种，分别是 **源码包** 和二进制包。
43. 在shell中， **管道符** 是由竖杠 `|` 代表，用来连接多条命令。
44. DNS服务使用的端口是 **53** 。
45. 使用 **su** 命令可以将用户身份临时改变为root。
46. 已知shell变量nu=aaa，现在希望nu的值是aaabbb，则应执行命令 `nu=${nu}bbb`。
47. 命令 `mount -a` 用来装载所有在/etc/fstab中定义的文件系统。
48. 通过DHCP获得信息的机器没有固定的IP地址，用 `ifup` 命令增加网络接口时，系统动态获得一个IP地址，用 `ifdown` 命令减少网络接口时，系统就释放一个IP地址。
49. VI打开文档后，想把10-15行中的第一个'abc'替换为'efg'，应输入命令 `10,15s/abc/efg` 。
50. 编译器GCC会在系统默认的路径中(如usr/lib) 寻找所需的库文件，当使用了 `-L` 选项指定库文件路径后，会首先到指定的目录名下去寻找相关库文件。

## 三、综合题

### 综合题1

在/tmp/source目录下有一个只读test.c文件如下：

```c
#include <stdio.h>
int main() {
    printf("This is test.\n");
    printf("This is another test.\n");
    return 0;
}
```

用户当前在 `/` 目录下，进行如下操作：

- 在 /tmp 目录下创建一个名为 target 的目录，应输入命令：`mkdir /tmp/target`
- `cd /tmp/target`，输入命令 `cp /tmp/source/test.c`，将 test.c 文件复制到当前目录
- 调用命令 `chmod a+rw test.c`，将文件改为可写形式
- `vi test.c` 启动编辑
- 使用 `1,$s/This/That/g` 命令把文件中的字符串 “This” 全都替换为 “That”
- 将光标移到第 4 行，输入命令 `dd` 删除该行
- 输入命令 `:wq` 保存并退出 vi 编辑器
- 用户用 scp 命令把 /tmp/target/test.c 文件上传至 IP 地址为 10.0.0.50 的服务器的 /tmp 目录下，命令中需指定访问服务器的用户名为 user1，应输入：`[root@localhost ~]# scp /tmp/target/test.c user1@10.0.0.50:/tmp/`
- 上传成功后，用户使用 ssh 以 user1 身份登录服务器，应输入：`[root@localhost ~]# ssh user1@10.0.0.50`
- 登录服务器后进入 /tmp 目录，调用 gcc 编译 test.c，指定输出文件名为 mytest，并要求产生调试信息，应输入：`[user1@10.0.0.50: /tmp]$ gcc -g test.c -o mytest`
- 编译成功后，输入命令 `gdb mytest` 启动 GDB 对 mytest 进行调试
- 调试过程中，如需在程序第 3 行设置断点，可输入命令 `break 3`

### 综合题2

写一个猜数字 shell 脚本，当用户输入的数字和预设数字 (随机生成一个小于 100 的数字)  一样时，直接退出，否则让用户一直输入，并且提示用户的数字比预设数字大或者小。答题要求：在横线处补充相应内容。

``` shell
___(1)___
m=`echo $RANDOM`
n1=$[___(2)___%100]
___(3)___ :
do
    ___(4)___ "Please input a number:" n
    if [ $n == $n1 ]
    then
        ___(5)___
    ___(6)___
    then
        echo "bigger"
        continue
    ___(7)___
        echo "smaller"
        continue
    ___(8)___
___(9)___
___(10)___ "You are right."
```


参考答案：
(1  #!/bin/bash
(2  $m
(3  while
(4  read -p
(5  break
(6  elif [ $n -gt $n1 ]
(7  else
(8  fi
(9  done
(10  echo
