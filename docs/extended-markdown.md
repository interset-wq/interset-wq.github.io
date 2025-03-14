---
title: Markdown 扩展语法
comments: true
icon: material/emoticon-happy-outline
status:  new # deprecated # new
description: 适用于 mkdocs 的 markdown 扩展语法
subtitle: Markdown 语法
---

# Markdown 扩展语法

## 一、告诫

支持嵌套使用。

常用的告诫有：`note` `abstract` `info` `tip` `success` `question` `warning` `failure` `danger` `bug` `example` `quote`

### 1.1 写法一

输入以下代码：

    !!! note

        这是一个 note

你可以看到：

!!! note

    这是一个 note

### 1.2 写法二

输入以下代码：

    !!! note "注意"

        这是一个 note

你可以看到：

!!! note "注意"

    这是一个 note

### 1.3 写法三

输入以下代码：

    !!! note ""

        这是一个 note

你可以看到：

!!! note ""

    这是一个 note

### 1.4 写法四

输入以下代码：

    ??? note

        这是一个 note

你可以看到：

??? note

    这是一个 note

### 1.5 写法五

输入以下代码：

    ???+ note

        这是一个 note

你可以看到：

???+ note

    这是一个 note

### 1.6 写法六

输入以下代码：

    !!! info inline end 

        这是一个 info

你可以看到：

!!! info inline end 

    这是一个 info

### 1.7 写法七

输入以下代码：

    !!! info inline 

        这是一个 info

你可以看到：

!!! info inline 

    这是一个 info

----

## 二、注释

使用`(1)`格式的编号来注释，注释的文字写在 `{ .annotate }` 后面的有序列表中

输入以下代码：

    你可以通过邮箱(1)来联系我。
    { .annotate }

    1. <d111kc@foxmail.com>

你可以看到：

你可以通过邮箱(1)来联系我。
 { .annotate }

 1. <d111kc@foxmail.com>

## 三、按钮

将超链接显示为按钮，小括号中写链接地址，花括号中控制按钮样式

输入以下代码：

    [回到顶部](#){ .md-button }

    [前往Python官网](https://www.python.org/){ .md-button .md-button--primary }

你可以看到：

[回到顶部](#){ .md-button }

[前往Python官网](https://www.python.org/){ .md-button .md-button--primary }

## 四、代码块

带标题的围栏代码块，使用 `title` 添加文件名， `linenums` 添加行号，`hl_lines` 突出显示某行

输入以下代码：

    ``` py title="hello.py" linenums="1" hl_lines="1 2"
    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    label = ttk.Label(root, text='hello tkinter')
    label.pack()
    root.mainloop()
    ```

你可以看到：

``` py title="hello.py" linenums="1" hl_lines="1 2"
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
label = ttk.Label(root, text='hello tkinter')
label.pack()
root.mainloop()
```

## 五、选项卡

### 5.1 对代码块使用

输入以下代码：

    === "C"

        ``` c
        #include <stdio.h>

        int main(void) {
        printf("Hello world!\n");
        return 0;
        }
        ```

    === "C++"

        ``` c++
        #include <iostream>

        int main(void) {
        std::cout << "Hello world!" << std::endl;
        return 0;
        }
        ```

你可以看到：

=== "C"

    ``` c
    #include <stdio.h>

    int main(void) {
      printf("Hello world!\n");
      return 0;
    }
    ```

=== "C++"

    ``` c++
    #include <iostream>

    int main(void) {
      std::cout << "Hello world!" << std::endl;
      return 0;
    }
    ```

### 5.2 对其他内容使用

输入以下代码：

    === "无序列表"

        * c
        * python
        * go

    === "有序列表"

        1. 青少年
        2. 中年
        3. 老年

你可以看到：

=== "无序列表"

     * c
     * python
     * go

=== "有序列表"

     1. 青少年
     2. 中年
     3. 老年

## 六、图形Mermaid

### 6.1 流程图

输入以下代码：

    ``` mermaid
    graph LR
    A[开始] --> B{出错?};
    B -->|是| C[认真思考...];
    C --> D[调试];
    D --> B;
    B ---->|否| E[输出结果!];
    ```

你可以看到：

``` mermaid
graph LR
  A[开始] --> B{出错?};
  B -->|是| C[认真思考...];
  C --> D[调试];
  D --> B;
  B ---->|否| E[输出结果!];
```

### 6.2 序列图

输入以下代码：

    ``` mermaid
    sequenceDiagram
    autonumber
    Alice->>John: Hello John, how are you?
    loop Healthcheck
        John->>John: Fight against hypochondria
    end
    Note right of John: Rational thoughts!
    John-->>Alice: Great!
    John->>Bob: How about you?
    Bob-->>John: Jolly good!
    ```

你可以看到：

``` mermaid
sequenceDiagram
  autonumber
  Alice->>John: Hello John, how are you?
  loop Healthcheck
      John->>John: Fight against hypochondria
  end
  Note right of John: Rational thoughts!
  John-->>Alice: Great!
  John->>Bob: How about you?
  Bob-->>John: Jolly good!
```

### 6.3 状态图

输入以下代码：

    ``` mermaid
    stateDiagram-v2
    state fork_state <<fork>>
        [*] --> fork_state
        fork_state --> State2
        fork_state --> State3

        state join_state <<join>>
        State2 --> join_state
        State3 --> join_state
        join_state --> State4
        State4 --> [*]
    ```

你可以看到：

``` mermaid
stateDiagram-v2
  state fork_state <<fork>>
    [*] --> fork_state
    fork_state --> State2
    fork_state --> State3

    state join_state <<join>>
    State2 --> join_state
    State3 --> join_state
    join_state --> State4
    State4 --> [*]
```

### 6.4 类图

输入以下代码：

    ``` mermaid
    classDiagram
    Person <|-- Student
    Person <|-- Professor
    Person : +String name
    Person : +String phoneNumber
    Person : +String emailAddress
    Person: +purchaseParkingPass()
    Address "1" <-- "0..1" Person:lives at
    class Student{
        +int studentNumber
        +int averageMark
        +isEligibleToEnrol()
        +getSeminarsTaken()
    }
    class Professor{
        +int salary
    }
    class Address{
        +String street
        +String city
        +String state
        +int postalCode
        +String country
        -validate()
        +outputAsLabel()  
    }
    ```

你可以看到：

``` mermaid
classDiagram
  Person <|-- Student
  Person <|-- Professor
  Person : +String name
  Person : +String phoneNumber
  Person : +String emailAddress
  Person: +purchaseParkingPass()
  Address "1" <-- "0..1" Person:lives at
  class Student{
    +int studentNumber
    +int averageMark
    +isEligibleToEnrol()
    +getSeminarsTaken()
  }
  class Professor{
    +int salary
  }
  class Address{
    +String street
    +String city
    +String state
    +int postalCode
    +String country
    -validate()
    +outputAsLabel()  
  }
```

### 6.5 实体关系图

输入以下代码：

    ``` mermaid
    erDiagram
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ LINE-ITEM : contains
    LINE-ITEM {
        string name
        int pricePerUnit
    }
    CUSTOMER }|..|{ DELIVERY-ADDRESS : uses
    ```

你可以看到：

``` mermaid
erDiagram
  CUSTOMER ||--o{ ORDER : places
  ORDER ||--|{ LINE-ITEM : contains
  LINE-ITEM {
    string name
    int pricePerUnit
  }
  CUSTOMER }|..|{ DELIVERY-ADDRESS : uses
```

## 七、脚注

输入以下代码：

    Tkinter[^1] 是python标准库之一，著名的 idle[^2] 就是使用它制作的。

    [^1]: Tkinter的小部件比较老旧，一般使用ttk来美化。

    [^2]:
        Idle 是 python 自带的代码编辑器，非常适合初学者使用。

你可以看到：

 Tkinter[^1] 是python标准库之一，著名的 idle[^2] 就是使用它制作的。

 [^1]: Tkinter的小部件比较老旧，一般使用ttk来美化。

 [^2]:
     Idle 是 python 自带的代码编辑器，非常适合初学者使用。

## 八、更多文字样式

### 8.1 示例

输入以下代码：

 ```
 文字可以使用 {--带底纹删除线--} 和 {++带底纹下划线++} 。 它们也可以放在一起使用 {~~一个~>示例~~} 。 为文字添加底纹表示 {==强调==} 这个文字 {>>添加JS风格的注释<<} 。

 {==

 为一整段文字添加底纹。

 ==}
 ```

你可以看到：

文字可以使用 {--带底纹删除线--} 和 {++带底纹下划线++} 。 它们也可以放在一起使用 {~~一个~>示例~~} 。 为文字添加底纹表示 {==强调==} 这个文字 {>>添加JS风格的注释<<} 。

{==

为一整段文字添加底纹。

==}

### 8.2 底纹、下划线、删除线

也可以直接使用html语法表示

输入以下代码：

    ==底纹==

    ^^下划线^^

    ~~删除线~~

你可以看到：

==底纹==

^^下划线^^

~~删除线~~

### 8.3 上下标

也可以使用html语法表示

输入以下代码：

    H~2~O

    m^2^

你可以看到：

H~2~O

m^2^

### 8.4 键盘按键

输入以下代码：

    ++ctrl++

    ++alt++

    ++del++

    ++enter++

    ++f5++

    ++backspace++

你可以看到：

++ctrl++

++alt++

++del++

++enter++

++f5++

++backspace++

## 九、网格

本质上是html语法

### 9.1 简单网格

输入以下代码：

    <div class="grid cards" markdown>

    - :fontawesome-brands-html5: __HTML__ 决定网页的结构和内容
    - :fontawesome-brands-js: __JavaScript__ 用于用户交互和动态效果
    - :fontawesome-brands-css3: __CSS__ 设定网页的样式
    - :fontawesome-brands-internet-explorer: __Internet Explorer__ 呃……我不认识前面三位

    </div>

你可以看到：

<div class="grid cards" markdown>

- :fontawesome-brands-html5: __HTML__ 决定网页的结构和内容
- :fontawesome-brands-js: __JavaScript__ 用于用户交互和动态效果
- :fontawesome-brands-css3: __CSS__ 设定网页的样式
- :fontawesome-brands-internet-explorer: __Internet Explorer__ 呃……我不认识前面三位

</div>

### 9.2 复杂网格

输入以下代码：

    <div class="grid cards" markdown>

    -   :fontawesome-brands-html5:{ .lg .middle } __HTML__

        ---

        决定网页的结构和内容

        [:octicons-arrow-right-24: 前往MDN查阅HTML](https://developer.mozilla.org/zh-CN/docs/Web/HTML)

    -   :fontawesome-brands-js:{ .lg .middle } __JavaScript__

        ---

        用于用户交互和动态效果

        [:octicons-arrow-right-24: 前往MDN查看JS](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript)

    -   :fontawesome-brands-css3:{ .lg .middle } __CSS__

        ---

        设定网页的样式

        [:octicons-arrow-right-24: 前往MDN查看CSS](https://developer.mozilla.org/zh-CN/docs/Web/CSS)

    -   :simple-mdnwebdocs:{ .lg .middle } __MDN__

        ---

        权威的 `HTML` `CSS` `JavaScript` 文档

        [:octicons-arrow-right-24: 去MDN官网](https://developer.mozilla.org/zh-CN/)

    </div>

你可以看到：

<div class="grid cards" markdown>

-   :fontawesome-brands-html5:{ .lg .middle } __HTML__

    ---

    决定网页的结构和内容

    [:octicons-arrow-right-24: 前往MDN查阅HTML](https://developer.mozilla.org/zh-CN/docs/Web/HTML)

-   :fontawesome-brands-js:{ .lg .middle } __JavaScript__

    ---

    用于用户交互和动态效果

    [:octicons-arrow-right-24: 前往MDN查看JS](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript)

-   :fontawesome-brands-css3:{ .lg .middle } __CSS__

    ---

    设定网页的样式

    [:octicons-arrow-right-24: 前往MDN查看CSS](https://developer.mozilla.org/zh-CN/docs/Web/CSS)

-   :simple-mdnwebdocs:{ .lg .middle } __MDN__

    ---

    权威的 `HTML` `CSS` `JavaScript` 文档

    [:octicons-arrow-right-24: 去MDN官网](https://developer.mozilla.org/zh-CN/)

</div>

### 9.3 通用轴网

输入以下代码：

    <div class="grid" markdown>

    === "无序列表"

        - c
        - python
        - java

    === "有序列表"

        1. 英语四级
        2. 英语六级

    ``` title="代码块"
    === "无序列表"

        - c
        - python
        - java

    === "有序列表"

        1. 英语四级
        2. 英语六级
    ```

    </div>

你可以看到：

<div class="grid" markdown>

=== "无序列表"

    - c
    - python
    - java

=== "有序列表"

    1. 英语四级
    2. 英语六级

``` title="代码块"
=== "无序列表"

    - c
    - python
    - java

=== "有序列表"

    1. 英语四级
    2. 英语六级
```

</div>

## 十、图标和表情符号

### 10.1 表情符号

输入以下代码：

    :smile:

你可以看到：

:smile:

### 10.2 图标

输入以下代码：

    :fontawesome-regular-face-laugh-wink:

你可以看到：

:fontawesome-regular-face-laugh-wink:

## 十一、图片优化

### 11.1 对齐方式

使用 `align` 指定图片对齐方式，是否有效取决于图片大小和屏幕大小

输入以下代码：

    ![图片](https://dummyimage.com/300x200/eee/aaa){ align=right }

    Lorem ipsum dolor sit amet， consectetur adipiscing elit.Nulla et euismod nulla.

你可以看到：

![图片](https://dummyimage.com/300x200/eee/aaa){ align=right }

Lorem ipsum dolor sit amet， consectetur adipiscing elit.Nulla et euismod nulla.


### 11.2 懒加载

使用 `loading=lazy` 设置图片懒加载

输入以下代码：

    ![Image title](https://www.dmoe.cc/random.php){ loading=lazy }

你可以看到：

![Image title](https://www.dmoe.cc/random.php){ loading=lazy }

## 十二、列表优化

### 12.1 自定义列表

输入以下代码：

    :fontawesome-brands-internet-explorer:  `Internet Explorer`

    :   曾经是世界上最好用的浏览器，后来被 :simple-firefox: `FireFox` 和 :material-google-chrome: `Chrome` 超越，最后 :material-microsoft: `Microsoft` 放弃了对其的开发。

    :material-microsoft-edge: `Edge`

    :   :fontawesome-brands-windows: `Windows11` 的默认浏览器。

        有着优于 :fontawesome-brands-internet-explorer:  `Internet Explorer` 的性能，同时保留了一些兼容IE的功能。

你可以看到：

:fontawesome-brands-internet-explorer:  `Internet Explorer`

:   曾经是世界上最好用的浏览器，后来被 :simple-firefox: `FireFox` 和 :material-google-chrome: `Chrome` 超越，最后 :material-microsoft: `Microsoft` 放弃了对其的开发。

:material-microsoft-edge: `Edge`

:   :fontawesome-brands-windows: `Windows11` 的默认浏览器。

    有着优于 :fontawesome-brands-internet-explorer:  `Internet Explorer` 的性能，同时保留了一些兼容IE的功能。

### 12.2 任务列表

输入以下代码：

    - [x] Python
    - [ ] JavaScript
          * [x] node.js
          * [ ] vue.js
          * [ ] react.js
    - [ ] Java

你可以看到：

- [x] Python
- [ ] JavaScript
    * [x] node.js
    * [ ] vue.js
    * [ ] react.js
- [ ] Java

## 十三、数学公式 KaTeX

输入以下代码：

    $$
    \cos x=\sum_{k=0}^{\infty}\frac{(-1)^k}{(2k)!}x^{2k}
    $$

你可以看到：

$$
\cos x=\sum_{k=0}^{\infty}\frac{(-1)^k}{(2k)!}x^{2k}
$$