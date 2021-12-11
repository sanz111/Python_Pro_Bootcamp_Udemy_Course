from turtle import Turtle

# 声明 Scoreboard 类
class Scoreboard(Turtle):

    # 初始化
    def __init__(self):
        super().__init__()
        # 改背景颜色为白色
        self.color("white")
        # 笔上抬
        self.penup()
        # 隐藏乌龟
        self.hideturtle()
        # 声明 l 比分，初始化为0
        self.l_score = 0
        # 声明 r 比分，初始化为0
        self.r_score = 0
        # 更新 scoreboard
        self.update_scoreboard()

    # 定义更新比分板函数
    def update_scoreboard(self):
        # 清除比分板当前显示内容
        self.clear()
        # 定位到 (-100,200) 位置
        self.goto(-100, 200)
        # 写入 l_score 比分
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        # 定位到（100,200）位置
        self.goto(100, 200)
        # 写入 r_score 比分
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    # 左得分+1
    def l_point(self):
        self.l_score += 1
        # 更新比分板
        self.update_scoreboard()

    # 右得分+1
    def r_point(self):
        self.r_score += 1
        # 更新比分板
        self.update_scoreboard()
