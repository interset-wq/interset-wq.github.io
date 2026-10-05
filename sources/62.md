# Web 服务器搭建、应用开发与部署

Linux 下，采用 Eclipse 开发工具，基于 MVC 的 Java Web 开发，使用当下较为流行的 SSM
框架进行演示。
16.1 Web 服务器搭建的准备
16.1.1 配置 Java
要先将 Linux 自带的 openJDK 卸载，后安装 Oracle 的 JDK
java -version 查看已安装的 Java 版本信息
rpm -qa | grep java 查找已安装的 openJDK 位置
之后逐一卸载，下载 JDK 压缩包
解压后，配置环境变量 gedit ~/.bashrc
bashrc 文件中配置 4 个环境变量：JAVA_HOME，JRE_HOME，PATH，CLASSPATH
配置完毕关闭文件，在终端执行 source ~/.bashrc 使环境变量立即生效
16.1.2 配置 MySQL
MySQL 的配置文件 my.cnf p350
#设置 MySQL 的安装目录 basedir
#设置 MySQL 数据库的数据存放目录 datadir
#
16.2 Web 服务器的搭建
16.2.1 安装配置 Tomcat
使用 startup.sh 命令启动服务，调用方法 /usr/local/tomcat8/bin/startup.sh
使用 shutdown.sh 命令关闭服务
16.2.2 配置 DNS、DHCP、FTP 服务
1. 配置域名系统 DNS
实现域名解析的软件模块是 BIND。
DNS 服务使用的端口是 53。
设置正向解析的数据库文件（named.bob.com)
设置反向解析的数据库文件（named.172.16.5)
2. 配置 DHCP
动态主机配置协议 DHCP 是一个局域网的网络协议。
3. 配置 FTP
FTP 是文件传输协议。
16.3 开发环境与配置
16.4 网站设计开发与部署
16.4.1 MVC 简介
MVC 是模型 Model 视图 View，控制器 Controller， 一种软件设计典范。
16.4.2 常见框架
1. Struts 2
Struts 2 是一个基于模型、视图、控制器的 MVC 设计模式应用框架。
2. Spring
Spring 是一个轻量级控制反转（IoC）和面向切面（AOP）的容器框架。
3. MyBatis
M 有 Batis 是一款优秀的持久层框架，支持定制化 SQL、存储过程以及高级映射。