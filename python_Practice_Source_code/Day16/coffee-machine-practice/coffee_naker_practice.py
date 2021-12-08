class CoffeeMaker:

    # 初始化咖啡机的资源值
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    # 打印当前的剩余值
    def report(self):
        print(f"Water: {self.resources['water']} ml")
        print(f"Milk: {self.resources['milk']} ml")
        print(f"Coffee: {self.resources['coffee']} g")

    # 判断当前的 剩余值 是否能够支持 消费值
    def is_resource_sufficient(self, drink):
        can_make = True
        for item in drink.ingredient:
            if drink.ingredient[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    # 开始制作咖啡
    def make_coffee(self, order):
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy! ")
