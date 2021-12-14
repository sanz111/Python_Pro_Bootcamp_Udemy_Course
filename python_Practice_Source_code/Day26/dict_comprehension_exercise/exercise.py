# --------------- Exercise 1 ---------------
# 统计句子中有哪些词语（词语作为key），每个词语有几个字母（字母数作为 value）
# 备注：sentence.split() 可以将句子按照单词拆成一个 list， len() 可以算出每个单词的长度
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}
print(result)

# --------------- Exercise 2 ---------------
# 将下面 dict 的摄氏度温度值转换为华氏度值，转换公式为： (temp_c * 9/5) + 32 = temp_f
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day: (temp_c * 9 / 5) + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)

# --------------- Exercise 3 ---------------
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
#   通过 dict 来循环
for (key, value) in student_dict.items():
    print(key)
    print(value)

#   通过 data frame 来循环，但是这个功能并不怎么常用
import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
for (key,value ) in student_data_frame.items():
    print(key)
    print(value)
#   通过 data frame 的 row 来循环，这个功能很常用，因为我们可以针对性的对每一行数据进行操作
for (index,row) in student_data_frame.iterrows():
    print(index)
    print(row)
    print(row.student)
    print(row.score)