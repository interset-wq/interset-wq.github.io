---
comments: true
# icon: simple/numpy
status: new
title: matplotlib
subtitle: 数据可视化PNG图像
---

:material-pen-plus: `本文创建于2025-5-16`

[matplotlib官方文档](https://matplotlib.org/stable/users/index.html){ .md-button .md-button--primary }

## 第三方库matplotlib
### 折线图plot
```py
import matplotlib.pyplot as plt
squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(squares) # 绘图
plt.show() # 显示图像
```

subplots()函数可在一个图形（figure）中绘制一或多个绘图（plot）。变量 fig 表示由生成的一系列绘图构成的整个图形。变量 ax 表示图形中的绘图，在大多数情况下，使用这个变量来定义和定制绘图。

```py
import matplotlib.pyplot as plt
squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)# 设置图线线宽
# 设置图题并给坐标轴加上标签
ax.set_title("Square Numbers", fontsize=24)# 图像标题
ax.set_xlabel("Value", fontsize=14)# x坐标名称
ax.set_ylabel("Square of Value", fontsize=14)# y坐标名称
# 设置刻度标记的样式
ax.tick_params(labelsize=14)# 设置坐标轴刻度标记字号
plt.show()
```

plot()方法默认为x轴从0开始。上面的图线有问题，需要纠正

```py
import matplotlib.pyplot as plt
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)
# 设置图题并给坐标轴加上标签
ax.set_title("Square Numbers", fontsize=24)# 图像标题
ax.set_xlabel("Value", fontsize=14)# x坐标名称
ax.set_ylabel("Square of Value", fontsize=14)# y坐标名称
# 设置刻度标记的样式
ax.tick_params(labelsize=14)# 设置坐标轴刻度标记字号
plt.show()
```

Matplotlib有很多内置样式：

```cmd
>>> import matplotlib.pyplot as plt
>>> plt.style.available
['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-v0_8', 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10']
```

使用内置样式seaborn-v0_8

```
import matplotlib.pyplot as plt
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)
# 设置图题并给坐标轴加上标签
ax.set_title("Square Numbers", fontsize=24)# 图像标题
ax.set_xlabel("Value", fontsize=14)# x坐标名称
ax.set_ylabel("Square of Value", fontsize=14)# y坐标名称
# 设置刻度标记的样式
ax.tick_params(labelsize=14)# 设置坐标轴刻度标记字号
plt.show()
```
### 散点图scatter

绘制一个点
```py
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200)# 参数分别为x坐标，y坐标，点的大小
# 设置图题并给坐标轴加上标签
ax.set_title("Square Numbers", fontsize=24)# 图像标题
ax.set_xlabel("Value", fontsize=14)# x标签
ax.set_ylabel("Square of Value", fontsize=14)# y标签
# 设置刻度标记的样式
ax.tick_params(labelsize=14)# 设置刻度标记字号
plt.show()
```

绘制一系列点

```
import matplotlib.pyplot as plt
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)# 参数分别为x坐标列表，y坐标列表，点的大小
# 设置图题并给坐标轴加上标签
ax.set_title("Square Numbers", fontsize=24)# 图像标题
ax.set_xlabel("Value", fontsize=14)# x标签
ax.set_ylabel("Square of Value", fontsize=14)# y标签
# 设置刻度标记的样式
ax.tick_params(labelsize=14)# 设置刻度标记字号
plt.show()
```

使用列表推导式绘制更多点

```py
import matplotlib.pyplot as plt
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]# 列表推导式
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, s=10)# 参数分别为x坐标列表，y坐标列表，点的大小
# ax.scatter(x_values, y_values, color='red', s=10)# 自定义颜色
# ax.scatter(x_values, y_values, color=(0, 0.8, 0), s=10)# 自定义颜色rgb表示法
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)# 使用颜色映射，数值越大，颜色越深
# 设置图题并给坐标轴加上标签
ax.set_title("Square Numbers", fontsize=24)# 图像标题
ax.set_xlabel("Value", fontsize=14)# x标签
ax.set_ylabel("Square of Value", fontsize=14)# y标签
# 设置刻度标记的样式
ax.tick_params(labelsize=14)# 设置刻度标记字号
# 设置每个坐标轴的取值范围
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style='plain')# 不使用科学计数法
plt.show()
# plt.savefig('squares_plot.png', bbox_inches='tight')
"""第一个实参指定要以什么文件名保存绘图，这个文件将被存储到py文件所
在的目录中。第二个实参指定将绘图多余的空白区域裁剪掉。如果要保留绘图周围多
余的空白区域，只需省略这个实参即可。你还可以在调用 savefig() 时使用 Path
对象，将输出文件存储到系统上的任何地方。"""
```

在刻度标记表示的数足够大时，Matplotlib 将默认使用科学记数法。

### 随机游走

创建关于随机游走的类

random_walk.py
```py
from random import choice


class RandomWalk:
    """一个生成随机游走数据的类"""
    def __init__(self, num_points=5000):# 默认点数5000
        """初始化随机游走的属性"""
        self.num_points = num_points
        # 所有随机游走都始于(0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机游走包含的所有点"""
        # 不断游走，直到列表达到指定的长度
        while len(self.x_values) < self.num_points:
            # 决定前进的方向以及沿这个方向前进的距离
            x_direction = choice([1, -1])# 在x方向向左或向右
            x_distance = choice([0, 1, 2, 3, 4])# 每次移动的距离
            x_step = x_direction * x_distance# x方向移动的距离
            y_direction = choice([1, -1])# 在y方向向上或向下
            y_distance = choice([0, 1, 2, 3, 4])# 每次移动的距离
            y_step = y_direction * y_distance# y方向移动的距离
            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue
            # 计算下一个点的 x 坐标值和 y 坐标值
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            self.x_values.append(x)
            self.y_values.append(y)
```

导入类，进行随机游走

rw_visual.py

```py
import matplotlib.pyplot as plt

from random_walk import RandomWalk


# 只要程序处于活动状态，就不断地模拟随机游走
while True:
    # 创建一个 RandomWalk 实例
    # rw = RandomWalk()# 点数使用默认值
    rw = RandomWalk(50_000)# 自定义点数
    rw.fill_walk()# 使用此方法随机游走
    # 将所有的点都绘制出来
    plt.style.use('classic')# 使用内置样式classic
    # fig, ax = plt.subplots()
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)# 调整绘图窗口尺寸（英寸）和分辨率dpi(像素，默认100)
    point_numbers = range(rw.num_points)# 创建点数列表（点数默认5000）
    # ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)# 对参数c颜色使用颜色映射，edgecolors删除点的轮廓
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, 
               cmap=plt.cm.Blues, edgecolors='none', s=1)# 自点数50_000适当减小点的大小
    ax.set_aspect('equal')# 指定两条轴上刻度的间距必须相等
    # 突出起点和终点
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)# 重绘起点，绿色，无轮廓
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)# 重绘终点
    # 隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    # 是否继续随机游走
    keep_running = input("是否创建另一次随机游走? (y/n): ")
    if keep_running == 'n':
        break
```

## 使用 Plotly 模拟掷骰子

安装plotly库和pandas库，因为plotly需要依赖pandas
plotly库绘制图形后使用浏览器显示，支持中文字体
创建Die类
die.py
```py
from random import randint# randint包括左右端点


class Die:
    """表示一个骰子的类"""
    def __init__(self, num_sides=6):
        """骰子默认为 6 面的 D6"""
        self.num_sides = num_sides
    def roll(self):# 掷骰子
        """"返回一个介于 1 和骰子面数之间的随机值"""
        return randint(1, self.num_sides)
```
### 投掷一枚六面骰子D6
```py
import plotly.express as px # 此库使用默认浏览器打开图像，支持中文字体

from die import Die


 # 创建一个 D6
die = Die()
# 掷几次骰子并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
# 分析结果
frequencies = []# 每种点数出现的次数的列表
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)# 计算某个点数出现的次数
    frequencies.append(frequency)
# 对结果进行可视化
title = "投掷D6骰子1000次的结果" # 图像标题
labels = {'x': '点数', 'y': '点数出现次数'} # 坐标轴标签
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)# bar()直方图
# fig = px.scatter(x=poss_results, y=frequencies)# scatter()散点图
# fig = px.line(x=poss_results, y=frequencies)# line()折线图
fig.show()
```

### 投掷2个D6

```py
import plotly.express as px # 此库使用默认浏览器打开图像，支持中文字体

from die import Die


# 创建两个 D6
die_1 = Die()
die_2 = Die()# 掷几次骰子并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
# 分析结果
frequencies = []# 每种点数出现的次数的列表
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)# 计算某个点数出现的次数
    frequencies.append(frequency)
# 对结果进行可视化
title = "投掷2个D6骰子1000次的结果" # 图像标题
labels = {'x': '点数', 'y': '点数出现次数'} # 坐标轴标签
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)# bar()直方图
# 进一步定制图形
fig.update_layout(xaxis_dtick=1)# 设置x轴刻度标签间隔
fig.show()
# fig.write_html('dice_visual_d6d10.html') # 保存绘制的图像
```

## 使用csv文件作为数据源

### 内置库csv

要在文本文件中存储数据，最简单的方式是将数据组织为一系列以逗号分隔的值（comma-separated values，CSV）并写入文件。这样的文件称为 CSV 文件。

### datetime

```cmd
>>> from datetime import datetime
>>> first_date = datetime.strptime('2021-07-01', '%Y-%m-%d')
>>> print(first_date)
2021-07-01 00:00:00
```

首先导入 datetime 模块中的 datetime 类，再调用 strptime() 方法来设置时间格式，并将包含日期的字符串作为第一个实参。第二个实参告诉 Python 如何设置日期的格式。在这里，'%Y-' 让 Python 将字符串中第一个连字符前面的部分视为四位数的年份，'%m-'让 Python 将第二个连字符前面的部分视为表示月份的两位数，'%d' 让 Python 将字符串的最后一部分视为月份中的一天（1～31）。strptime() 方法的第二个实参可接受各种以 % 打头的参数，并根据它们来决定如何解读日期。

| 参数 | 含义 |
|----|----|
| %A | 星期几，如 Monday |
| %B | 月份名，如 January |
| %m | 用数表示的月份（01～12） |
| %d | 用数表示的月份中的一天（01～31） |
| %Y | 四位数的年份，如 2019 |
| %y | 两位数的年份，如 19 |
| %H | 24 小时制的小时数（00～23） |
| %I | 12 小时制的小时数（01～12） |
| %p | am 或 pm |
| %M | 分钟数（00～59） |
| %S | 秒数（00～61） |

### 某地最高温度和最低温度数据可视化

death_valley_highs_lows.py.py
```py
from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime


path = Path('death_valley_2021_simple.csv')
# splitlines()获取包含文件中各行的列表，如果文件中有中文，应使用utf-8
lines = path.read_text(encoding='utf-8').splitlines() 
reader = csv.reader(lines)# 创建一个 reader 对象
# 函数 next() 返回文件中的下一行（从文件开头开始）,首次调用时返回第一行列表（表头列表）
header_row = next(reader)
"""
# 在循环中，对列表调用 enumerate() 来获取每个元素的索引及其值
for index, column_header in enumerate(header_row):
    print(index, column_header)
"""
# 提取日期和最高温度
dates, highs, lows = [], [], []
# 遍历文件中余下的各行,已经使用函数 next()读取了第一行，之后reader对象从第二行开始读取
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')# 将日期格式设置为2025-01-11
    # 防止csv文件有些数据缺失导致报错（忽略有数据缺失的数据）
    try:
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f"{current_date}有数据缺失")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
# 根据数据绘图
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5) # 最高温度折线图，alpha设置透明度，0完全透明，1完全不透明
ax.plot(dates, lows, color='blue', alpha=0.5) # 最低温度折线图
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1) # 填充区域，x坐标，y坐标，y坐标
# 设置绘图的格式
title = "Daily High and Low Temperatures, 2021\nDeath Valley, CA"
ax.set_title(title, fontsize=20)
fig.autofmt_xdate()# 绘制倾斜的日期标签，以免它们彼此重叠
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)
plt.show()
```

## 使用json文件作为数据源

绘制散点图

eq_explore_data.py
```py
from pathlib import Path
import json
import plotly.express as px


# 将数据作为字符串读取并转换为 Python 对象
path = Path('eq_data_1_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)
# 将数据文件转换为更易于阅读的版本
path = Path('readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)# 可选参数indent，指定数据结构中嵌套元素的缩进量
path.write_text(readable_contents)
# 查看数据集中的所有地震
all_eq_dicts = all_eq_data['features'] # 与地震信息相关的列表，里面嵌套某次地震的信息
# print(len(all_eq_dicts))
mags, titles, lons, lats = [], [], [], [] 
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag'] # 震级
    title = eq_dict['properties']['title'] # 地震地点名称
    lon = eq_dict['geometry']['coordinates'][0] # 坐标：经度
    lat = eq_dict['geometry']['coordinates'][1] # 坐标：纬度
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)
fig = px.scatter(
    x=lons,
    y=lats,
    labels={'x': '经度', 'y': '纬度'},# 坐标轴标题
    range_x=[-200, 200],# x坐标范围
    range_y=[-90, 90],# y坐标范围
    width=800,# 在屏幕上的显示宽度
    height=800,# 显示高度
    title='全球地震散点图',# 图像标题
)
# fig.write_html('global_earthquakes.html')# 保存图像
fig.show()
```
另一种表示方法
eq_explore_data.py
```py
from pathlib import Path
import json
import plotly.express as px
import pandas as pd


# 将数据作为字符串读取并转换为 Python 对象
path = Path('eq_data_1_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)
# 将数据文件转换为更易于阅读的版本
path = Path('readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)# 可选参数indent，指定数据结构中嵌套元素的缩进量
path.write_text(readable_contents)
# 查看数据集中的所有地震
all_eq_dicts = all_eq_data['features'] # 与地震信息相关的列表，里面嵌套某次地震的信息
# print(len(all_eq_dicts))
mags, titles, lons, lats = [], [], [], [] 
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag'] # 震级
    title = eq_dict['properties']['title'] # 地震地点名称
    lon = eq_dict['geometry']['coordinates'][0] # 坐标：经度
    lat = eq_dict['geometry']['coordinates'][1] # 坐标：纬度
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)
    
data = pd.DataFrame(data=zip(lons, lats, titles, mags), columns=['经度', '纬度', '位置', '震级'])
data.head()

fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    labels={'x': '经度', 'y': '纬度'},# 坐标轴标题
    range_x=[-200, 200],# x坐标范围
    range_y=[-90, 90],# y坐标范围
    width=800,# 在屏幕上的显示宽度
    height=800,# 显示高度
    title='全球地震散点图',# 图像标题
)
fig.show()
```

进一步美化图像

eq_explore_data.py
```py
from pathlib import Path
import json
import plotly.express as px
import pandas as pd


# 将数据作为字符串读取并转换为 Python 对象
path = Path('eq_data_1_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)
# 将数据文件转换为更易于阅读的版本
path = Path('readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)# 可选参数indent，指定数据结构中嵌套元素的缩进量
path.write_text(readable_contents)
# 查看数据集中的所有地震
all_eq_dicts = all_eq_data['features'] # 与地震信息相关的列表，里面嵌套某次地震的信息
# print(len(all_eq_dicts))
mags, titles, lons, lats = [], [], [], [] 
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag'] # 震级
    title = eq_dict['properties']['title'] # 地震地点名称
    lon = eq_dict['geometry']['coordinates'][0] # 坐标：经度
    lat = eq_dict['geometry']['coordinates'][1] # 坐标：纬度
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

data = pd.DataFrame(data=zip(lons, lats, titles, mags), columns=['经度', '纬度', '位置', '震级'])
data.head()

fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    labels={'x': '经度', 'y': '纬度'},# 坐标轴标题
    range_x=[-200, 200],# x坐标范围
    range_y=[-90, 90],# y坐标范围
    width=800,# 在屏幕上的显示宽度
    height=800,# 显示高度
    title='全球地震散点图',# 图像标题
    # 震级越大，点越大
    size='震级',# 以震级参数为参考设置点的大小
    size_max=10,# 设置点的大小
)
fig.show()
```

使用更多数据的json文件

数据可视化

```py
from pathlib import Path
import json
import plotly.express as px
import pandas as pd


# 将数据作为字符串读取并转换为 Python 对象
path = Path('eq_data_30_day_m1.geojson')
try:
    contents = path.read_text()
except:
    contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)
# 将数据文件转换为更易于阅读的版本
path = Path('readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)# 可选参数indent，指定数据结构中嵌套元素的缩进量
path.write_text(readable_contents)
# 查看数据集中的所有地震
all_eq_dicts = all_eq_data['features'] # 与地震信息相关的列表，里面嵌套某次地震的信息
# print(len(all_eq_dicts))
mags, titles, lons, lats = [], [], [], [] 
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag'] # 震级
    title = eq_dict['properties']['title'] # 地震地点名称
    lon = eq_dict['geometry']['coordinates'][0] # 坐标：经度
    lat = eq_dict['geometry']['coordinates'][1] # 坐标：纬度
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

data = pd.DataFrame(data=zip(lons, lats, titles, mags), columns=['经度', '纬度', '位置', '震级'])
data.head()

fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    labels={'x': '经度', 'y': '纬度'},# 坐标轴标题
    range_x=[-200, 200],# x坐标范围
    range_y=[-90, 90],# y坐标范围
    width=800,# 在屏幕上的显示宽度
    height=800,# 显示高度
    title='全球地震散点图',# 图像标题
    # 震级越大，点越大
    size='震级',# 以震级参数为参考设置点的大小
    size_max=10,# 设置点的大小
    color='震级',# 以震级参数为参考设置点的颜色，默认变色范围是从蓝色到红色再到黄色
    hover_name='位置',# 添加鼠标悬停文本
)
fig.show()
```
其他渐变色
```cmd
>>> import plotly.express as px
>>> px.colors.named_colorscales()
['aggrnyl', 'agsunset', 'blackbody', 'bluered', 'blues', 'blugrn', 'bluyl', 'brwnyl', 'bugn', 'bupu', 'burg', 'burgyl', 'cividis', 'darkmint', 'electric', 'emrld', 'gnbu', 'greens', 'greys', 'hot', 'inferno', 'jet', 'magenta', 'magma', 'mint', 'orrd', 'oranges', 'oryel', 'peach', 'pinkyl', 'plasma', 'plotly3', 'pubu', 'pubugn', 'purd', 'purp', 'purples', 'purpor', 'rainbow', 'rdbu', 'rdpu', 'redor', 'reds', 'sunset', 'sunsetdark', 'teal', 'tealgrn', 'turbo', 'viridis', 'ylgn', 'ylgnbu', 'ylorbr', 'ylorrd', 'algae', 'amp', 'deep', 'dense', 'gray', 'haline', 'ice', 'matter', 'solar', 'speed', 'tempo', 'thermal', 'turbid', 'armyrose', 'brbg', 'earth', 'fall', 'geyser', 'prgn', 'piyg', 'picnic', 'portland', 'puor', 'rdgy', 'rdylbu', 'rdylgn', 'spectral', 'tealrose', 'temps', 'tropic', 'balance', 'curl', 'delta', 'oxy', 'edge', 'hsv', 'icefire', 'phase', 'twilight', 'mrybm', 'mygbm']
```

## 使用GitHub API对GitHub的数据可视化

API 是网站的一部分，用于与程序进行交互。这些程序使用非常具体的 URL 请求特定的信息，而这种请求称为 API 调用。请求的数据将以程序易于处理的格式（如 JSON或 CSV）返回。使用外部数据源的应用程序（如集成了社交媒体网站的应用程序）大多依赖 API 调用。
https://api.github.com/search/repositories?q=language:python+sort:stars
这个 API 调用返回 GitHub 当前托管了多少个 Python 项目，以及有关最受欢迎的Python 仓库的信息。下面来仔细地研究这个 API 调用。开头的https://api.github.com/ 是 GitHub 的 API 地址。接下来的search/repositories 让 API 搜索 GitHub 上的所有仓库。repositories 后面的问号指出需要传递一个参数。参数 q 表示查询，而等号（=）让我们能够开始指定查询（q=）。接着，通过 language:python 指出只想获取主要语言为 Python 的仓库的信息。最后的 +sort:stars 指定将项目按星数排序。
大多数 API 存在速率限制，即在特定时间内可执行的请求数存在限制。要获悉是否接近了 GitHub 的限制，请在浏览器中输入 https://api.github.com/rate_limit
注意：很多 API 要求，在通过注册获得 API 密钥（访问令牌）后，才能执行 API调用。GitHub 没有这样的要求，但获得访问令牌后，配额将高得多。
```py 
import requests
import plotly.express as px


# 执行 API 调用并查看响应
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000" # 只查找获得超过 10 000 颗星的 Python 仓库
headers = {"Accept": "application/vnd.github.v3+json"}# 通过指定 headers 显式地要求使用第三版的GitHub API
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")# 指出请求是否成功（状态码 200表示请求成功）
# 将响应转换为字典
response_dict = r.json()
print(f"Complete results: {not response_dict['incomplete_results']}")
# 处理有关仓库的信息
repo_dicts = response_dict['items']
repo_links, stars, hover_texts = [], [], [] # 带链接的仓库名称列表，stars列表,鼠标悬停文本列表
for repo_dict in repo_dicts:
    # 将仓库名转换为链接
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>" # 插入链接
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])
    # 创建悬停文本
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}" # 在仓库和描述之间添加换行符<br />
    hover_texts.append(hover_text)
# 可视化
title = "GitHub上面最受欢迎的python项目" # 图像标题
labels = {'x': '仓库', 'y': 'Stars'} # 坐标轴标题
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts)
# 设置字体大小
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
# 自定义颜色和不透明度
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
fig.show()
```

