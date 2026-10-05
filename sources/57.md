# 设备管理

## 设备文件

Linux 中，用户是通过文件系统与设备连接的。每个设备都是在其驱动程序控制下运行的，驱动程序则与/dev 目录下的特殊文件联系在一起，在选择设备或者操作设备时都以这个文件的名称来代表这一设备。

Linux 系统采用设备文件 统一管理硬件设备,从而将硬件设备的特性及管理细节对用户隐藏，实现用户程序与设备无关性。从用户的角度来看；对设备的使用和一般文件的使用一样。

设备的命名规则：在/dev 目录下，每一个驱动器以一个单独的设备文件来表现；设备的文件名一般由两部分组成，第一部分是 主设备号 ，第二部分是 次设备号 。主设备号代表设备的类型，如 hd 表示 IDE 硬盘，sd 表示 SCSI 硬盘，tty 表示终端设备等；次设备号代表同类设备中的序号，如 IDE 硬盘一般可以有 4 个，即/dev/hda、/dev/hdb、/dev/hdc、/dev/hdd，a 代表第一个设备，hda1 中的”1”代表 had 的第一个硬盘主分区，以此类推。

SCSI 硬盘就是/dev/sda、/dev/sdb 等。fd 是软盘，设备名称是/dev/fd0。Linux 系统中，磁带机的设备名是/dev/st*和/dev/nst*，其中 nst*是指操作完成后不自动回卷磁带，st*自动回卷磁带，常用 nst*。主机 SCSI 总线上找到的第一个磁带机是 nst0 或 st0，第二个是 nst1 或st1，依此类推。磁带机的 SCSI 号越小，其设备名也就越靠前。

一台主机上可以有多块硬盘，系统采用 a~p 来代表 16 块不同的硬盘，硬盘的分区编号规则：主分区或扩展分区的编号从 1 开始，到 4 结束；逻辑分区从编号 5 开始。

硬盘设备有大量的扇区组成的，第一个扇区最重要，里面保存着主引导记录与分区表信息。主引导记录（信息） 需要占用 446 字节，分区表为 64 字节，结束符占用 2 字节；跟去表中没记录一个分区信息就需要 16 字节，最多只有 4 个分区信息可以写到第一个扇区中，这 4 个分区就是 4 个主分区。

/dev/null 文件是空设备，等价于一个只写文件，所有写入它的内容都会永远丢失。读取数据返回为空。

/dev/zero 也是一个伪文件，是一个输入设备。主要用处是创建一个指定长度的初始化空文件。

/dev/full 是一个特殊的设备文件，在向其写入时总是返回“设备无剩余空间”（错误码为ENPOSPC），读取时则与/dev/zero 相似，放回无限的二进制流。常被用来测试程序在遇到磁盘无剩余空间错误时的行为

/dev/random[urandom]用作随机数发生器或伪随机数发生器。

Linux 系统采用 设备文件 统一管理硬件设备。按照是否对应物理实体，设备可以分为两种：物理设备，虚拟设备。

## 常用的设备命令

系统启动时会检测主机硬件并加载适当的驱动程序（模块，modules），让硬件正确地启动与运行。内核所检测到的各项硬件设备，会记录在/proc 中

### 查看 CPU 信息的命令

lscpu 命令 查看 CPU 和处理单元的信息

``` bash
$ lscpu
Architecture:             x86_64
  CPU op-mode(s):         32-bit, 64-bit
  Address sizes:          39 bits physical, 48 bits virtual
  Byte Order:             Little Endian
CPU(s):                   16
  On-line CPU(s) list:    0-15
Vendor ID:                GenuineIntel
  Model name:             12th Gen Intel(R) Core(TM) i5-1240P
    CPU family:           6
    Model:                154
    Thread(s) per core:   2
    Core(s) per socket:   8
    Socket(s):            1
    Stepping:             3
    BogoMIPS:             4223.99
    Flags:                fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse s
                          se2 ss ht syscall nx pdpe1gb rdtscp lm constant_tsc rep_good nopl xtopology tsc_reliable nonst
                          op_tsc cpuid pni pclmulqdq vmx ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadl
                          ine_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch invpcid_single ssbd i
                          brs ibpb stibp ibrs_enhanced tpr_shadow vnmi ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 sme
                          p bmi2 erms invpcid rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves avx_
                          vnni umip waitpkg gfni vaes vpclmulqdq rdpid movdiri movdir64b fsrm md_clear serialize flush_l
                          1d arch_capabilities
Virtualization features:
  Virtualization:         VT-x
  Hypervisor vendor:      Microsoft
  Virtualization type:    full
Caches (sum of all):
  L1d:                    384 KiB (8 instances)
  L1i:                    256 KiB (8 instances)
  L2:                     10 MiB (8 instances)
  L3:                     12 MiB (1 instance)
Vulnerabilities:
  Gather data sampling:   Not affected
  Itlb multihit:          Not affected
  L1tf:                   Not affected
  Mds:                    Not affected
  Meltdown:               Not affected
  Mmio stale data:        Not affected
  Reg file data sampling: Mitigation; Clear Register File
  Retbleed:               Mitigation; Enhanced IBRS
  Spec rstack overflow:   Not affected
  Spec store bypass:      Mitigation; Speculative Store Bypass disabled via prctl and seccomp
  Spectre v1:             Mitigation; usercopy/swapgs barriers and __user pointer sanitization
  Spectre v2:             Mitigation; Enhanced / Automatic IBRS; IBPB conditional; RSB filling; PBRSB-eIBRS SW sequence;
                           BHI BHI_DIS_S
  Srbds:                  Not affected
  Tsx async abort:        Not affected
```

### 查看内存信息的命令
最常用命令 free，查看虚拟内存最常用命令 vmstat

#### free 命令

显示系统内存状态，包括空闲的和已用的物流内存，swap 内存，以及被内核使用的缓冲区。

语法 `$ free [选项]`

``` bash
$ free
               total        used        free      shared  buff/cache   available
Mem:         7975248      596900     7442636        3248      137100     7378348
Swap:        2097152           0     2097152
```

-k：以 KB 为单位，显示内存的使用情况，默认选项
-b：以字节为单位，显示内存使用情况
-m：以 MB 为单位，显示
-g：以 GB 为单位
-t：在输出的最终结果中，输出内存和 swap 分区的总量
-o：不显示系统缓冲区这一列
-s：间隔秒数：根据指定的间隔时间，持续显示内存使用情况

Swap 指的是交换分区，也就是虚拟内存。

#### vmstat 命令
Virtual Meomory Statistics 虚拟内存统计。Linux 内存管理主要通过“调页（Paging）”和” 交换（Swapping）”来完成内存调度。页面写入磁盘的过程称作 Page-Out，页面从磁盘重新回到内存的过程被称作 Page-In。

当内核需要一个页面，但发现此页面不在物理内存中（因为被 Page-Out）时，就发生页面错误（Page Fault）。若 pageout 频繁发生，内核管理分页的时间超过运行程序的时间时，系统性能会急剧下降。这时系统已经运行非常慢或进入暂停状态，这种状态亦被称作颠簸 Thrashing

``` bash
$ vmstat
procs -----------memory---------- ---swap-- -----io---- -system-- -------cpu-------
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st gu
 1  0      0 7442724   1308 136264    0    0   481   133   57    0  0  0 100  0  0  0
```

### 查看块设备的命令

#### dmesg 命令

可以查看 Linux 系统启动信息的命令
常用于查看系统的硬件信息。除此之外，开机信息也可以通过/var/log/目录中的 dmesg 文件查看。

``` bash
$ dmesg | grep CPU
[    0.025044] smpboot: Allowing 16 CPUs, 0 hotplug CPUs
[    0.029566] setup_percpu: NR_CPUS:256 nr_cpumask_bits:256 nr_cpu_ids:16 nr_node_ids:1
[    0.071783] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=16, Nodes=1
[    0.089216] rcu:     RCU restricting CPUs from NR_CPUS=256 to nr_cpu_ids=16.
[    0.104760] smpboot: CPU0: 12th Gen Intel(R) Core(TM) i5-1240P (family: 0x6, model: 0x9a, stepping: 0x3)
[    0.104760] Performance Events: unsupported p6 CPU model 154 no PMU driver, software events only.
[    0.104760] smp: Bringing up secondary CPUs ...
[    0.104760] .... node  #0, CPUs:        #1  #2  #3  #4  #5  #6  #7  #8  #9 #10 #11 #12 #13 #14 #15
[    0.104760] smp: Brought up 1 node, 16 CPUs
$ dmesg | grep eth0
[    1.794310] IPv6: ADDRCONF(NETDEV_CHANGE): eth0: link becomes ready
```

#### lsblk 命令

列出系统中的所有可用块设备信息，还能显示他们之间的依赖关系，但不会列出 RAM 盘的信息。块设备如，硬盘、闪存盘、CD-ROM 等。

块设备指设备将数据按可寻址的块为单位进行输入/输出，一次 I/O 操作固定大小的数据块，通过缓冲区来读写块设备，允许随机访问。这种方式适用于发送大量的信息，常见的块设备有硬盘、磁盘、光盘驱动器等。

``` bash
$ lsblk
NAME
    MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
sda   8:0    0 388.4M  1 disk
sdb   8:16   0     2G  0 disk [SWAP]
sdc   8:32   0     1T  0 disk /mnt/wslg/distro
                              /
```

### 磁盘配额的命令

1. quota 命令
查询磁盘空间的限制，并得知已使用多少空间。
quota [选项] 用户名
quota [选项] 群组名
1. quotacheck 命令
扫描文件系统（必须含有挂载参数 usrquota 和 grpquota）并建立磁盘配额记录文件。
quotacheck [选项] 文件系统
1. quotaon 命令
启动磁盘配额服务。
1. quotaoff 命令
关闭磁盘配额服务。