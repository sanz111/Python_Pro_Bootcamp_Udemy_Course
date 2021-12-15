from tkinter import *

# 创建窗口
window = Tk()
window.title("My First GUI Program ")
window.minsize(width=500, height=300)


def button_click():
    print("I got clicked!")
    my_label.config(text="Button Got Clicked!")
    # 获取 input 的输入
    input_text = input.get()


# Label
my_label = Label(text="I'm a label", font=("Arial", 24, "bold"))
# 更改 label
my_label["text"] = "New Text"  # 方法1
my_label.config(text="New Text")  # 方法2

# 组件的定位
    # 第一种方法：设置模糊位置
# my_label.pack(side="left")
    # 第二种方法：设置绝对位置
# my_label.place(x=100,y=200 )
    # 第三种方法：设置网格grid位置。注意：不能同时在一个程序中混用 pack 和 grid
my_label.grid(column=0,row=0)

# Button
button = Button(text="Click Me", command=button_click)
button.grid(column=1,row=1)

# Entry 组件
input = Entry(width=10)
input.grid(column=3,row=3)

# 维持窗口（一般放在程序最末尾）
window.mainloop()
