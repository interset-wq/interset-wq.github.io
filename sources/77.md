# DrissionPage 浏览器自动化操作

[DrissionPage官方文档](https://drissionpage.cn/)

## 两个核心的类

- `ChromiumPage` 用于操作浏览器
- `SessionPage` 

## 使用ChromiumPage类操作浏览器

### 第一步：导入模块

    from DrissionPage import Chromium

### 第二步：创建浏览器driver对象，并打开浏览器

    driver = Chromium()

??? note "driver对象的一些方法和属性"
    - `latest_tab`属性  获取激活的Tab对象，即当前使用的标签页或打开浏览器时自动打开的标签页
    - `quit()`方法 关闭浏览器，程序运行结束时不会自动关闭浏览器
    - `tabs_count`属性 返回当前打开的标签页数量
    - `tab_ids`属性 返回所有标签页id的列表
    - `new_tab()`方法 新建一个标签页，传入了url参数是新建一个标签页并访问网址，url为None时新建一个空白标签页
    - `activate_tab()`方法 激活指定的标签页
    - `close_tabs()`方法 关闭指定的标签页
    - `set_timeout()`方法 设置超时时间，单位为秒
    - `set.load_mode.normal()`方法 等待所有资源加载完毕的模式
    - `set.load_mode.eager()`方法 等待文档加载完即停止加载的模式
    - `set.load_mode.none()`方法 不会主动停止加载的模式
    - `set.retry_times()`方法 用于设置页面连接失败重连次数
    - `set.retry_interval()`方法 用于设置连接失败重连间隔（秒）
    - `set.cookies()`方法 用于设置一个或多个 cookie

### 第三步：创建标签页Tab对象

    tab = browser.latest_tab # 获取最新打开的标签页

???+ note "其他创建Tab对象的方法"
    - `tab = browser.new_tab()`  传入URL，新建一个标签页并访问网址
    - `tab = browser.get_tab()` 有多个标签页时，按条件获取一个标签页对象，模糊匹配
    - `tab = browser.get_tabs()` 有多个标签页时，按条件获取多个标签页对象，模糊匹配
  

### 第四步：通过Tab对象访问网页

    tab.get(url) # 传入网页地址，访问网页，相当于`requests.get()`方法

???+ note "访问网页的其他方法"
    - `tab.post()`方法 发送POST请求，相当于`requests.post()`方法，返回`requests.Response`对象

??? note "Tab对象的页面交互相关方法"
    - `back()`方法 传入整数，用于在浏览历史中后退若干步
    - `forward()`方法 传入整数，用于在浏览历史中前进若干步
    - `refresh()`方法 刷新当前页面
    - `stop_loading()`方法 停止加载当前页面
    - `set.blocked_urls()`方法 用于设置页面加载过程中需要屏蔽的 URL 列表，传入一个列表，列表中每个元素为一个 URL 字符串
        - `tab.set.blocked_urls('*.css*')` 设置不加载css文件

??? note "Tab对象的获取网页信息相关方法和属性"
    - `html`属性 获取当前页面的HTML文本，获取到的html中不包括iframe元素中的内容
    - `json`属性 获取当前页面的JSON数据
    - `title`属性 获取当前页面的标题
    - `user_agent`属性 获取当前页面的User-Agent
    - `save()`方法 将当前页面保存为文件，参数如下：
        - `path` 保存文件的路径
        - `name` 保存文件的名称，默认为当前页面的标题
        - `as_pdf` 是否将页面保存为PDF格式，默认为False
        - `**kwargs` 其他参数，用于设置PDF格式的参数，如：
    - `url`属性 返回当前访问的URL
    - `tab_id`属性 返回当前标签页的ID
    - `states.is_loading`属性 判断当前页面是否正在加载
    - `states.is_alive`属性 判断当前标签页是否已关闭
    - `states.ready_state`属性 返回页面当前加载状态，值为：
        - `complete` 页面加载完成
        - `loading` 页面正在加载
        - `interactive` DOM 已加载，但资源未加载完成
        - `connecting` 网页连接中
    - `url_avaiable`属性 判断当前链接是否可用
    - `states.has_alert`属性 判断当前页面是否有弹窗

### 第五步：使用Tab对象操作浏览器

#### 5.1 定位元素并操作

Tab对象常用的方法：

- `ele()` 通过css、xpath等定位元素，返回Element对象，可以使用类似于bs4的简写法，即把对象名看作是函数
- `eles()` 同上，返回Slement对象的列表
- `get_frame()` 针对iframe和frame标签，用法与ele()类似
- `get_frames()` 同上，不建议使用
- `s_ele()` 用法和ele()类似，将所有元素转换为静态的，这样可以加快获取速度
- `s_eles()` 同上

DrissionPage支持的元素定位法

- CSS选择器 `ele('css: 选择器')`，可简写为`ele('c: 选择器')`，`css:`与`css=`效果一致，没有`css^`和`css$`语法

    ```py
    ele = tab.ele('css:.div')  # 查找 div 元素
    ele = tab.ele('css:>div')  # 查找 div 子元素元素，这个写法是本库特有，原生不支持
    ```

- XPath `ele('xpath: 选择器')`，可简写为`ele('x: 选择器')`，`xpath:`与`xpath=`效果一致，没有`xpath^`和`xpath$`语法

    ```py
    ele2 = ele1.ele('xpath:.//div')  # 查找后代中第一个 div 元素
    ele2 = ele1.ele('xpath://div')  # 和上面一行一样，查找元素的后代时，// 前面的 . 可以省略
    ele_class_str = ele1.ele('xpath://div/@class')  # 使用xpath获取div元素的class属性（selenium页面元素无此功能）
    ```

- selenium By对象 `from DrissionPage.common import By` 用法和selenium相同
- id选择器`#`，相当于当属性定位`@id=id值`

    ```python
    ele = tab.ele('#one')  # 查找id="one"的元素
    ele = tab.ele('#=one')  # 同上
    ele = tab.ele('#:ne')  # 查找id属性包含ne的元素
    ele = tab.ele('#^on')  # 查找id属性以on开头的元素
    ele = tab.ele('#$ne')  # 查找id属性以ne结尾的元素
    ```

- 类选择器`.`，相当于单属性定位"@class=属性值"，和id选择器用法类似。如果一个元素有多个class属性，将其看做是一个属性
    
    ```py
    ele = tab.ele('.p_cls')  # 查找class属性为p_cls的元素
    ele = tab.ele('.=p_cls')  # 与上一行一致
    ele = tab.ele('.:_cls')  # 查找class属性包含_cls的元素
    ele = tab.ele('.^p_')  # 查找class属性以p_开头的元素
    ele = tab.ele('.$_cls')  # 查找class属性以_cls结尾的元素
    ```

- 文本匹配`text`，可简写为`tx`，相当于单属性定位"@text()=文本"，如果文本中包含html实体，需要使用转义字符将html实体转换为十六进制形式

    ```py
    ele = tab.ele('text=第二行')  # 查找文本为“第二行”的元素
    ele = tab.ele('text:第二')  # 查找文本包含“第二”的元素
    ele = tab.ele('第二')  # 与上一行一致
    ele = tab.ele('第\u00A0二')  # 匹配包含&nbsp;文本的元素，需将&nbsp;转为\u00A0
    ```

- 类型匹配`tag`，可简写为`t`，相当于单属性查找`@tag()=标签名`，相当于元素选择器，`tag:`与`tag=`效果一致，没有`tag^`和`tag$`语法

    ```py
    ele = tab.ele('tag:div')  # 查找第一个div元素
    ele = tab.ele('tag:p@class=p_cls')  # 与单属性查找配合使用，相当于css选择器 p > .p_cls
    ele = tab.ele('tag:p@@class=p_cls')  # 与单属性查找配合使用，相当于css选择器 p .p_cls
    ele = tab.ele('tag:p@@class=p_cls@@text()=第二行')  # 与多属性查找配合使用，相当于匹配css选择器 p .p_cls 且文本内容为“第二行”的元素
    ```

- DrissionPage原生

???+ note "DrissionPage原生元素定位法"
    - 单属性定位 `@`，这种方法只能通过标签名、属性名、文本内容三者之一进行定位，不能同时使用多种
        
        - `@tag()`，可简写为`t()`，相当于元素选择器
        - `@元素属性名` 通过html标签的属性名定位元素
        - `@text()`，可简写为`tx()`，通过元素的文本内容定位元素，`@@text()技巧`，此处省略

        ```python
        tab.ele('@tag()=div')  # 获取第一个div元素
        tab.ele('@id=one')  # 获取第一个`id="one"`的元素
        tab.ele('@id')  # 获取第一个有`id`属性的元素
        tab.ele('@text()=第一行')  # 获取第一个文本为“第一行”的元素
        ```

    - 多属性定位且 `@@`，这种方法可以同时使用标签名、属性名、文本内容等多种条件进行定位，用法和`@`相同，只是把`@`换成`@@`

        ```python
        ele = tab.ele('@@id=one')  # 查找id="one"的元素
        ele = tab.ele('@@class=demo@@text()=第三行')  # 查找class="demo"且文本为“第三行”的元素
        ```

    - 多属性定位或 `@|`，用法与`@@`相似

        ```python   
        eles = tab.eles('@|id=row1@|id=row2')  # 查找所有id="row1"或id="row2"的元素
        ```

    - 多属性定位非 `@!`，用法与`@@`相似

        ```
        ele = tab.ele('@!id=one')  # 获取第一个id不等于“one”的元素
        ele = tab.ele('@!class')  # 匹配没有class属性的元素
        ```

    - 且`@@`、或`@|`不能同时出现的查找语句中，非`@!`则可与两者混合使用。

    匹配模式（类似于正则表达式）

    - 精确匹配 `=`，用于匹配属性值完全等于指定值的元素

        ```py
        ele = tab.ele('@id=row1')  # 获取id='row1'的元素
        ```

    - 模糊匹配 `:`，用于匹配属性值包含指定值的元素

        ```py
        ele = tab.ele('@id:ow')  # 获取id属性包含'ow'的元素
        ```

    - 开头匹配 `^`，用于匹配属性值以指定值开头的元素

        ```py
        ele = tab.ele('@id^row')  # 获取id属性以'row'开头的元素
        ```

    - 结尾匹配 `$`，用于匹配属性值以指定值结尾的元素

        ```py 
        ele = tab.ele('@id$w1')  # 获取id属性以'w1'结尾的元素
        ```

<!-- ## 一、监听数据包，获取json数据

### 第一步：导入模块

    from DrissionPage import ChromiumPage

### 第二步：创建浏览器对象，并打开浏览器

    page = ChromiumPage()

### 第三步：监听数据包

- 开始监听数据包

    page.listen.start(url) # 传入数据包地址（url地址?参数之间的内容）

- 打开网页（必须先开始监听，在打开网页）

    page.get(url) # 传入网页地址

- 等待数据包加载
    
    res = page.listen.wait()

- 获取响应的json数据

    json_data = res.response.body

## 二、通过css选择器控制浏览器

### 第一步：导入

    from DrissionPage import ChromiumPage
    from DrissionPage.common import Keys

### 第二步：创建page对象

    page = ChromiumPage()

### 第三步：通过css选择器定位元素，进行操作

- 打开网页

    page.get(url)

- 使用css选择器定位并执行输入操作，常用操作：

    page.ele('css: 选择器').input('输入的内容') # 输入表单
    page.ele('css: 选择器').input(Keys.ENTER) # 输入回车
    page.ele('css: 选择器').click() # 模拟鼠标点击

- 提取文本内容
    - `page.ele()` 返回element对象，此对象用法与page对象类似，可以通过`text`属性提取文本内容
    - `page.eles()` 返回所有element对象的列表 -->