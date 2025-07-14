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

## 楼梯绘制

参考这位大佬的视频

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113781283756539&bvid=BV1DPrjYzEpj&cid=27732674616&p=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>