# jieba 中文分词结巴

[README.md](https://github.com/fxsjy/jieba){ .md-button .md-button--primary }

> 这个模块已无人维护

## 安装

    pip install jieba

## 导入

    import jieba

## 分词

- `jieba.cut(sentence, cut_all=False, HMM=True, use_paddle=False)` 函数 返回generator迭代器, 可以使用 `list()`函数 转换为分词之后的 `list` 对象
    - `sentence` 需要分词的字符串
    - `cut_all` 参数用来控制是否采用全模式
    - `HMM` 参数用来控制是否使用 HMM 模型
    - `use_paddle` 参数用来控制是否使用paddle模式下的分词模式
- `jieba.cut_for_search(sentence, HMM=True)` 函数 返回generator迭代器, 可以使用 `list()`函数 转换为分词之后的 `list` 对象. 搜索引擎模式, 该方法适合用于搜索引擎构建倒排索引的分词. 效果类似于 `jieba.cut()`全模式
    - `sentence` 需要分词的字符串. unicode 或 UTF-8 字符串、GBK 字符串。注意：不建议直接输入 GBK 字符串，可能无法预料地错误解码成 UTF-8
    - `HMM` 是否使用 HMM 模型        

???+ note
    `jieba.cut()` 以及 `jieba.cut_for_search()` 返回的结构都是一个可迭代的 `generator` ，可以使用 for 循环来获得分词后得到的每一个词语(unicode)，或者用 `jieba.lcut()` 以及 `jieba.lcut_for_search()` 直接返回 `list`对象

???+ quote
    如果需要返回字典,请直接使用`jieba.lcut()` 以及 `jieba.lcut_for_search()`


```py
import jieba

string = '今天下午我要去打乒乓球'

"""精确模式cut_all=False"""
# seg_gener = jieba.cut(string) # 返回generator
# seg_list = list(seg_gener) # 将generator转换为list对象
seg_list = jieba.lcut(string) # lcut()直接返回list对象,不返回generator
print(seg_list) # ['今天下午', '我要', '去', '打乒乓球']
seg_string = '/'.join(seg_list)
print('cut_all=False精确模式', seg_string) # cut_all=False精确模式 今天下午/我要/去/打乒乓球

"""全模式cut_all=True"""
# full_seg_gener = jieba.cut(string, cut_all=True)
# full_seg_list = list(full_seg_gener)
full_seg_list = jieba.lcut(string, cut_all=True)
print(full_seg_list) # ['今天', '今天下午', '天下', '下午', '我', '要', '去', '打乒乓球', '乒乓', '乒乓球']
full_seg_string = '/'.join(full_seg_list)
print('cut_all=True全模式', full_seg_string) # cut_all=True全模式 今天/今天下午/天下/下午/我/要/去/打乒乓球/乒乓/乒乓球

"""cut_for_search搜索引擎模式"""
search_seg_gener = jieba.cut_for_search(string)
search_seg_list = list(search_seg_gener)
print(search_seg_list) # ['今天', '天下', '下午', '今天下午', '我要', '去', '乒乓', '乒乓球', '打乒乓球']
search_seg_string = '/'.join(search_seg_list)
print('cut_for_search搜索引擎模式', search_seg_string) # cut_for_search搜索引擎模式 今天/天下/下午/今天下午/我要/去/乒乓/乒乓球/打乒乓球
```
