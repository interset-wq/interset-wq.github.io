---
comments: true
icon: material/language-python
# status: new
title: Python基础语法
---

:material-pen-plus: `本文创建于2025-3-17`

[:simple-python: 前往PEP8规范](https://peps.python.org/pep-0008/){ .md-button .md-button--primary }
[:simple-python: 前往Python官方文档](https://docs.python.org/zh-cn/3/){ .md-button }

## 一、注释和变量命名规范

注释

- 单行注释 `#`
- 多行注释 三重引号

变量命名规则

- 只能包含数字、字母、下划线，且不能以数字开头
- 推荐使用下划线命名法（蛇形命名法）
- 见名知意
- 区分大小写，变量一般使用小写
- 命名时谨慎使用小写字母l和大写字母O，以免和数字混淆
- 不能和python关键字重名
- 常量命名时字母全大写

## 二、内置函数

- `print()`函数
- `input()`函数 返回用户输入的字符串
- `type()`函数 返回数据类型
- `range()`函数 生成数字序列，左闭右开区间
    - `range(num)` 返回0到num之间的整数序列
    - `range(num1,num2)` 返回两个数字之间的整数序列
    - `range(num1,num2,step)` 返回两个数字之间的整数序列，通过step指定间隔大小
- 类型转换
    - `int()` 函数 转换为整型,不是四舍五入，而是舍弃小数点之后的部分
    - `float()` 转换成小数
    - `str()` 转换成字符串
    - `list()` 函数
    - `str()` 函数
    - `tuple()` 函数
    - `set()` 函数

## 三、运算符

=== "算术运算符"

    - `+` 加
    - `-` 减
    - `*` 乘
    - `/`除
    - `//` 取整除
    - `%` 取余
    - `**` 乘方

=== "赋值运算符"

    - `=` 赋值
    - `+=` 加法赋值运算符
    - `-=` 减法赋值运算符
    - `*=` 乘法赋值运算符
    - `/=` 除法赋值运算符
    - `%=` 取模赋值运算符
    - `**=` 幂赋值运算符
    - `//=` 取整除赋值运算符

=== "比较运算符"

    - `==` 判断内容是否相等，满足为True，不满足为False
    - `!=` 判断内容是否不相等，满足为True，不满足为False
    - `>` 判断运算符左侧内容是否大于右侧,满足为True，不满足为False
    - `<` 判断运算符左侧内容是否小于右侧，满足为True，不满足为False
    - `>=` 判断运算符左侧内容是否大于等于右侧，满足为True，不满足为False
    - `<=` 判断运算符左侧内容是否小于等于右侧，满足为True，不满足为False

=== "逻辑运算符"

	- 与 `and`
	- 或 `or`
	- 非 `not`

## 四、数据类型

基本数据类型有 `整型int` `浮点数float` `布尔数bool -> True/False` `字符串str` `复数complex` `空NoneType -> None` `列表list` `集合set` `元组tuple` `字典dict`。整数和浮点数可以适当添加下划线让数字更易读。可以通过使用逗号分割同时为多个变量赋值。

数据容器：一种可以容纳多份数据的数据类型，容纳的每一份数据称之为1个元素，每一个元素，可以是任意类型的数据，如字符串、数字、布尔等。五种数据容器分别是 `列表list` `集合set` `元组tuple` `字典dict` `字符串str`

### 4.1 空类型None

python中一个特殊的字面量，表示空，无意义。无返回值的函数返回的实际上是None，在if判断语句中None相当于False，定义变量但是暂时不想赋值时使用None当占位符

### 4.2 数据容器通用操作

1. 遍历 全都可以使用for循环，集合和字典不能使用while循环
2. 共有的函数
- `len()` 函数
- `max()` 函数
- `min()` 函数
- `sorted(容器, [reverse=True])` 函数 排序，`reverse=True` 表示降序，返回一个排好序的列表

### 4.3 字符串str

使用单引号、双引号、三重引号包裹，可以使用 `+` 进行字符串的拼接，使用 `* n` 进行字符串的重复，`n` 表示重复次数

三重引号用于包裹多行字符串。一个引号的写法也可以跨行，只需要在每行的末尾加入表示连接的字符 `\` 即可

转义字符 

- `\n` 换行符
- `\t` 制表符

可以切片，也可以使用while循环或for循环遍历

#### 4.3.1 字符串格式化

- f字符串
- 占位符字符串

在不需要控制数字的精度时，采用 *f字符串* 明显比 *占位符字符串* 简单。以下重点介绍占位符字符串

占位符

- `%s` 将内容转换成字符串，放入占位位置
- `%d` 将内容转换成整数，放入占位位置
- `%f` 将内容转换成浮点型，放入占位位置

用于控制精度的符号

- `m` 控制宽度，要求是数字（很少使用），设置的宽度小于数字自身，不生效。可以在 `m` 前添加 `0` 来使用 `0` 来补位
- `.n` 控制小数点精度，要求是数字，会进行小数的四舍五入
- `-` 配合 `m` 使用，控制宽度不够时在右边补空格，默认在左边补空格

=== "占位符字符串"
	占位符字符串常用于控制数字的精度
	```py
	num1 = 3.14
	num2 = 123
	string = 'hello world'
	msg = 'num1的值是%-6.2f，num2的值是%06d，string的值是%s' % (num1, num2, string) #(1)
	print(msg)
	```

	1. 字符串中出现多个占位符时，引号外面的 `%` 后面的用来替换的变量使用逗号连接，并用小括号包裹
   
	输出结果

	`num1的值是3.14  ，num2的值是000123，string的值是hello world`
=== "f字符串"
	```py
	num1 = 3.14
	num2 = 123
	string = 'hello world'
	msg = f'num1的值是{num1}，num2的值是{num2}，string的值是{string}'
	print(msg)
	```
	输出结果

	`num1的值是3.14，num2的值是123，string的值是hello world`



#### 4.3.2 字符串操作

常用函数和方法

- `index(元素)` 方法
- `replace(str1,str2)` 方法 将字符串内的全部：str1，替换为str2。不改变原字符串
- `split(分隔str)` 方法 以分隔str为分隔符，将原字符串拆分，返回一个列表。不改变原字符串
- `strip()` 方法 删除字符串前后的空白字符,传入参数时，删除参数字符串中的字母，比如传入'ab'，删除的是字符串前后的字母a和字母b
    - `rstrip()` 方法
    - `lstrip()` 方法
- `count()` 方法
- `len()` 函数 字符串中的符号和空白也被看做是字符
- `upper()`方法 将字符串所以字母转换为大写
- `lower()`方法 将字符串所有字母转换为小写
- `title()`方法 单词首字母大写
- `removeprefix()`方法 删除前缀，需要传入需要删除的前缀

??? note "字符串特点"

    - 只可以存储字符串
    - 长度任意（取决于内存大小）
    - 支持下标索引
    - 允许重复字符串存在
    - 不可以修改（增加或删除元素等）
    - 支持for循环

### 4.4 列表list

使用方括号 `[]` 包裹，元素之间使用逗号分隔，列表中的数据可以是不同的数据类型，有顺序，使用下标获取元素。正向下标从 `0` 开始，反向下标从 `-1` 开始，==列表命名时建议使用名词复数形式==

可以使用for循环或while循环遍历

=== "常用方法"
    - `index(元素)` 方法 返回查询元素的下标（正向下标）
    - `列表名[下标] = 新值` 更改元素的值
    - `insert(下标，值)` 方法 在指定位置插入元素
    - `append(值)` 方法 在列表末尾追加元素
    - `extend(数据容器)` 方法 将其它数据容器的内容取出，依次追加到列表尾部
    - `pop(下标)` 方法 删除元素，不传入参数时删除末尾的元素，返回删除的元素
    - `remove(元素)` 方法 删除某元素在列表中的第一个匹配项，根据值删除元素，可以与while循环配合使用删除所有匹配项
        ```py
        my_list = ['a', 'b', 'c', 'a', 'd', 'a']
        while 'a' in my_list:
            my_list.remove('a')
        print(my_list) # 输出结果 ['b', 'c', 'd']
        ```
    - `clear()` 方法 将列表转换为空列表 `[]`
    - `count(元素)` 方法 统计某元素在列表中出现次数
    - `sort()`方法 正序排列，传入`reverse=True`时倒序排列（按照数字或字母顺序）
    - `reverse()`方法 倒置，将原顺序倒置

=== "del语句"
    `del 列表名[下标]` 删除元素
  
=== "常用函数"
    - `len()` 函数 返回列表长度
    - `sorted()`函数 正序排列，传入参数reverse=True时倒序排列
    - `range([start,] end [,step])`函数 取值左闭右开区间，生成整数数值列表
    - `max(lst)`函数 取列表中的最大值
    - `min(lst)`函数 取列表中的最小值
    - `sum(lst)`函数 计算列表元素之和
    - `{==zip(lst1, lst2)==}`函数 同时遍历多个列表
        
        ??? example

            代码
            ```py
            langs = ['python', 'javascript', 'c++']
            extensions = ['py', 'js', 'cpp']
            for lang, extension in zip(langs, extensions):
                print(f'{lang}语言的后缀名是{extension}')
            ```
            输出结果
            ```
            python语言的后缀名是py
            javascript语言的后缀名是js
            c++语言的后缀名是cpp
            ```
    - `{==enumerate(lst, start)==}` 函数 同时遍历列表下标和元素，可选参数 `start` 表示列表下标开始值，默认0

        ??? example

            代码
            ```py
            langs = ['python', 'javascript', 'c++']
            for index, lang in enumerate(langs, start=1):
                print(index, lang)
            ```
            输出结果
            ```
            1 python
            2 javascript
            3 c++
            ```

=== "列表推导式"

    使用 *列表推导式* 能明显简化代码

    ???+ example

        不使用列表推导式
        ```py
        nums = range(1, 10)
        squires = []
        for num in nums:
            squire = num ** 2
            squires.append(squire)
        print(squires) # 输出结果 [1, 4, 9, 16, 25, 36, 49, 64, 81]
        ```
        使用列表推导式
        ```py
        squires = [num**2 for num in range(1, 10)]
        print(squires) # 输出结果 [1, 4, 9, 16, 25, 36, 49, 64, 81]
        ```

??? note "列表特点"

    - 可以容纳多个元素（上限为2**63-1、9223372036854775807个）
    - 可以容纳不同类型的元素（混装）
    - 数据是有序存储的（有下标序号）
    - 允许重复数据存在
    - 可以修改（增加或删除元素等）

切片

序列是指：内容连续、有序，可使用下标索引的一类数据容器，列表、元组、字符串，均可以可以视为序列。序列的典型特征就是：有序并可用下标索引，字符串、元组、列表均满足这个要求

语法：`{==序列[起始下标: 结束下标: 步长]==}` 左闭右开区间

- 起始可以省略，省略从头开始
- 结束可以省略，省略到尾结束
- 步长可以省略，省略步长为1（可以为负数，表示倒序执行）
- 使用切片创建列表副本	`序列[:]`

### 4.5 元组tuple

使用小括号包裹，元素之间使用逗号分隔，单元素元组需要在元素后添加逗号。元组相当于不可修改的列表，元组中的数据可以是不同的数据类型

可以切片，可以使用while循环或for循环遍历

常用函数和方法

- len()函数
- index(元素)方法
- count(元素)方法

??? warning

	- 不可以修改元组的内容，否则会直接报错
	- 可以修改元组内嵌套的list的内容（修改元素、增加、删除、反转等）但是不可以替换list为其它list或其它类型

??? note "元组特点"

    - 可以容纳多个数据
    - 可以容纳不同类型的数据（混装）
    - 数据是有序存储的（下标索引）
    - 允许重复数据存在
    - 不可以修改（增加或删除元素等）
    - 支持for循环

### 4.6 集合set

使用花括号包裹，元素使用逗号分隔。元素无序，互不相同，没有下标索引。

只能使用for循环，不能使用while循环遍历。

常用函数和方法

- `add(元素)` 方法 添加元素，会导致集合本身遭到修改
- `remove(元素)` 方法 移除元素，会导致集合本身遭到修改
- `pop()` 方法 从集合中随机取出一个元素，会导致集合本身遭到修改
- `clear()` 方法 清空集合，返回空集 `set()`,会导致集合本身遭到修改变为 `set()`
- `集合1.difference(集合2)` 方法 取出集合1和集合2的差集（集合1有而集合2没有的），得到一个新集合，不改变原来的两个集合
- `集合1.difference_update(集合2)` 方法 消除2个集合的差集，对比集合1和集合2，在集合1内，删除和集合2相同的元素。会导致集合1被修改，集合2不变
- `集合1.union(集合2)` 方法 得到两个集合的并集，不改变原来两个集合
- `len()` 函数

??? note "集合特点"

	- 可以容纳多个数据
	- 可以容纳不同类型的数据（混装）
	- 数据是无序存储的（不支持下标索引）
	- 不允许重复数据存在
	- 可以修改（增加或删除元素等）
	- 支持for循环

### 4.7 字典dict

通过键获取值，使用花括号包裹，键值对使用逗号分隔，键和值使用冒号连接。

常用操作

- 新增元素 `字典名[Key] = Value`
- 更新元素 `字典名[Key] = Value` 对已存在的键使用
- 删除元素 `pop(Key)` 方法 字典被修改，指定Key的键值对被删除，返回键对应的值value
- 清空字典 `clear()` 方法 字典被修改为空字典{}，元素被清空
- 字典长度 `len()`函数
- 删除字典中的键值对：使用 del 语句将指定字典名中要删除的键相应的键值对彻底删除。例如 使用 `del mydict['name']` 删除mydict字典中的name对应的键值对
- `get()` 方法 
    - 用来访问字典某个键对应的值，如果键不存在，返回默认值或`None`
    - `my_dict.get(key, [default])`：根据键获取值，默认值 `default` 实参是可选的
- `{==items()==}`方法 用于同时遍历字典的键和值
    
    ??? example

        代码
        ```py
        languages = {'python': 'py', 'javascript': 'js', 'c++': 'cpp'}
        for lang, extension in languages.items():
            print(f'{lang}语言的文件后缀名是{extension}')
        ```
        输出结果
        ```
        python语言的文件后缀名是py
        javascript语言的文件后缀名是js
        c++语言的文件后缀名是cpp
        ```

- `keys()`方法	返回键的列表，一般用于遍历所有键，直接使用字典名遍历，默认是遍历字典的键的列表
- `values()`方法，返回值的列表，一般用于遍历所有的值
- *字典推导式* 能明显简化代码

    ???+ example

        ```py
        langs = ['python', 'javascripts', 'c++']
        extensions = ['py', 'js', 'cpp']
        languages = {lang: extension for lang, extension in zip(langs, extensions)}
        print(languages) # 输出结果 {'python': 'py', 'javascripts': 'js', 'c++': 'cpp'}
        ```


??? note "字典特点"

	- 可以容纳多个数据
	- 可以容纳不同类型的数据
	- 每一份数据是KeyValue键值对
	- 可以通过Key获取到Value，Key不可重复（重复会覆盖）
	- 不支持下标索引
	- 可以修改（增加或删除更新元素等）
	- 支持for循环，不支持while循环

## 五、判断语句和循环语句

### 5.1 判断语句 

判断语句if，和布尔数以及比较运算符一起使用。关键字`in` 检查特定值是否在列表、元组中。将数值 0、空值 None、空字符串“”、空列表[]、空元组()、空字典{} 用作条件表达式时，Python 都会返回 False

三种if语句

- `if` 语句
- `if else` 语句和 *双目运算符*

    ???+ example

        使用双目运算符可以简化 `if else` 语句

        === "if else语句"
            ```py
            num1 = 9
            num2 = 7
            if num1 < num2:
                num3 = num1
            else:
                num3 = num2
            print(num3) # 输出结果 7
            ```

        === "双目运算符"
            ```py
            num1 = 9
            num2 = 7
            num3 = num1 if num1 < num2 else num2
            print(num3) # 输出结果 7
            ```

- `if elif else` 语句

`match case` 语句

- `case _:` 相当于是默认值，没有满足前面的条件时，执行此条件
- 管道 `|` 相当于或，同一个 `case` 可以匹配多种情况

???+ tip

    === "值匹配"
        ```py
        num = 10
        match num:
            case 1: print('one') # num=1时，输出结果 one
            case 2: print('two') # num=2时，输出结果 two
            case 3: print('three') # num=3时，输出结果 three
            case _: print('default') # num!以上三个数字时，输出结果 default
        ```
    === "类型匹配"
        ```py
        var = 10
        match var:
            case int(): print('整数') # var的数据类型是整数时，输出结果 整数
            case str(): print('字符串') # var的数据类型是字符串时，输出结果 字符串
            case dict(): print('字典') # var的数据类型是字典时，输出结果 字典
            case _: print('其他') # var是以上三者之外的数据类型时，输出结果 其他
        ```
    === "使用管道"
        ```py
        var = 'hi'
        match var:
            case 'hello' | 'hi': print('你好') # var的值是'hello'或'hi'时，输出结果 你好
            case 'for' | 'while': print('循环语句') # var的值是'for'或'while'时，输出结果 循环语句
            case _: print('默认') # var的值不是以上结果时，输出结果 默认
        ```
    === "变量绑定"
        ```py
        my_list = ['javascript', 'html', 'css']
        match my_list:
            case [x, y, z]: print(f'{x}控制行为，{y}控制结构，{z}控制样式') # 当my_list有且仅有三个元素时，执行此语句
            case _: print('match的列表不是只有三个元素的列表') 
        ```

### 5.2 循环语句

while循环 不断地运行，直到指定的条件不再满足为止。用途比for循环更广泛

for循环 适用于可迭代类型（列表，字符串，元组，字典，`range()`函数生成的数字序列等）

循环中断

- `continue` 中断本次循环，进入下一次循环
- `break` 结束循环

## 六、函数function和模块

使用 `def` 关键字定义函数，函数必须先定义再使用。使用 `return` 关键字设置返回值，没有定义返回值的函数返回 `None`，==使用下划线命名法（蛇形命名法）==

定义函数之后，在 `def` 的下一行使用三重引号解释函数的作用

- `:param` 用于解释参数，使用之后代码编辑器鼠标悬停时会出现用法说明
- `:return` 用于解释返回值

使用 `global` 关键字 可以在函数内部声明变量为全局变量

多返回值

return语句得到返回值，如果想要返回多个可以使用逗号分隔，然后赋值给多个变量，类似于使用元组同时给多个变量赋值

传参方式

=== "位置参数"
      - 调用函数时根据函数定义的参数位置来传递参数
      - 传递的参数和定义的参数的顺序及个数必须一致
=== "关键字参数"
      - 函数调用时通过 `"键=值"` 形式传递参数，不受传参顺序影响，关键字参数必须写在位置参数之后默认值
      - 定义函数时可以为参数设置默认值，所有位置参数必须放在默认值参数之前
      - 通过将参数的默认值设为 `''` 或 `None`，可以使其成为可选参数，具体用哪个当做占位符取决于参数的数据类型
=== "不定长参数"
      - 多个位置参数 `*args`，args是多个位置参数的习惯性写法。传入的所有参数都会被args变量收集，它会根据传进参数的位置合并为一个元组(tuple)，args是元组类型，这就是位置传递
      - 多个关键字参数 `**kwargs`，kwargs是习惯性写法，可以自己命名。参数是“键=值”形式的形式的情况下, 所有的“键=值”都会被kwargs接受, 同时会根据“键=值”组成字典.

!!! example 

    ```py
    def person_info(name, gender, age=None):
        info = {'姓名': name, '性别': gender}
        if age:
            info['年龄'] = age
        return info
    my_dict = person_info('cook', 'male', 17)
    print(my_dict) # 输出结果 {'姓名': 'cook', '性别': 'male', '年龄': 17}
    ```

!!! tip

    当函数的参数是列表时，为了防止原列表被函数修改，传参数可以传入原列表的副本进行操作



???+ tip "函数编写指南"

    - 要给函数和模块一个描述性名称，且只使用小写字母和下划线。
    - 每个函数都应包含简要阐述其功能的注释，该注释应紧跟在函数定义后面，并采用文档字符串的格式。

        ??? note "函数注释"

            对函数进行解释说明，鼠标悬停在函数名上时，显示函数参数和返回值的解释说明。
            ```py
            def person_info(name, gender, age=None):
                """
                一个人的基本信息
                :param name: 这个人的姓名
                :param gender: 这个人的年龄
                :param age: 这个人的年龄，可选参数
                :return: 返回这个人的基本信息字典
                """
                info = {'姓名': name, '性别': gender}
                if age:
                    info['年龄'] = age
                return info
            ```

    - {==给形参指定默认值和调用函数传入实参时，等号两边不要有空格==}
    - 应使用两个空行分开不同的函数块
    - 所有的 `import` 语句都应放在文件开头，唯一的例外是，你要在文件开头使用注释来描述整个程序。

匿名函数

=== "将函数作为参数"
    
    ```py
    def anonymous(func):
        result = func(2, 5)
        print(result)

    def get_sum(x, y):
        return x + y

    anonymous(get_sum) # 输出结果 7
    ```

=== "lambda函数"

    lambda匿名函数 临时使用的函数，只能使用一次

    语法 `lambda 参数 ： 函数体` 传入参数表示匿名函数的形式参数，函数体只能写一行代码

    ```py
    get_sum = lambda x, y : x + y
    print(get_sum(2, 5)) # 输出结果 7
    ```

导入模块

- `import module_name` 通过`module_name.function_name()`使用模块中的函数
- `from module_name import function_0, function_1, function_2` 直接通过`function_0()`使用模块中的函数，这种用法需要防止有函数重名
- `from module_name import function_name as fn` 使用`as`为函数取别名
- `import module_name as mn` 使用`as`为模块取别名
- `from module_name import *` 导入模块中所有函数（不推荐使用）


## 七、文件操作

``` mermaid
graph LR
A[打开文件] --> B{读写文件} ;
B --> C[关闭文件];
```

=== "open函数"

    1. 打开文件
    	- `open(name, mode, encoding)` 函数，返回文件对象，用于打开文件或创建文件
    	- name参数 文件路径字符串
    	- mode参数 文件访问模式
    	- encoding参数 编码方式，推荐使用utf-8

    	???+ note

    		mode参数的可选值

    		- 'r' 只读模式（默认）
    		- 'w' 覆写模式，覆盖文件原有内容，写入新内容。文件不存在时，自动创建文件
    		- 'a' 追加模式，在原文件末尾写入内容。文件不存在时，自动创建文件
    		- 'rb' 使用只读模式打开二进制文件（图片等）
    		- 'wb' 使用覆写模式写入二进制文件
    		- + 配合以上方法使用，在原有功能上增加同时读写功能

    2. 读写文件
    	- `read()`方法 读取文件内容，默认读取全部内容。传入数字可指定读取的字节长度
    	- `readlines()`方法 按行读取，返回列表
    	- `readline()`方法 一次读取一行，此方法和 for i in open()相同，一次读取一行内容
    	- `write()`方法 将内容写入文件
    	- `flush()`方法 刷新内容，使write()函数的内容成功写入文件
    	- `write()`函数将文件内容写到缓冲区，需要使用flush()方法或者close()方法才可以完全写入文件
    	- `writelines()`方法 传入字符串列表，将此列表写入文件
    	- `seek()`方法 传入数字，改变当前文件操作指针的位置，英语占一个字节，GBK编码中文占2个字节，UTF-8编码中文占3个字节

    3. 关闭文件 `close()`方法

    !!! tip

        快捷操作 `with open() as f` 使用with open语句对文件操作结束后，会自动关闭文件

=== "pathlib库"
    
    1. 导入标准库 `pathlib`

            from pathlib import Path   
    2. 创建 `Path` 对象

            path = Path() # 传入文件路径
    3. 对 `Path` 对象进行操作

        `Path` 对象的常用方法：

        - `read_text()` 方法 读取path对象路径文件的所有内容，可选参数encoding指定读取文件使用的编码，常用utf-8
        - `write_text()` 方法 将字符串写入文件，如果指定路径的文件不存在，则会创建它，使用此方法写入时会删除文件原有内容
        - `exists()` 方法 判断文件是否存在

        !!! note

            常和字符串的 `splitlines()` 方法一起使用，按行分割字符串，返回列表

## 八、异常

Python 使用称为异常（exception）的特殊对象来管理程序执行期间发生的错误。

`try except else finally`语句

- `try` 语句 可能引发异常的代码
- `except` 语句 出现异常时，不出现traceback终止程序
    - 捕获一种异常 `except NameError as e:`
    - 捕获多种异常 `except (NameError, ZeroDivisionError):`
    - 捕获所有异常 `except Exception as e:`
- `else` 语句（可选） 不出现异常继续执行的代码
- `finally` 语句（可选） 无论是否异常都要执行的代码

## 九、类和面向对象

[:octicons-arrow-right-24: 详情见GUI/预备节：面向对象](../GUI/tkinter0.md)

此处列举几个典型事例

??? example
    === "示例1"
        ```py title="dog.py" linenums="1"
        class Dog:
            """一个用来表示小狗的类"""

            def __init__(self, name, gender, age):
                # 实例属性
                self.name = name
                self.gender = gender
                self.age = age

            def sit(self):
                # 小狗坐下这种行为
                print(self.name + '坐下来了')
                
            def roll_over(self):
                # 小狗打滚这种行为
                print(self.name + '开始打滚了')
        ```
    
    === "示例2"
        ``` title="car1.py" linenums="1"
        class Car:
            """一个代表汽车的类"""

            def __init__(self, brand, model, year):
                # 汽车的基本信息——品牌，型号，生产年份，里程表示数
                self.brand = brand
                self.model = model
                self.year = year
                self.odometer = 0

            def get_detailed_info(self):
                # 返回一条包含品牌，型号和生产年份的字符串
                return f'这辆车是{self.brand} {self.model}，生产年份是{self.year}。'

            def print_odometer(self):
                # 打印里程表示数
                print(f'这辆汽车总共行驶了{self.odometer}公里。')

            def set_odometer(self, km_mileage):
                # 基本上没有汽车的里程表示数是0，汽车里程表不允许回调
                if km_mileage >= self.odometer:
                    self.odometer = km_mileage
                else:
                    raise ValueError('汽车里程表的示数禁止回调')

            def increse_odometer(self, kilometers):
                # 汽车每次行驶时，里程数都要增加
                self.odometer += kilometers


        class ElectricCar(Car):
            """一个用于表示电动汽车的类，继承自Car"""
            
            def __init__(self, brand, model, year):
                # 继承父类的属性
                super().__init__(brand, model, year)
                self.battery_size = 40

            def print_battery(self):
                # 打印电池容量信息
                print(f'这辆电动汽车的电池容量是{self.battery_size}千瓦时')
        ```
    
    === "示例3"
        ```py title="car2.py" linenums="1"
        class Car:
            """一个代表汽车的类"""

            def __init__(self, brand, model, year):
                # 汽车的基本信息——品牌，型号，生产年份，里程表示数
                self.brand = brand
                self.model = model
                self.year = year
                self.odometer = 0

            def get_detailed_info(self):
                # 返回一条包含品牌，型号和生产年份的字符串
                return f'这辆车是{self.brand} {self.model}，生产年份是{self.year}。'

            def print_odometer(self):
                # 打印里程表示数
                print(f'这辆汽车总共行驶了{self.odometer}公里。')

            def set_odometer(self, km_mileage):
                # 基本上没有汽车的里程表示数是0，汽车里程表不允许回调
                if km_mileage >= self.odometer:
                    self.odometer = km_mileage
                else:
                    raise ValueError('汽车里程表的示数禁止回调')

            def increse_odometer(self, kilometers):
                # 汽车每次行驶时，里程数都要增加
                self.odometer += kilometers


        class Battery:
            """一个表示电动汽车电池的类"""

            def __init__(self, battery_size=40):
                # 实例属性
                self.battery_size = battery_size

            def print_battery(self):
                # 打印电池容量信息
                print(f'这辆电动汽车的电池容量是{self.battery_size}千瓦时')

            def print_battery_km(self):
                # 电池续航能力
                if self.battery_size == 40:
                    distance = 100
                elif self.battery_size == 65:
                    distance = 150
                print(f'充满电，这辆电动汽车可以行驶{distance}公里')



        class ElectricCar(Car):
            """一个用于表示电动汽车的类，继承自Car"""
            
            def __init__(self, brand, model, year):
                # 继承父类的属性
                super().__init__(brand, model, year)
                self.battery = Battery() # 将类作为属性


        my_electric_car = ElectricCar('BYD', 'test', 2025)
        my_electric_car.battery.print_battery() # 输出结果 这辆电动汽车的电池容量是40千瓦时
        my_electric_car.battery.print_battery_km() # 输出结果 充满电，这辆电动汽车可以行驶100公里
        ```


## 十、测试unittest/pytest

可以使用 *标准库unittest* 或 *第三方库pytest* 进行单元测试。一种最简单的测试是单元测试（unit test），用于核实函数的某个方面没有问题。测试用例（test case）是一组单元测试，这些单元测试一道核实函数在各种情况下的行为都符合要求。良好的测试用例考虑到了函数可能收到的各种输入，包含针对所有这些情况的测试。全覆盖（full coverage）测试用例包含一整套单元测试，涵盖了各种可能的函数使用方式。

使用 pytest 进行测试，会让单元测试编写起来非常简单。我们将编写一个测试函数，它会调用要测试的函数，并做出有关返回值的断言 （`assert` 语句）。如果断言正确，表示测试通过；如果断言不正确，表示测试未通过。

测试函数和测试文件必须以 `test_` 开头

几种常用的断言（类似于if语句的条件判断）：

| unittest断言 | pytest断言 | 用途 |
|:---:|:---:|:---|
| assertEqual(a, b) | assert a == b | 断言两个值相等 |
| assertNotEqual(a, b) | assert a != b | 断言两个值不等 |
| assertTrue(a) | assert a | 断言 a 的布尔求值为 True |
| assertFalse(a) | assert not a | 断言 a 的布尔求值为 False |
| assertIn(element, list) | assert element in list | 断言元素在列表中 |
| assertNotIn(element, list) | assert element not in list | 断言元素不在列表中 |

### 10.1 对函数进行单元测试

需要被测试的函数：

```py title="demo/name_func.py" linenums="1"
def get_format_name(first, last):
    """返回完整格式的姓名"""
    return first + ' ' + last


"""手动测试"""
print('输入q结束程序')
while True:
    first_name = input('输入你的名： ')
    if first_name == 'q':
        break
    last_name = input('输入你的姓： ')
    if last_name == 'q':
        break
    full_name = get_format_name(first_name, last_name)
    print(f'你的全名是 {full_name}')
```

测试函数

!!! warning
    测试文件和被测试文件要放在同一个目录下，此处都放置在 `c:/desktop/demo` 目录下。
=== "pytest"
    ```py title="demo/test_name_func.py" linenums="1"
    from name_func import get_format_name

    def test_first_last_name():
        """这个测试函数用于测试 Tom White 格式的全名"""
        full_name = get_format_name('Tom', 'White')
        assert full_name == 'Tom White'
    ```

    运行测试

    === "cmd/powershell"
        先使用 `cd` 或 `pushd` 命令将目录切换到 `demo` 目录，再输入 `pytest`，如果输入 `pytest` 不起作用，可是输入 `python -m pytest`
        ```cmd
        
        C:\Users\86183>cd c:/desktop/demo

        c:\Desktop\demo>pytest
        ================================================= test session starts =================================================
        platform win32 -- Python 3.12.1, pytest-8.2.2, pluggy-1.5.0
        rootdir: c:\Desktop\demo
        collected 1 item

        test_name_func.py .                                                                                              [100%]

        ================================================== 1 passed in 0.02s ==================================================
        ```

    === "VS Code/Pycharm"
        直接在内置的终端中输入 `pytest`
        
        ```powershell
        PS C:\Desktop\demo> pytest
        ========================================== test session starts ==========================================
        platform win32 -- Python 3.12.1, pytest-8.2.2, pluggy-1.5.0
        test_name_func.py .                                                                                [100%]    

        =========================================== 1 passed in 0.01s ===========================================    
        ```

=== "unittest"
    ```py title="demo/test_name_func.py" linenums="1"
    import unittest
    from name_func import get_format_name


    class NameTestCasse(unittest.TestCase):
        """用于测试name_func.py的类"""

        def test_first_last_name(self):
            """这个测试函数用于测试 Tom White 格式的全名"""
            full_name = get_format_name('Tom', 'White')
            self.assertEqual(full_name, 'Tom White') # 断言

    if __name__ == '__main__': 
        unittest.main()
    ```
    !!! note
        `if __name__ == '__main__':` 语句中的特殊变量 `__name__` 只有当这个文件作为程序的主文件执行时，才会返回 `__main__` ，如果将此文件作为模块导入的话，此语句之后的代码都不会被执行。

    运行测试：

    ```cmd
    C:\Users\86183>python C:\Desktop\demo\test_name_func.py
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.000s

    OK
    ```


如果我们修改被测试函数，使它能够处理有中间名的姓名：

```py title="demo/name_func.py" linenums="1"
def get_format_name(first, middle, last):
    """返回完整格式的姓名"""
    return first + ' ' + middle + ' ' + last
```

此时运行测试，测试将不会通过：

=== "pytest"
    ```cmd
    C:\Desktop\demo>pytest
    =========================================== test session starts ============================================
    platform win32 -- Python 3.12.1, pytest-8.2.2, pluggy-1.5.0
    rootdir: C:\Desktop\demo
    collected 1 item                                                                                             

    test_name_func.py F                                                                                   [100%]

    ================================================= FAILURES ================================================= 
    ___________________________________________ test_first_last_name ___________________________________________ 

    >   ???
    E   TypeError: get_format_name() missing 1 required positional argument: 'last'

    C:\Desktop\新建文件夹\test_name_func.py:6: TypeError
    ========================================= short test summary info ========================================== 
    FAILED test_name_func.py::test_first_last_name - TypeError: get_format_name() missing 1 required positional argument: 'last'
    ============================================ 1 failed in 0.06s ============================================= 
    ```

=== "unittest"
    ```cmd
    C:\Users\86183>python C:\Desktop\demo\test_name_func.py
    E
    ======================================================================
    ERROR: test_first_last_name (__main__.NameTestCasse.test_first_last_name)
    这个测试函数用于测试 Tom White 格式的全名
    ----------------------------------------------------------------------
    Traceback (most recent call last):
    File "C:\Desktop\demo\test_name_func.py", line 24, in test_first_last_name
        full_name = get_format_name('Tom', 'White')
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    TypeError: get_format_name() missing 1 required positional argument: 'last'

    ----------------------------------------------------------------------
    Ran 1 test in 0.000s

    FAILED (errors=1)
    ```

测试不通过，说明我们编写的用于获取全名的函数 `name_func()` 并没有完成我们预期的行为：将只有姓和名的名字合成为全名，以及将有姓、名以及中间名的名字合成为全名。这种情况下我们应该修改 `name_func()` 这个函数，而不是修改测试。

修改后的 `demo/name_func.py`

```py title="demo/name_func.py" linenums="1"
def get_format_name(first, last, middle=''):
    """返回完整格式的姓名"""
    if middle:
        return first + ' ' + middle + ' ' + last
    else:
        return first + ' ' + last
```

此时运行测试，测试将通过。但是我们编写的测试函数只会测试只有姓和名的情况，并不会测试有中间名的情况，因此我们要添加一个用于测试含有中间名名字的测试。

在 `demo/test_name_func.py` 中添加以下代码

=== "pytest"
    ```py title="demo/test_name_func.py" linenums="8"
    # -- snip --
    def test_first_last_middle_name():
        """用于测试 Tom Walt White 格式的全名"""
        full_name = get_format_name('Tom', 'White', middle='Walt')
        assert full_name == 'Tom Walt White'
    ```

    此时运行测试，测试将通过：

    ```cmd
    PS C:\Desktop\demo> pytest
    =========================================== test session starts ============================================
    platform win32 -- Python 3.12.1, pytest-8.2.2, pluggy-1.5.0
    rootdir: C:\Desktop\demo
    collected 2 items                                                                                            

    test_name_func.py ..                                                                                  [100%] 

    ============================================ 2 passed in 0.02s ============================================= 
    ```

=== "unittest"
    ```py title="demo/test_name_func.py"
    # -- snip --
    class NameTestCasse(unittest.TestCase):
        # -- snip --
        def test_first_last_middle_name(self):
            """用于测试 Tom Walt White 格式的全名"""
            full_name = get_format_name('Tom', 'White', middle='Walt')
            self.assertEqual(full_name, 'Tom Walt White')
    # -- snip --
    ```

    此时运行测试：

    ```cmd
    C:\Users\86183>python C:\Desktop\demo\test_name_func.py
    ..
    ----------------------------------------------------------------------
    Ran 2 tests in 0.000s

    OK
    ```

### 10.2 对类进行单元测试

一个需要被测试的类

```py title="demo/survey.py" linenums="1"
class AnonymousSurvey:
    """一个表示匿名问卷的类"""
    def __init__(self, question):
        self.question = question
        self.answers = []

    def print_question(self):
        """将问卷的问题打印在屏幕上"""
        print(self.question)

    def store_answer(self, answer):
        """收集单份问卷的答案"""
        self.answers.append(answer)

    def print_answers(self):
        print('这个问题得到的答案是：')
        for index, answer in enumerate(self.answers, start=1):
            print(index, answer)

"""以下代码在使用pytest测试时请删除"""
"""手动测试"""
# 创建一个AnonymousSurvey实例对象
question = '你会什么编程语言或标记语言？'
my_survey = AnonymousSurvey(question)
my_survey.print_question()
while True:
    answer = input('输入你的答案，输入q停止： ')
    if answer == 'q':
        break
    my_survey.store_answer(answer)
my_survey.print_answers()
```

编写测试函数：

=== "pytest"
    ```py title="demo/test_survey.py" linenums="1"
    from survey import AnonymousSurvey

    def test_store_1_answer():
        """测试只回答1个答案的情况"""
        question = '你会什么编程语言或标记语言？'
        my_survey = AnonymousSurvey(question)
        my_survey.store_answer('C')
        assert 'C' in my_survey.answers

    def test_store_3_answers():
        """测试回答3个答案的情况"""
        question = '你会什么编程语言或标记语言？'
        my_survey = AnonymousSurvey(question)
        answers = ['html', 'css', 'javascripts']
        for answer in answers:
            my_survey.store_answer(answer)
        for answer in answers:
            assert answer in my_survey.answers
    ```

    上面的代码每个测试函数都分别创建了一个AnonymousSurvey实例，显得非常繁琐。

    在测试中，夹具（fixture）可帮助我们搭建测试环境。这通常意味着创建供多个测试使用的资源。在 pytest 中，要创建夹具，可编写一个使用装饰器 @pytest.fixture装饰的函数。装饰器（decorator）是放在函数定义前面的指令。在运行函数前，Python将该指令应用于函数，以修改函数代码的行为。

    使用夹具简化后的测试：

    ```py title="demo/survey.py" linenums="1"
    from survey import AnonymousSurvey
    import pytest


    @pytest.fixture
    def my_survey():
        """一个可供所有测试函数使用的 AnonymousSurvey 实例"""
        question = '你会什么编程语言或标记语言？'
        my_survey = AnonymousSurvey(question)
        return my_survey

    def test_store_1_answer(my_survey):
        """测试只回答1个答案的情况"""
        my_survey.store_answer('C')
        assert 'C' in my_survey.answers

    def test_store_3_answers(my_survey):
        """测试回答3个答案的情况"""
        answers = ['html', 'css', 'javascripts']
        for answer in answers:
            my_survey.store_answer(answer)
        for answer in answers:
            assert answer in my_survey.answers
    ```


=== "unittest"
    ```py title="demo/test_survey.py" linenums="1"
    from survey import AnonymousSurvey
    import unittest

    class TestAnonymousSurvey(unittest.TestCase):
        """用于测试AnonymousSurvey类的类"""

        def test_store_1_answer(self):
            """测试只回答1个答案的情况"""
            question = '你会什么编程语言或标记语言？'
            my_survey = AnonymousSurvey(question)
            my_survey.store_answer('C')
            self.assertIn('C', my_survey.answers)

        def test_store_3_answers(self):
            """测试回答3个答案的情况"""
            question = '你会什么编程语言或标记语言？'
            my_survey = AnonymousSurvey(question)
            answers = ['html', 'css', 'javascripts']
            for answer in answers:
                my_survey.store_answer(answer)
            for answer in answers:
                self.assertIn(answer, my_survey.answers)

    if __name__ == '__main__':
    unittest.main()
    ```

    上面的代码每个测试函数都分别创建了一个AnonymousSurvey实例，显得非常繁琐。

    使用 `TestCase` 类中的 `setUp()` 方法可以简化。

    ```py title="demo/test_survey.py" linenums="1"
    from survey import AnonymousSurvey
    import unittest

    class TestAnonymousSurvey(unittest.TestCase):
        """用于测试AnonymousSurvey类的类"""

        def setUp(self):
            """创建一个问卷调查对象和一组答案"""
            question = '你会什么编程语言或标记语言？'
            self.my_survey = AnonymousSurvey(question)
            self.answers = ['html', 'css', 'javascripts']

        def test_store_1_answer(self):
            """测试只回答1个答案的情况"""
            self.my_survey.store_answer(self.answers[0])
            self.assertIn(self.answers[0], self.my_survey.answers)

        def test_store_3_answers(self):
            """测试回答3个答案的情况"""
            for answer in self.answers:
                self.my_survey.store_answer(answer)
            for answer in self.answers:
                self.assertIn(answer, self.my_survey.answers)

    if __name__ == '__main__':
        unittest.main()
    ```

!!! note
    虽然上面的测试看起来比之前的测试代码要长一些，但是修改后的代码逻辑性更好，也更容易理解。

## 十一、标准库

json库 用于存储数据和处理json数据。模块 json 让你能很容易地将 Python 数据结构转换为 JSON 格式的字符串，并在程序再次运行时从文件中加载数据。	列表和字典都可以转换成json数据

- `json.dumps()`函数 将python数据转换为json数据，可以配合pathlib库使用，将pyhon数据转换为json数据，并写入json文件中
- `json.loads()`函数 读取数据，将json数据转换为python数据

random库 与随机有关的库

- random.randint(start, end)函数 随机生成两个数之间的随机数，闭区间
- random.choice(lst)函数，随机返回传入的列表中的一个元素