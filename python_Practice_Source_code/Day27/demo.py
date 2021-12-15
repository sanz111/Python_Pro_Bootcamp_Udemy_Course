from tkinter import *

# 创建窗口
window = Tk()
window.title("My First GUI Program ")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I'm a label", font=("Arial", 24, "bold"))
my_label.pack()
# 更改 label
my_label["text"] = "New Text"  # 方法1
my_label.config(text="New Text")  # 方法2


# Button
def button_click():
    print("I got clicked!")
    my_label.config(text="Button Got Clicked!")
    # 获取 input 的输入
    input_text = input.get()


button = Button(text="Click Me", command=button_click)
button.pack()

# Entry 组件
input = Entry(width=10)
input.pack()

# Text 组件
text = Text(height=5, width=30)
text.focus()
text.insert(END, "Example of multi-line text entry.")
print(text.get("1.0", END))
text.pack()


# Spinbox
def spinbox_used():
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)


# Scale
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    print(checked_state.get())


checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# RadioButton
def radio_used():
    print(radio_state.get())


radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    print()


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListbioxSelect>>", listbox_used)
listbox.pack()

# 维持窗口（一般放在程序最末尾）
window.mainloop()
