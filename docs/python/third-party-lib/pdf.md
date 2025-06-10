---
comments: true
icon: material/language-python
status: new
title: pdfplumber
subtitle: 处理PDF文档
---

:material-pen-plus: `本文创建于2025-4-30`

[:material-github: README.md](https://github.com/jsvine/pdfplumber){ .md-button .md-button--primary }

## 一、导入

    import pdfplumber

## 二、打开pdf文件，并创建一个pdf对象

```py
with pdfplumber.open(path) as pdf:
```

因为是对pdf文件的内容进行操作，所以通过`with open`语句可以避免忘记关闭文件

`pdfplumber.open()` 返回一个PDF对象，函数的参数如下：

- 第一个位置参数 文件路径或文件对象
- `password` 参数 用于打开加密的 PDF 文件，传入密码即可

PDF对象的属性和方法：

- `metadata` 属性 用于获取 PDF 文件的元数据信息，返回一个字典
- `pages` 属性 用于获取 PDF 文件的所有页面，返回一个Page对象列表

## 三、创建Page对象（核心类）

PDF文档的每一页都是一个Page对象

Page对象的属性和方法：

- `close()` 方法 用于关闭某页PDF
- `page_number` 属性 用于获取这个Page对象在PDF文档中的页码，Page对象在`pdf.pages`属性中的下标从0开始，但是页码从1开始
- `width` 属性 用于获取这个Page对象的页面宽度
- `height` 属性 用于获取这个Page对象的高度
- `crop(bounding_box, relative=False, strict=True)` 方法 用于裁剪页面，返回裁剪后的Page对象。参数说明：
    - `bounding_box` 矩形裁剪框，传入4元素元组 `(x0, top, x1, bottom)`。裁剪的页面保留至少部分位于边界框内的对象。{==元组四个元素分别是左上角角点和右下角角点的坐标，坐标的范围不能超出页面。==}如果对象仅部分落在裁剪框中，则将剖切其被边界框包含的部分。
    - 如果relative=True，则边界框计算为距页面左上角的偏移量，而不是绝对位置。
    - 当strict=True (默认值), 裁剪框必须在页面边界内部
- `within_bbox(bounding_box, relative=False)` 方法 类似`crop()`方法，但仅保留完全落在裁剪框内的对象
- `outside_crop(bounding_box, relative=False)` 方法 类似`crop()` ，仅保留裁剪框外部的对象
- `filter()` 方法 过滤页面，返回一个新的Page对象。返回页面内容，仅保留满足条件的对象
- `.objects / .chars / .lines / .rects / .curves / .images` 这些属性都返回的是列表

??? note "Page对象和PDF对象共有的属性和方法"
以下属性全都返回字典：

- `chars` , 代表文本字符，返回一个字典列表，每个字典代表一个字符。
- `lines` , 代表一条一维线.
- `rects` , 代表单个二维矩形.
- `curves` , 代表一序列 pdfminer.six 无法识别成线或矩形的连接点,.
- `images` , 代表图像.
- `annots` , 代表一个 PDF 批注 
- `hyperlinks` , 代表链接注释 Link 包含 URI 属性


??? note "返回的字典的键及其含义"
    - `page_number` 找到这个字符的页码。
    - `text` 文本内容
    - `fontname` 字符字体
    - `size` 字号
    - `adv` 等于 文本宽度 * 字体大小 * 缩放倍数 的值
    - `upright` 字符是否直立
    - `height` 字高
    - `width` 字宽
    - `linewidth` 线的厚度
    - `x0` 字符左侧到页面左侧的水平距离
    - `x1` 字符右侧到离页面左侧的水平距离
    - `y0` 字符底部到页面底部的垂直距离
    - `y1` 字符顶部到页面底部的垂直距离
    - `top` 字符顶部到页面顶部的垂直距离
    - `bottom` 字符底部的距离到页面顶部的垂直距离
    - `doctop` 字符顶部到文档顶部的垂直距离
    - `matrix` 这个字符的“当前变换矩阵”，矩阵控制字符的尺度、偏斜和位置翻译。旋转是尺度和偏斜的组合,但在大多数情况下可以被认为是等于X轴偏斜
    - `ncs` TKTK
    - `stroking_pattern` TKTK
    - `non_stroking_pattern` TKTK
    - `stroking_color` 字体轮廓颜色
    - `non_stroking_color` 字体内部填充颜色
    - `object_type` 对象类型char/line/rect/curve/image
    - `mcid` 实验属性
    - `tag` 实验属性
    - `pts`  一个(x, top) 元组列表表示曲线上的点
    - `path` 一个 (cmd, *(x, top)) 描述完整路径描述的元组列表,包括(例如)Bezier曲线中使用的控制点
    - `fill` 曲线是否被填充
    - `dash` 用`([dash_array], dash_phase)` 元组表示曲线的样式
    - `srcsize` 图像原始尺寸，(width, height) 郁元组
    - `colorspace` 图像的色域(例如RGB)
    - `bits` 进制，例如GBA颜色是八进制
    - `stream` 图像的像素值,作为 pdfminer.pdftypes.PDFStream 对象
    - `imagemask` 一个空的布尔;如果 True “指定图像数据用作当前颜色绘画的模板掩码。
    - `name` 图像名称

## 四、操作Page对象

### 4.1 将页面Page对象转换为图片PageImage对象

`page.to_image()` 方法可以将页面转换为Image对象，返回一个PageImage对象。可以对裁剪后的Page对象使用。可选参数如下：

- `resolution` 传入整数，图片每英寸的像素，默认值:72，像素越大图片越清晰，但是体积越大
- `width` 传入整数，图片宽度（像素px），默认值由resolution决定
- `height` 传入整数，图片高度（像素px），默认值由resolution决定
- `antialias` 传入布尔值，抗锯齿。默认值False，使用抗锯齿会增大图片的体积
- `force_mediabox` 传入布尔值，使用页面 .mediabox 尺寸,而不是 .cropbox 尺寸。默认值: False

PageImage对象的属性和方法：

- `reset()` 	重置,清除已绘制的所有内容。
- `copy()` 	将图像复制到新的“PageImage”对象。
- `show()` 	使用本地图片查看器浏览图片
- `save(path_or_fileobject, format="PNG")` 	保存已标记的图片
- `save(path_or_fileobject, format="PNG", quantize=True, colors=256, bits=8)` 	将带有注释的图像保存为 PNG 文件。默认参数会将图像量化为一个包含 256 种颜色的调色板，并以 8 位色深保存 PNG 文件。如果想禁用量化，可以传递quantize=False参数；如果想调整颜色调色板的大小，可以传递colors=N参数，其中 N 表示颜色的数量

### 4.2 从Page对象中提取文本

- `extract_text(x_tolerance=3, x_tolerance_ratio=None, y_tolerance=3, layout=False, x_density=7.25, y_density=13, line_dir_render=None, char_dir_render=None, **kwargs)`方法 将页面的所有字符对象拼贴成单个字符串。
    - 当 layout=False: 如果一个字符的x1与下一个字符的x0之间的差大于x_tolerance，则添加空格。(如果 x_tolerance_ratio 不是 None，提取器将使用等于 x_tolerance_ratio * previous_character["size"] 的动态 x_tolerance)。如果一个字符的doctop与下一个字符的doctop之间的差大于y_tolerance，则添加换行符。
    - 当 layout=True (实验性功能): 尝试模拟页面上文本的结构布局，使用x_density和y_density来确定每个"点"（PDF 的单位）所需的最小字符数/换行符数。所有剩余的**kwargs参数会传递给.extract_words(...)（见下文），这是计算布局的第一步
- `extract_text_simple(x_tolerance=3, y_tolerance=3)`方法 同上，简化版的`extract_text()`方法
