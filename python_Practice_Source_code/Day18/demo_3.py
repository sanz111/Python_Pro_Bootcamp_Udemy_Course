# 将笔画颜色改为随机生成 RGB 的颜色

import turtle as t
import random

tim = t.Turtle()

# 设置颜色模式为 rgb
t.colormode(255)

directions = [0, 90, 180, 270]
tim.pensize(1)
tim.speed('fastest')


# 生成一个随机的rgb tuple
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
        tim.circle(100)


tim.speed("fastest")
draw_spirograph(20)

screen = t.Screen()
screen.exitonclick()
