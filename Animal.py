
class Animal:
    zoo_name = "hayatoon"

    def __init__(self, name, hunger=0):
        self._name = name
        self._hunger = hunger

    def get_name(self):
        return self._name

    def is_hungry(self):
        if self._hunger > 0:
            return True
        return False

    def feed(self):
        if (self._hunger > 0):
            self._hunger -= 1

    def talk(self):
        pass