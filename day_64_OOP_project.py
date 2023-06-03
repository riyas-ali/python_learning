class Character:
    name = None
    health = 100
    mp = 100

    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"{self.name}\tHP: {self.health}\tMP: {self.mp}")

    def set_stats(self, health, mp):
        self.health = health
        self.mp = mp


class Player(Character):
    nick_name = None
    lives = 3

    def __init__(self, nick_name):
        self.name = "Player"
        self.nick_name = nick_name

    def print(self):
        print(f"{self.name}\tHP: {self.health}\tMP:{self.mp}\tNick name: {self.nick_name}\tLives: {self.lives}")

    def is_alive(self):
        if self.lives > 0:
            print(f"{self.nick_name} lives on!")
            return True
        else:
            print(f"{self.nick_name} has expired!")
            return False


class Enemy(Character):
    type: None
    strength = None

    def __init__(self, name, type, strength):
        self.name = name
        self.type = type
        self.strength = strength

    def print(self):
        print(f"{self.name}\tHP: {self.health}\tMP: {self.mp}\tType: {self.type}\tStrength: {self.strength}")


class Orc(Enemy):
    speed = None

    def __init__(self, speed):
        self.name = "Orc"
        self.type = "Orc"
        self.strength = 200
        self.speed = speed

    def print(self):
        print(f"{self.name}\tHP: {self.health}\tMP: {self.mp}\tType: {self.type}\tStrength: {self.strength}\tSpeed: ",
              f"{self.speed}")


class Vampire(Enemy):
    day = True

    def __init__(self, day):
        self.name = "Vampire"
        self.type = "Vampire"
        self.strength = 150
        self.day = day

    def print(self):
        print(f"{self.name}\tHP: {self.health}\tMP: {self.mp}\tType: {self.type}\tStrength: {self.strength}\tDay: ",
              f"{self.day}")


ian = Player("Riyas Ali")
ian.print()
print(ian.is_alive())

sharron = Orc(250)
gary = Orc(205)

sharron.print()
gary.print()

eric = Vampire(False)
eric.print()
