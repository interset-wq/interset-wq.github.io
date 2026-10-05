# shell脚本

1. 用Shell编程，判断一文件是不是字符设备文件，如果是将其拷贝到/dev目录下。

参考程序：
    #!/bin/sh
    FILENAME=
    echo "Input file name:"
    read FILENAME
    if [ -c "$FILENAME" ]
    then
    cp $FILENAME /dev
    fi

1. 请下列shell程序加注释，并说明程序的功能和调用方法：
    #!/bin/sh 
    #!/bin/sh 
    # 
    # /etc/rc.d/rc.httpd 
    # 
    # Start/stop/restart the Apache web server. 
    # 
    # To make Apache start automatically at boot, make this 
    # file executable: chmod 755 /etc/rc.d/rc.httpd 
    # 
    case "$1" in 
    'start') 
    /usr/sbin/apachectl start 
    ;; 
    'stop') 
    /usr/sbin/apachectl stop 
    ;; 
    'restart') 
    /usr/sbin/apachectl restart 
    ;; 
    *) 
    echo "usage $0 start|stop|restart" 
    ;; 
    esac
参考答案：
（1）程序注释
    #!/bin/sh  #定义使用的shell
    #  #注释行，以#开始的行均为注释行
    # /etc/rc.d/rc.httpd  #指定该脚本文件的路径和名称
    #  #注释行
    # Start/stop/restart the Apache web server.  #说明脚本功能：启动、停止、重启Apache web服务器
    #  #注释行
    # To make Apache start automatically at boot, make this  #说明使Apache在系统启动时自动运行的方法
    # file executable: chmod 755 /etc/rc.d/rc.httpd  #具体操作命令：赋予该脚本文件执行权限
    #  #注释行
    case "$1" in  #case结构开始，判断位置参数$1的值，决定执行对应的操作，本程序携带一个位置参数
    'start')  #若位置参数为start
    /usr/sbin/apachectl start  #执行启动httpd进程的命令
    ;;  #跳出当前case分支
    'stop')  #若位置参数为stop
    /usr/sbin/apachectl stop  #执行停止httpd进程的命令
    ;;  #跳出当前case分支
    'restart')  #若位置参数为restart
    /usr/sbin/apachectl restart  #执行重新启动httpd进程的命令
    ;;  #跳出当前case分支
    *)  #若位置参数不是start、stop或restart时
    echo "usage $0 start|stop|restart"  #显示命令提示信息，告知程序的调用方法
    ;;  #跳出当前case分支
    esac  #case结构结束
（2）程序的功能是启动、停止或重新启动httpd进程
（3）程序的调用方式有三种：
    - 启动：/etc/rc.d/rc.httpd start
    - 停止：/etc/rc.d/rc.httpd stop
    - 重新启动：/etc/rc.d/rc.httpd restart

1. 设计一个shell程序，添加一个新组为class1，然后添加属于这个组的30个用户，用户名的形式为stdxx，其中xx从01到30。
参考答案：
    #!/bin/sh
    i=1
    groupadd class1
    while [ $i -le 30 ]
    do 
    if [ $i -le 9 ];then 
    USERNAME=stu0${i}
    else 
    USERNAME=stu${i}
    fi 
    useradd $USERNAME
    mkdir /home/$USERNAME
    chown -R $USERNAME /home/$USERNAME
    chgrp -R class1 /home/$USERNAME
    i=$(($i+1)) 
    done

1. 编写shell程序，实现自动删除50个账号的功能。账号名为stud1至stud50。
参考程序：
    #!/bin/sh
    i=1
    while [ $i -le 50 ]
    do
    userdel -r stud${i}
    i=$(($i+1))
    done