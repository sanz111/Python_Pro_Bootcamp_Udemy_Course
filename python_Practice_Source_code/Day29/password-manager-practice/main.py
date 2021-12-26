# 注： * 导入时，实际只导入了所有的类和常量
from tkinter import *
# message 并不是一个类和常量，所以还需要再次导入
from tkinter import messagebox

from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    password_entry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # 随机抽取字母，符号，数字，返回数组
    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]

    # 将抽取到的 字母，符号，数字 连成一个新的数组
    password_list = password_letters + password_symbols + password_numbers
    # 将数组内元素随机打乱
    shuffle(password_list)
    # 将数组拼成一个字符串, "" 表示拼接时中间不加别的符号
    password = "".join(password_list)
    # 将生成的字符串写入到文本框中
    password_entry.insert(0, password)
    # 复制生成的字符串
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website)==0 or len(password) ==0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it OK to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                # 清空输入框内的内容， 0 表示首字符位置， END 表示末尾字符位置
                website_entry.delete(0,END)
                password_entry.delete(0,END)




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image = logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)
email_label = Label(text="Email/username:")
email_label.grid(row=2,column=0)
password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
    # 当进入界面时，光标自动聚焦在 website 输入框上
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2,column=1, columnspan=2)
    # 输入框最开始默认填入字符串。 0 表示起点位置。 END 表示末尾，当已经有字符串，希望在最后再添加字符时，可以使用 END 常量
email_entry.insert(0, "abcd@hao123.com")
password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()