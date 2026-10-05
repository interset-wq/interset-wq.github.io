# 用户管理

## 用户与用户组管理

用户和用户组管理，就是添加用户和用户组、更改密码和设定权限等操作。用户和用户组管理对个人计算机来讲意义不大，但服务器上是多用户多任务操作系统，如Linux，换句话说，Linux系统支持多个用户在同一时间内登录，不同用户可以执行不同的任务，并且互不影响。

例如，某台Linux服务器上有4个用户，分别是root、www、ftp和mysql，在同一时间内，root用户可能在查看系统日志、管理维护系统；www用户可能在修改自已的网页程序；ftp用户可能在
上传软件到服务器；mysql用户可能在执行自己的SQL查询，每个用户互不干扰，有条不紊地进行着自己的工作。与此同时，每个用户之间不能越权访问，比如www用户不能执行mysql用户的SQL查询操作，ftp用户也不能修改www用户的网页程序。

因此，必须确保不同用户具有不同的权限，每个用户在权限允许的范围内完成不同的任务。如果要使用Linux系统的资源，就必须向系统申请一个账户，然后通过这个账户进人系统（账户和用户是同一个概念）。通过建立不同属性的用户，可以合理地控制用户使用和访问系统资源，Linux正是通过这种用户权限的划分与管理，实现了多用户多任务的安全运行机制。

### 用户和用户组

每个用户都有唯一的用户名和密码。在登录系统时，只有正确输人用户名和密码，才能进人系统和自己的主目录。

用户组是具有相同特征用户的逻辑集合。简单理解就是，有时需要让多个用户具有相同的用户管理权限，最好的方式是建立一个组，让这个组具有查看、修改此文件的权限，然后将所有需要访问此文件的用户放人这个组中。那么，这个组中所有用户就具有了和组一样的权限，这就是用户组。

将用户分组是Linux系统对用户进行管理及控制访问权限的一种手段，通过定义用户组，简化了对用户的管理工作。用户和用户组的对应关系有以下4种：

- 一对一：一个用户可以在一个组中，是组中的唯一成员。
- 一对多：一个用户可以在多个用户组中，此用户具有这些组的共同权限。
- 多对一：多个用户可以在一个组中，这些用户具有和组相同的权限。
- 多对多：多个用户可以在多个组中，也就是以上3种关系的扩展。

### 用户和用户组管理

登录Linux系统时，虽然输入的是自己的用户名和密码，但其实Linux并不认识用户名，它只认识用户名对应的ID（也就是一串数字）。Linux系统将所有用户名与ID的对应关系都存储在`/etc/passwd`文件中。用户名并无实际作用，仅是为了方便用户记忆而已。同理，Linux也不认识用户组名称，每个用户组的名称也有一个ID与之对应，对应关系存储在/etc/group文件中。

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
postfix:x:105:109::/var/spool/postfix:/usr/sbin/nologin
$ cat /etc/group
root:x:0:
daemon:x:1:
bin:x:2:
sys:x:3:
adm:x:4:syslog,d111kc
tty:x:5:
disk:x:6:
lp:x:7:
mail:x:8:
news:x:9:
uucp:x:10:
man:x:12:
proxy:x:13:
kmem:x:15:
dialout:x:20:d111kc
fax:x:21:
voice:x:22:
cdrom:x:24:d111kc
floppy:x:25:d111kc
tape:x:26:
sudo:x:27:d111kc
audio:x:29:d111kc
dip:x:30:d111kc
www-data:x:33:
backup:x:34:
operator:x:37:
list:x:38:
irc:x:39:
src:x:40:
shadow:x:42:
utmp:x:43:
video:x:44:d111kc
sasl:x:45:
plugdev:x:46:d111kc
staff:x:50:
games:x:60:
users:x:100:d111kc
nogroup:x:65534:
systemd-journal:x:999:
systemd-network:x:998:
crontab:x:997:
systemd-timesync:x:996:
input:x:995:
sgx:x:994:
kvm:x:993:
render:x:992:
messagebus:x:101:
syslog:x:102:
systemd-resolve:x:991:
uuidd:x:103:
_ssh:x:104:
landscape:x:105:
polkitd:x:990:
admin:x:106:
netdev:x:107:d111kc
d111kc:x:1000:
ssl-cert:x:108:
postfix:x:109:
postdrop:x:110:
docker:x:1001:d111kc
```

在`/etc/passwd`文件中，每一行用户记录的各个数据段用 `:` 分隔，分别定义了用户的各方面属性。第1字段就是用户的用户名，用户名是方便用户记忆的登录系统的唯一身份标识，而系统是以用户ID作为用户登录系统的唯一身份标识。第3字段和第4字段分别记录了用户的两种ID，即用户ID（UserID，简
称UID）和用户组ID（GroupID，简称GID）。用户名和UID的对应关系记录在/etc/passwd文件中。

为了合理地控制用户访问系统资源，UID、GID与文件拥有者和拥有群组两种属性相对应。

``` bash
$ ls -l
total 12
-rwxr--r-- 1 d111kc d111kc  41 Aug  6 20:55 forloop.sh
-rwxr--r-- 1 d111kc d111kc 196 Aug  6 21:39 login.sh
-rwxr--r-- 1 d111kc d111kc 353 Aug  6 21:12 selectin.sh
```

长格式显示了文件控制块的内容，第3字段和第4字段表示文件拥有者和拥有群组，对应于用户的UID和GID。真正在文件控制块（在Linux系统中是inode表，即索引节点表）中存放的是该文件的拥有者ID和群组ID，当显示文件属性时，系统会根据/etc/passwd和/etc/group文件中的内容，分别找到UID和GID对应的用户名和群组名，然后显示出来。

## 用户和用户组管理相关的文件

为了管理用户账号和用户组，系统设置了多个文件存放有关的信息。最重要的文件有`/etc/passwd`文件、`/etc/shadow`文件、`/etc/group`文件和`/etc/gshadow`文件。

### /etc/passwd

Linux系统中的/etc/passwd文件是系统用户配置文件，存储了系统中所有用户的基本信息，并且所有用户都可以对此文件执行读操作。

/etc/passwd文件中的每行记录对应一个用户。Linux系统中默认的用户很多，这些用户中的绝大多数是系统或服务正常运行所必需的用户，这种用户通常称为系统用户或伪用户。系统用户无法用来登录系统，但也不能删除，因为一旦删除，依赖这些用户运行的服务或程序就不能正常执行，会导致系统问题。在有的系统中，1～499的ID是保留给系统使用的。所以通常500以后的ID是给一般用户使用的。

`/etc/passwd`文件中的每行用户信息都划分为7个字段（`:`分隔各个字段），每个字段含义如下：

- 字段1 用户名
- 字段2 密码
- 字段3 UID（用户ID）
- 字段4 GID（组ID）
- 字段5 描述性信息
- 字段6 家目录
- 字段7 默认shell

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
postfix:x:105:109::/var/spool/postfix:/usr/sbin/nologin
```

字段1：用户名。用户名仅是为了方便用户记忆，Linux系统是通过UID来识别用户身份、分配用户权限的。`/etc/passwd`文件定义了用户名和UID之间的对应关系。

字段2：密码。系统用密码来验证用户的合法性。在`/etc/passwd`文件中用“x”表示此用户设有密码，但它不是真正的密码，真正的密码保存在`/etc/shadow`文件中。

字段3：UID。UID是一个数值，每个用户都有唯一的UID，Linux系统通过UID来识别不同的用户。实际上，UID取值范围为0～65535。在某些情况下，系统允许存在多个拥有不同用户名但UID相同的用户。

字段4：GID。这个字段表示用户初始组的组ID。具有相似属性的多个用户被分配到同一个组内，每个组都有组名和ID。Linux中的每个用户可以同时属于多个组。初始组，指用户登录时就拥有这个用户组的相关权限。每个用户的初
始组只能有一个，通常就是将和此用户的用户名相同的组名作为该用户的初始组。比如说，手工添加用户lamp，在建立用户lamp的同时，就会建立lamp组作为lamp用户的初始组。附加组，指用户可以加人多个其他的用户组，并拥有这些组的权限。每个用户只能有一个初始组，除初始组外，用户再加人其他的用户组，这些用户组就是这个用户的附加组。附加组可以有多个，而且用户可以有这些附加组的权限。例如，lamp用户除属于初始组lamp外，它又加入了users组，那么lamp用户同时属于lamp组和users组，其中lamp是初始组，users是附加组。在/etc/passwd文件的第4个字段中看到的ID是用户的初始组。

字段5：描述性信息。这个字段并不重要，只是用来记录用户的相关信息，如真实姓名等。

字段6：主目录。用户登录后有操作权限的访问目录，通常称为用户的主目录。例如，root超级管理员账户的主目录为/root，普通用户的主目录为/home/yourname，即在/home目录下建立和用户名相同的目录作为主目录，如lamp用户的主目录就是/home/lamp目录。用户登录后均有自己独立的工作环境，个人用户的文件都放在各自的主目录下。

### /etc/shadow

/etc/shadow文件用于存储Linux系统中用户的密码信息，又称为“影子文件”。/etc/passwd文件，由于该文件允许所有用户读取，易导致用户密码泄露，因此Linux系统将用户的密码信息从/etc/passwd文件中分离出来，单独放到了/etc/shadow文件中。/etc/shadow文件只有root用户拥有读权限，其他用户没有任何权限，这样就保证了用户密码的安全性。

``` bash
# cat /etc/shadow
root:$y$j9T$ZrywLYh0e4DLF5n/9Ks3A0$ClR3vOIXpIho6s8R.qF68WTvqSspvkFmfw6V2UTIcG5:20291:0:99999:7:::
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
d111kc:$y$j9T$ey7cqETMjc2Fgf0OXWWSf.$YdlWJY/HWXzNZtJb5BGh.JrSdT3aSoD6Ebe1q94GBeD:20299:0:99999:7:::
postfix:!:20302::::::
```

同/etc/passwd文件一样，文件中每行代表一个用户，同样使用`:`作为分隔符，不同之处在于，每行用户信息被划分为9个字段：

- 字段1 用户名
- 字段2 加密密码
- 字段3 最后一次修改时间
- 字段4 最小修改时间间隔
- 字段5 密码有效期
- 字段6 密码需要变更前的警告天数
- 字段7 密码过期后的宽限时间
- 字段8 账号失效时间
- 字段9 保留字段

字段1：用户名。该字段与/etc/passwd文件的用户名有相同的含义。

字段2：加密密码。这里保存的是真正加密的密码。目前Linux的密码采用的是SHA512散列加密算法，原来采用的是MD5或DES加密算法。SHA512散列加密算法的加密等级更高，也更加安全。注意，这串密码产生的乱码不能手动修改，如果手动修改，系统将无法识别密码，导致密码失效。在密码串前加上`!` `*` 或`x`使密码暂时失效。

字段3：最后一次修改时间。此字段表示最后一次修改密码的时间。显示的是从1970.1.1到上次修改密码的天数，换算时间：

``` bash
$ date -d "1970-01-01 20291 days"
Tue Jul 22 00:00:00 CST 2025
```

字段4：最小修改时间间隔。也就是说，该字段规定了从字段3（最后一次修改时间）起，多长时间之内不能修改密码。如果是0，则密码可以随时修改；如果是10，则代表密码修改后10天之内不能再次修改。此字段是针对某些人频繁更改账户密码而设计的。

字段5：密码有效期。经常变更密码是个好习惯，为了强制用户变更密码，这个字段可以指定距离字段3（最后一次修改时间）多长时间内需要再次变更密码，否则该账户密码会过期。该字段的默认值为99999，约274年，可认为永久生效。如果改为90，则表示密码被修改90
天之后必须再次修改，否则该密码将过期。管理服务器时，可通过这个字段强制用户定期修改密码。

字段6：密码需要变更前的警告天数。与字段5相比较，当账户密码有效期快到时，系统会发出警告信息给此账户，提醒用户“再过n天你的密码就要过期了，请尽快重新设置你的密码！”。该字段的默认值是7，也就是说，距离密码到期的第7天开始，该账户在每次登录系统时都会收到“修改密码”的警告信息。

字段7：密码过期后的宽限时间。简单理解就是，在密码过期后，用户如果还是没有修改密码，则在此字段规定的宽限天数内，用户还是可以登录系统的；如果过了宽限天数，系统将不再让此账户登录，也不会提示账户过期，是完全禁用的。比如，此字段规定的宽限天数是10，则代表密码过期10天后失效；如果是0，则代表密码过期后立即失效；如果是-1，则代表密码永远不会失效。

字段8：账号失效时间。该字段同字段3一样，使用自1970年1月1日以来的总天数作为账户的失效时间。该字段表示，账号在此字段规定的时间之外，不论密码是否过期，都将无法使用！该字段通常被使用在具有收费服务的系统中。

字段9：保留字段。这个字段目前没有使用，等待新功能的加人。

对于普通账户的密码遗失，可以通过root账户解决，它会重新配置好指定账户的密码，而不需要知道原来的密码（利用root的身份使用passwd命令即可）。如果root账号的密码遗失，则需要重新启动系统，进人单用户模式，系统会提供root权限的bash接口，此时可以用passwd命令修改账户密码。

### /etc/gshadow

/etc/passwd文件存储用户基本信息，同时考虑到账户的安全性，将用户的密码信息存放在另一个文件/etc/shadow中。/etc/gshadow文件也是如此，组用户信息存储在/etc/group文件中，而将组用户的密码信息存储在/etc/gshadow文件中。

``` bash
# cat /etc/gshadow
root:*::
daemon:*::
bin:*::
sys:*::
adm:*::syslog,d111kc
tty:*::
disk:*::
lp:*::
mail:*::
news:*::
uucp:*::
man:*::
proxy:*::
kmem:*::
dialout:*::d111kc
fax:*::
voice:*::
cdrom:*::d111kc
floppy:*::d111kc
tape:*::
sudo:*::d111kc
audio:*::d111kc
dip:*::d111kc
www-data:*::
backup:*::
operator:*::
list:*::
irc:*::
src:*::
shadow:*::
utmp:*::
video:*::d111kc
sasl:*::
plugdev:*::d111kc
staff:*::
games:*::
users:*::d111kc
nogroup:*::
systemd-journal:!*::
systemd-network:!*::
crontab:!*::
systemd-timesync:!*::
input:!*::
sgx:!*::
kvm:!*::
render:!*::
messagebus:!::
syslog:!::
systemd-resolve:!*::
uuidd:!::
_ssh:!::
landscape:!::
polkitd:!*::
admin:!::
netdev:!::d111kc
d111kc:!::
ssl-cert:!::
postfix:!::
postdrop:!::
docker:!::d111kc
```

每行代表一个组用户的密码信息，各行信息用`:`作为分隔符，分为4个字段。

- 字段1 组名
- 字段2 加密密码
- 字段3 组管理员
- 字段4 组附加用户列表

字段1：组名。此字段与/etc/group文件中的组名相对应。

字段2：加密密码。对大多数用户来说，通常不设置组密码，因此该字段常为空，但有时为“！”，指的是该组没有组密码，也不设组管理员。

字段3：组管理员。从系统管理员的角度来说，该文件最大的功能就是创建组管理员。

字段4：组附加用户列表。该字段显示这个用户组中有哪些附加用户，和/etc/group文件中附加组显示内容相同。

## 用户和用户组管理的命令

实现用户账号的管理，要完成的工作主要有用户的添加，密码配置，修改用户信息、密码状态，用户组管理等。

### 用户的添加

新建用户语法：`# useradd [选项] 用户名`

选项：

- `-u` 手动指定用户的UID，注意UID的范围（不小于500）。
- `-d` 手动指定用户的主目录；主目录必须写绝对路径
- `-c` 手动指定/etc/passwd文件中各用户信息中字段5的描述性内容，可随意配置。
- `-g` 手动指定用户的初始组。一般以和用户名相同的组作为用户的初始组，在创建用户时会默认建立初始组。一旦手动指定，系统将不会再创建此默认的初始组目录。
- `-G` 指定用户的附加组。将用户加人其他组，一般都使用附加组。
- `-s` 手动指定用户的登录shell，默认为/bin/bash。
- `-e` 指定用户的失效日期，格式为"YYYY-MM-DD”。也就是/etc/shadow文件的字段8。
- `-o` 允许创建的用户UID相同。例如，执行`useradd -u 0 -o user1`命令建立用户user1，它的UID和root用户的UID相同，都是0
- `-m` 建立用户时强制建立用户的主目录。在建立系统用户时，该选项是默认的。
- `-r` 创建系统用户，也就是UID在1~499、供系统程序使用的用户。由于系统用户主要用于运行系统所需服务的权限配置，因此创建系统用户时默认不会创建主目录。

在没有特殊要求时，无须使用任何选项即可成功创建用户。

useradd命令创建用户的过程：首先，系统读取/etc/login.defs和/etc/default/useradd，根据这两个配置文件中定义的规则添加用户，也就是在/etc/passwd、/etc/group、/etc/shadow、/etc/gshadow文件中添加用户数据；然后，接着系统会自动在/etc/default/useradd文件设定的目录下建立用户主目录；最后，复制/etc/skel目录中的所有文件到此主目录中。由此，一个新的用户就创建完成了。

### 密码配置命令

使用useradd命令创建新用户时，并没有设定用户密码，passwd可以设定用户密码。passwd命令的基本格式：`# passwd [选项] 用户名`

选项：

- `-S` 查询用户密码的状态，也就是/etc/shadow文件中此用户密码的内容；仅root用户使用。
- `-l` 暂时锁定用户，该选项会在/etc/shadow文件中指定用户的加密密码串前添加“!”，使密码失效；仅root用户使用。
- `-u` 解锁用户，和-1选项相对应，就是将添加的“！”去掉；仅root用户使用。
- `--stdin` 可以将通过管道符输出的数据作为用户的密码；主要在批量添加用户时使用。
- `-n` 设置该用户修改密码后，多长时间不能再次修改密码，也就是修改/etc/shadow文件中各行密码的字段4。
- `-x` 设置该用户的密码有效期，对应/etc/shadow文件中各行的字段5。
- `-w` 设置用户密码过期前的警告天数，对应/etc/shadow文件中各行密码的字段6。
- `-i` 设置用户密码失效日期，对应/etc/shadow文件中各行密码的字段7。

例如，使用root账户修改普通用户d111kc的密码，可以使用如下命令：

``` bash
# passwd d111kc
New password:
Retype new password:
passwd: password updated successfully
```

普通用户只能使用passwd命令修改自己的密码，而不能修改其他用户的密码。与使用root账户修改普通用户的密码不同，普通用户修改自己的密码需要先输人自己的旧密码，只有旧密码输人正确后才能输人新密码。

``` bash
$ passwd
Changing password for d111kc.
Current password:
New password:
Retype new password:
passwd: password updated successfully
```

### 修改用户信息命令

``` bash
# usermod [选项] 用户名
```

### 修改用户密码状态命令

``` bash
# change [选项] 用户名
```

### 删除用户命令

``` bash
# userdel -r 用户名
```

只用 root 用户才能用

`-r` 表示在删除用户的同时删除用户的家目录。

### 查看用户的UID和GID命令

id命令可以查询用户的UID、GID和附加组的信息。命令比较简单，格式如下：

``` bash
$ id 用户名
```

``` bash
$ id root
uid=0(root) gid=0(root) groups=0(root)
```

### 用户间切换命令

```
$ su [选项] 用户名
```

选项：

- `-` 当前用户不仅切换为指定用户的身份同时所用的工作环境也切换（包括 PATH 变量、MAIL 变量等），使用`-`选项可省略用户名，默认切换为 root 用户。
- `-l` 同 `-` 的使用类似，也就是在切换用户身份的同时，完整切换工作环境，但后面需要添加欲切换的使用者账号。
- `-p` `-m` 表示切换为指定用户的身份，但不改变当前的工作环境（不使用切换用户的配置文件）。
- `-c` 仅切换用户并执行一次命令，执行后自动切换回来，该选项后通常会带有要执行的命令。

### 用户组管理命令

- 添加用户组 `# groupadd [选项] 组名`
- 修改用户组相关信息 `# groupmod [选项] 组名`
- 删除用户组 `# groupdel 组名` 仅适用于删除那些不是任何用户初始组的组
- 设置组管理员 `# gpasswd [选项] 组名`
