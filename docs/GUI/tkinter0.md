---
comments: true
---

# 预备节：面向对象

:material-pen-plus: `本文创建于2025-3-16`

要使用tkinter进行GUI设计，就不得不用到**面向对象**的编程思想。Tkinter提供的小部件非常有限，而且大多数小部件的功能往往不足以完成相应的任务。在这种情况之下，就不得不使用继承来加强小部件的功能，或者创建新的小部件。

## 一、属性

### 1.1 类属性

通俗来说，类属性就是定义在类中的变量。不需要创建实例就能直接使用，当然实例也可以使用类属性。通过类名就可以调用，可以更改属性值，还可以创建新属性。

我们来创建一个 *Banana* 类：

```py title='banana.py' hl_lines="3 4" linenums="1"
class Banana:
    """一种美味的热带水果"""
    food_group = 'fruit'
    colors = ['green', 'green-yellow', 'yellow', 'brown spotted', 'black']
```

上面代码中的 *food_group* 和 *colors* 就是类属性。它们不需要创建实例就可以使用，对二者调用 `print()` 函数：

    print(Banana.food_group)
    print(Banana.colors)

输出：

    fruit
    ['green', 'green-yellow', 'yellow', 'brown spotted', 'black']

### 1.2 实例属性

实例属性就是定义在构造方法 `__init__()` 中的带有 *self.* 前缀的变量，必须创建实例之后才能使用。不创建实例通过类名调用会报错。需要先创建实例，才能调用，创建实例后，可以对属性重新赋值，还可以创建新属性。

```py title='banana.py' linenums="1" hl_lines="3 4"
class Banana:
    # --snip--(1)
    def __init__(self, color='green'):
        self.color = color
```

1. 我使用 *# --snip--* 来省略前面已经写过的一些代码

此处的 *self.color* 就是实例属性，它是定义在 `__init__()` 方法中的一个变量。

???+ warning

    - `__init__(self)` 方法的第一个参数必须是 *self*，用来表示实例本身
    - *self.color* 和 *color* 并不是同一个变量，而是两个不同的变量，但常常定义在 `__init__()` 中定义的属性会命名为 `__init__()` 方法传入参数的名字，*self.color* 是一个不可分割的整体

为了使用 *self.color* 属性，我们需要创建实例：

    my_banana = Banana()
    print(my_banana.color)

输出：

    green

## 二、方法

### 2.1 实例方法

定义在类中的函数，和 `__init__()` 方法一样，第一个参数必须是 *self*。需要先创建实例，才能调用。创建实例后，可以新建方法（先定义一个函数，再使用self.的方式将创建的函数名赋值给self）。

```py title='banana.py' linenums="1" hl_lines="3 4"
class Banana:
    # --snip--
    def print_color(self):
        print(self.color)
```

需要创建实例才可以使用：

    my_banana.print_color()

输出：

    my_banana.print_color()

未完待续……

测试