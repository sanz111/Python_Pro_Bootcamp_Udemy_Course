# 读取 CSV 文件内的值
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# 调用 csv 库来处理 CSV 内的数据。
# 缺点：对行列数据进行处理时非常的麻烦（使用下例中的 Pandas 库）
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     temperatures = []
#     for row in data:
#         print(row)
#         print(row[1])
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# 使用 Pandas 库
import pandas as p

data = p.read_csv("weather_data.csv")
print(type(data))
print(data["temp"])  # e可以非常方便的调用其中某一列的值

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].tolist()
print(temp_list)
print(len(temp_list))

# 求一列数的平均值：
# 方法1：
average = sum(temp_list) / len(temp_list)
print(average)
# 方法2：
average2 = data["temp"].mean()
print(average2)
# 获取最大值
max_num = data["temp"].max()
print(max_num)

# 获取一列元素
print(data["condition"])  # 方法1
print(data.condition)  # 方法2

# 获取一行元素(筛选)
print(data[data.day == "Monday"])

# 获取温度最高的一行数据
print(data[data.temp == data.temp.max()])

# 从头创建一个 dataframe  （create a dataframe from scratch）
stu_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
stu_data = p.DataFrame(stu_dict)
print(stu_data)

# 将数据存入 csv 中
stu_data.to_csv("stu_data.csv")
