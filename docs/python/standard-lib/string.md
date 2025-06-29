---
comments: true
icon: material/language-python
status: new
title: string
subtitle: 字符串常量
---

:material-pen-plus: `本文创建于2025-6-29`

[:simple-python: string官方文档](https://docs.python.org/zh-cn/3.13/library/string.html#module-string){ .md-button .md-button--primary }

???+ abstract
    string模块中的绝大多数方法已成为str数据类型的方法，使用时已没有必要导入string

- `string.ascii_lowercase` 小写字母 'abcdefghijklmnopqrstuvwxyz'
- `string.ascii_uppercase` 大写字母 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
- `string.ascii_letters` 英文大小写字母 `ascii_lowercase` 和 `ascii_uppercase` 常量的拼连
- `string.digits` 阿拉伯数字 '0123456789'
- `string.hexdigits` 十六进制字符 '0123456789abcdefABCDEF'
- `string.octdigits` 八进制字符 '01234567'
- `string.whitespace` 空白字符 其中包括空格、制表、换行、回车、进纸和纵向制表符。
- `string.punctuation` 标点符号字符，特殊符号字符 

    !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

- `string.printable` 可打印字符 这是 digits, ascii_letters, punctuation 和 whitespace 的总和

