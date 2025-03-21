import random

class Human:
    def __init__(self, name="Human", job=None, home=None, car=None, pet=None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.pet = pet
        self.money = 100
        self.gladness = 50
        self.satiety = 50

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car and self.car.drive():
            self.job = Job(job_list)
        else:
            self.to_repair()

    def get_pet(self):
        self.pet = Pet()

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
            else:
                self.satiety += 5
                self.home.food -= 5

    def work(self):
        if self.car and self.car.drive():
            self.money += self.job.salary
            self.gladness -= self.job.gladness_less
            self.satiety -= 4
        else:
            self.to_repair()

    def shopping(self, manage):
        if self.car and self.car.drive():
            if manage == "fuel":
                self.money -= 100
                self.car.fuel += 100
            elif manage == 'food':
                self.money -= 50
                self.home.food += 50
            elif manage == "delicacies":
                self.gladness += 10
                self.satiety += 2
                self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5
        if self.pet:
            self.pet.play()

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def feed_pet(self):
        if self.pet:
            self.pet.eat()

    def to_repair(self):
        if self.car:
            self.car.strength += 100
            self.money -= 50

    def is_alive(self):
        if self.gladness < 0:
            print("Depression…")
            return False
        if self.satiety < 0:
            print("Dead…")
            return False
        if self.money < -500:
            print("Bankrupt…")
            return False
        return True

class Pet:
    def __init__(self, name="Buddy"):
        self.name = name
        self.happiness = 50
        self.hunger = 50

    def play(self):
        self.happiness += 10
        self.hunger -= 5
        print(f"{self.name} is happy!")

    def eat(self):
        self.hunger += 10
        print(f"{self.name} is eating!")

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move")
            return False

brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
    "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
    "Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
    "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14},
}

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]['gladness_less']

job_list = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    "Python developer": {"salary": 40, "gladness_less": 3},
    "C++ developer": {"salary": 45, "gladness_less": 25},
    "Rust developer": {"salary": 70, "gladness_less": 1},
}

human = Human(name="Alex")
human.get_home()
human.get_car()
human.get_job()
human.get_pet()
human.chill()
human.feed_pet()