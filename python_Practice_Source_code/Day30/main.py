# ########################## 示例1：各种异常 ##########################
# FileNotFound Error  文件未找到error
# with open("a_file.txt") as a_file:
#     a_file.read()

# KeyError 键值对错误
# a_dict ={"name": "Jack"}
# value = a_dict["non_exist_key"]

# IndexError 引用错误
# fruit_list = ["apple", "banana", "pear"]
# fruit = fruit_list[4]

# TypeError 类型错误
# text = "abc"
# print(text +5)

# ########################## 示例2：try 异常 ##########################
# 执行 try 里面的代码。如果报错，执行 except 的代码；如果正常，执行 else 的代码；无论报错与否，都执行 finally 里面的代码
# try:
#     file = open("a_file.txt")
#     a_dict = {"name": "Jack", "age": "23"}
#     print(a_dict["age"])
# except FileNotFoundError:
#     print("There was an error")
#     file = open("a_file.txt", "w")
#     file.write("Something.")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
#
# else:
#     print("There was no error")
#     content = file.read()
#     print(content)
#
# finally:
#     print("Oh, Yes!")
#     raise TypeError("This is an error that I made up.")   # 自定义抛出异常

# ########################## 示例3： ##########################
height = float(input("Please Input Your Height: \n"))
weight = int(input("Please Input Your Weight: \n"))
if height > 3:
    raise ValueError("Human height should not be over 3 meters!")

bmi = weight / (height ** 2)
print(bmi)
