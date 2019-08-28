# 使用turtle库绘制一个颜色图谱。
import turtle

turtle.hideturtle()

def draw_sqrt(color):
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(color)
    for i in range(4):
        turtle.fd(40)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()

color = ['red', 'blue', 'green', 'yellow', 'purple']
turtle.pensize(3)
turtle.penup()
x = -100
for i in color:
    turtle.goto(x,20)
    draw_sqrt(i)
    x += 40
turtle.done()
