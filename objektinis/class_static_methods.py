class Animal:
    def __init__(self, name):
        self.name = name
        self.strength = 100

    def say_something(self):
        pass

    def eat(self):
        self.strength = self.strength + 10

    def move_a_lot(self):
        self.strength = self.strength - 10

class Cat(Animal):
    count = 0
    def __init__(self, name):
        super().__init__(name)
        legs = 4

    @staticmethod
    def say_something():
        print("meow")

    def introduce(self):
        print(f"Hi, my name is {self.name}")

    @classmethod
    def born(cls):
        cls.count += 1



class Pigeon(Animal):
    def __init__(self, name):
        super().__init__(name)
        legs = 2

    def say_something(self):
        print("burr burr")

    def introduce(self):
        print(f"Hi, my name is {self.name}")

class Sphinx(Cat):
    pass

cat1 = Cat("Garfield")
pigeon1 = Pigeon("dfgsdg")

cat1.say_something()
pigeon1.say_something()

Cat.say_something()

# can't do this:
# Pigeon.say_something()

cat1.born()

cat2 = Cat("Tom")
cat2.born()

print(Cat.count)

