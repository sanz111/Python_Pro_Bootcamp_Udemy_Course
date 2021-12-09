# 将笔画颜色改为随机生成 RGB 的颜色

import turtle as t
import random

tim = t.Turtle()

# 设置颜色模式为 rgb
t.colormode(255)

directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed('fastest')

# 生成一个随机的rgb tuple
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


for _ in range(200):
    set_color = random_color()
    tim.color(set_color)
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()
