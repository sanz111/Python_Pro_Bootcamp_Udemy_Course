from turtle import Screen, Turtle
from paddle_practice import Paddle
from ball_practice import Ball
from scoreboard_practice import Scoreboard
import time

# 创建屏幕，定义背景颜色为black，屏幕尺寸为 width 800， height 600，并停止屏幕刷新
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# 创建 r 与 l 两个 paddle，并声明初始位置
r_paddle = Paddle((350,0))
l_paddle=Paddle((-350,0))
# 创建ball对象，scoreboard 对象
ball=Ball()
scoreboard = Scoreboard()

# 创建监听，监听键盘 up，down，w，s 四个按键
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# 开始游戏
game_is_on = True

while game_is_on:
    # 更新屏幕
    screen.update()
    # 移动小球
    ball.move()

    # 检测墙壁碰撞，并调用 bounce_y 函数
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # 检测paddle碰撞，并调用 bounce_x 函数
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()

    # 检测 R paddle 失误
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # 检测 L paddle 失误
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()