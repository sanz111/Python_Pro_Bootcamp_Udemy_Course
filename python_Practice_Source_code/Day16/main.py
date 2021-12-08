from turtle import Turtle, Screen
from prettytable import PrettyTable

# timmy = Turtle()
# print(timmy)
# timmy.shape('turtle')
# timmy.color('coral')
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheig ht)
# print(my_screen.canvwidth)
#
# # 直到点击后窗口才消失
# my_screen.exitonclick()

x = PrettyTable()
print("下面这个是x")
print(x)
print("上面这个是x")

# 添加表头
x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]

# 添加行数据
x.add_row(["Adelaide", 1295, 1158259, 600.5])
x.add_row(["Brisbane", 5905, 1857594, 1146.4])
x.add_row(["Darwin", 112, 120900, 1714.7])
x.add_row(["Hobart", 1357, 205556, 619.5])
x.add_row(["Sydney", 2058, 4336374, 1214.8])
x.add_row(["Melbourne", 1566, 3806092, 646.9])
x.add_row(["Perth", 5386, 1554769, 869.4])

# 添加列数据
x.add_column('add something',[1,2,3,4,5,6,7])

# 设置左对齐
x.align = 'l'

print(x)


