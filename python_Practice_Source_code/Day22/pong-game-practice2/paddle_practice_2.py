from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        # turtle初始尺寸为 20*20 像素，我们需要 100*20 方块的话，宽度拉伸5倍，长度维持1倍不变即可
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 40
        new_x = self.xcor()
        self.goto(new_x, new_y)

    def go_down(self):
        new_y = self.ycor() - 40
        new_x = self.xcor()
        self.goto(new_x, new_y)