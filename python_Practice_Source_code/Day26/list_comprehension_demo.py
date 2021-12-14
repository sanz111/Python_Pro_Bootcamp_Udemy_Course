numbers = [1, 2, 3]

# --------------- Example 1 ---------------
# 目标：创建一个新的 list ，每个元素是 numbers 元素+1
# 传统的写法
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
print(new_list)
# 用 list comprehension 的方式创建
new_list2 = [n + 1 for n in numbers]
print(new_list2)

# --------------- Example 2 ---------------
# list comprehension 的方式同样可以应用于遍历字符串
name = "Angela"
new_list3 = [letter for letter in name]
print(new_list3)

# --------------- Example 3 ---------------
# list comprehension 的方式同样可以应用于 range
test = [2 * n for n in range(1, 5)]
print(test)

# --------------- Example 4 ---------------
# list comprehension 内也可以用 if 筛选条件
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [n for n in names if len(n) < 5]
print(short_names)
long_names = [n.upper() for n in names if len(n) > 4]
print(long_names)
