---
comments: true
icon: material/language-python
status: new
title: turtle
subtitle: 海龟绘图, 海龟的爬行足迹
---

:material-pen-plus: `本文创建于2025-4-17`

[:simple-python: turtle官方文档](https://docs.python.org/zh-cn/3.13/library/turtle.html#module-turtle){ .md-button .md-button--primary }

## 导入

    import turtle as t

## 海龟移动和方向

海龟的起始位置是坐标原点, 数学平面直角坐标系. 海龟在图形中用三角箭头表示, 箭头的指向就是海龟前进的方向

- `t.forward(distance)` 函数 传入数字float类型,单位是像素 海龟前进(海龟的初始方向是X轴正方向)
- `t.backward(distance)` 函数 传入数字float类型,单位是像素 海龟后退
- `t.left(angle)` 函数 传入数字float类型,单位角度 海龟朝逆时针方向转向
- `t.right(angle)` 函数 传入数字float类型,单位角度 海龟朝顺时针方向转向