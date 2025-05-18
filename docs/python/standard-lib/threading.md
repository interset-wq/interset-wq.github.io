---
comments: true
# icon: material/language-python
# status: new
title: threading
subtitle: 多线程
---

:material-pen-plus: `本文创建于2025-4-17`

[:simple-python: threading官方文档](https://docs.python.org/zh-cn/3/library/threading.html){ .md-button .md-button--primary }

## 导入threading

    from threading import Thread

## 第一步：创建thread对象

Thread类：

`Thread(group, target, name, args, kwargs, daemon)`

创建thread对象时必须使用关键字参数传参，禁止使用位置参数。各参数说明如下：

- group 必须为 None或者不传入这个参数，这是一个预留的参数
- target 传入新线程需要调用的函数的函数名
- name 是线程名称。 在默认情况下，会以 "Thread-N" 的形式构造唯一名称，其中 N 为一个较小的十进制数值，或是 "Thread-N (target)" 的形式，其中 "target" 为 `target.__name__`，如果指定了 target 参数的话。
- args 传入元组，给target参数调用的函数传入位置参数
- kwargs 传入字典，给target参数调用的函数传入关键字参数
- daemon 守护线程。如果不是 None，daemon 参数将显式地设置该线程是否为守护模式。 如果是 None (默认值)，线程将继承当前线程的守护模式属性。


## 第二步：对thread对象进行操作

thread对象的属性和方法：

- `start()` 方法 开启线程，使用了此方法，thread创建的线程才会执行
- `join()` 方法 等待
