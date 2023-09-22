class SuperHero:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    def get_health(self):
        return self.health
    def increase_health(self):
        self.health = self.health * 2

class LocalHero(SuperHero):
    def __init__(self, name, health, power, damage):
        super().__init__(name, health, power)
        self.damage = damage
        self.fly = False

    def increase_health(self):
        self.health = self.health ** 2
        self.fly = True
    def print_true_phrase(self):
        print("True in the True_phrase")

class Villain(LocalHero):
    def __init__(self, name, health, power, damage):
        super().__init__(name, health, power, damage)
        self.people = 'monster'
    def gen_x(self):
        pass
    def crit(self, other):
        other.damage = other.damage ** self.power
    # Create objects for the new classes

air_hero = LocalHero('Air Hero', 100, 3, 10)
land_hero = LocalHero('Land Hero', 150, 5, 20)
space_hero = LocalHero('Space Hero', 200, 7, 30)
villain = Villain('Villain', 300, 6, 40)
# Call the new methods
air_hero.increase_health()
land_hero.increase_health()
space_hero.increase_health()
air_hero.print_true_phrase()
villain.crit(air_hero)
