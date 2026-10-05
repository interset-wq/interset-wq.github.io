# re 正则表达式Regular Expression

[re官方文档](https://docs.python.org/zh-cn/3/library/re.html)

[正则表达式指南](https://docs.python.org/zh-cn/3/howto/regex.html)

## 正则表达式匹配模式

- `[]` 匹配其中之一,例如 `ma[dnt]` 匹配 `mad` , `man` 或 `mat`, `[a-d3-6]` 表示 `[a-d]` 和 `[3-6]` 的结合,即 `[abcd3456]`
- `-` 到,例如 `a-d` 相当于 `abcd`, `0-9` 相当于 `0123456789`
- `^` 否定,例如 `[^abc]`匹配不在方括号内的任意字符
- `.` 任意单个字符(换行符除外)
- `+` 匹配一次或多次前面的分组
- `\` 转义字符,要匹配 `+`,需要使用 `\+`
- `r` 纯字符串(raw string),用法类似于f-string,并且可以和f-string一起使用,纯字符串情况下,所有特殊字符被当作普通字符看待,此时不需要使用转义字符
- ?匹配零次或一次前面的分组.
- *匹配零次或多次前面的分组.
- {n}匹配n次前面的分组.
- {n,}匹配n次或更多前面的分组.
- {,m}匹配零次到m次前面的分组.
- {n,m}匹配至少n次、至多m次前面的分组.
- {n,m}?或*?或+?对前面的分组进行非贪心匹配.
- ^spam意味着字符串必须以spam开始.
- spam$意味着字符串必须以spam结束.

## 常用缩写

- `\d` 单个数字字符,相当于 `[0-9]`
- `\D` 单个非数字字符,相当于 `[^0-9]`
- `\w` 单个字母/数字/下划线字符,相当于 `[a-zA-Z0-9_]`
- `\W` 单个非字母/数字/下划线的字符,相当于 `[^a-zA-Z0-9_]`
- `\s` 单个空白字符,相当于 `[ \t\n\r\v\f]`
- `\S` 单个非空白字符,相当于 `[^ \t\n\r\v\f]`

## 函数式编程和面向对象编程

search和findall可以使用函数,也可以使用方法进行匹配.两种写法差别不大,代码量也没有很大区别.

- search 只匹配第一个符合匹配模式的字符串,返回Match对象
- findall 匹配所有符合匹配模式的字符串,返回 `list[str]` 对象

绝大多数情况下,findall明显比search更好用

search和findall的函数式写法和方法式写法并没有太大的差别,只是采用了不同的编程思想——函数式编程和面向对象编程.

### search

=== "方法"
    ```python
    import re
    my_str = 'Math is intresting, and I like learing mathmatics.'
    pattern = re.compile('ma')
    match = pattern.search(my_str)
    print(match) # <re.Match object; span=(39, 41), match='ma'>
    print(match.group()) # ma
    ```

    - `re.compile()` 函数,传入一个字符串,返回一个Pattern对象,表示正则表达式的匹配模式,用pattren表示这个变量名
    - Pattern对象的 `pattern.search()` 方法,在search方法传入的字符串中寻找满足条件的字符串,返回Match对象,用match表示这个变量名
    - Match对象的 `match.group()`方法,返回查找字符串中实际匹配的文本

=== "函数"
    ```python
    import re
    my_str = 'Math is intresting, and I like learing mathmatics.'
    pattern = 'ma'
    match = re.search(pattern, my_str)
    print(match) # <re.Match object; span=(39, 41), match='ma'>
    print(match.group()) # ma
    ```

### findall

=== "方法"
    ```python
    import re
    my_str = 'Math is intresting, and I like learing mathmatics.'
    pattern = re.compile('ma')
    match = pattern.findall(my_str)
    print(match) # ['ma', 'ma']
    ```
=== "函数"
    ```python
    import re
    my_str = 'Math is intresting, and I like learing mathmatics.'
    pattern = 'ma'
    match = re.findall(pattern, my_str)
    print(match) # ['ma','ma']
    ```
    
### sub

正则表达式不仅能找到文本模式,而且能够用新的文本替换掉这些模式. Pattern对象的sub()方法需要传入两个参数.第一个参数是一个字符串,用于取代发现的匹配.第二个参数是一个字符串,返回替换完成后的字符串.

=== "方法"
    ```python
    import re
    my_str = 'Hello World!'
    pattern = re.compile(r'World')
    new_str = pattern.sub('Python', my_str)
    print(new_str) # Hello Python!
    ```

=== "函数"
    ```py
    import re
    my_str = 'Hello World!'
    pattern = 'World'
    new_str = re.sub(pattern, 'Python', my_str)
    print(new_str) # Hello Python!
    ```

有时候,你可能需要使用匹配的文本本身,作为替换的一部分.在sub()的第一个参数中,可以输入\1、\2、\3…….表示“在替换中输入分组1、2、3……的文本”.

```python
import re
my_str = 'My email is d111kc@foxmail.com, his email is jerry@example.com'
pattern = re.compile(r'(\w)\w*@')
new_str = pattern.sub(r'\1****@', my_str)
print(new_str) # My email is d****@foxmail.com, his email is j****@example.com
```

字符串中的 `\1` 将由分组1匹配的文本所替代,也就是正则表达式的 `(\w)` 分组.

## 正则表达式的特殊符号

### 利用小括号 `()` 分组

=== "search方法"
    ```python
    import re
    my_str = 'My phone num is 123-456-7890.'
    pattern = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
    match = pattern.search(my_str)
    print(match.group()) # 123-456-7890
    print(match.group(0)) # 123-456-7890
    print(match.group(1)) # 123
    print(match.group(2)) # 456-7890
    print(match.groups()) # ('123', '456-7890')
    ```

=== "search函数"
    ```python
    import re
    my_str = 'My phone num is 123-456-7890.'
    pattern = r'(\d\d\d)-(\d\d\d-\d\d\d\d)'
    match = re.search(pattern, my_str)
    print(match.group()) # 123-456-7890
    print(match.group(0)) # 123-456-7890
    print(match.group(1)) # 123
    print(match.group(2)) # 456-7890
    print(match.groups()) # ('123', '456-7890')
    ```

Pattern对象中的第一对括号是第1组,第二对括号是第2组(这与list等序列的下标从0开始不同,分组是从1开始)

Match对象的 `.group()` 方法 和 `.groups()` 方法

- `match.group()` 或 `match.group(0)` 无视分组,返回符合匹配文本
- `match.group()` 传入组号,返回对应分组的文本
- `match.groups()` 获取所有分组的文本,返回 `tuple[str]` 对象

---

=== "findall方法"
    ```py
    import re
    my_str = 'My phone num is 123-456-7890.'
    pattern = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
    match = pattern.findall(my_str)
    print(match) # [('123', '456-7890')]
    ```

=== "findall函数"
    ```py
    import re
    my_str = 'My phone num is 123-456-7890.'
    pattern = r'(\d\d\d)-(\d\d\d-\d\d\d\d)'
    match = re.findall(pattern, my_str)
    print(match) # [('123', '456-7890')]
    ```

面对分组时,findall的返回值是 `list[tuple]`,每个分组就是元组的元素

### 使用管道 `|` 匹配多个分组

字符“|”称为“管道”,表示“或”.如果有多个符合匹配的文本,则第一个出现的作为match对象返回.

```py
import re
pattern = re.compile('Tom|Jerry') # 匹配Tom或Jerry字符串
match1 = pattern.search('Tom and Jerry')
print(match1.group()) # Tom
match2 = pattern.search('Jerry and Tom')
print(match2.group()) # Jerry
```

```py
import re
pattern = re.compile(r'He(y|llo|ro)')
match = pattern.search('Hello world.')
print(match.group()) # Hello （无视分组）
print(match.group(1)) # llo （第1组）
```

### 用问号 `?` 实现可选匹配

字符?表示它前面的分组在这个匹配模式中是可选的,即匹配问号之前的分组一次或零次.

```python
import re
pattern = re.compile(r'(py)?torch')
match1 = pattern.search('I want to learn pytorch this week.')
print(match1.group()) # pytorch
match2 = pattern.search('I want to learn torch this week.')
print(match2.group()) # torch
```

### 用星号 `*` 匹配任意次

星号之前的分组,可以在文本中出现任意次.

```python
import re
pattern = re.compile(r'Bat(wo)*man')
match1 = pattern.search('the adventure of Batman')
print(match1.group()) # Batman
match2 = pattern.search('the adventure of Batwoman')
print(match2.group()) # Batwoman
match3 = pattern.search('the adventure of Batwowowowoman')
print(match3.group()) # Batwowowowoman
```

从这个例子也可以看出正则表达式默认执行贪心匹配

### 用加号 `+` 匹配一次或多次

加号前面的分组至少出现一次.

### 用花括号 `{}` 匹配特定次数

如果想要一个分组重复特定次数,就在正则表达式中该分组的后面,跟上花括号包围的数字.除了一个数字,还可以指定一个范围,即在花括号内写下一个最小值、逗号、最大值.例如正则表达式(ha){3,5}匹配'hahaha','hahahaha','hahahahaha'.也可以不写花括号中的第一个或第二个数字,表示不限定最小值或最大值.

### 非贪心匹配 `?`

Python的正则表达式默认是贪心匹配,这表示在有二义的情况下,它们会尽可能匹配最长的字符串.花括号的“非贪心”版本匹配尽可能最短的字符串,即在结束的花括号后跟着一个问号.

```python
import re
greed_pattern = re.compile(r'(Ha){3,5}')
mo1 = greed_pattern.search('HaHaHaHaHa')
print(mo1.group()) # HaHaHaHaHa
nongreed_pattern = re.compile(r'(Ha){3,5}?')
mo2 = nongreed_pattern.search('HaHaHaHaHa')
print(mo2.group()) # HaHaHa
```

### 使用方括号 `[]` 建立字符分类

可以用方括号定义自己的字符分类.例如,字符分类 `[aeiouAEIOU]` 将匹配所有元音字符,不论大小写.

```python
import re
pattern = r'[aeiouAEIOU]'
my_str = 'Python is VERY interesting.'
my_list = re.findall(pattern, my_str)
print(my_list) # ['o', 'i', 'E', 'i', 'e', 'e', 'i']
```

也可以使用连字符 `-` 表示字母或数字的范围.例如,字符分类 `[a-zA-Z0-9]` 将匹配所有小写字母、大写字母和数字.

注意,在方括号 `[]` 内,普通的正则表达式符号不会被解释.你不需要前面加上倒斜杠转义`.`、`*`、`?`或`()`字符.例如,字符分类将匹配数字0到5和一个句点,则需要将它写成[0-5.] .通过在字符分类的左方括号后加上一个插入字符 `^`,就可以得到“非字符类”.非字符类将匹配不在这个字符类中的所有字符.

```python
import re
pattern = r'[^aeiouAEIOU]'
my_str = 'Python'
my_list = re.findall(pattern, my_str)
print(my_list) # ['P', 'y', 't', 'h', 'n']
```
### 插入字符 `^` 和美元字符 `$`

可以在正则表达式的开始处使用插入符号 `^`,表明匹配必须发生在被查找文本开始处.类似地,可以再正则表达式的末尾加上美元符号 `$`,表示该字符串必须以这个正则表达式的模式结束.可以同时使用 `^` 和 `$`,表明整个字符串必须匹配该模式,也就是说,只匹配该字符串的某个子集是不够的.

### 通配符 `.`

在正则表达式中,句点字符 `.` 称为“通配符”.它匹配除了换行之外的所有字符.

```python
import re
pattern = r'.at'
my_str = 'The cat in the hat sat on the flat mat.'
my_list = re.findall(pattern, my_str)
print(my_list) # ['cat', 'hat', 'sat', 'lat', 'mat']
```

要记住,句点字符只匹配一个字符,所以,对于文本 `flat` ,只匹配 `lat.` 要匹配真正的句点,就是用倒斜杠转义.

### 用点星 `.*` `.*?` 匹配所有字符

可以用点星(.*)表示“任意文本”.句点字符表示“除换行外所有单个字符”,星号字符表示“前面字符出现零次或多次”.

```python
import re
my_str = 'Hello world!'
pattern = re.compile(r'(.*) world')
match = pattern.search(my_str)
print(match.group()) # Hello world!
print(match.group(1)) # Hello
```

点星 `.*` 使用贪心匹配.要用非贪心模式匹配所有文本,就使用点星问 `.*?` .像和花括号一起使用时那样,问号告诉Python用非贪心模式匹配.

```python
import re
my_str = '<Hello> <World>'
# 非贪心匹配
nongreddy_pattern = re.compile(r'<.*?>')
match1 = nongreddy_pattern.search(my_str)
print(match1.group()) # 输出结果 <Hello>
# 贪心匹配
greedy_regex = re.compile(r'<.*>')
match2 = greedy_regex.search(my_str)
print(match2.group()) # 输出结果 <Hello> <World>
```
## `re.compile()` 的可选参数

### 用句点字符匹配换行 `re.DOTALL` (不建议使用)

点-星将匹配除换行外的所有字符.通过传入 `re.DOTALL` 作为 `re.compile()` 的第二个参数,可以让句点字符匹配所有字符,包括换行字符.

### 不区分大小写的匹配 `re.I` `re.IGNORECASE`

通常,正则表达式默认区分大小写.要让正则表达式不区分大小写,可以向 `re.compile()` 传入 `re.IGNORECASE` 或 `re.I` ,作为第二个参数.

```python 
import re
pattern = re.compile(r'hello', re.I)
my_str1 = 'Hello World!'
match1 = pattern.search(my_str1)
print(match1.group()) # Hello
my_str2 = 'HELLO World!'
match2 = pattern.search(my_str2)
print(match2.group()) # HELLO
my_str3 = 'hello World!'
match3 = pattern.search(my_str3)
print(match3.group()) # hello
```

### 正则表达式中编写注释 `re.VERBOSE`

可以向`re.compile()`传入变量`re.VERBOSE`,作为第二个参数.忽略正则表达式字符串中的空白符和注释.

```python
pattern = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')# 这个正则表达式难以阅读,可以添加注释简化阅读
# 三重引号表示多行字符串,也可表示注释
pattern = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # 区号
    (\s|-|\.)? # 分隔符
    \d{3} # 3个数字
    (\s|-|\.) # 分隔符
    \d{4} # 4个数字
    (\s*(ext|x|ext.)\s*\d{2,5})? # 扩展
    )''', re.VERBOSE)
```

使用了三重引号('"),创建了一个多行字符串.这样就可以将正则表达式定义放在多行中,让它更可读.正则表达式字符串中的注释规则,与普通的Python代码一样：#符号和它后面直到行末的内容,都被忽略.而且,表示正则表达式的多行字符串中,多余的空白字符也不认为是要匹配的文本模式的一部分.

### 使用管道 `|` 组合使用 `re.IGNORECASE` `re.DOTALL`和 `re.VERBOSE`(不推荐使用)

如果你希望在正则表达式中使用re.VERBOSE来编写注释,还希望使用re.IGNORECASE来忽略大小写,该怎么办？遗憾的是,re.compile()函数只接受一个值作为它的第二参数.可以使用管道字符(|)将变量组合起来,从而绕过这个限制.管道字符在这里称为“按位或”操作符.所以,如果希望正则表达式不区分大小写,并且句点字符匹配换行,就可以这样构造re.compile()调用：

```python
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
```
