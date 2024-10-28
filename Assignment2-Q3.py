class Weapon:
    def __init__(self, damage, range):
        self.damage = damage
        self.range = range
        self.durability = 10  # default durability
        self.is_broken = False

    def attack(self, monster):
        if not self.is_broken:
            monster.health -= self.damage  # reduce monster's health by weapon's damage
            self.durability -= 1  # reduce weapon's durability by 1
            monster.attack(self)  # call monster's attack to potentially counterattack
            self.check_broken()  # check if weapon is broken

    def check_broken(self):
        # Check if the weapon is broken based on its durability
        self.is_broken = self.durability <= 0


class Monster:
    def __init__(self, damage):
        self.damage = damage
        self.health = 10  # default health
        self.is_alive = True

    def check_alive(self):
        # Check if the monster is alive based on its health
        if self.health <= 0:
            self.is_alive = False
        return self.is_alive


class RangeMonster(Monster):
    def __init__(self, damage, range):
        super().__init__(damage)
        self.range = range

    def attack(self, weapon):
        if self.check_alive() and self.range >= weapon.range:
            weapon.durability -= self.damage  # reduce weapon's durability by monster's damage


class MeleeMonster(Monster):
    def __init__(self, damage):
        super().__init__(damage)
        self.range = 1  # Melee monsters have a fixed range of 1

    def attack(self, weapon):
        if self.check_alive() and self.range >= weapon.range:
            weapon.durability -= 2 * self.damage  # reduce weapon's durability by 2x the monster's damage
