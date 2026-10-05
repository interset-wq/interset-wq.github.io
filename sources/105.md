# 知识点整理

## 第3章 Linux 系统使用基础

### 3.3 常用Linux 命令

#### 3.3.1 Linux 命令的基本格式

1. 打开shell 方式:"开始"菜单中选择应用程序-附件-终端,命令提示符格式:`[root@localhost:~]#`
   - `root`:当前登录用户;
   - `localhost`:当前系统的简写主机名(完整名localhost.localdommain);
   - `~`:用户当前所在目录;
   - `#`:命令提示符(root用户为#,普通用户为$)｡
2. 家目录(主目录):用户登录后的初始位置,超级用户家目录为`/root`,普通用户家目录为`/home/用户名`;初始登录状态下,用户创建的文件默认放入家目录;切换目录命令是cd｡
3. Linux 命令的基本格式: `命令 [选项] [参数]`
   - 选项:分为短格式选项(-l,英文简写)和长格式选项(--all,完整英文单词),用于调整命令执行方式;
   - 参数:命令的操作对象｡

#### 3.3.2 Linux 简单命令

##### 3.3.2.1 w 和who 命令

1. 功能:均用于查看服务器上已登陆的用户信息;区别是w 命令还能显示每个用户执行任务的情况｡
2. w 命令基本格式: `w [选项] [用户名]`
   - 仅跟用户名:只显示该用户信息;
   - 选项:-h(不显示输出标题)､-l(详细格式输出)､-s(简洁格式输出)｡
3. who 命令基本格式: `who [选项] [file]`
   - 无指定文件:默认通过/var/run/utmp 文件获取登录用户信息;
   - 选项:-a(列出所有信息,相当于所有选项)､-b(列出系统最近启动时间)､-l(列出所有可登录终端信息)､-m(仅列出当前终端信息,相当于who am I)､-s(仅显示名称､线路和时间字段,默认选项)｡

``` bash
$ w
 23:03:55 up 3 min,  1 user,  load average: 0.02, 0.06, 0.02
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU  WHAT
d111kc   pts/1    -                23:02    1:49   0.02s  0.01s -bash
$ who
d111kc   pts/1        2025-09-15 23:02
```

##### 3.3.2.2 echo 命令

1. 功能:将命令行中的参数显示到标准输出(屏幕)上｡
2. 命令格式: `echo [选项] [输出内容]`
3. 选项:
   - -n:取消输出后行末的换行符号(内容输出后不换行);
   - -e:使用转义字符
4. -e 选项支持的控制字符:
   - \\:输出\本身;
   - \a:输出警告音;
   - \b:退格键(向左删除键);
   - \c:取消输出行末的换行符(同-n);
   - \e:Esc 键;
   - \f:换页符;
   - \n:换行符;
   - \r:回车键;
   - \t:制表符(Tab 键);
   - \v:垂直制表符;
   - \0nnn:按八进制ASCII 码表输出字符;
   - \xhh:按十六进制ASCII 码表输出字符｡

``` bash
$ echo -e "hello\nworld"
hello
world
$ echo "hello\nworld"
hello\nworld
```

##### 3.3.2.3 date 命令

1. 功能:显示或设定系统的日期与时间｡
2. 设定时间格式: `date -s 时间值` (仅root 权限可设置)｡

``` bash
$ date
Mon Sep 15 23:05:50 CST 2025
```

##### 3.3.2.4 passwd 命令

1. 功能:密码配置指令｡
2. 基本格式: `passwd [选项] 用户名`
3. 权限规则:
   - 普通用户:仅能修改自己的密码,需先输入旧密码;
   - 超级用户(root):可修改自己和普通用户的密码,无需输入旧密码｡

``` bash
$ passwd
Changing password for d111kc.
Current password:
New password:
Retype new password:
passwd: password updated successfully
```

### 3.4 软件包

1. Linux 的软件包分类:源码包和二进制包｡
2. 源码包:因常用打包压缩格式为"tar.gz",故又称Tarball(Tarball 是打包工具)｡
3. 二进制包管理系统:两大主流——RPM 包管理系统､DPKG 包管理系统｡

### 3.5 本地软件安装､运行与卸载

#### 3.5.1 RPM 包安装､卸载和升级

在 Linux 系统中，rpm 是 Red-Hat Package Manager（红帽包管理器） 的缩写，是一种用于管理软件包的工具和文件格式，主要应用于基于 Red Hat 架构的 Linux 发行版（如 CentOS、Fedora、RHEL 等）。

RPM二进制包的命名须遵守统一的命名规则，用户通过名称就可以直接获取这类包的版本、适用平台等信息。

RPM二进制包命名的一般格式如下：`包名-版本号-发布次数.发行商.Linux平台.适合的硬件平台.包扩展名`

例如，RPM包的全名是 `httpd-2.2.15-15.el6.centos.1.i686.rpm`

1. RPM 包默认安装路径:`/etc/`､`/usr/bin/`､`/usr/lib/`､`/usr/share/doc/`､`/usr/share/man/`(建议不手动指定安装路径)｡
2. RPM 包安装命令格式: `rpm -ivh 包全名`
   - 选项含义:-i(安装,install)､-v(显示详细信息,verbose)､-h(显示安装进度,hash);
   - 批量安装:空格分隔多个包,如 `rpm -ivh a.rpm b.rpm c.rpm`
3. 安装后启动服务: `service 服务名 start | stop | restart | status`
   - 参数含义:start(启动)､stop(停止)､restart(重启)､status(查看状态)｡
4. RPM 包升级:
   - `rpm -Uvh 包全名`:若软件未安装则直接安装,若已安装则升级至最新版本(-U 选项);
   - `rpm -Fvh 包全名`:仅升级已安装的软件,未安装则不操作(-F 选项)｡
5. RPM 包卸载:
   - 注意事项:需考虑包之间的依赖性(如先装httpd,后装mod_ssl,卸载时需先卸mod_ssl,再卸httpd);
   - 命令格式: `rpm -e 包名` (-e:卸载,erase);
   - 可选选项:"-nocteps":不检测依赖性直接卸载(不推荐)｡
6. 软件包查询:
   - 命令格式: `rpm 选项 查询对象`
   - 常用选项:
     - -q 包名:查询是否安装(querry);
     - -qa:查询所有已安装软件包(可搭配管道符,如 rpm -qa | grep httpd);
     - -qi 包名:查询已安装软件包的详细信息(-i:information);
     - -qip 包全名:查询未安装软件包的详细信息(-p:package,需指定绝对路径+包全名);
     - -ql 包名:查询已安装软件包包含的所有文件及安装位置(-l:list);
     - -qlp 包全名:查询未安装软件包包含的文件及计划安装路径;
     - -qf 系统文件名:反向查询文件所属的RPM 包(-f:file,仅RPM 安装的文件可用),如 rpm -qf /bin/ls｡

## 第4章 shell 脚本编程基础

### 4.1 shell 编程概述

1. shell 本质:用C 语言编写的程序,是连接用户和UNIX/Linux 内核的桥梁｡
2. 脚本头部标识:`#!/bin/bash`:放在脚本第一行,指定脚本使用的shell,用于调用相应解释程序执行｡
3. 注释符:#:单行注释符,用于说明程序功能､结构､算法和变量作用,增加可读性｡
4. 脚本执行前提:Linux 中创建文件默认不可执行,需修改文件权限(增加可执行权限)后,在命令行输入相对路径`./文件名`运行｡
5. 创建文件命令: `touch 文件名`
6. 查看shell 种类: `cat /etc/shells`

``` bash
$ cat /etc/shells 
# /etc/shells: valid login shells
/bin/sh
/usr/bin/sh
/bin/bash
/usr/bin/bash
/bin/rbash
/usr/bin/rbash
/usr/bin/dash
/usr/bin/tmux
```

7. 命令/脚本执行与PATH 环境变量的关系:
   - PATH 环境变量的作用:决定shell 到哪些目录中寻找命令或可执行程序;
   - 运行命令/程序时,shell 按PATH 目录顺序依次搜寻｡
8. 脚本运行3 种方式:
   - 脚本权限设为可执行,提示符下直接运行;
   - 将脚本名作为参数传递给shell 程序;
   - 将脚本以输入重定向的方式传递给bash｡

### 4.2 shell 基础

#### 4.2.1 通配符

1. 通配(Globbing):文件名的扩展功能｡
2. 常用通配符:
   - `*`:匹配任意字符的0 次或多次出现;
   - `?`:匹配任意单个字符;
   - `[ ]`:匹配该字符组限定的任何一个字符;
   - `[^ ]` 或`[! ]`:匹配不在该字符组中的任何一个字符;
   - `{string1,string2,...}`:匹配其中一个指定的字符串｡

``` bash
$ ls
chapter  chapter1  chapter123  oschapter1
$ ls chapter[0-9]*
chapter1:

chapter123:
```

#### 4.2.2 引号与转义字符

1. 转义字符"\":按下前,特殊字符按特殊含义执行;按下后,特殊字符按普通含义执行｡
2. shell 中的3 种引用字符:
   - 单引号:引用的所有字符均为普通字符,无特殊含义;
   - 双引号:保留"$"(引用变量值)､"\"(转义)和倒引号"`"(引用命令)的特殊含义;
   - 倒引号:引用的字符被解释为命令行,shell 先执行该命令,并以输出结果取代倒引号部分｡

``` bash
$ echo `pwd`
/mnt/e/MyNoteRepo/linux/temp
```

#### 4.2.3 输入/输出重定向符

输入/输出方向:数据的流动方向｡

##### 4.2.3.1 标准输入重定向

- `command < file`:将文件作为命令的输入

``` bash
$ cat hello.txt 
total 0
drwxrwxrwx 1 d111kc d111kc 4096 Sep 11 09:40 ./
drwxrwxrwx 1 d111kc d111kc 4096 Sep 10 19:27 ../
drwxrwxrwx 1 d111kc d111kc 4096 Sep 11 09:31 .git/
drwxrwxrwx 1 d111kc d111kc 4096 Aug 25 21:53 .vscode/
drwxrwxrwx 1 d111kc d111kc 4096 Aug 25 21:53 JavaScript/
-rwxrwxrwx 1 d111kc d111kc   29 Aug 13 11:52 README.md*
drwxrwxrwx 1 d111kc d111kc 4096 Aug 25 21:53 algo/
drwxrwxrwx 1 d111kc d111kc 4096 Sep  6 20:45 c/
drwxrwxrwx 1 d111kc d111kc 4096 Aug 25 21:53 english/
drwxrwxrwx 1 d111kc d111kc 4096 Aug 25 21:53 git/
drwxrwxrwx 1 d111kc d111kc 4096 Aug 25 21:53 h5/
drwxrwxrwx 1 d111kc d111kc 4096 Sep 11 09:34 linux/
drwxrwxrwx 1 d111kc d111kc 4096 Aug 25 21:53 math/
drwxrwxrwx 1 d111kc d111kc 4096 Aug 25 21:53 other/
drwxrwxrwx 1 d111kc d111kc 4096 Aug 25 21:53 powershell/
drwxrwxrwx 1 d111kc d111kc 4096 Aug 25 21:53 python/
drwxrwxrwx 1 d111kc d111kc 4096 Sep 11 09:30 reference/
$ wc -l < hello.txt 
18
```

- 2. `command << 分界符`:从标准输入读入,直到遇见分界符停止(替代默认的Ctrl+D 结束输入)｡

##### 4.2.3.2 标准输出重定向
- `command > file`:以覆盖方式,将command 的正确输出写入file(文件不存在则创建,存在则覆盖原内容)
- `command >> file`:以追加方式,将command 的正确输出写入file｡

``` bash
$ echo hello > file1
$ echo world > file2
$ echo "hello linux" >> file2
$ cat file1 file2 > file3
$ cat file1
hello
$ cat file2
world
hello linux
$ cat file3
hello
world
hello linux
```

##### 4.2.3.3 文件描述符

- 定义:输出重定向完整写法为fd>file 或fd>>file,fd 为文件描述符,默认不写为1;
- 常用文件描述符:
  - 标准输入(stdin):0;
  - 标准输出(stdout):1;
  - 错误输出(stderr):2;
- 示例:
  -  grep li si file 2> errfile(将错误输出写入errfile);
  -  grep li si file > file1 2>&1(正确和错误输出均写入file1,注意2>& 之间无空格);
  -  ls -l > /dev/null(输出重定向到/dev/null,数据被丢弃,无法恢复)｡

#### 4.2.4 命令执行操作符

1. 顺序执行:用";"连接多条命令,依次执行｡
2. 逻辑与("&&"):仅当前一条命令正确执行时,后一条命令才执行｡
3. 逻辑或("||"):仅当前一条命令执行错误时,后一条命令才执行｡

#### 4.2.5 小括号和大括号

1. shell 类型:
   - 交互shell:启动后等待用户输入命令,执行完显示提示符;
   - 非交互shell:运行外部命令或脚本时,交互shell 创建的子shell,运行结束后子shell 进程结束｡
2. 命令组合:小括号()和大括号{}均可将若干命令括起,逻辑上视为一条命令｡
3. 后台进程:运行过程中不响应用户输入和终端控制信号,但结果仍可能输出到显示器｡

## 第5章 用户管理

### 5.1 用户与用户组管理

1. 用户名和ID 对应关系存储文件:/etc/passwd

``` bash
$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
_apt:x:42:65534::/nonexistent:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:998:998:systemd Network Management:/:/usr/sbin/nologin
systemd-timesync:x:996:996:systemd Time Synchronization:/:/usr/sbin/nologin
dhcpcd:x:100:65534:DHCP Client Daemon,,,:/usr/lib/dhcpcd:/bin/false
messagebus:x:101:101::/nonexistent:/usr/sbin/nologin
syslog:x:102:102::/nonexistent:/usr/sbin/nologin
systemd-resolve:x:991:991:systemd Resolver:/:/usr/sbin/nologin
uuidd:x:103:103::/run/uuidd:/usr/sbin/nologin
landscape:x:104:105::/var/lib/landscape:/usr/sbin/nologin
polkitd:x:990:990:User for polkitd:/:/usr/sbin/nologin
d111kc:x:1000:1000:,,,:/home/d111kc:/bin/bash
postgres:x:105:109:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash
postfix:x:106:110::/var/spool/postfix:/usr/sbin/nologin
sshd:x:107:65534::/run/sshd:/usr/sbin/nologin
```

2. 用户主目录创建规则:默认情况下,管理员创建用户时,在`/home` 目录下创建用户主目录｡
3. 用户密码信息存储目录:/etc

### 5.2 用户和用户组管理相关的文件

文件权限:

- /etc/passwd(用户基本信息):权限为rw-r--r--
- /etc/shadow(用户密码信息):权限为rw-------

``` bash
$ sudo cat /etc/shadow
[sudo] password for d111kc: 
root:$y$j9T$p3soBj08aYrVMxMB60k9Q.$FTWVh8JDB45bJnCbewcKfz7XtnZM17yyqzVTEYS6KN/:20313:0:99999:7:::
daemon:*:20094:0:99999:7:::
bin:*:20094:0:99999:7:::
sys:*:20094:0:99999:7:::
sync:*:20094:0:99999:7:::
games:*:20094:0:99999:7:::
man:*:20094:0:99999:7:::
lp:*:20094:0:99999:7:::
mail:*:20094:0:99999:7:::
news:*:20094:0:99999:7:::
uucp:*:20094:0:99999:7:::
proxy:*:20094:0:99999:7:::
www-data:*:20094:0:99999:7:::
backup:*:20094:0:99999:7:::
list:*:20094:0:99999:7:::
irc:*:20094:0:99999:7:::
_apt:*:20094:0:99999:7:::
nobody:*:20094:0:99999:7:::
systemd-network:!*:20094::::::
systemd-timesync:!*:20094::::::
dhcpcd:!:20094::::::
messagebus:!:20094::::::
syslog:!:20094::::::
systemd-resolve:!*:20094::::::
uuidd:!:20094::::::
landscape:!:20094::::::
polkitd:!*:20094::::::
d111kc:$y$j9T$ozJT7Pr6nfn8l1rFCo.yW1$5XIWHKWz2GQrmbZiuLdyl/4ljpgRvYLb48NxTv5l5F/:20313:0:99999:7:::
postgres:!:20337::::::
postfix:!:20341::::::
sshd:!:20341::::::
```

### 5.3 用户和用户组管理的命令

#### 5.3.1 用户的添加

1. 命令格式: `useradd 用户名`
2. 创建过程:
   - 系统读取/etc/login.defs 和/etc/default/useradd 配置文件;
   - 在/etc/passwd､/etc/shadow､/etc/group､/etc/gshadow 文件中添加用户数据;
   - 在/etc/default/useradd 设定目录下建立用户主目录;
   - 复制/etc/skel 目录所有文件到用户主目录｡
3. /etc/passwd 文件结构:每行7 个字段,格式为"用户名:密码:UID:GID:描述性信息:主目录:默认shell"，例如 `root:x:0:0:root:/root:/bin/bash`
   - 用户名:字符序列;
   - 密码:x 表示设密码,实际密码存于/etc/shadow;
   - UID:取值0-65535(0 为root,1-499 为系统用户,500+为普通用户);
   - GID:初始组仅1 个,附加组可多个;
   - 主目录:root 主目录为 `/root`,普通用户主目录为`/home/用户名`;
   - 默认shell:一般为`/bin/bash`｡



#### 5.3.2 密码配置命令

1. 命令格式: `passwd 用户名`
2. 权限规则:
   - 普通用户:仅能修改自己的密码;
   - 超级用户(root):可修改自己和其他用户的密码｡

#### 5.3.3 修改用户信息命令

1. 命令格式: `usermod [选项] 用户名`
2. 常用选项:
   - -L:临时锁定用户(Lock);
   - -U:解锁用户(Unlock)｡

#### 5.3.4 修改用户密码状态命令

命令格式: `change 用户名`

#### 5.3.5 删除用户命令

1. 命令格式: `userdel -r 用户名` (仅root 可用)｡
2. 选项含义:-r:删除用户的同时删除其家目录｡
3. 用户个人文件路径:
   - 主目录:/home/用户名;
   - 邮箱:/var/spool/mail/用户名｡

#### 5.3.7 用户间切换命令

1. 命令格式: `su [-] 用户名`
2. 选项含义:
   - `-`:切换用户身份的同时,切换工作环境(包括PATH 变量､MAIL 变量等);省略用户名时,默认切换为root

#### 5.3.8 用户组管理命令

1. 添加用户组: `groupadd [选项] 组名`
2. 修改用户组信息: `groupmod [选项] 组名`
3. 删除用户组:`groupdel 组名`(仅删除非用户初始组的组)
4. 组管理员设置(代替root 管理组): `gpasswd [选项] 组名`
   - 无选项:为组设置密码(仅root 可用);
   - -a user:将user 用户加入组;
   - -d user:将user 用户从组移除｡

## 第6章 文件管理

### 6.1 文件系统

1. 文件定义:文件系统中存储数据的命名对象,是用户最小的逻辑存储单元｡
2. Linux 文件系统结构:所有文件和目录组织成从根节点"/"开始的倒置树状结构,按名访问文件｡

#### 6.1.2 文件结构和类型

1. 文件组成:所有文件由数据项和文件控制块(索引节点)组成｡
2. 文件分类:
   - 按数据项结构:无结构文件(字符流文件)､有结构文件(如目录文件);
   - 常用分类:普通文件､目录文件､链接文件及设备文件｡
3. 路径表示方法:
   - 绝对路径:从根目录(/)开始的文件/目录名称;
   - 相对路径:相对于当前路径的文件/目录名称｡

### 6.2 文件与目录操作

#### 6.2.1 文件操作命令

##### 6.2.1.1 cat 命令

1. 功能:显示文件内容或连接合并文件｡
2. 命令格式:
   - 显示内容: `cat [选项] 文件名`
   - 合并文件: `cat 文件1 文件2 > 文件3`(覆盖文件3 内容,不存在则创建)｡
3. 常用选项:
   - -n:对输出的所有行编号;
   - -b:仅对非空行编号｡

##### 6.2.1.2 more 命令

1. 功能:分页显示文本文件内容，空格键翻页｡
2. 命令格式: `more 文件名`

##### 6.2.1.3 head 命令

1. 功能:显示文件的前若干行内容｡
2. 命令格式: `head [选项] 文件名`
3. 选项:`-n k`:显示前k 行内容(默认显示10 行)｡

``` bash
$ more hello.txt 
total 0
drwxrwxrwx 1 d111kc d111kc 4096 Sep 11 09:40 ./
drwxrwxrwx 1 d111kc d111kc 4096 Sep 10 19:27 ../
drwxrwxrwx 1 d111kc d111kc 4096 Sep 11 09:31 .git/
drwxrwxrwx 1 d111kc d111kc 4096 Aug 25 21:53 .vscode/
drwxrwxrwx 1 d111kc d111kc 4096 Aug 25 21:53 JavaScript/
-rwxrwxrwx 1 d111kc d111kc   29 Aug 13 11:52 README.md*
drwxrwxrwx 1 d111kc d111kc 4096 Aug 25 21:53 algo/
drwxrwxrwx 1 d111kc d111kc 4096 Sep  6 20:45 c/
drwxrwxrwx 1 d111kc d111kc 4096 Aug 25 21:53 english/
drwxrwxrwx 1 d111kc d111kc 4096 Aug 25 21:53 git/
drwxrwxrwx 1 d111kc d111kc 4096 Aug 25 21:53 h5/
drwxrwxrwx 1 d111kc d111kc 4096 Sep 11 09:34 linux/
drwxrwxrwx 1 d111kc d111kc 4096 Aug 25 21:53 math/
drwxrwxrwx 1 d111kc d111kc 4096 Aug 25 21:53 other/
drwxrwxrwx 1 d111kc d111kc 4096 Aug 25 21:53 powershell/
drwxrwxrwx 1 d111kc d111kc 4096 Aug 25 21:53 python/
drwxrwxrwx 1 d111kc d111kc 4096 Sep 11 09:30 reference/
$ head -n 2 hello.txt 
total 0
drwxrwxrwx 1 d111kc d111kc 4096 Sep 11 09:40 ./
$ head hello.txt 
total 0
drwxrwxrwx 1 d111kc d111kc 4096 Sep 11 09:40 ./
drwxrwxrwx 1 d111kc d111kc 4096 Sep 10 19:27 ../
drwxrwxrwx 1 d111kc d111kc 4096 Sep 11 09:31 .git/
drwxrwxrwx 1 d111kc d111kc 4096 Aug 25 21:53 .vscode/
drwxrwxrwx 1 d111kc d111kc 4096 Aug 25 21:53 JavaScript/
-rwxrwxrwx 1 d111kc d111kc   29 Aug 13 11:52 README.md*
drwxrwxrwx 1 d111kc d111kc 4096 Aug 25 21:53 algo/
drwxrwxrwx 1 d111kc d111kc 4096 Sep  6 20:45 c/
drwxrwxrwx 1 d111kc d111kc 4096 Aug 25 21:53 english/
```

##### 6.2.1.4 tail 命令

1. 功能:查看文件末尾的数据｡
2. 命令格式: `tail [选项] 文件名`
3. 选项:
   - `-n k`:显示后k 行内容;
   - `-f`:监听文件新增内容(中止按Ctrl+C)｡

##### 6.2.1.5 touch 命令

1. 功能:创建文件或修改文件时间参数｡
2. 命令格式: `touch [选项] 文件名`
3. 选项:-a:仅修改文件访问时间｡

##### 6.2.1.6 grep 命令

1. 功能:在一个或多个文件中搜索特定字符模式(正则表达式),模式可为字符､字符串､单词或句子｡
2. 正则表达式基础(与通配符含义不同):
   - `c*`:匹配0 个或多个字符c;
   - `.`:匹配任意一个字符;
   - `[xyz]`:匹配方括号中任意一个字符;
   - `[^xyz]`:匹配方括号中字符外的所有字符;
   - `^`:行首定位符;
   - `$`:行尾定位符｡
3. 命令格式: `grep [选项] 文件名`
4. 常用选项:-n:在每一行最前面列出行号｡

``` bash
$ cat file3
hello
world
hello linux
$ grep world file3
world
$ grep linux file3
hello linux
$ cat file3 | grep linux
hello linux
```

##### 6.2.1.7 sed 命令

1. 功能:自动编辑一个或多个文件,简化文件反复操作,编写转换程序｡
2. 命令格式: sed [选项] sed 命令文件名｡
3. 选项:
   - -n:仅显示匹配处理的行;
   - -e:执行多个编辑命令(一般用";"代替);
   - -i:直接在文件中修改(不输出到显示器);
   - -f:从脚本文件读取命令执行(每行一个命令,无需";")｡
4. 常用sed 编辑命令:
   - p:打印匹配行(print);
   - d:删除指定行(delete);
   - a:在匹配行后追加(append);
   - i:在匹配行前插入(insert);
   - c:整行替换;
   - r:读取文件内容;
   - w:将文本写入文件;
   - s:字符串替换(匹配正则表达式,substitution)｡

##### 6.2.1.8 awk 命令

1. 功能:格式化文本,进行复杂格式处理,擅长处理文本文件中的数据｡
2. 命令格式: awk [选项] ‘匹配规则|执行命令|’ 文件名｡
3. 数据字段变量(默认以空白字符为分隔符):
   - $0:代表整个文本行;
   - $1:代表第1 个数据字段;
   - $2:代表第2 个数据字段;
   - $n:代表第n 个数据字段｡
4. 自定义分隔符:用-F 选项指定,如 awk -F ',' '{print $1}' file｡
5. 示例:
   -  awk '{print $1}' file(打印每行第1 个字段);
   -  awk 'BEGIN {print "The File Contents:"} {print $0} END {print "End of File"}' file(添加文件首尾提示)｡

##### 6.2.1.9 cp 命令

1. 功能:复制文件和目录,支持复制整个目录｡
2. 命令格式: `cp [选项] 源文件 目标文件`
3. 常用选项:
   - -a:相当于-d､-p､-r 选项的集合;
   - -d:源文件为软链接时,复制的目标文件也为软链接;
   - -i:目标文件存在时,询问是否覆盖;
   - -l:创建源文件的硬链接(非复制文件);
   - -s:创建源文件的软链接(非复制文件);
   - -p:复制后保留原文件属性;
   - -r:递归复制(用于复制目录)｡

``` bash
$ ls
file1  folder
$ cp file1 folder
$ find
.
./file1
./folder
./folder/file1
$ cp file1 folder/file2
$ find
.
./file1
./folder
./folder/file1
./folder/file2
```

##### 6.2.1.10 rm 命令

1. 功能:永久性删除文件或目录，root用户谨慎使用这个命令｡
2. 命令格式: `rm [选项] 文件或目录`
3. 常用选项:
   - -f:强制删除(force);
   - -i:删除前询问;
   - -r:递归删除(用于删除目录,含目录内所有内容)｡

##### 6.2.1.11 mv 命令

1. 功能:移动文件/目录,或对文件/目录重命名｡
2. 命令格式: `mv [选项] 源文件 目标文件`
3. 常用选项:
   - -f:强制覆盖;
   - -i:目标文件存在时,询问是否覆盖(默认);
   - -n:目标文件存在时,不覆盖且不询问;
   - -v:显示移动过程;
   - -u:目标文件存在且源文件更新时,升级目标文件｡

##### 6.2.1.12 sort 命令

1. 功能:对文本排序,默认按ASCII 码值升序输出｡
2. 常用选项:-r:反向排序｡

##### 6.2.1.13 wc 命令

1. 功能:统计文本的行数､单词数或字符数｡
2. 常用选项:
   - -l:仅统计行数;
   - -w:仅统计单词数;
   - -m:仅统计字符数｡

#### 6.2.2 目录操作命令

##### 6.2.2.1 mkdir 命令

1. 功能:创建目录(make directories)｡
2. 命令格式: `mkdir [选项] 目录名`
3. 常用选项:
   - -m:手动配置目录权限(不使用默认权限);
   - -p:递归创建所有目录(如创建多级目录)｡

##### 6.2.2.2 rmdir 命令

1. 功能:删除空目录｡
2. 常用选项:-p:递归删除空目录｡

##### 6.2.2.3 cd 命令

1. 功能:切换工作目录(change directory)｡
2. 特殊符号含义:
   - ~:代表当前登录用户的主目录;
   - -:代表上次所在目录;
   - .:代表当前目录;
   - ..:代表上级目录｡

##### 6.2.2.4 pwd 命令

功能:显示当前所在目录(print working directory)｡

##### 6.2.2.5 ls 命令

1. 功能:显示当前目录下的内容｡
2. 默认行为:仅显示非隐藏文件名称,按文件名排序｡
3. 常用选项:-a:显示全部文件(包括开头为"."的隐藏文件)｡

##### 6.2.2.6 ln 命令

1. 功能:创建链接文件｡
2. 命令格式: `ln [选项] 源文件 目标文件`
3. 选项:-s:创建软链接(不加则创建硬链接)｡
4. 硬链接与软链接的区别:
   - 硬链接:修改源文件或硬链接,另一方数据均改变;不能跨文件系统(分区)建立,不能链接目录;
   - 软链接:相当于快捷方式;可跨分区,可链接目录;若删除源文件,软链接无法访问数据｡

### 6.3 访问权限管理

查看权限命令:`ls -al`(显示文件和目录的权限信息)

#### 6.3.2 权限位

1. 权限类型:对文件的读(r)､写(w)､执行(x)权限｡
2. 权限位格式:共10 位,第1 位表示文件类型,后9 位分3 组(每组3 位),分别对应所有者(u)､所属组(g)､其他人(o)的权限｡

``` bash
$ ls -l
total 0
-rwxrwxrwx 1 d111kc d111kc    0 Sep 11 12:49 file1
drwxrwxrwx 1 d111kc d111kc 4096 Sep 11 12:50 folder
```

#### 6.3.2 修改权限位的命令

##### 6.3.2.1 chmod 命令

1. 权限与数字对应关系:r=4､w=2､x=1｡
2. 数字方式修改权限:
   - 命令格式:`chmod 权限值 文件名`
   - 选项:-R:连同子目录中所有文件一起修改权限｡
3. 符号方式修改权限:
   - 格式:chmod 用户身份+/-/=权限 文件名;
   - 用户身份:u(所有者)､g(所属组)､o(其他人)､a(所有身份);
   - 操作符:+（添加权限）､-（移除权限）､=（设置权限）;
   - 示例:`chmod go+rwx file`(给所属组和其他人添加读､写､执行权限)｡

##### 6.3.2.2 umask 命令

1. 功能:设置新建文件和目录的默认权限｡
2. 默认umask 值:0022(第1 位为特殊权限,后3 位为实际掩码值,对应权限----w--w-)｡
3. 初始权限计算方式:文件(或目录)的初始权限=最大默认权限-umask 权限(按字母形式减法)｡
   - 文件最大默认权限:666(rw-rw-rw-);
   - 目录最大默认权限:777(rwxrwxrwx);
   - 示例:666-033=644(rw-r--r--)｡

##### 6.3.2.3 chown 命令
1. 功能:修改文件(或目录)的所有者｡
2. 命令格式:
   - 修改所有者:chown 所有者 文件或目录;
   - 同时修改所有者和所属组:chown 所有者:所属组 文件或目录;
   - 选项:-R:连同子目录中所有文件一起修改｡

##### 6.3.2.4 chgrp 命令

1. 功能:修改文件(或目录)的所属组｡
2. 命令格式:chgrp 所属组 文件名(或目录名)｡

## 第7章 进程管理
进程管理的3 个核心作用:

- 判断服务器的健康状态;
- 查看系统中所有进程;
- 杀死进程｡

### 7.2 进程监控

#### 7.2.1 ps 命令

1. 功能:查看系统中运行进程的详细信息(缺乏时效性,但最常用)｡
2. 常用选项:
   - -a:显示一个终端的所有进程(除会话引线外);
   - -u:显示进程的归属用户及内存使用情况;
   - -x:显示没有控制终端的进程;
   - -l:以长格式显示详细信息;
   - -e:显示所有进程｡
3. 推荐固定选项组合:
   - ps -aux:查看系统中所有进程;
   - ps -le:查看所有进程,并显示父进程PID 和进程优先级;
   - ps -l:仅查看当前shell 产生的进程｡
4. 僵尸进程:因进程非正常停止或程序编写错误,子进程先于父进程结束,且父进程未正确回收子进程,导致子进程长期存在于内存中｡

#### 7.2.2 pstree 命令

功能:以树形结构显示程序和进程之间的关系｡

#### 7.2.3 top 命令

1. 功能:动态持续监听进程运行状态,提供交互界面,支持定制输出｡
2. 默认行为:每隔3 秒刷新一次输出｡
3. 缓存与缓冲的区别:
   - 缓存:读取硬盘数据时,将常用数据存入内存缓存区,后续读取直接从缓存获取,加快读取速度;
   - 缓冲:写入硬盘数据时,先将数据放入缓冲区,再集中写入硬盘,减少磁盘碎片和寻道次数,加快写入速度｡

#### 7.2.4 lsof 命令

1. 功能:list opened files,查询进程调用的文件(ps 命令可查进程, lsof 可查进程关联的文件)｡
2. 常用选项:
   - -c 字符串:仅列出以该字符串开头的进程打开的文件;
   - -p PID:列出指定PID 进程打开的文件｡

### 7.3 结束进程

1. 进程信号:进程管理(关闭､重启)依赖信号,可用"kill -l"查询系统识别的信号｡
2. 常见进程信号:
   - 1(SIGHUP):进程立即关闭,重新读取配置文件后重启;
   - 9(SIGKILL):立即结束程序运行,不可被阻塞､处理和忽略,用于强制终止进程;
   - 15(SIGTERM):正常结束进程的默认信号,若进程异常则无法终止,需用SIGKILL(信号9)｡
3. 强制终止高资源消耗进程:最合适的信号值是9｡

### 7.4 进程优先级

1. 优先级参数:Linux 中用PRI 和NI 表示进程优先级,数值越小,进程越优先被CPU 处理｡
   - PRI:由内核动态调整,用户不能直接修改;
   - NI:用户可修改,通过调整NI 间接影响PRI;
   - 关系:PRI(最终值)=PRI(原始值)+NI｡
2. 修改NI 值的注意事项:
   - NI 范围:-20~19;
   - 普通用户:仅能调整自己的进程,且NI 值范围为0~19(只能调高,不能调低);
   - root 用户:可设定NI 为负值,并调整任何用户的进程;
   - 默认NI 值:0｡
3. 调整优先级的命令:
   - nice 命令:给待启动的进程赋予NI 值,不能修改已运行进程｡格式: nice [-n NI 值] 命令;
   - renice 命令:修改已运行进程的NI 值｡格式: renice [优先级] PID｡

## 第8章 存储管理

### 8.1 存储设备的查看

#### 8.1.1 硬盘分类与结构

1. 硬盘按存储介质分类:
   - 机械硬盘(HDD):采用磁性碟片存储数据;
   - 固态硬盘(SSD):通过闪存颗粒存储数据｡
2. 机械硬盘:
   - 逻辑结构:磁道､扇区和柱面;
   - 接口类型:IDE(电子集成驱动器)､SATA(串口)､SCSI(小型计算机系统接口);
   - 最小存储单位:扇区｡
3. 固态硬盘与机械硬盘的区别:
   - 优势:低能耗､无噪声､抗震动､低散热､体积小､速度快;
   - 劣势:价格更高,使用寿命有限｡

#### 8.1.3 存储设备的挂载

1. 挂载定义:将硬件设备的文件系统与Linux 系统的文件系统,通过指定目录(挂载点)关联,硬件设备需挂载后才能使用｡
2. 自动挂载与手动挂载:
   - 自动挂载:部分设备(如硬盘)系统启动时自动挂载;
   - 手动挂载:部分设备(如U盘､光盘)需手动操作｡

##### 8.1.3.1 mount 命令

1. 查看挂载信息:
   -  mount:显示已挂载设备信息;
   -  mount -l:额外显示卷标名称｡
2. 自动挂载遗漏设备: mount -a:检查/etc/fstab 文件,自动挂载未挂载设备(/etc/fstab 为系统开机自动挂载配置文件)｡
3. 手动挂载格式: mount [-t 系统类型] [-L 卷标名] [-o 特殊选项] [-n] 设备文件名 挂载点｡
   - 选项含义:
     - -t 系统类型:指定文件系统类型(如EXT2､EXT3､EXT4､iso9660､vfat);
     - -L 卷标名:通过卷标名挂载(替代设备文件名);
     - -n:不将挂载情况写入/etc/mtab 文件(如单人维护模式);
     - -o 特殊选项:指定额外选项(如读写权限､同步/异步)｡

##### 8.1.3.2 卸载命令

命令:umount 设备文件名或挂载点｡

##### 8.1.3.3 具体设备挂载示例

1. 挂载光盘:
   - 创建挂载点: mkdir /mnt/cdrom/;
   - 挂载命令: mount /dev/cdrom /mnt/cdrom/｡
2. 挂载U盘:
   - 查看设备文件名: fdisk -l(假设为sda1);
   - 创建挂载点: mkdir /mnt/usb;
   - 挂载命令: mount -t vfat /dev/sda1 /mnt/usb/｡
3. 自动挂载配置:root 身份在/etc/fstab 文件中添加设备信息,实现开机自动挂载｡

### 8.2 分区管理

分区命令:fdisk 和parted｡

- fdisk:常用,不支持大于2TB 的分区;
- parted:支持大于2TB 的分区,也可分配小分区｡

#### 8.2.1 fdisk 命令

1. 查询硬盘和分区: fdisk -l｡
2. 给硬盘分区: fdisk 设备文件名(注意:不要在当前系统硬盘上尝试,会删除系统)｡
3. 建立主分区过程:fdisk 硬盘名→n(新建)→p(建立主分区)→l(指定分区号)→按Enter(默认从柱面1 开始)→+5G(指定分区大小)｡
4. 分区规则:
   - 主分区+扩展分区最多4 个;
   - 扩展分区最多1 个｡
5. 分区生效:
   - 保存退出:w 命令;
   - 不保存退出:q 命令;
   - 不重启刷新分区表:partprobe 命令｡

#### 8.2.2 parted 命令

1. 交互模式进入: parted 硬盘设备文件名｡
2. 交互模式帮助:输入help 查看支持的命令｡
3. 格式化限制:parted 交互命令格式化仅支持ext2 文件系统,其他格式需用系统mkfs 命令｡
4. 注意事项:parted 所有操作立即生效,无需保存｡

### 8.3 磁盘管理工具

#### 8.3.1 df 命令

1. 功能:显示Linux 系统中各文件系统的硬盘使用情况(总容量､已用容量､剩余容量等),数据来源于超级块(Super Block)｡
2. 命令格式: df [选项] [目录或文件名]｡
3. 常用选项:
   - -a:显示所有文件系统信息(包括/proc､/sysfs 等);
   - -h:用MB/GB 等习惯单位显示;
   - -i:显示inode 数量(不显示硬盘容量);
   - 无选项:默认以KB 为单位显示｡
4. 目录关联:df 后加目录名,自动分析目录所在分区并显示该分区信息｡

#### 8.3.2 du 命令

1. 功能:统计目录或文件所占磁盘空间容量｡
2. 命令格式: du [选项] [目录或文件名]｡
3. 常用选项:
   - -a:显示所有子目录和子文件的磁盘占用量;
   - -h:用习惯单位显示;
   - -s:仅统计总磁盘占用量(不列出子目录/子文件);
   - 无选项:统计当前目录总占用量及所有子目录占用量(默认KB,不统计子文件)｡
4. 文件删除特点:删除文件后,需所有程序不再使用该文件,系统才释放空间;df 命令会统计已删除但未释放的空间,更精确｡

#### 8.3.3 fsck 命令

1. 功能:检查文件系统并尝试修复错误｡
2. 命令格式: fsck [选项] 分区设备文件名｡
3. 常用选项:
   - -a:自动修复,无提示;
   - -r:交互式修复,修改前询问用户｡
4. 丢失文件恢复:修复后若有文件丢失,可到"lost+found"目录查找,用file 命令查看文件类型判断用途｡

## 第9章 设备管理

### 9.1 设备文件

1. Linux 设备管理方式:通过设备文件统一管理硬件设备,隐藏硬件特性和管理细节,实现用户程序与设备无关性(用户使用设备与使用普通文件一致)｡
2. 设备文件位置:/dev 目录,每个设备对应一个设备文件｡

#### 9.1.1 设备命名规则
1. 设备文件名组成:主设备号+次设备号｡
   - 主设备号:代表设备类型(如hd=IDE 硬盘､sd=SCSI 硬盘､tty=终端);
   - 次设备号:代表同类设备中的序号｡
2. 常见设备文件名:
   - IDE 硬盘:/dev/hda､/dev/hdb､/dev/hdc､/dev/hdd(最多4 个),hda1 表示hda 的第一个主分区;
   - SCSI 硬盘:/dev/sda､/dev/sdb 等;
   - 软盘:/dev/fd0;
   - 磁带机:/dev/st*(自动回卷)､/dev/nst*(不自动回卷,常用),序号越小越靠前(如nst0 为第一个);
   - 硬盘分区编号:主分区/扩展分区1-4,逻辑分区5+;
   - 硬盘数量标识:系统用a~p 代表16 块不同硬盘｡

#### 9.1.2 硬盘第一个扇区
1. 组成:主引导记录(446 字节)+分区表(64 字节)+结束符(2 字节)｡
2. 分区表限制:每个分区信息占16 字节,最多记录4 个分区(即4 个主分区)｡

#### 9.1.3 特殊设备文件
1. /dev/null:空设备,只写文件,写入内容永久丢失,读取返回空｡
2. /dev/zero:伪输入设备,用于创建指定长度的初始化空文件｡
3. /dev/full:特殊设备文件,写入时返回"设备无剩余空间"(错误码ENPOSPC),读取返回无限二进制流,用于测试程序磁盘满时的行为｡
4. /dev/random/urandom:随机数发生器/伪随机数发生器｡

#### 9.1.4 设备分类
按是否对应物理实体:物理设备､虚拟设备｡

### 9.2 常用的设备命令

系统硬件检测:启动时检测硬件并加载驱动程序(模块),检测结果记录在/proc 目录｡

#### 9.2.1 查看CPU 信息的命令

lscpu 命令:查看CPU 和处理单元的信息｡

#### 9.2.2 查看内存信息的命令

##### 9.2.2.1 free 命令

1. 功能:显示系统内存状态(空闲/已用物理内存､swap 内存､内核使用的缓冲区)｡
2. 命令格式: free [选项]｡
3. 常用选项:
   - -k:以KB 为单位(默认);
   - -b:以字节为单位;
   - -m:以MB 为单位;
   - -g:以GB 为单位;
   - -t:输出内存和swap 分区总量;
   - -o:不显示系统缓冲区列;
   - -s 间隔秒数:按指定间隔持续显示｡
4. swap:交换分区,即虚拟内存｡

##### 9.2.2.2 vmstat 命令

1. 功能:Virtual Memory Statistics,统计虚拟内存,Linux 内存管理通过"调页(Paging)"和"交换(Swapping)"实现｡
2. 相关概念:
   - Page-Out:页面写入磁盘;
   - Page-In:页面从磁盘回到内存;
   - 页面错误(Page Fault):内核需要的页面不在物理内存中(因Page-Out);
   - 颠簸(Thrashing):pageout 频繁发生,内核管理分页时间超过运行程序时间,系统性能急剧下降或暂停｡

#### 9.2.3 查看块设备的命令

##### 9.2.3.1 dmesg 命令

1. 功能:查看Linux 系统启动信息,常用于查看硬件信息｡
2. 启动信息文件:/var/log/dmesg(也可通过该文件查看)｡

##### 9.2.3.2 lsblk 命令

1. 功能:列出系统中所有可用块设备信息及依赖关系(不列出RAM 盘)｡
2. 块设备定义:按可寻址块为单位I/O,一次操作固定大小数据块,通过缓冲区读写,允许随机访问,适用于大量信息传输(如硬盘､闪存盘､CD-ROM)｡

#### 9.2.4 磁盘配额的命令

##### 9.2.4.1 quota 命令

1. 功能:查询磁盘空间限制及已使用空间｡
2. 命令格式:
   - quota [选项] 用户名;
   - quota [选项] 群组名｡

##### 9.2.4.2 quotacheck 命令

1. 功能:扫描含挂载参数usrquota 和grpquota 的文件系统,建立磁盘配额记录文件｡
2. 命令格式:quotacheck [选项] 文件系统｡

##### 9.2.4.3 quotaon 命令

功能:启动磁盘配额服务｡

##### 9.2.4.4 quotaoff 命令

功能:关闭磁盘配额服务｡

## 第10章 网络管理

### 10.1 管理网络接口

#### 10.1.1 计算机基本网络参数

1. IP 地址:标识一块网卡接口,由网络号和主机号组成｡
2. 子网掩码:与IP 地址成对出现,确定网络部分位数(对应子网掩码为1 的位为网络部分)｡
3. 网关:实现跨区域通信｡
4. DNS:实现域名与IP 地址的映射｡

#### 10.1.2 Linux 联网配置步骤
1. 为每个网络接口分配IP 地址和子网掩码(Netmask);
2. 配置默认网关(Gateway);
3. 配置一个或多个DNS 服务器｡

#### 10.1.3 网络接口卡(NIC)
1. 功能:实现联网操作的PCI 设备｡
2. 内核检测:Linux 内核可检测所有连接的PCI 设备,用lspci 命令验证｡

#### 10.1.4 网络接口
1. 访问方式:Linux 内核不允许将NIC 作为文件访问,/dev 目录无NIC 设备节点,通过网络接口访问NIC｡
2. 常用网络接口名称及类型:
   | 名称  | 类型                 |
   |-------|----------------------|
   | eth0  | 以太网               |
   | lo    | (虚拟)回环设备       |
   | ppp0  | 使用PPP 协议的串口设备(调制解调器) |
   | tr0   | 令牌环(token ring)   |
   | fddi0 | 光纤                 |

#### 10.1.5 网络接口检测与配置
1. 检测所有接口:ifconfig -a(显示已识别的所有网络接口信息);
2. 检测活跃接口:ifconfig(不加选项,仅显示活跃接口)｡
3. 接口配置文件:
   - 激活脚本:/etc/init.d/network;
   - 配置文件目录:/etc/sysconfig/network-scripts;
   - 配置文件命名:以ifcfg-<interface> 命名(如ifcfg-eth0)｡
4. 回环接口默认配置:IP 地址127.0.0.1,子网掩码255.0.0.0｡

### 10.2 基本IP 路由和网关
1. IP 地址结构:每个IP 地址包括网络部分和主机部分｡
2. 子网掩码对应网络类型:
   - A 类网络:子网掩码255.0.0.0(网络地址含第1 个IP 字段);
   - B 类网络:子网掩码255.255.0.0(网络地址含前2 个IP 字段);
   - C 类网络:子网掩码255.255.255.0(网络地址含前3 个IP 字段)｡
3. 以太网地址:
   - 每个以太网接口有两个地址:IP 地址(用于跨网络主机通信)､MAC 地址(用于同一IP 网络内主机通信)｡
4. 本地网络通信过程:
   - 确认目标主机与本机在同一网络;
   - 通过ARP 协议(地址解析协议)获取目标主机的MAC 地址;
   - 保存IP 地址/MAC 地址对到ARP 缓存(用arp -a 检测缓存,arp -n 查看IP 与MAC 映射表)｡
5. ARP 协议作用:将以太网MAC 地址与IP 地址关联｡

### 10.3 配置DNS 客户机
#### 10.3.1 域名系统(DNS)
1. 功能:分布式数据库,将复杂的IP 地址转换为简明的域名,实现主机名与IP 地址的转换,在TCP/IP 网络中至关重要｡
2. /etc/hosts 文件:早期实现IP 与主机名对应的静态表｡

#### 10.3.2 DNS 查询方式
1. 静态查询:通过/etc/hosts 文件查询;
2. 动态查询:通过/etc/resolv.conf 文件中列出的域名服务器查询｡
3. resolve 库解析流程:先执行静态查询,再通过/etc/resolv.conf 中的域名服务器进行动态查询｡

### 10.4 DHCP 配置详解
1. DHCP 定义:Dynamic Host Configuration Protocol(动态主机配置协议),局域网网络管理协议｡
2. DHCP 工作方式:
   - 客户端无固定IP 地址,接口启用(ifup)时动态获取IP,接口停用(ifdown)时释放IP;
   - 客户端配置:接口配置文件中BOOTPROTO 变量设为dhcp;
   - dhclient 守护进程:管理DHCP 通信,自动应用接收的信息(添加默认网关到路由表､写入DNS 服务器到/etc/resolv.conf､设定NIS 域)｡

### 10.5 配置Web 服务器
1. HTTP 协议:Hyper Text Transfer Protocol(超文本传输协议),用于客户端和服务器之间的通信｡
2. Apache 应用程序:实现WWW 服务器功能,为用户提供Web 浏览服务｡

### 10.6 配置Telnet
(文档中未提及详细内容,暂略,仅提及为远程控制Web 服务器的常用方法之一)

### 10.7 其他网络设置
#### 10.7.1 分配主机名
1. hostname 命令:检验机器主机名,或动态分配主机名｡

#### 10.7.2 /etc/sysconfig/network 文件
1. 功能:记录通用联网配置信息,定义整合到启动过程中的shell 变量｡

#### 10.7.3 网络配置作为service 管理
1. 命令格式:service network stop/start/restart(管理网络服务的启动/停止/重启)｡

### 10.8 网络诊断工具
#### 10.8.1 常用诊断命令
##### 10.8.1.1 ping 命令
1. 功能:测试本机与远程主机的底层IP 连通性｡
2. 用法:接受主机名或IP 地址作为参数,如 ping www.baidu.com｡

##### 10.8.1.2 host 命令
1. 功能:直接执行DNS 查询｡
2. 用法:默认使用/etc/resolv.conf 中的域名服务器,如 host www.baidu.com｡

##### 10.8.1.3 traceroute 命令
1. 功能:显示数据包从本机到目标主机的路由器路径｡

#### 10.8.2 tcpdump 命令
1. 功能:监视网络,显示独立数据包信息概要,持续执行直到Ctrl+C 取消｡
2. 示例:截取HTTP 协议(端口80)数据并以二进制格式保存到http.capture: tcpdump -p 80 > http.capture｡

#### 10.8.3 常见网络配置问题与答案
1. 列出所有当前活跃网络接口的命令:ifconfig｡
2. 回环接口默认IP 和子网掩码:127.0.0.1/255.0.0.0｡
3. 定义本地主机名和IP 地址转换的文件:/etc/hosts｡
4. 动态设置主机名为station.example.com 的命令:hostname station.example.com｡
5. 定义主机名并在启动时自动设定的文件:/etc/hosts｡
6. 启用Linux 机器路由功能的配置文件:/etc/sysctl.conf(内核配置文件)｡
7. 启用路由功能的参数:net.ipv4.ip_forward(设为1 启用,0 禁用)｡
8. 直接执行DNS 主机名解析的程序:system-config-network-tui｡
9. ifconfig 与修改配置文件的区别:ifconfig 暂时修改网络参数,不写入配置文件,重启后恢复配置文件设置｡

## 第11章 系统服务与日志
### 11.1 Linux 系统服务
1. 服务定义:又称守护程序,系统启动时自动加载,系统退出时自动停止的系统服务｡

### 11.2 启动和关闭服务
1. 守护程序分类:
   - 独立启动服务(stand alone):可独立启动;
   - 总管程序管理服务(super daemon):通过总管程序统一管理｡
2. 独立服务启动方式:
   - 使用/etc/init.d/目录中的启动脚本;
   - 使用service 服务命令｡

### 11.3 查看日志
1. 日志管理服务:绝大多数系统日志由rsyslogd 服务统一管理｡
2. Apache 服务日志:由Apache 软件自行产生,日志格式与系统默认日志一致｡
3. 日志文件位置:/var/log/目录( /var/ 目录用于保存系统动态数据)｡

### 11.4 管理日志
1. rsyslogd 服务配置文件:/etc/rsyslogd.conf,定义各服务不同等级日志的记录位置｡

## 第12章 VI 编辑器
### 12.2 工作模式
VI 编辑器有3 种工作模式:命令模式､文本编辑模式和末行模式｡

### 12.3 进入和退出VI
#### 12.3.1 进入VI
1. 常用进入方式:
   - vi:直接进入VI;
   - vi 文件名:文件不存在则创建,存在则打开;
   - vi+ 文件名:进入后光标停在文件最后一行开始处;
   - vi+n 文件名:进入后光标停在文件第n 行开始处;
   - vi+/字符串 文件名:进入后光标停在文件中指定字符串第一次出现的行首｡

#### 12.3.2 保存文件或退出VI
1. 命令模式:按两次Z 键,保存文件并退出VI｡
2. 末行模式(常用命令):
   - w:保存文件,不退出VI(write);
   - q:不保存,直接退出VI(quit),文件有未保存改动时出错;
   - q!:强行退出VI,丢弃未保存改动(恢复文件原始内容);
   - wq:保存并退出VI(同ZZ)