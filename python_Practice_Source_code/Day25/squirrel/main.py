# 任务目标：从【纽约中央公园松鼠数据集】中，统计出如下信息，并导出为 csv 文件：
# ,Fur_Color,Count

import pandas as p

    # 读入文件数据
data = p.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
    # 统计数据
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)
    # 生成数据字典
data_dict = {
    "Fur Color" : ["gray", "Cinnamon","Black"],
    "Count": [gray_squirrel_count,red_squirrel_count,black_squirrel_count]
}
    # 转换为 dataframe
df = p.DataFrame(data_dict)
    # 写入 CSV 文件
df.to_csv("squirrel_count.csv")