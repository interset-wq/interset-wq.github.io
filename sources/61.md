# OpenSSH

OpenSSH 是安全 shell 协议（secure shell，简称 SSH）的免费开源实现。可以用来进行远
程控制、在计算机之间传送文件等。
SSH 采用非对称加密技术（RSA）加密所有传输的数据。
OpenSSH 提供了服务端后台程序和客户端工具，对远程控制和文件传输过程的数据进行加
密处理。
SSH 是 安全外壳 协议。
14.1 安装 OpenSSH
OpenSSH 是 Linux 最常用的 SSH 服务器/客户端软件。
CentOS 下，查看是否默认安装了 OpenSSH，rpm -qa openssh* 启动服务：service sshd start
开启防火墙的 22 号端口：
sudo firewall -cmd –zone =public –add-port=22/tcp --permanent
14.2 配置 OpenSSH
OpenSSH 的主配置文件 /etc/ssh/sshd_config。
常见的配置选项：
1）设置 SSH 的端口号是 22（默认端口号 22）：Port=22。
14.3 OpenSSH 的使用
14.3.2 文件传输
SFTP 是安全文件传送协议，可以为传输文件提供一种安全的加密方法。SCP 是远程文件复
制的协议，复制过程是加密的。
1）以下协议中，为远程登录会话和其他网络服务提供安全性的协议是
A. FTP B. HTTP C. SSH D. ICMP
2）SSH 采用的加密算法是： RSA
3）SSH 是由 IETF（the Internet Engineering Task Force）指定的建立在应用层基础上的 安
全网络 协议。
4）SSH 是专为 远程登陆 会话和其它网络服务提供安全性的协议。
5）SSH 采用了 非对称加密技术（RSA）加密所有传输的数据