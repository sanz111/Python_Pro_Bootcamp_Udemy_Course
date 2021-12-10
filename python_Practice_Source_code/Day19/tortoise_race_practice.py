from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

# 当用户什么都没输入的时候，user_bet 为空
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        # 判断是否到达屏幕右侧
        if turtle.xcor() > 230:
            # 标定比赛结束
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You won!")
            else:
                print("You lost!")
        # 给每一个 turtle 一个前进距离的随机数
        rand_instance = random.randint(0, 10)
        turtle.forward(rand_instance)

screen.exitonclick()
