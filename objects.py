from other_animals import *


class Animal:
    """
    Base class for all animals in the zoo.

    Attributes:
        name (str): The name of the animal.
        hunger (int): The hunger level of the animal.
    """
    zoo_name = "Hayaton"

    def __init__(self, name, hunger=0):
        """
        Initialize the animal with a name and hunger level.

        Args:
            name (str): The name of the animal.
            hunger (int): The hunger level of the animal. Default is 0.
        """
        self.name = name
        self.hunger = hunger

    def get_name(self):
        """
        Get the name of the animal.

        Returns:
            str: The name of the animal.
        """
        return self.name

    def is_hungry(self):
        """
        Check if the animal is hungry.

        Returns:
            bool: True if the animal's hunger level is greater than 0, False otherwise.
        """
        return self.hunger > 0

    def feed(self):
        """
        Feed the animal by reducing its hunger level by 1.

        Returns:
            None
        """
        if self.hunger > 0:
            self.hunger -= 1

    def talk(self):
        """
        Make the animal talk. Should be overridden by subclasses.

        Returns:
            None
        """
        pass


class Dog(Animal):
    """
    Dog class, subclass of Animal.
    """

    def talk(self):
        print("woof woof")

    def fetch_stick(self):
        print("There you go, sir!")


class Cat(Animal):
    """
    Cat class, subclass of Animal.
    """

    def talk(self):
        print("meow")

    def chase_laser(self):
        print("Meeeeow")


class Skunk(Animal):
    """
    Skunk class, subclass of Animal.
    """

    def __init__(self, name, hunger=0, stink_count=6):
        super().__init__(name, hunger)
        self.stink_count = stink_count

    def talk(self):
        print("tsssss")

    def stink(self):
        print("Dear lord!")


class Unicorn(Animal):
    """
    Unicorn class, subclass of Animal.
    """

    def talk(self):
        print("Good day, darling")

    def sing(self):
        print("I’m not your toy...")


class Dragon(Animal):
    """
    Dragon class, subclass of Animal.
    """

    def __init__(self, name, hunger=0, color="Green"):
        super().__init__(name, hunger)
        self.color = color

    def talk(self):
        print("Raaaawr")

    def breath_fire(self):
        print("$@#$#@$")


def main():
    """
    Main function to simulate the zoo behavior.

    Creates a list of various animals and iterates through it to feed hungry animals, make them talk,
    and perform any specific actions each animal type can do.

    Returns:
        None
    """
    zoo_lst = [
        Dog("Brownie", 10),
        Cat("Zelda", 3),
        Skunk("Stinky", 0),
        Unicorn("Keith", 7),
        Dragon("Lizzy", 1450),
        Dog("Doggo", 80),
        Cat("Kitty", 80),
        Skunk("Stinky Jr.", 80),
        Unicorn("Clair", 80),
        Dragon("McFly", 80)
    ]

    for animal in zoo_lst:
        if animal.is_hungry():
            print("Type:", type(animal).__name__)
            print("Name:", animal.get_name())
            while animal.is_hungry():
                animal.feed()
        animal.talk()
        if isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()
        elif isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
    print("zoo name: ", Animal.zoo_name)


if __name__ == '__main__':
    main()
