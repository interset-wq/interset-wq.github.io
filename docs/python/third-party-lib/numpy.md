---
comments: true
icon: simple/numpy
status: new
title: NumPy
subtitle: 科学计算
---

:material-pen-plus: `本文创建于2025-5-16`

[:simple-numpy: NumPy官方文档](https://numpy.org/doc/stable/index.html){ .md-button .md-button--primary }

## 一 导入

    import numpy as np

## 二 数组ndarray

在NumPy中基本数组类被称为`ndarray`, 它代表一个“N维数组”, 类似于python基本数据类型的列表。大多数 NumPy 数组都有一些限制, 类似于数学中的矩阵. 例如:

- 数组的所有元素必须具有相同类型的数据 `int`类型
- 一旦创建,数组的总大小无法更改。
- 形状必须是“矩形”的,而不是“锯齿状”;例如,每一排二维数组必须具有相同数量的列。

### 2.1 通过一系列元素创建数组ndarray对象

创建数组ndarray对象类似于创建Python列表,一维数组相当于普通的列表,二维或更高维的数组相当于嵌套列表.

**一维数组**

    a = np.array([1, 2, 3, 4, 5, 6])

返回一个ndarray对象 `array([ ])`, 使用 `print()` 函数打印列表. 类似于python列表,操作与其几乎相同:可以通过下标访问元素,可以切片,可以修改元素.

???+ warning "list对象和ndarray对象的区别"
    - Python内置的list对象使用切片得到的是一个新列表,对这个新列表操作不会影响到原列表.
    - NumPy的ndarray对象使用切片得到的是原阵列的一个视图,对其的任何操作都会影响到原阵列.

**二维或更高维的数组**

``` shell
>>> a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
>>> a
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
>>> a[1, 3]
8
```

不同于Python的嵌套列表, ndarray对象可以通过坐标访问元素, `a[1, 3]`表示访问坐标为`[1, 3]`的元素,即第二行第四个元素

???+ warning
    此例中的数组a是并不是三维数组,而是二维数组,因为它摆成了一个矩形

### 2.2 数组ndarray对象的属性

``` shell
>>> a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
>>> a.ndim
2
>>> a.shape
(3, 4)
>>> a.size
12
>>> a.dtype
dtype('int32')
```

- `.ndim`属性,返回数组维度
- `.shape`属性,返回元组,数组摆放成的矩形的高和宽
- `.size`属性,返回数组的元素数
- `.dtype`属性,返回数组元素的数据类型(数组中的所有元素数据类型都是相同的),例如`dtype('int32')`表示32位整数

### 2.3 创建基本数组

???+ warning
    NumPy数组中默认数据类型是64位浮点(np.float64),因此整数之后都有一个小数点`.`,例如`0`在NumPy数组中表示为`0.`,以下函数创建数组时都可以通过`dtype`关键字参数指定数组元素的数据类型

- `np.zeros()`函数 传入整数,创建只有0的一维数组

    ```shell
    >>> np.zeros(3)
    array([0., 0., 0.])
    ```

- `np.ones()`函数 传入整数,创建只有1的一维数组

    ```shell
    >>> np.ones(2)
    array([1., 1.])
    ```

- `np.empty()`函数 传入整数,创建为初始化数组,数组内容随机(取决于记忆的状态),创建数组的速度快于`np.ones()`和`np.zeros()`
- `np.arange()`函数 类似于Python内置函数`range()`,创建一系列连续元素的数组

    ```shell
    >>> np.arange(5)
    array([0, 1, 2, 3, 4])
    >>> np.arange(1, 10, 3)
    array([1, 4, 7])
    ```

- `np.linspace()`函数 关键字参数`num`表示该数组的元素数,类似于Python内置函数`range()`,但是是按照相等的步长,创建指定元素个数的数组

    ```shell
    >>> np.linspace(0, 1, num=5)                       
    array([0.  , 0.25, 0.5 , 0.75, 1.  ])
    ```

未完待续