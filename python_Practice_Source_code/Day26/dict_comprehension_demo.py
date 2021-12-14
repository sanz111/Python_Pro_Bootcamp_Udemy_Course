# --------------- Example 1 ---------------
# 目标：快速创建一个新的 dict ，key 是 names 中的学生姓名，value 是一个随机数
import random
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
student_scores = {student:random.randint(1,100) for student in names }
print(student_scores)

# --------------- Example 2 ---------------
# 目标：创建一个新的 dict ，将上例中生成的 dict 中，成绩在 60 分以上的学生挑出来
# 注意：使用 dict comprehension 时，绝对不要忘记调用 .items() 方法，否则会报错
passed_student = {student:score for(student, score) in student_scores.items() if score >=60}
print(passed_student)