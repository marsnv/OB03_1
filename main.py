class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Создайте метод в подклассе...")

    def eat(self):
        print(f"{self.name} ест.")

class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"{self.name} говорит: Чирик!")

    def fly(self):
        print(f"{self.name} летает далеко, на {self.wing_span} метра.")

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} говорит: Ррр!")

    def run(self):
        print(f"{self.name} бегает в {self.fur_color} шубке.")

class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        print(f"{self.name} говорит: Шшш!")

    def crawl(self):
        print(f"{self.name} ползает с {self.scale_type} чешуей.")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

# Примеры использования
bird = Bird("Птица", 2, "три")
mammal = Mammal("Тигр", 4, "полосатой")
reptile = Reptile("Змея", 3, "гладкой")

animals = [bird, mammal, reptile]
animal_sound(animals)

# Дополнительно можно вызвать специфические методы
bird.fly()
mammal.run()
reptile.crawl()