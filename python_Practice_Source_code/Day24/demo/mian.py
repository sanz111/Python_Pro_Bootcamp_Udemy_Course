# 打开文件 方法1：
    # 缺点：需要记住，对文件处理完之后一定要 close()
my_file = open("my_file.txt")
content = my_file.read()
print(content)
my_file.close()

# 打开文件 方法2：
    # 优点：文件处理的代码都被括起来，所以处理完后不需要 close()
with open("my_file.txt") as file:
    contents2 = file.read()
    print(contents2)

# open() 的 mode：
    # r: 只读模式
    # w: 写入模式（如果文件不存在，就会创建同名文件 ）
    # a: 追加模式（在原字符串后再追加）
with open("my_file.txt",mode="a") as file:
    file.write("\nSome New Text!!!")
    print(contents2)

# 相对位置打开文件
with open("./data/data.txt", mode="a") as data:
    data.write("\n 666666")