# 本例子用于演示 slicing 切片


# ################### 数组切片 ###################
a_key = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print(a_key[2:7])
print(a_key[:7])
print(a_key[:7:2])

# 小技巧：快速将 a_key 倒序
print(a_key[::-1])

# ################### 元组切片 ###################
b_tuple=('do','re','mi','fa','so','la','xi')

print(b_tuple[2:5])

