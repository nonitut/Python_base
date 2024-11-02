class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        return f"{self.name} говорит: Мяу!" # для возврата строки

my_cat = Cat("Мурка")
print(my_cat.meow())  


class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} говорит: Гав-гав!"

my_dog = Dog("Бобик")
print(my_dog.bark())  


class Bird:
    def __init__(self, name):
        self.name = name

    def chirp(self):
        return f"{self.name} говорит: Чик-чирик!"


my_bird = Bird("Кеша")
print(my_bird.chirp()) 
