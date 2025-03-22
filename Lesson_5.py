# class Human():
#     height = 170
#
# class Student(Human):
#     satiety = 0
#
# class Worker(Human):
#     satiety = 100
#
#
# h = Human()
# g = Student()
# v = Worker()
#
# print(h.height)
# print(g.height)
# print(g.satiety)
# print(v.height)
# print(v.satiety)

class Grandparent():
    height = 170
    satiety = 100
    age = 60

class Parent(Grandparent):
    age = 40

class Child(Parent):
    height = 50
    age = 1
    def __init__(self):
        print(f"height = {self.height}")
        print(f"satiety = {self.satiety}")
        print(f"age = {self.age}")

Nick = Child()

class Hello():
    def __init__(self):
        print("Hello")

class Hello_world(Hello):
    def __init__(self):
        super().__init__()
        print("World")

hw = Hello_world()

class Computer:
    def __init__(self, model, *args, **keywards):
        super().__init__(*args, **keywards)
        self.model = model
        self.memory = 128
    def calculate(self):
        print("Calculation...")

class Display:
    def __init__(self, *args, **keywards):
        super().__init__(*args, **keywards)
        self.resolution = "4k"
    def display(self):
        print("I can display something on the screen")

class SmartPhone(Computer, Display):
    def print_info(self):
        print(self.display())
        print(self.calculate())
        print(self.model)
        print(self.memory)
        print(self.resolution)

sp = SmartPhone(model = "Last+")
sp.print_info()


