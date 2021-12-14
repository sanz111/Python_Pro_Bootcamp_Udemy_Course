# --------------- Exercise 1 ---------------
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
out_num = [n ** 2 for n in numbers]  # 求平方
print(out_num)
out_num2 = [n for n in numbers if n % 2 == 0]  # 取出偶数
print(out_num2)

# --------------- Exercise 2 ---------------
# 找出两个 txt 文件中共同存在的数字，并输出
import pandas as p
with open("file1.txt") as file_1:
    file_data_1 = file_1.readlines()
    print(file_data_1)

with open("file2.txt") as file_2:
    file_data_2 = file_2.readlines()
    print(file_data_2)

result = [int(n.strip()) for n in file_data_1 if n in file_data_2]
print(result)