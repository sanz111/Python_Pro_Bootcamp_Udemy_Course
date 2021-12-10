from turtle import Turtle, Screen
import time
from snake_practice import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# 停止屏幕刷新
screen.tracer(0)

snake = Snake()

screen.listen( )
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right,"Right ")



game_is_on = True
while game_is_on:
    # 刷新一次屏幕
    screen.update()
    # 延迟 0.5 秒
    time.sleep(0.1 )
    snake.move()


screen.exitonclick()
