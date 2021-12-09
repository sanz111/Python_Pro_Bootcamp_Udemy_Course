from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("red")

# ################# Test1 #################
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)

# ################# Test2 #################
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# ################# Test3 #################

# def draw_shap(edge_num):
#     angle = 360 / edge_num
#     for _ in range(edge_num):
#         tim.forward(100)
#         tim.left(angle)
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shap(shape_side_n)

# ################# Test4 Random Walk #################
directions = [0, 90, 180, 270]
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

tim.pensize(10)
tim.speed('fastest')

for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(15)
    tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()

# import heroes
# print(heroes.gen())
