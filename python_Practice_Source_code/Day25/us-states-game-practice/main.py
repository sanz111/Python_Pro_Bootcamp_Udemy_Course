import turtle as t
import pandas as p

screen = t.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

# 在屏幕窗口上添加图片
screen.addshape(image)
t.shape(image)

# 从 CSV 文件中读入所有州的数据
data = p.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    # 获取用户输入， title() 用于将回答的首字母转换为答谢
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct.", prompt="What's another state's name? \n").title()
    print(answer_state)

    # 输入 Exit 时退出程序
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = p.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        turtle = t.Turtle()
        turtle.hideturtle()
        turtle.penup()
        state_data = data[data.state == answer_state]
        turtle.goto(int(state_data.x), int(state_data.y))
        turtle.write(state_data.state.item())

# 生成 CSV 文件，其中只包含没有答上来的 state 名称



# screen.exitonclick()  # 代码跑完后，点击屏幕，才会关闭屏幕

# ############# 备用代码段 #############
# 获取鼠标点击的位置坐标
# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()  # 保持屏幕一直打开，即使是代码已经跑完
# ############# 备用代码段 #############
