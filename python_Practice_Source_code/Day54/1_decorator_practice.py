# 本 demo 用于演示 decorator装饰器 的原理
import time

# ----------------------------- demo:1 -----------------------------
# 下面的几个方法，都有一个延迟 2s 的功能。要实现的话，就需要每个函数中都写一遍延迟。
# 同样的，如果多个函数都需要一些共同的特性，也需要重复的写，并且非常不方便进行后期维护

# def say_hello():
#     time.sleep(2)
#     print("Hello")
#
# def say_bye():
#     time.sleep(2)
#     print("Bye bye~")
#
# def say_goodmorning():
#     time.sleep(2)
#     print("Good morning!")
#
# say_hello()
# say_goodmorning()
# say_bye()


# ----------------------------- demo:2 -----------------------------
# 使用装饰器函数，来实现多个函数都共通的一些特性
# 使用时，只需要在函数前 @装饰器 的方式，就可以给这个函数加入某特性
# @装饰器  这样的写法，也可以被称为"语法糖 syntax sugar"，本质上并没有引入新特性，而是对现有特性实现的简化

def delay_decorator(function):  # 装饰器函数
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function

# 使用 @decorator 的写法
@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye bye~")

def say_goodmorning():
    print("Good morning!")

say_hello()
say_goodmorning()
say_bye()

# 不使用 @decorator 的写法
decorated_say_hello = delay_decorator(say_hello)
decorated_say_hello()

decorated_say_bye = delay_decorator(say_bye)
decorated_say_bye()