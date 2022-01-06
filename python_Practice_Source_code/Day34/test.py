age:int
name:str
height:float
is_human:bool

# 对变量进行类型声明
# 称为 Type Hint

def police_check(age:int) -> bool:  # 对返回值进行变量声明
    if age>18:
        can_drive = True
    else:
        can_drive = False
    return can_drive

print(police_check(20))