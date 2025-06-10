---
comments: true
icon: material/language-python
# status: new
title: bs4
subtitle: 解析网页
---

:material-pen-plus: `本文创建于2025-4-12`

[bs4官方文档](https://beautifulsoup.readthedocs.io/zh-cn/v4.4.0/){ .md-button .md-button--primary }

## 第一步：创建soup对象

`BeautifulSoup()` 类

- 第一个参数是html格式的文本，常传入 `res.text`
- 第二个位置参数是解析器，常使用 `"lxml"`
- 关键字参数 `multi_valued_attributes` （默认按照html语法规范解析，不推荐使用此参数修改配置）
    - `multi_valued_attributes=None` ，将所有html标签的属性当做是单值属性解析
    - `multi_valued_attributes=class_is_multi` ，将所有属性当做多值属性解析


常用的解析器：

- html.parser解析器（属于python标准库） `BeautifulSoup(res.text, "html.parser")`
    - Python的内置标准库
    - 执行速度较快
    - 容错能力强
    - 速度没有 lxml 快，容错没有 html5lib强
- lxml HTML解析器（第三方库，推荐使用） `BeautifulSoup(res.text, "lxml")`
    - 速度快
    - 容错能力强	
    - 额外的 C 依赖
- lxml XML解析器（第三方库） `BeautifulSoup(markup, ["lxml-xml"])` 或 `BeautifulSoup(markup, "xml")`
    - 速度快
    - 唯一支持 XML 的解析器	
    - 额外的 C 依赖
    - 使用此解析器，所有属性当做是单值属性解析
- html5lib解析器（第三方库） `BeautifulSoup(markup, "html5lib")`
    - 最好的容错性
    - 以浏览器的方式解析文档
    - 生成 HTML5 格式的文档
    - 速度慢
    - 额外的 Python 依赖

```py
import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:5500/docs/demos/bs4-demo.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0',
}

res = requests.get(url=url, headers=headers)
# res.encoding = 'utf-8'
# print(res.text)

# 创建soup对象
soup = BeautifulSoup(res.text, 'lxml')
```

## 第二步：对soup对象进行操作

```py
# print(soup.prettify())
# 获取html的title标签，即浏览器标签页标题
# print(soup.title)
# 获取title标签的标签名（这个属性有些鸡肋）
# print(soup.title.name)
# 获取title标签的文字
# print(soup.title.string)
# 获取title标签的父标签
# print(soup.title.parent)
# 获取title标签的父标签名
# print(soup.title.parent.name)
# 获取第一个h2标签
# print(soup.h2)
# 获取第一个h2标签的id
# print(soup.h2['id'])
# print(soup.h2.get('id'))
# 获取第一个h2标签的所有属性
# print(soup.h2.attrs)
# 获取第一个h2标签的class属性，由于class多值属性，返回列表
# print(soup.h2['class']) # 或使用get()方法
# print(soup.h2.get('class'))
# 获取所有的h2标签，返回列表
# print(soup.find_all('h2'))
# 获取id值是author的标签，返回列表（注意class不能使用这种用法）
# print(soup.find_all(id='author'))
# 获取网页所有的文本内容
# print(soup.get_text())
```

soup对象的属性和方法：

- 所有html标签都可以看做是soup对象的属性，`soup.标签` 相当于对soup对象使用了元素选择器，且只选中 {==第一个==} 匹配到的对象，返回tag对象，以下是tag对象的属性和方法（soup对象支持大多数tag对象的属性和方法）
    
    ???+ note "子节点"
        tag 可能包含多个字符串或其它的 tag，这些都是这个 Tag 的子节点。

    - `name` 属性，用于获取标签名（有些鸡肋），可以对其重新赋值，并会对tag对象产生影响（改变html元素的标签），对子节点使用时，如果子节点是字符串，则返回None
    - `string` 属性，用于获取标签包裹的文字，返回NavigableString 对象，使用str()函数可以将NavigableString 对象转换成python字符串，如果tag对象中还嵌套了其他html标签（子节点），返回None。NavigableString 对象的属性和方法如下：
        - `replace_with()` 方法 将NavigableString 对象中的字符串替换为传入的字符串
    - `attrs` 属性，返回所有属性的字典，属性名作为键，属性值作为值，多值属性（如class）的值用字典表示
    - `contents` 属性，返回tag对象所有节点的列表
    - `tag['key']` 字典操作，可以把tag对象的名称当做是字典的变量名，这个字典实际上就是 `tag.attrs`，tag对象 的属性可以被添加、删除或修改。tag的属性操作方法与字典一样
    - `get_attribute_list()`方法 传入属性名，返回属性值列表，单值属性（id等单值属性，即使因为书写不规范导致属性值之间有空格，仍然返回单元素列表）返回单元素列表
- `find_all()` 方法 传入html标签，返回所有匹配的列表，tag对象也可以使用
- `prettify()` 方法 类似于 `pprint.pprint()` 格式化soup对象，增加可读性


## find_all()方法

标准写法：

`find_all(name , attrs , recursive , string , **kwargs)`

简写：可以将soup或tag对象的对象名直接当成是函数使用，它们的用法和find_all()方法完全相同

`tag(name , attrs , recursive , string , **kwargs)`

`soup(name , attrs , recursive , string , **kwargs)`

各参数说明：

- name参数（常使用位置参数传入），返回tag对象列表，参数值如下
    - 标签名，传入html标签名
    - 列表，传入html标签名列表，匹配列表中的所有标签的tag对象
    - 正则表达式，需要先导入re，传入 `re.compile("正则表达式")`，匹配所有符合要求的tag对象
    - 函数名，自定义函数
    - 字符串
    - True，可以匹配任何值，查找到所有的 tag，但是不会返回字符串节点
- 关键字参数**kwargs，常用关键字参数如下：
    - `id="id值"` 通过id查找tag对象
    - `id=True` 查找所有带有id属性的参数的tag对象
    - `href=re.compile("正则表达式")` 查找所有带有href属性并符合匹配的tag对象
    - `class_="类名"` 通过类名查找tag对象
    - `limit=数字` 限制查找的tag对象的个数
- attrs参数（常作为关键字参数使用），`attrs={"属性名": "属性值"}`，以字典的方式传入属性名和属性值，查找对应的tag对象
- `recursive=False` 设置此参数只查找子节点，默认查找所有后代节点
- string参数（常作为关键字参数传入），用法和name参数类似，只是针对的是html中的文本来进行查找，而不是针对标签

## find()方法

用法和find_all()相同，只查找第一个tag对象，返回tag对象

## css选择器进行查找

`css.select("css选择器")` 方法 使用css选择器查找，返回tag对象列表

`select()` 和 `select_one()`方法，两个方法作用相同，与`css.select()`用法相同，值查找第一个匹配到的tag对象，返回tag对象