# 创建一个能接受任意数量传入参数的函数：此时 *args 将会以元组的形式传入
def add(*args):
    sum =0
    for _ in args:
        sum += _
    return sum
a = add(1,2,3,4,5)
print(a)


# 创建一个无限关键字参数：此时 **kwargs 将会以字典dict的形式传入
def calculate(n, **kwargs):
    for key,value in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

# 创建一个接收无限关键字参数的类
class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]
        self.color = kw["color"]
        self.seats = kw["seats"]

my_car = Car(make="Honda", model="FIT")
print(my_car.make)
print(my_car.model)