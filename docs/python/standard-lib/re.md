---
comments: true
# icon: material/language-python
status: new
title: re
subtitle: 正则表达式
---

:material-pen-plus: `本文创建于2025-5-11`


[:simple-python: re官方文档](https://docs.python.org/zh-cn/3/library/re.html){ .md-button .md-button--primary }
[:simple-python: 正则表达式指南](https://docs.python.org/zh-cn/3/howto/regex.html){ .md-button }



(.*?) 匹配所有字符
## re库
用法举例：
```python
import re

phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phone_regex.search('my phone num is 123-456-7890')
print(mo)
print(mo.group())
"""运行结果
<re.Match object; span=(16, 28), match='123-456-7890'>
123-456-7890
"""
```
compile()函数，返回一个regex对象（匹配方法）。regex对象的search()方法，在search方法传入的字符串中寻找满足条件的字符串，返回match对象，常用mo表示。mo的group()方法，返回查找字符串中实际匹配的文本。
## 常用
?匹配零次或一次前面的分组。
*匹配零次或多次前面的分组。
+匹配一次或多次前面的分组。
{n}匹配n次前面的分组。
{n,}匹配n次或更多前面的分组。
{,m}匹配零次到m次前面的分组。
{n,m}匹配至少n次、至多m次前面的分组。
{n,m}?或*?或+?对前面的分组进行非贪心匹配。
^spam意味着字符串必须以spam开始。
spam$意味着字符串必须以spam结束。
.匹配所有字符，换行符除外。
\d、\w和\s分别匹配数字、单词和空格。
\D、\W和\S分别匹配出数字、单词和空格外的所有字符。
[abc]匹配方括号内的任意字符（诸如a、b或c）。
[^abc]匹配不在方括号内的任意字符。
## 正则表达式的匹配模式
### 利用括号分组
```python
import re

phone_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_regex.search('my phone num is 123-456-7890')
print(mo.group())
# 运行结果123-456-7890
print(mo.group(0))
# 123-456-7890
print(mo.group(1))
# 123
print(mo.group(2))
# 456-7890
print(mo.groups())
# ('123', '456-7890')
```
正则表达式字符串中的第一对括号是第1组，第二对括号是第2组。向group()方法传入相应的数字获取相应的文本，传入0或不传参，则返回整个匹配文本。使用groups()方法一次性获取所有分组。如果匹配的文字中有括号需要使用转义字符。
### 使用管道（竖线）匹配多个分组
字符“|”称为“管道”，表示“或”。如果有多个符合匹配的文本，则第一个出现的作为match对象返回。
```python
import re

hero_regex = re.compile(r'Batman|Tina Fey')
mo1 = hero_regex.search('Batman and Tina Fey.')
print(mo1.group())# 有多个符合条件的匹配时，返回第一个
# 输出结果 Batman
mo2 = hero_regex.search('Tina Fey and Batman.')
print(mo2.group())# 有多个符合条件的匹配时，返回第一个
# 输出结果 Tina Fey
```
```python
import re

bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = bat_regex.search('Batmobile lost a wheel.')
print(mo.group())
print(mo.group(1))# 第1个分组
"""输出结果
Batmobile
mobile
"""
```
### 用问号实现可选匹配
字符?表示它前面的分组在这个匹配模式中是可选的,即匹配问号之前的分组一次或零次。
```python
import re

bat_regex = re.compile(r'Bat(wo)?man')
mo1 = bat_regex.search('the adventure of Batman')
print(mo1.group())
# 输出结果 Batman
mo2 = bat_regex.search('the adventure of Batwoman')
print(mo2.group())
# 输出结果 Batwoman
```
### 用星号匹配零次或多次
星号之前的分组，可以在文本中出现任意次。
```python
import re

bat_regex = re.compile(r'Bat(wo)*man')
mo1 = bat_regex.search('the adventure of Batman')
print(mo1.group())
# 输出结果 Batman
mo2 = bat_regex.search('the adventure of Batwoman')
print(mo2.group())
# 输出结果 Batwoman
mo3 = bat_regex.search('the adventure of Batwowowowoman')
print(mo3.group())
# 输出结果 Batwowowowoman
```
### 用加号匹配一次或多次
加号前面的分组至少出现一次。
### 用花括号匹配特定次数
如果想要一个分组重复特定次数，就在正则表达式中该分组的后面，跟上花括号包围的数字。除了一个数字，还可以指定一个范围，即在花括号内写下一个最小值、逗号、最大值。例如正则表达式(ha){3,5}匹配'hahaha','hahahaha','hahahahaha'。也可以不写花括号中的第一个或第二个数字，表示不限定最小值或最大值。
## 贪心匹配和非贪心匹配
Python的正则表达式默认是“贪心”的，这表示在有二义的情况下，它们会尽可能匹配最长的字符串。花括号的“非贪心”版本匹配尽可能最短的字符串，即在结束的花括号后跟着一个问号。
```python
import re

greed_ha_regex = re.compile(r'(Ha){3,5}')
mo1 = greed_ha_regex.search('HaHaHaHaHa')
print(mo1.group())
nongreed_ha_regex = re.compile(r'(Ha){3,5}?')
mo2 = nongreed_ha_regex.search('HaHaHaHaHa')
print(mo2.group())
```
## findall()方法和函数
regex对象的findall()方法，返回一个列表，包含被查找的字符串中的所有匹配。而search()方法返回的match对象只包含第一次匹配的文本。如果正则表达式有分组，则使用findall()方法将返回元组的列表。
```python 
import re

phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
list = phone_regex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(list)
# 输出结果['415-555-9999', '212-555-0000']
phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phone_regex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo.group())
# 输出结果 415-555-9999
phone_regex2 = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') 
list2 = phone_regex2.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(list2)
# 输出结果 [('415', '555', '9999'), ('212', '555', '0000')]
```
findall()函数 findall(r'正则表达式', '被查找的字符串')
## 字符分类
| 字符 | 表示 |
|---|---|
| \d | 0到9任何数字 |
| \D | 除0到9之外的任意字符 |
| \w | 单词（任何字母、数字、下划线） |
| \W | 除字母、数字、下划线之外的字符 |
| \s | 空白字符（空格、制表位、换行符） |
| \S | 除空白字符意外的任意字符 |
## 建立自己的字符分类
可以用方括号定义自己的字符分类。例如，字符分类[aeiouAEIOU]将匹配所有元音字符，不论大小写。
```python
import re
# 匹配所有元音字母
list = re.findall(r'[aeiouAEIOU]', 'RoboCop eats baby food. BABY FOOD.')
print(list)# 输出结果 ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']
```
也可以使用短横表示字母或数字的范围。例如，字符分类[a-zA-Z0-9]将匹配所有小写字母、大写字母和数字。注意，在方括号内，普通的正则表达式符号不会被解释。你不需要前面加上倒斜杠转义.、*、?或()字符。例如，字符分类将匹配数字0到5和一个句点，则需要将它写成[0-5.] 。通过在字符分类的左方括号后加上一个插入字符（^），就可以得到“非字符类”。非字符类将匹配不在这个字符类中的所有字符。
```python
import re
# 匹配所有非元音字母
list = re.findall(r'[^aeiouAEIOU]', 'RoboCop eats baby food. BABY FOOD.')
print(list)# 输出结果 ['R', 'b', 'C', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', ' ', 'B', 'B', 'Y', ' ', 'F', 'D', '.']
```
## 插入字符和美元字符
可以在正则表达式的开始处使用插入符号（^），表明匹配必须发生在被查找文本开始处。类似地，可以再正则表达式的末尾加上美元符号（$），表示该字符串必须以这个正则表达式的模式结束。可以同时使用^和$，表明整个字符串必须匹配该模式，也就是说，只匹配该字符串的某个子集是不够的。
## 通配符
在正则表达式中，.（句点）字符称为“通配符”。它匹配除了换行之外的所有字符。
```python
import re

list = re.findall(r'.at', 'The cat in the hat sat on the flat mat.')
print(list)# 输出结果 ['cat', 'hat', 'sat', 'lat', 'mat']
```
要记住，句点字符只匹配一个字符，所以，对于文本flat，只匹配lat。要匹配真正的句点，就是用倒斜杠转义。
### 用点-星匹配所有字符
可以用点-星（.*）表示“任意文本”。句点字符表示“除换行外所有单个字符”，星号字符表示“前面字符出现零次或多次”。
在交互式环境中输入以下代码：
```python
import re

name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = name_regex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))# 输出结果 Al
print(mo.group(2))# 输出结果 Sweigart
```
点-星使用“贪心”模式：它总是匹配尽可能多的文本。要用“非贪心”模式匹配所有文本，就使用点-星和问号。像和花括号一起使用时那样，问号告诉Python用非贪心模式匹配。
```python
import re
# 非贪心匹配
nongreddy_regex = re.compile(r'<.*?>')
mo1 = nongreddy_regex.search('< To serve man> for dinner.>')
print(mo1.group())# 输出结果 < To serve man>
# 贪心匹配
greedy_regex = re.compile(r'<.*>')
mo2 = greedy_regex.search('< To serve man> for dinner.>')
print(mo2.group())# 输出结果 < To serve man> for dinner.>
```
### 用句点字符匹配换行(不建议使用)
点-星将匹配除换行外的所有字符。通过传入re.DOTALL作为re.compile()的第二个参数，可以让句点字符匹配所有字符，包括换行字符。
## 不区分大小写的匹配
通常，正则表达式默认区分大小写。要让正则表达式不区分大小写，可以向re.compile()传入re.IGNORECASE或re.I，作为第二个参数。
```python 
import re

regex = re.compile(r'robocop', re.I)
mo1 = regex.search('RoboCop is part man, part machine, all cop.')
print(mo1.group())# 输出结果 RoboCop
mo2 = regex.search('ROBOCOP protects the innocent.')
print(mo2.group())# 输出结果 ROBOCOP
mo3 = regex.search('Al, why does your programming book talk about robocop so much?')
print(mo3.group())# 输出结果 robocop
```
## 用sub()方法替换字符串
正则表达式不仅能找到文本模式，而且能够用新的文本替换掉这些模式。Regex对象的sub()方法需要传入两个参数。第一个参数是一个字符串，用于取代发现的匹配。第二个参数是一个字符串，即正则表达式。sub()方法返回替换完成后的字符串。
```python
import re

regex = re.compile(r'Agent \w+')
new_text = regex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(new_text)# 输出结果 CENSORED gave the secret documents to CENSORED.
```
有时候，你可能需要使用匹配的文本本身，作为替换的一部分。在sub()的第一个参数中，可以输入\1、\2、\3……。表示“在替换中输入分组1、2、3……的文本”。
```python
import re

regex = re.compile(r'Agent (\w)\w*')
new_text = regex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(new_text)# 输出结果 A**** told C**** that E**** knew B**** was a double agent.
```
可以使用正则表达式Agent (\w)\w，传入r'\1****'作为sub()的第一个参数。字符串中的\1将由分组1匹配的文本所替代，也就是正则表达式的(\w)分组。
## 管理复杂的正则表达式
可以向re.compile()传入变量re.VERBOSE，作为第二个参数。忽略正则表达式字符串中的空白符和注释。
```python
phone_regex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')# 这个正则表达式难以阅读,可以添加注释简化阅读
# 三重引号表示多行字符串，也可表示注释
phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # 区号
    (\s|-|\.)? # 分隔符
    \d{3} # 3个数字
    (\s|-|\.) # 分隔符
    \d{4} # 4个数字
    (\s*(ext|x|ext.)\s*\d{2,5})? # 扩展
    )''', re.VERBOSE)
```
使用了三重引号('")，创建了一个多行字符串。这样就可以将正则表达式定义放在多行中，让它更可读。正则表达式字符串中的注释规则，与普通的Python代码一样：#符号和它后面直到行末的内容，都被忽略。而且，表示正则表达式的多行字符串中，多余的空白字符也不认为是要匹配的文本模式的一部分。
## 组合使用re.IGNOREC ASE、re.DOTALL和re.VERBOSE（不推荐使用）
如果你希望在正则表达式中使用re.VERBOSE来编写注释，还希望使用re.IGNORECASE来忽略大小写，该怎么办？遗憾的是，re.compile()函数只接受一个值作为它的第二参数。可以使用管道字符（|）将变量组合起来，从而绕过这个限制。管道字符在这里称为“按位或”操作符。所以，如果希望正则表达式不区分大小写，并且句点字符匹配换行，就可以这样构造re.compile()调用：
```python
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
```
