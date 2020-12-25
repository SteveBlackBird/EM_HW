# Cubes

from random import randint

class DieTwenty():
    """   Экзэмпляр кубика с 20 гранями   """

    def __init__(self, sides=20):
        self.sides = sides

    def roll_ten(self):
        for i in range(1,10+1):
            a = randint(1, self.sides)
            print(f"{a}")
            i += 1


class DieTen():
    """   Экземляр кубика с 10 гранями   """

    def __init__(self, sides=10):
        self.sides = sides

    def roll_die(self):
        a = randint(1, self.sides)
        print(f"{a}")

class Die():
    """   Класс стандартного кубика   """

    def __init__(self, sides=6):
        self.sides = sides
        self.ten = DieTen()
        self.twenty = DieTwenty()

    def roll_ten(self):
        for i in range(1,10+1):
            a = randint(1, self.sides)
            print(f"{a}")
            i += 1


cube = Die()
# cube.ten.roll_die()
cube.roll_ten()
print("----")
cube.ten.roll_die()
print("----")
cube.twenty.roll_ten()
