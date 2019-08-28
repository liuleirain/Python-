# 使用turtle库绘制一个蜂窝状的六边形。
from turtle import *
from math import *


setup(600, 500, None, None)
for y in range(11):
    pen_y = 190 - 45 * y
    pen_x = -300 - 7.5 * sqrt(3) * pow(-1, y) + 7.5 * sqrt(3)
    penup()
    goto(pen_x, pen_y)
    pendown()
    for x in range(12):
        circle(30, steps=6)
        penup()
        forward(30 * sqrt(3))
        pendown()
done()
