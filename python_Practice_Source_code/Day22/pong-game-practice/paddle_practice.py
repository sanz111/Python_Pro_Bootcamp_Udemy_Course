from turtle import Turtle

# 声明 Paddle 类，在使用是要传入 position 值， position 为元组形式 （x,y）
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        # 声明形状为 square
        self.shape("square")
        # 颜色为 white
        self.color("white")
        # 声明形状尺寸
        self.shapesize(stretch_wid=5, stretch_len=1)
        # 抬笔
        self.penup()
        # 去 position 位置
        self.goto(position)

    # 控制paddle上移，每调用一次位置+40
    def go_up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)

    # 控制paddle下移，每调用一次位置-40
    def go_down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)
