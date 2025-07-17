---
comments: true
title: Revit 操作技巧
# icon: material/calendar-start-outline
# status: new
# pdf: true
# subtitle: 为HTML5和CSS3打下基础
---

:material-pen-plus: `本文创建于2025-5-10`

## 一、常用命令

- `RP` 放置参考平面
- `HH` 隐藏
- `HI` 隔离显示，只显示选中的图元
- `HR` 全显示，取消隐藏
- `DI` 尺寸标注
- `EL` 高程标注
- `LL` 绘制标高
- `LI` 放置线
- `TR` 修剪
- `SL` 打断
- `DL` 详图线

## 二、绘制轴网

参考这位大佬是视频：

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=114846536306689&bvid=BV14FuNzcEeS&cid=31019960957&p=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>

针对不同情况，有以下两种方式快速绘制：

### 2.1 复制CO

如果没有连续相同间距的轴线时，直接使用 `CO` 复制命令，并且勾选 `多个` 复选框。

不要直接通过 ++ctrl+c++ 和 ++ctrl+v++ 进行复制粘贴，因为这样无法勾选 `多个` 复选框。

![轴网1](https://d111kc.github.io/picx-images-hosting/revit/轴网1.4n803kbcuw.webp)

### 2.2 阵列AR

如果有n个连续相同间距的轴线时，使用 `AR` 阵列命令，**不要**勾选 `成组并关联` 复选框，`项目数` 填 n+1

![轴网2](https://d111kc.github.io/picx-images-hosting/revit/轴网2.icerge6s9.webp)

## 三、尺寸标注DI

### 3.1 轴网尺寸标注

1. 绘制矩形 *辅助外墙*

    ![尺寸标注1](https://d111kc.github.io/picx-images-hosting/revit/尺寸标注1.7sni2k191k.webp)

2. 设置 `DI` 尺寸标注命令相关参数，按图示勾选

    ![尺寸标注2](https://d111kc.github.io/picx-images-hosting/revit/尺寸标注2.2a5dmet0y0.webp)

    ![尺寸标注3](https://d111kc.github.io/picx-images-hosting/revit/尺寸标注3.99tn4b5ds9.webp)

3. 选取某面 *辅助墙*
4. 尺寸标注完成后删除辅助墙

### 3.2 门窗尺寸标注

操作与前面相同，只是 `DI` 尺寸标注命令的参数设置不相同，按图示勾选

![尺寸标注4](https://d111kc.github.io/picx-images-hosting/revit/尺寸标注4.9dd92155sg.webp)

## 四、楼梯绘制

参考这位大佬的视频

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113781283756539&bvid=BV1DPrjYzEpj&cid=27732674616&p=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>

## 五、族——公制常规模型

参考这位大佬的视频：

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=112949016396889&bvid=BV1U2eceFE3Z&cid=500001647133567&p=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>

### 5.1 拉伸和空心拉伸

![拉伸](https://d111kc.github.io/picx-images-hosting/revit/拉伸.8adju0rwr7.webp)

面动成体。

点击 `拉伸` 在 `属性` 中设置好相关的参数，然后 `楼层平面-参照标高` 上面绘制截面，打对勾生成经过这个界面移动后形成的三维图形。例如，绘制的是圆形，通过 `拉伸` 得到的就是圆柱了。

`拉伸` 绘制截面时，除了绘制外边框，还可以在外边框内部继续绘制图形，这样可以挖去里面的结构。

也可以通过 `空心形状-空心拉伸` 形成需要挖去的几何体，实体这个几何体相交的部分会被挖空。

### 5.2 融合

![融合](https://d111kc.github.io/picx-images-hosting/revit/融合.md5twgt0.webp)

点击 `融合` 设置好相关参数之后，在 `楼层平面-参照标高` 上面绘制图形，点击 `编辑顶部` ，再次绘制图形，打对勾。通过 `融合` 可以绘制圆台等上下两个底面形状不同的几何体。

### 5.3 旋转

![旋转](https://d111kc.github.io/picx-images-hosting/revit/旋转.2325tw4dsj.webp)

点击 `旋转` 设置好相关参数之后，在 `楼层平面-参照标高` 上面绘制图形，然后再绘制 `旋转轴` ，打对勾。例如：矩形旋转形成圆柱，三角形旋转形成圆锥

### 5.4 放样（常用）

![放样](https://d111kc.github.io/picx-images-hosting/revit/放样.4g4sb3tieg.webp)

通过放样可以绘制各种复杂的台阶等。

点击 `放样` 之后，在 `楼层平面-参照标高` 上面 `绘制路径`，打对勾，然后再 `编辑轮廓`，在弹出的对话框中选一个里面，绘制图形 ，打对勾。放样也是面动成体，只是这个面时沿着这条路径运动的，即路径上的每一个点的截面都是在立面中绘制的轮廓。

### 5.5 放样融合

放样和融合的结合，操作与放样和融合类似。

## 六、描图

可以直接在revit中导入图片，然后通过缩放 `RE` 使图片中的尺寸和revit中的尺寸一致，这样就可以描着图片绘制模型。

![图片](https://d111kc.github.io/picx-images-hosting/revit/图片.sz8ohpm3x.webp)

1. `插入` - `图像`，将图像放置在平面视图中
2. 选中刚才放置的图像，使用 `RE` 缩放命令
3. 在图像上点击某个尺寸标记的两端，显然这时候显示的数值并不与图上标出的数值相同，此时直接输入图上的尺寸，图像就可完成缩放
