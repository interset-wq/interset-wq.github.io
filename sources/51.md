# shell 脚本编程基础

## shell 编程概述

shell 本身是一个用 C 语言编写的程序，是连接 用户 和 UNIX/Linux 内核 的桥梁。

一个简单的shell脚本 `ShowHello.sh` （Linux脚本一般使用 `.sh` 作为文件后缀名）：

``` shell
#! /bin/bash
#ShowHello
#To show hello to somebody
echo -n "Enter your name:"
read name
echo "Hello, $name"
```

- 第一行 `#! /bin/bash` 这是一个特殊的标记（称为 shebang），告诉系统这个脚本需要用 `/bin/bash` 这个程序来执行，是 shell 脚本的标准开头。通常放在脚本第一行，从而调用相应的解释程序予以执行
- 第二行 `#ShowHello` 和第三行 `#To show hello to somebody` 以 `#` 开头的行是注释，不会被执行，用来解释脚本的功能
- 第四行 `echo -n "Enter your name:"` echo 是输出文字的命令，-n 选项表示输出后不自动换行。这行的效果是在屏幕上显示 "Enter your name:"，光标会停在冒号后面等待输入
- 第五行 `read name` read 命令用来接收用户从键盘输入的内容，这里把输入的内容保存到变量 name 中。比如你输入 "Tom"，那么 name 这个变量就代表 "Tom"
- 第六行 `echo "Hello, $name"` 再次使用 echo 输出内容，$name 表示取出变量 name 中保存的值。如果之前输入了 "Tom"，这行就会输出 "Hello, Tom"

这个shell脚本还不能运行，因为它没有 `x` 权限，无法作为应用程序执行。为这个脚本的所有者 `u` 添加 `x` 权限 `$ chomd u+x ShowHello.sh`

Linux 中，创建文件默认是不可执行的文件，需要修改文件的权限，为文件增加可执行权限，后在命令行模式下直接输入该文件的相对路径 ./文件名，即可运行

``` bash
$ vim ShowHello.sh
$ ./ShowHello.sh
-bash: ./ShowHello.sh: Permission denied
$ ls -l
total 8
-rw-r--r-- 1 d111kc d111kc  108 Jul 31 20:23 ShowHello.sh
-rw-r--r-- 1 d111kc d111kc    0 Jul 30 21:05 note1.txt
drwxr-xr-x 2 d111kc d111kc 4096 Jul 30 21:04 test1
$ chmod u+x ShowHello.sh
$ ./ShowHello.sh
Enter your name:Mike
Hello, Mike
```

## shell 的种类

shell脚本的第一行需要指出该脚本的解释程序，即shell的种类。Linux系统提供了多种不同的shell。

查看Linux系统提供的shell种类：

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

最常见的shell有Bourne shell（简称sh）、C shell（简称csh）、Korn shell（简称ksh）和Bourne-again shell（简称bash）。默认的shell是bash，它具有以下优点：

- 命令记忆功能 通过键盘上的上下箭头可以快速输入之前输入过的命令
- Tab自动补全
- 设置别名功能 例如 `$ alias ll='ls -l'` 可以将 `ls -l`的别名设置为 `ll`

## shell 脚本的运行

有3中方式执行shell脚本：

### 方式一

将shell脚本的权限设置为可执行，然后在提示符下直接运行。脚本文件的编辑完成后，利用chmod命令修改脚本文件的权限为可执行，如前面的示例：

``` bash
$ chmod u+x ShowHello.sh
$ ./ShowHello.sh
```

在运行该脚本时，必须给出该脚本的相对路径（如 `./ShowHello.sh`，这个相对路径不能省略 `./`）或绝对路径。在执行系统命令时，只需要给出命令文件名。因为命令和用户的可执行脚本文件是否能够执行，与环境变量PATH有关。

查看环境变量PATH `$ echo $PATH`

环境变量PATH的值决定了shell将到哪些目录中寻找命令或可执行程序，当用户运行一个命令或可执行程序时，Linux在这些目录下按顺序依次搜寻。由于用户的可执行脚本是放在用户家目录下的，所以直接输入 `ShowHello.sh`，系统无法找到该文件。

通过这种方式运行脚本，脚本文件第一行的`#！/bin/bash`一定要写对，好让系统查找到正确的解释器。

### 方式二

以脚本名作为参数传递给shell程序。

``` bash
$ bash ShowHello.sh
Enter your name:Mike
Hello, Mike
```

这种执行方式就是运行bash，将脚本 `ShowHello.sh` 作为参数传递给bash。通过这种方式运行脚本，不需要在脚本文件的第一行指定解释器信息，并且脚本名后面还可以带参数。

### 方式三（不推荐使用）

将脚本以输入重定向的方式传递给bash。

运行bash程序，以输入重定向的方式让bash从给定文件中读入命令行，并进行相应处理。

``` bash
d111kc@D111KC:~$ bash < ShowHello.sh
Enter your name:d111kc@D111KC:~$
```

这种方式的脚本后面是不能带参数的

## shell 基础

shell脚本是文本文件

### 通配符

文件名的扩展称为通配（Globbing）

- `*` 匹配任意字符（不包括路径分隔符`/`）的 0 次或多次出现
- `?` 匹配任意单个字符（不包括 `/`）
- `[]` 将一组字符列表括起来，其作用是匹配该列表中的任意一个字符。例如，`space.[co]`匹配`space.c`或者`space.o`，`[Hh]*`匹配以“H"或“h”开头的文件名。`[]`中无论有几个字符，都只代表某一个字符。在`[]`中，可以使用 `-` 指定字符的范围，例如`[0-9]`匹配任何0至9的数字。
- `[^]` 或 `[!]` 为了匹配不在列表中的字符，需要在列表的开头加一个`^`或者`!`，代表反向选择。例如，`[^Hh]*`和`[!Hh]*`匹配以非“H"或“h”开头的文件名。
- `{stringl,string2,...}` 匹配 sringl或 string2（或更多）中的一个字符串。`{}`告诉shell依次使用每种string形成一个单独的文件名进行匹配，大括号扩展只适用于bash、tcsh和Cshell，不适用于Kornshell和FreeBSDshell。例如，用户希望查看目录/home/student，/home/cs1，/home/re中所有文件的名称，`$ ls /home/student /home/cs1 /home/re`
使用通配符命令就比较简单：`$ ls /home/{student,cs1,re}` 大括号中的逗号前面和后面都不能有空格

### 转义字符

shell默认支持转义字符，如果是特殊字符想要表示字面意义需要在前面添加 `\` 转义

### 引号

shell 中引用字符有 3 种：单引号`''`，双引号`""`和反引号`

1. 单引号引用一串字符，所有字符都是普通字符

#### 单引号

被单引号括起来的所有字符都是普通字符，就算特殊字符也不再有特殊含义。在某些时候，会希望使用个别特殊字符，如`$`来引用变量的值，例如：

``` bash
$ echo 'the directory is $HOME; the userid is $USER'
the directory is $HOME; the userid is $USER
```

很显然这样的输出并不是我们所需要的。这时命令就不能正常工作，在不使用转义字符 `\`（若命令中存在多个特殊字符，使用转义字符“\”会让命令可读性变差）时，双引号可以很好地解决这个问题。

#### 双引号

由双引号括起来的字符（除`$`、反引号和转义字符 `\` 外）均作为普通字符。“$”“\”和倒引号是拥有特殊含义的，“$”代表引用变量的值，而反引号代表引用命令。在上述例题中，采用双引号可以使 `$` 保留特殊含义

``` bash
d111kc@D111KC:~$ echo 'the directory is $HOME; the userid is $USER'
the directory is $HOME; the userid is $USER
d111kc@D111KC:~$ echo "the directory is $HOME; the userid is $USER"
the directory is /home/d111kc; the userid is d111kc
```

``` bash
$ name=d111kc
$ echo '$name'
$name
$ echo "$name"
d111kc
```

如果需要在双引号中间输出“$”和倒引号，则要在符号前加转义符“\”

#### 反引号

由反引号括起来的字符串被shell解释为命令行，shell会先执行该命令，并以它的标准输出结果取代整个倒引号部分。

``` bash
$ today=`date`
$ echo "Today is $today"
Today is Thu Jul 31 21:45:01 CST 2025
```

### 重定向符

shell重定向分为两种，一种是输入重定向，另一种是输出重定向。从字面上理解，输入/输出重定向就是改变输入与输出方向。

每个程序都有输入和输出，那么程序应该能够从任何源接受输入，并可以向任何目标输出。例如，一个排序程序可以选择从键盘输入文本，从已有文件中读取文本，或者读入另一个程序的输出结果。同样，排序程序应该能够在显示器上显示输出，将输出写入文件或者将输出发送给另一个程序做进一步处理。

这样的设计思想有一个突出的优点就是，当编写程序时，可以依靠Linux处理输入/输出，程序员不必考虑输入/输出的各种情况，只需处理输入/输出的内容，当程序真正开始运行时，shell会将程序连接到用户希望使用的输入和输出设备上。在程序员眼里，一切设备皆文件，他以一种通用的方式编写程序的读取和写入。为了实现这一思想，UNIX（Linux）的开发入员设计了一种读/写数据的通用方法，这些功能被称为标准I/O

在默认情况下，大多数程序都会从键盘读取输入，并将输出到显示器。因此在登录时，shell会自动地将程序的输入源设置为键盘，称为标准输入；设置程序运行的正确结果输出到显示器，称为标准输出；将程序运行中的出错信息输出位置也设置为显示器，称为标准错误。标准输入、标准输出和标准错误都以文件的方式存在，通常缩写为`stdin`、`stdout`和`stderr`。

每次输入命令，都可以告诉shell在此命令执行期间重新设置输入和输出的方向，这正是UNIX（Linux）功能强大的地方。

使用输出重定向符 `>` ，改变内容输出的位置：

``` bash
$ ls
ShowHello.sh  bash  name  note1.txt  test1
$ ls > filelist.txt
$ cat filelist.txt
ShowHello.sh
bash
filelist.txt
name
note1.txt
test1
```

上面的代码 `ls > filelist.txt` 将 `ls` 命令输出的内容到文件 `filelist.txt` 中

输入/输出方向就是数据的流动方向。输入方向就是数据从哪里流向程序。数据默认从键盘流向程序，如果改变了它的方向，数据就从其他地方流入，这就是输入重定向。输出方向就是数据从程序流向哪里。数据默认从程序流向显示器，如果改变了它的方向，数据就流向其他地方，这就是输出重定向。

常用的输入/输出重定向符：

- 标准输入重定向
    - `command < file` 将文件作为命令的输入
    - `command < 分界符`从标准输入中读入，直到遇见分界符才停止
- 标准错误输入重定向
    - `command 2 > file` 以覆盖的方式，把command的错误信息输出到file文件中
    - `command2 >> file`以追加的方式，把command的错误信息输出到file文件中
- 标准输出重定向
    - `command > file`以覆盖的方式，把command的正确输出结果输出到file文件中
    - `command >> file`以追加的方式，把command的正确输出结果输出到file文件中

#### 输入重定向符号 `<`

输入重定向符 `<` 的作用是把命令（或可执行文件）的标准输入重新定向到指定文件，如：

``` bash
$ wc -l < ShowHello.sh
6
$ wc -l ShowHello.sh
6 ShowHello.sh
```

使用 `wc -l` 统计 `ShowHello.sh`这个文件有几行，是否使用输入重定向符并没有太大的差异。

#### 输入重定向符号 `<<`

与输出重定向 `>>` 不同，输入重定向符 `<<` 不代表追加的意思。它的作用是使用特定的分界符作为命令输入的结束标志，而不使用默认的Ctrl+D组合键。

``` bash
$ wc -l << a
> 123
> 456
> abc
> a
3
```

不停的输入，直到输入字符 `a` 之后按回车，才结束输入。上面的 `>` 表示命令没有结束时的换行

#### 输出重定向符 `>`

输出重定向符 `>` 的作用是把命令（或可执行文件）的标准输出重新定向到指定文件（或其他输出目标）。这样，该命令的结果就不在屏幕上显示，而是写入指定文件中（或其他输出目标）。例如：

``` bash
$ ls
ShowHello.sh  bash  filelist.txt  hello.txt  name  note1.txt  test1
d111kc@D111KC:~$ ls > list.txt
d111kc@D111KC:~$ cat list.txt
ShowHello.sh
bash
filelist.txt
hello.txt
list.txt
name
note1.txt
test1
```

将 `ls` 的输出结果写入 `list.txt` 中（这个文件不存在时，会自动创建。文件存在时，会覆盖原文件）。

为了避免原文件内容被覆盖，可以使用输出追加重定向符 `>>`

#### 输出追加重定向符 `>>`

和 `>` 类似，不覆写原文件，而是在原文件的末尾追加新内容。

#### 文件描述符

Linux中一切皆文件，包括标准输入设备（键盘）和标准输出设备（显示器）在内的所有计算机硬件都是文件。在每个进程中，为了表示和区分已经打开的文件，Linux会给每个文件分配一个ID，这个ID就是一个整数，被称为文件描述符（FileDescriptor）。Linux程序在执行任何形式的I/O操作时，都是在读或者写一个文件描述符。在编写程序时，程序员只关注文件的内容。一个文件描述符只是一个和打开的文件相关联的整数，它的背后可能是一个硬盘上的普通文件、FIFO、管道、终端、键盘、显示器，甚至是一个网络连接。在进程创建的时候，系统为每个进程自动打开3个标准文件（即标准输入stdin、标准输出stdout和错误输出stderr），它们默认都是打开
的，其文件描述符分别为0、1、2。在重定向的过程中，0、1、2这3个文件描述符可以直接使用。

标准输出和标准错误输出虽然对应的设备都是显示器，但是它们是两个文件

#### 命令执行操作符

多条命令可以在一行中出现，用命令执行操作符连接，则将按如下规则执行命令：

##### 顺序执行 `;`

如果使用 `;` 连接多条命令，那么这些命令会依次执行，各命令之间没有任何逻辑关系，也就是说，不论哪条命令报错了，后面的命令仍会依次执行。

``` bash
$ ls; date; pwd
ShowHello.sh  bash  filelist.txt  hello.txt  list.txt  name  note1.txt  test1
Fri Aug  1 21:31:32 CST 2025
/home/d111kc
```

它与写成多行的形式是等价的。

##### 逻辑与 `&&`

如果使用 `&&` 连接多条命令，那么这些命令之间就有逻辑关系了。只有第一条命令正确执行了，`&&` 连接的第二条命令才会执行。

##### 逻辑或 `||`

使用 `||` 连接多条命令，则只有前一条命令执行错误，后一条命令才能执行。

##### 小括号`()`和大括号`{}`

当用户登录后启动shell时，这个shell是交互式的。当以这种方式工作时，shell是用户界面，当它执行完一条命令后，接着显示另一个提示符，始终在前台等待用户交互。还有一种shell是非交互的，当在交互shell中运行一个外部命令或者执行一个脚本时，交互shell会创建一个子shell，这个shell在不需要输入的情况下一次性处理所有的命令，运行结束后子shell进程结束。

小括号`()` 和大括号 `{}` 都可以将若干命令括起来，组合在一起，在逻辑上被视为一条命令。使用时在格式上应注意，左括号后面应有一个空格，右括号之前应有一个分号 `;`。大括号也可以包括若干单独占一行的命令，大括号中的命令表必须用分号或者换行符终止。

成组命令也可以用小括号括起来，在成组命令用小括号括起来时，左括号后不必有空格，右括号之前也不需要加上分号。在用于成组命令的执行时，小括号和大括号的主要区别在于：小括号执行成组命令时，重新开启一个子shell来执行；而大括号在执行成组命令时，是在当前shell中执行

##### 管道符、后台命令符和注释符

在shell中，管道符`|`用来连接多条命令，如“命令1丨命令2”。每个命令执行时都有一个独立的进程，前一个命令的输出是下一个命令的输入。这里需要注意，命令1必须有正确输出，而命令2必须可以处理命令1的输出结果；而且命令2只能处理命令1的正确输出，而不能处理错误输出。

为了使这些进程能够在后台运行，可以在命令后面加上`&`，实现后台运行。后台命令符`&`使得在shell中实现多道进程运行成为可能：一个进程在前台运行，其他进程在后台运行。前台进程在执行过程中，用户和进程可以发生交互一一响应用户输入数据，进程处理数据并输出结果，这种方式就是前台方式。后台进程在运行过程中，与用户无交互，即不响应用户的输入和中断控制信号。

适合在后台运行的命令是一些执行时间较长且无交互的命令，如编译程序、费时的排序程序及一些shell脚本。在后台运行作业时要注意，在后台运行的命令一样会将结果输出到屏幕上，干扰用户的工作。如果放在后台运行的作业会产生大量的输出，最好把它的输出重定向到某个文件中。

## shell 编程

shell语法和C语言类似。

### 变量

shell变量分为两类：用户自定义变量和系统预定义的特殊变量。

#### 用户自定义变量

变量名：用户自定义的变量是最普通的shell变量。变量名以字母或下画线开头，由字母、数字和下划线`_`组成。注意，数字不能做变量的开头符，大写字母通常是系统默认的变量，用户自定义变量通常用小写字母。

变量赋值：变量命名后，需要赋值，未赋值的变量其值为空。变量赋值的一般形式为：`变量名=值`。注意，变量与变量内容以等号`=`来连接。赋值时等号两边不能有空格。如果出现空格，赋值语句执行失败，变量未被赋值，依然为空。如果字符串中一定包括空格，字符串要加上引号。

变量引用：在程序中使用变量的值时，要在变量名前面加上`$`符，表示使用变量的值。例如：

``` bash
$ name=d111kc
$ echo $name
d111kc
$ echo name
name
```

在下述情况下，变量的引用会出现歧义：

``` bash
$ dir=/home/student
$ cat $dir01/file1.txt
```

在/home目录下，是以student开头，加学号的学生账户，所以上述命令的本意是要显示`/home/student01/file1.txt`文件，但是shell无法区别变量名是dir还是dir01，在这种情况下，shell默认到第一个非法变量名字符为止，第一个非法变量名字符是/，所以shell认为变量名为dir01，而dir01
未赋值，所以为空，命令执行失败。在这种情况下，要正确引用变量，需要用大括号将该变量名括起来，如下所示：

```
$ cat ${dir}01/filel.txt
```

除了用大括号外，还可以用引号引用变量，上述命令还可以表达成：

``` bash
$ cat "$dir"01/filel.txt
```

需要注意的是，大括号一定不要错写成小括号，`$()`等价于倒引号，其作用是把括号内命令的执行结果赋值给变量，如

```
$ working_dir=$(pwd)
$ echo $working_dir
/home/d111kc
$ echo `pwd`
/home/d111kc
```

数组的定义和使用与变量类似。所谓数组，就是相同数据类型的元素按一定顺序排列的集合，也就是把有限个类型相同的变量用一个名字命名，然后用编号区分它们的变量集合，把这个名字称为数组名，把编号称为下标。组成数组的各个变量被称为数组的元素。但是bash仅支持一维数组（不支持多维数组），并且没有限定数组的大小。数组下标从0开始，不能使用负数下标。

在bash中，用小括号 `()` 来表示包裹数组，数组元素用“空格”分隔。

``` bash
$ langs=(html css javascript)
$ echo ${langs[*]}
html css javascript
$ langs[0]=python
$ langs[1]=c
$ echo ${langs[*]}
python c javascript
```

还可以用declare命令显式声明一个数组，而不赋值，其形式是 `declare -a langs` 这时langs就是一个数组名，而不会被解释成变量了。

通过下标获取数组元素的值 `${数组名[下标]}`，如果没有给出数组元素的下标，则数组名表示下标为0的数组元素。

获取整个数组的值 `${数组名[*]}` 或 `${数组名[@]}`

``` bash
$ langs=(html css javascript)
$ echo ${langs[0]}
html
$ echo $langs
html
$ echo ${langs[*]}
html css javascript
$ echo ${langs[@]}
html css javascript
```

`${langs[*]}` 和 `${langs[@]}` 的区别就是，`${langs[*]}` 将整个数组扩展为一
个词（即字符串），这个词由以空格分开的各个数组元素组成；`${langs[@]}` 将整个数组扩展为多个词，每个数组元素是一个词。例如：

``` bash
$ langs=(html css javascript)
$ for i in "${langs[*]}"; do echo $i; done
html css javascript
$ for i in "${langs[@]}"; do echo $i; done
html
css
javascript
```

代码对数组进行了遍历，`do` 表示循环体的开始，`done` 表示循环体的结束。

#### 系统预定义变量

系统预定义变量是在shell中已定义好的变量，系统预定义变量不能被用户重新定义。

常用的预定义变量：

- `$?` 上一条命令执行后的返回值（也称返回码，退出状态等）
- `$$` 当前进程的进程号（PID）
- `$!` 上一个后台命令对应的进程号（PID）
- `$-` 当前在运行shell程序的选项
- `$#` 命令行上参数的个数
- `$*`，`$@` 命令行上实际给出的所有实参

`$?` 是上一条命令执行后的返回值，它是一个十进制数。大多数的shell命令（除了let命令计算表达式的值等）执行成功后，返回值为0；执行失败，则返回非0值（不同的值代表不同的错误）

``` bash
$ pwd
/home/d111kc
$ echo $?
0
```

`$$` 表示当前进程的进程号。每个进程都有唯一的进程号（PID）

``` bash
$ echo $$
300
```

新开一个终端再次运行上面的命令时，输出的值会发生改变。

`$!` 是上一个后台命令对应的进程号

`$-` 是当前在运行shell程序的选项。shell命令的一般格式是：`命令名 [选项] [参数]` 登录后启动的交互式shell也是一个程序，它和上述命令一样有选项（默认不带参数），它的选项可以通过执行 `echo $-`显示出来：

``` bash
$ echo $-
himBHs
```

#### 位置参数变量

位置参数变量也属于预定义变量。

在Linux的命令行中，当一条命令或脚本执行时，后面可以跟多个参数，使用位置参数变量来表示这些参数。其中，`$0` 代表命令行本身，`$1` 代表第1个参数，依次类推。当参数个数超过10个时，就要用大括号把这个数字括起来，例如，`${10}`；代表第10个参数，`${14}`则代表第14个参数。举个例子：

``` bash
$ cat filel file2
```

在这里，cat对应于`$0`，file1对应于`$1`，file2对应于`$2`

常用的位置参数变量：

- `$n` n为数字，`$0`代表命令本身，`$1` 到 `$9`代表第1—9个参数，10以上的参数需要用大括号包含，如`${10}`
- `$*` 代表命令行中所有的参数，把所有的参数看成一个整体
- `$@` 代表命令行中所有的参数，把每个参数区别对待
- `$#` 命令行上参数的个数

位置参数变量用于向命令或程序脚本传递信息，比如要写一个做加法计算的脚本 `add.sh`，在编写脚本的时候，并不知道add脚本将要处理的数据对象，所以编写代码的时候，以位置参数变量来代替将要处理的数据对象：

``` bash
$ vim add.sh
$ cat add.sh
#! /bin/bash
let num1=$1
let num2=$2
let sum=num1+num2
echo $sum
$ chmod u+x add.sh
$ ./add.sh 1 2
3
```

上面的 `add.sh` 脚本可以带两个参数，脚本根据它们在命令上的位置来识别并予以处理，所以称之为位置参数。

上面的脚本必须传入两个参数，如果想要使用不定长参数，脚本就需要用到循环语句，循环语句需要确定循环的次数，这时候就需要应用`$#`来解决这个问题，`$#`代表命令行上参数的个数，但不包含shell脚本名本身，即不包括`$0`的参数的个数。

除了使用$#来控制循环次数，还可以使用shift来解决这个问题。shift命令移动位置参数，每执行一次shift命令，就把命令行上的实参向左移动一位。注意shift命令不能将$O移走，shift命令执行后，新$1的值是原$2的值，新$2的值是原$3的值，以此类推。例如可以传入不定长参数的加法运算脚本 `add2.sh`：

``` bash
$ vim add2.sh
$ cat add2.sh
#! /bin/bash
let sum=0
while [ $1 ]
do
        let num1=$1
        let sum=num1+sum
        shift
done
echo $sum
$ chmod u+x add2.sh
$ ./add2.sh 1 3 5 7 9
25
```

位置参数除了通过脚本运行时的实参传递赋值外，还可以利用set命令赋值。

#### 环境变量

环境变量也是系统预定义变量。环境变量是全局变量，而用户自定义变量是局部变量。用户自定义变量只在当前的shell中生效，而环境变量会在当前shell和这个shell的所有子shell中生效。

环境变量是写入相应的配置文件的，在执行过程中修改环境变量修改的是进程内存中的变量值，而没有写入配置文件，所以当前shell一旦终止，这个环境变量的修改就会结束，而只有写入配置文件才会在所有shell中生效。

在Linux中一般通过环境变量配置操作系统的环境，如提示符、查找命令的路径、用户家目录等，这些系统默认的环境变量的变量名是固定的，一些环境变量为只读变量，只读变量的值通常是在登录过程中定义的，意味着不能改变这些变量的值；而另一些为非只读变量，可以修改。

环境变量名一般都大写，便于区分。

在bash中可以用env命令列出已经定义的所有环境变量：

``` bash
$ env
SHELL=/bin/bash
WSL2_GUI_APPS_ENABLED=1
WSL_DISTRO_NAME=Ubuntu
NAME=D111KC
PWD=/home/d111kc
LOGNAME=d111kc
HOME=/home/d111kc
LANG=C.UTF-8
WSL_INTEROP=/run/WSL/320_interop
LS_COLORS=rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=00:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.avif=01;35:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.webp=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:*~=00;90:*#=00;90:*.bak=00;90:*.crdownload=00;90:*.dpkg-dist=00;90:*.dpkg-new=00;90:*.dpkg-old=00;90:*.dpkg-tmp=00;90:*.old=00;90:*.orig=00;90:*.part=00;90:*.rej=00;90:*.rpmnew=00;90:*.rpmorig=00;90:*.rpmsave=00;90:*.swp=00;90:*.tmp=00;90:*.ucf-dist=00;90:*.ucf-new=00;90:*.ucf-old=00;90:
WAYLAND_DISPLAY=wayland-0
LESSCLOSE=/usr/bin/lesspipe %s %s
TERM=xterm-256color
LESSOPEN=| /usr/bin/lesspipe %s
USER=d111kc
DISPLAY=:0
SHLVL=1
XDG_RUNTIME_DIR=/run/user/1000/
WSLENV=
XDG_DATA_DIRS=/usr/local/share:/usr/share:/var/lib/snapd/desktop
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/lib/wsl/lib:/mnt/e/workstation/bin/:/mnt/c/Program Files/Common Files/Autodesk Shared/:/mnt/c/Program Files/Microsoft SQL Server/120/Tools/Binn/:/mnt/c/Windows/system32:/mnt/c/Program Files/nodejs/:/mnt/d/Bandizip/:/mnt/c/Program Files/Go/bin:/mnt/d/hugo_extended_withdeploy_0.143.0_windows-amd64:/mnt/c/WINDOWS/system32:/mnt/c/WINDOWS:/mnt/c/WINDOWS/System32/Wbem:/mnt/c/WINDOWS/System32/WindowsPowerShell/v1.0/:/mnt/c/WINDOWS/System32/OpenSSH/:/mnt/c/Program Files/Git/cmd:/mnt/e/dev/python/python3.12/Scripts/:/mnt/e/dev/python/python3.12/:/mnt/c/Program Files/MySQL/MySQL Server 8.0/bin:/mnt/c/Program Files/PowerShell/7/:/mnt/c/Program Files/Docker/Docker/resources/bin:/mnt/c/Program Files/MySQL/MySQL Shell 8.0/bin/:/mnt/c/Users/86183/AppData/Local/Microsoft/WindowsApps:/mnt/c/Users/86183/AppData/Roaming/Python/Python312/Scripts:/mnt/d/PyCharm/PyCharm Community Edition 2024.3.1.1/bin:/mnt/c/Users/86183/AppData/Roaming/npm:/mnt/d/ffmpeg-7.1-full_build/ffmpeg-7.1-full_build/bin:/mnt/c/Users/86183/go/bin:/mnt/c/Users/86183/AppData/Local/Programs/Microsoft VS Code/bin:/mnt/d/vscode/Microsoft VS Code/bin:/snap/bin
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
HOSTTYPE=x86_64
PULSE_SERVER=unix:/mnt/wslg/PulseServer
_=/usr/bin/env
```

常用环境变量：

`HOME` 用户家目录

``` bash
$ echo $HOME
/home/d111kc
```

`PATH` shell查找命令的目录列表。PATH变量包含带冒号分界符的字符串，这些字符串代表存放系统命令的绝对路径。通常，用户会在家目录下建一个bin目录，存放自己编写的所有可执行命令，把这个目录加人PATH变量中，如下：`$ PATH=$PATH:$HOME/bin`即在当前的命令查找路径下增加一个目录$HOME/bin，这时用户就可以像使用系统命令一样使用自已编写的命令，而不用再给出相对路径./sh01。需要注意的是，$HOME/bin一定要放在PATH的最后面，因为系统是严格按照PATH变量值中的路径顺序来查找命令的，也就是说PATH变量值中的路径顺序决定了先从哪个目录查找

`PS1` shell的主提示符。主提示符是在 shell准备接受命令时显示的字符串。PS1定义主提示符是怎样构成的。

``` bash
$ echo $PS1
\[\e]0;\u@\h: \w\a\]${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$
```

“\u”表示当前用户的用户名；“\h”显示主机名的第一个字段（简称），如locallhost；“\W”显示完整的工作目录，`~` 代表家目录在PS1中常用的转义字符及其含义如下：

- `\$`：提示字符，如果是root用户，提示符为#，普通用户则为$。
- `\t`：显示时间为24小时格式，如“HH：MM：SS”
- \T：显示时间为12小时格式
- \H：显示完整的主机名
- \s：所用shell名称
- \v:bash的版本号。

`PWD` 当前工作目录的绝对路径。

`SHELL` 当前使用的shell。它指出shell解释程序放在什么地方。

``` bash
$ echo $SHELL
/bin/bash
```

环境变量和用户自定义变量的作用域不同，是通过export命令来设置的。用户自定义变量是局部变量，仅限于自身范围，不能自动传给子进程。如果希望父进程在创建子进程时将变量传递给子进程，须用export命令将这些变量送人进程转出区，进程转出区的变量将被子进程继承，从而使得用户自定义变量成为全局变量。

export命令的一般使用形式是：`$ export变量名`

变量通过export命令声明即可被子进程继承。用户自定义变量都是通过export设置为全局变量的。用户自定义变量只能在当前shell中有效，而export命令声明的变量在当前shell和所有子 shell 中有效。

``` bash
$ name=d111kc
$ echo $name
d111kc
$ bash
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

$ echo $name

```

这时name变量为空，因为第一句赋值是在父shell中执行的，在执行了bash语句后，处于子shell，在子shell中未对name变量赋值，所以name变量为空，下面继续执行如下命令：

``` bash
$ exit
exit
$ export name
$ echo $name
d111kc
$ bash
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

$ echo $name
d111kc
```

这时显示name变量的值为zhang，因为在父shell中已经通过export声明了变量name，子shell继承该变量，所以该变量值为d111kc

#### 变量的查询和删除

用户可以定义变量，在不需要使用该变量的时候也可以注销该变量，注销变量用unset命令，其一般形式是：`$ unset 变量名`

``` bash
d111kc@D111KC:~$ name=d111kc
d111kc@D111KC:~$ echo $name
d111kc
d111kc@D111KC:~$ unset name
d111kc@D111KC:~$ echo $name

d111kc@D111KC:~$
```

环境变量的删除方法和用户自定义变量是一样的，都使用unset命令。在注销变量之前，通常需要查询系统内已有的变量列表，查询所有变量的命令有set、env和export。三者都可以查询系统当前已有的变量列表，set的用法如下，env和export用法与set类似。

`$ set`

三者的区别就是：set可以查询所有的变量，包括局部变量和全局变量；env命令可以查询所有的环境变量，包括本进程及“祖先进程”所设置的全局（环境）变量；export命令可以显示本进程利用export命令所输出的全部变量。

### 数值运算

在在shell中所有的变量默认都是“字符串型”。也就是说，如果不手动指定变量的类型，那么所有的数值都是不能进行运算的。

``` bash
$ a=11
$ b=12
$ c=$a+$b
$ echo $c
11+12
```

如果需要进行数值运算，则可以采用以下三种方法中的任意一种：

#### 使用declare声明变量类型

使用declare命令就可以声明变量的类型。declare命令格式如下：`$ declare [选项] 变量名`

选项：

- `-`给变量设定类型属性，配合字母使用
- `+`取消变量的类型属性，配合字母使用
- `-a` 将变量声明为数组型
- `-i` 将变量声明为整数型
- `-r` 将变量声明为只读变量
- `-x`将变量声明为环境变量
- `-p` 显示指定变量被声明的类型

``` bash
$ a=11
$ b=12
$ declare -i c=$a+$b
$ echo $c
23
```

数组与变量类似，变量和数组都是用来保存数据的，只是变量只能被赋予一个数据值，一旦重复赋值，后一个值就会覆盖前一个值；而数组可以被赋予一组相同类型的数据值。

`$ declare -a name`

name会被认为是数组，虽然还未赋值，也不会被视为变量。如果没有把name变量声明为数组型，只要在定义变量时采用了`变量名[下标]`的格式，这个变量就会被系统视为数组型了，不用强制声明。

declare命令还可以把变量声明为环境变量，它和export命令的作用是一样的。例如：`$ declare -x test=123`表示把变量test声明为环境变量。

#### 使用expr和let命令

进行数值运算的第二种方法是使用expr命令，这个命令没有declare命令那么复杂。命令如下：

``` bash
$ a=11
$ b=12
$ c=$(expr $a + $b)
$ echo $c
23
```

注意使用expr命令进行运算时，“+”号左右两侧必须有空格，否则运算不执行。

let命令和expr命令类似，let比expr更常用。用法如下：

``` bash
$ a=11
$ b=12
$ let c=$a+$b
$ echo $c
23
```

#### 使用`$(())`运算

凡是用let命令的地方都可以用 `$(())` 取代，但其中只能包含一个算术表达式

``` bash
$ a=11
$ b=12
$ c=$(( $a + $b ))
$ echo $c
23
```

## if条件语句

if语句用于条件控制结构，其一般格式为：

``` bash
if 测试条件
    then 命令1
    else 命令2
fi
```

其中，if、then、else 和fi是关键字。

条件测试有两种常用形式：一种是用test命令`if test condition`；另一种是用一对方括号将测试条件括起来 `if [condition]`。这两种形式是完全等价的。`[  ]` 内部左右两端需要有空格。

条件测试常用来测试文件的属性、做字符串的比较和数值的比较。有关文件测试运算符的形式及其功能如下：

- `-r` 若文件存在且用户可读，则测试条件为真
- `-w` 若文件存在且用户可写，则测试条件为真
- `-x` 若文件存在且用户可执行，则测试条件为真
- `-f` 若文件存在且是普通文件，则测试条件为真
- `-d` 若文件存在且是目录文件，则测试条件为真
- `-b` 若文件存在且是块设备文件，则测试条件为真
- `-c` 若文件存在且是字符设备文件，则测试条件为真
- `-s` 若文件存在且文件长度大于0，则测试条件为真
- `-e` 该文件是否存在

有关字符串测试运算符的形式及其功能如下：

- `-z s1`若字符串s1的长度为0，则测试条件为真
- `-n s1`若字符串s1的长度大于0，则测试条件为真
- `sl = s2`若s1等于s2，则测试条件为真，“=”前后应有空格
- `s1 != s2`若s1不等于s2，则测试条件为真

数值比较运算：

- `n1 -eq n2`若n1等于n2，则测试条件为真
- `n1 -ne n2`若n1不等于n2,则测试条件为真
- `n1 -lt n2`若n1小于n2，则测试条件为真
- `n1 -le n2`若n1小于或等于n2，则测试条件为真
- `n1 -gt n2`若n1大于n2,则测试条件为真
- `n1 -ge n2`若n1大于或等于n2，则测试条件为真

if语句使用fi结尾，和一般语言使用大括号结尾不同。

if条件语句的判断思路是测试条件判断式是否成立，如果成立，则执行“then”中的命令；如果不成立，则执行“else”中的命令。

else部分还可以嵌套if，用关键字“elif”代替“elseif”，其一般格式如下：

``` bash
if [ 条件 ]
    then 命令1
    elif [ 条件 ]
    then 命令2
    else 命令3
fi
```

## case 多分支条件语句

case语句和if语句一样都是多分支条件语句，不过和多分支if条件语句不同的是，case语句只能判断一种条件关系，而if语句可以判断多种条件关系。

case语句的语法如下：

``` bash
case $变量名 in
    "值1") 命令
    命令;;
    “值2") 命令
    命令;;
    ...
    *) 命令
    命令;;
esac
```

case语句会取出变量中的值，然后与语句体中的值逐一比较。如果数值符合，则执行对应的程序；如果数值不符，则依次比较下一个值；如果所有的值都不符合，则执行`*)` 的命令，`*`可以缺省。

case语句以“case”开头，以“esac”结尾。

在每个分支程序之后要以`;;`（双分号）结尾，代表该程序段结束。

``` bash
$ vim yesno.sh
$ chmod u+x yesno.sh
$ ./yesno.sh
输入是或否（y/n): y
Your answer is yes!
yes
$ ./yesno.sh
输入是或否（y/n): n
Your answer is no!
no
$ ./yesno.sh
输入是或否（y/n): 5
Your choice is error!
$ cat yesno.sh
#! /bin/bash
echo -n "输入是或否（y/n): "
read answer
case $answer in
        "y") echo "Your answer is yes!"
                echo "yes";;
        "n") echo "Your answer is no!"
                echo "no";;
        *) echo "Your choice is error!";;
esac
```

## while 循环语句

shell有多种循环形式，包括while循环、until循环、for循环和selectin循环。此外，还需要了解continue和break关键字，以便在不满足结束条件的时候跳出循环。

while循环是shell脚本中最简单的一种循环，当条件满足时，while重复地执行一组语句，当条件不满足时，则退出while循环。while循环的用法如下：

``` bash
while condition
    do
        statements
    done
```

condition表示判断条件，statements表示要执行的语句（可以只有一条，也可以有多条），do和
done都是shell 中的关键字。

while循环的执行流程为：先对condition进行判断，如果该条件成立，则进入循环，执行while循环体中的语句，也就是do和done之间的语句。这样就完成了一次循环。每一次执行到done的时候都会重新判断condition是否成立，如果成立，则进人下一次循环，继续执行do和done之间的语句，如果不成立，则结束整个while循环，执行done后面的其他shell代码。如果一开始condition就不成立，那么程序就不会进人循环体，do和done之间的语句就没有执行的机会。

注意，在while循环体中必须有相应的语句使得condition越来越趋近于“不成立”，只有这样才能最终退出循环，否则while就成了死循环，会一直执行下去，永无休止。

while语句和if语句中的条件判断用法是一样的，可以使用test或`[]`命令，也可以使用 `(())`。

例如：计算1-100的整数之和：

``` bash
$ vim sum.sh
$ chmod u+x sum.sh
$ ./sum.sh
the sum is 5050
$ cat sum.sh
#! /bin/bash
i=1
sum=0
while [ "$i" -le 100 ]
do
        (( sum += i ))
        (( i++ ))
done
echo "the sum is $sum"
```

## until 循环

until循环和while循环恰好相反，当判断条件不成立时才进行循环，一旦判断条件成立终止循环。until循环的用法如下：

``` bash
until condition
    do
        statements
    done
```

## for 循环

for循环有两种使用形式，一种是算术表达式方式，另一种是值表方式。算术表达式方式的for循环用法如下：

``` bash
for ((expl;exp2;exp3))
    do
        statements
    done
```

expl、exp2、exp3是3个表达式，其中exp2是判断条件，for循环根据exp2的结果来决定是否继续下一次循环；statements是循环体语句，可以有一条，也可以有多条；do和done是shell中的关键字。

它的运行过程为：步骤一，执行expl；步骤二，执行exp2，如果它的判断结果是成立的，则执行循环体中的语句，否则结束整个for循环；步骤三，执行完循环体后再执行exp3；步骤四，重复执行步骤二和三，直到exp2的判断结果不成立，则结束循环。在上面的步骤中，步骤二和步骤三会重复执行，for语句的主要作用就是不断执行步骤二和三。exp1仅在第一次循环时执行，以后都不会再执行，可以认为这是一个初始化语句。exp2一般是一个关系表达式，决定了是否还要继续下次循环，称为“循环条件”。exp3很多情况下是一个带有自增或自减运算的表达式，以使循环条件逐渐变得“不成立”

使用for循环计算 1 + 2 + ... + 100:

``` bash
$ vim sumfor.sh
$ chmod u+x sumfor.sh
$ ./sumfor.sh
the sum is 5050
$ cat sumfor.sh
#! /bin/bash
sum=0
for (( i=0; i<=100; i++ ))
do
        (( sum+=i ))
done
echo "the sum is $sum"
```

for循环中的expl（初始化语句）、exp2（循环条件）和exp3（自增或自减）都是可选项，都可以省略（但分号；必须保留）。

值表方式的for循环的用法如下：

``` bash
for variable in value_list
do
    statements
done
```

variable表示变量，value_list表示取值列表，in是shell中的关键字。每次循环都会从value_list中取出一个值赋给变量variable，然后进入循环体（do和done之间的部分），执行循环体中的statements。直到取完value_list中的所有值，循环就结束了。invalue_list部分可以省略，省略后的效果相当于`in $@($*)`，变量依次取位置参数的值，然后执行循环体内的命令，直至所有的位置参数取完为止。例如：

``` bash
$ vim forloop.sh
$ chmod u+x forloop.sh
$ ./forloop.sh
1
2
3
4
5
the sum is 15
$ cat forloop.sh
#! /bin/bash
sum=0
for n in 1 2 3 4 5
do
        echo $n
        (( sum+=n ))
done
echo "the sum is $sum"
```

下面是缺省value_list的情况，这时变量将匹配位置参数，如下：

``` bash
$ vim forloop.sh
$ chmod u+x forloop.sh
$ ./forloop.sh python c html css javascript
python
c
html
css
javascript
$ cat forloop.sh
#! /bin/bash
for str
do
        echo $str
done
```

## select in 循环

select in是shell独有的一种循环，非常适合终端这样的交互场景，是C语言所没有的。selectin循环用来增强交互性，它可以显示出带编号的菜单，用户输人不同的编号就可以选择不同的菜单，并执行不同的功能。select in循环的用法如下：

``` bash
select variable in value_list
do
    statements
done
```

variable表示变量，value_list表示取值列表，in是shell中的关键字。select in和for in的语法是相似的。

``` bash
$ vim selectin.sh
$ chmod u+x selectin.sh
$ ./selectin.sh
what's is your favorite os?
1) linux
2) windows
3) mac
4) android
#? 1
you select linux
#? 4
you select android
#?
```

`#?` 用来提示用户输人菜单编号；Ctrl+D组合键，它的作用是结束select in循环。select语句取值列表value_list中的内容会以菜单的形式显示出来，用户输人菜单编号，就表示选中了某个值，这个值就会赋给变量variable，然后再执行循环体中的statements（do和done之间的部分）。每次循环时select都会要求用户输人菜单编号，并使用环境变量PS3的值作为提示符，PS3的默认值为#?，修改PS3的值就可以修改提示符。如果用户输人的菜单编号不在范围之内，例如上面输入的9，就会给variable赋一个空值；如果用户输人一个空值（什么也不输人，直接回车），会重新显示一遍菜单。需要注意，select是无限循环（死循环），输人空值，或者输入的值无效，都不会结束循环，只有遇到break语句，或者按下Ctrl+D组合键才能结束循环。

select in通常和case in一起使用，在用户输人不同的编号时可以做出不同的反应。修改上面的代码，加人case in语句：

``` bash
$ ./selectin.sh
what's is your favorite os?
1) linux
2) windows
3) mac
4) android
#? 2
my pc is win11
$ cat selectin.sh
#! /bin/bash
echo "what's is your favorite os?"
select name in "linux" "windows" "mac" "android"
do
        case $name in
                "linux")
                        echo "linux is opensource"
                        break;;
                "windows")
                        echo "my pc is win11"
                        break;;
                "mac")
                        echo "i want to buy a macbook in the future"
                        break;;
                "android")
                        echo "i have an android phone"
                        break;;
        esac
done
```

## break 和 continue

使用while、until、for、select循环时，如果想提前结束循环（在不满足结束条件的情况下结束循环），可以使用关键字break或者continue。

在C语言中，break和continue只能跳出当前或本次循环，内层循环中的break和continue对外层循环不起作用；但是shell中的break和continue却能够跳出多层循环，也就是说，内层循环中的break和continue能够跳出外层循环。不过在实际应用中，break和continue一般只用来跳出当前层次的循环，很少有需要跳出多层循环的情况。

### break关键字

break关键字的用法为：

``` bash
break n
```

n表示跳出循环的层数，如果省略n，则表示跳出整个循环。break关键字通常和if语句一起使用，即在满足条件时便跳出循环。

### continue关键字

continue关键字的用法为：

``` bash
continue n
```

n表示循环的层数，如果省略n，则表示continue只对当前层次的循环语句有效，遇到continue会跳过本次循环，忽略本次循环的剩余代码，直接进人下一次循环。如果带上n，比如n的值为2，那么continue对内层和外层循环语句都有效，不但内层会跳过本次循环，外层也会跳过本次循环，其效果相当于内层循环和外层循环同时执行了不带n的continue。continue关键字通常也和if语句一起使用，即在满足条件时便跳出循环。

## shell函数

shell函数的本质是一段可以重复使用的脚本代码，这段代码被提前编写好了，放在了指定的位置，使用时直接调取即可。shell中的函数和C语言中的函数类似，只是在语法细节上有所差别。

### 函数定义

shell函数定义的语法格式如下：

``` bash
function name() {
    statements
    [ return value ] 
}
```

function是shell中的关键字，专门用来定义函数；name是函数名；statements是函数要执行的代码，也就是一组语句；returnvalue表示函数的返回值，其中return是shell的关键字，专门用在函数中返回一个值，这一部分可以写也可以不写。由一包围的部分称为函数体，调用一个函数，实际上就是执行函数体中的代码。

函数定义时也可以不写function关键字，如下：

``` bash
name() {
    statements
    [ return value ] 
}
```

如果写了function关键字，也可以省略函数名后面的小括号，如下：

``` bash
function name {
    statements
    [ return value ] 
}
```

建议使用标准的写法，这样能够做到“见名知意”。

调用shell函数时可以给它传递参数，也可以不传递。如果不传递参数，直接给出函数名字即可：

``` bash
name
```

如果传递参数，那么多个参数之间以空格分隔：

``` bash
name param1 param2 param3
```

不管是哪种形式，函数名字后面都不需要带括号。

和其他编程语言不同的是，shell函数在定义时不能指明参数，但是在调用时却可以传递参数，并且给它传递什么参数它就接收什么参数。shell也不限制定义和调用的顺序，可以将定义放在调用的前面，也可以将定义放在调用的后面。

### 函数参数

和C语言等大部分编程语言不同，shell中的函数在定义时不能指明参数，但是在调用时却可以传递参数。函数参数是shell位置参数的一种，在函数内部可以使用`$n`来接收，例如，`$1`表示第一个参数，`$2`表示第二个参数，依次类推。除了`$n`，还有另外3个比较重要的变量：`$#`可以获取传递的参数的个数；`$@`或者`$*`可以一次性获取所有的参数（用法同shell位置参数`$*`和`$@`）。