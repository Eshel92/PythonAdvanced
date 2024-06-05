from Animal import Animal

class Dog(Animal):
    def talk(self):
        print("woof woof")

    def fetch_stick(self):
        print("there you go, sir!")


class Cat(Animal):
    def talk(self):
        print("meow")

    def chase_laser(self):
        print("Meeeeow")


class Skunk(Animal):
    def __init__(self, name, hunger=0, stink_count=6):
        super().__init__(name, hunger)
        self._stink_count = stink_count
    def talk(self):
        print("tsssss")

    def stink(self):
        print("Dear lord!")


class Unicorn(Animal):
    def talk(self):
        print("Good day, darling")
    def sing(self):
        print("I’m not your toy...")


class Dragon(Animal):
    def __init__(self, name, hunger=0, color="Green"):
        super().__init__(name, hunger)
        self._color = color
    def talk(self):
        print("Raaaawr")

    def breath_fire(self):
        print("$@#$#@$")