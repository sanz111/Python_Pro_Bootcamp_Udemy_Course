# 类的继承
class Animal:
    def __init__(self):
        self.num_of_eyes = 2

    def breathe(self):
        print("Inhale, Exhale.")

# Fish 继承了 Animal
class Fish(Animal):
    def __init__(self):
        super().__init__()

    # 继承了 Animal 中的方法，同时根据 Fish 的需要做了添加
    def breathe(self):
        super().breathe()
        print("Doing this under water.")

    def swim(self):
        print("Move in water.")


nemo = Fish()
nemo.breathe()