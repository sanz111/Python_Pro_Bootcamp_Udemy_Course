from turtle import Turtle
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.1

    # 声明移动函数，以同时在 x与y 上加相同的位移，从而实现45度方向的移动
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    # 声明y碰撞函数，调用时，y增加量 * -1
    def bounce_y(self):
        self.y_move *=-1

    # 声明x碰撞函数，调用时，x增加量 * -1，同时移动速度降低
    def bounce_x(self):
        self.x_move *=-1
        self.move_speed *= 0.9

    # 位置 reset 函数，将白球位置归零点，移动速度复原，
    def reset_position(self):
        self.goto(0,0)
        self.move_speed =0.1
        self.bounce_x()