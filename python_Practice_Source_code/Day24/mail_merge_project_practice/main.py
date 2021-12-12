PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    # 读取文件内所有的值
    # names = names_file.read()
    # print(names)

    # 按行读取文件，返回 list
    names_list = names_file.readlines()
    print(names_list)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    # 读取letter内容
    letter_contents = letter_file.read()
    print(letter_contents)

    for name in names_list:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        print(new_letter)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
