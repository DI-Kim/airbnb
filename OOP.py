class Human:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"hello my name is {self.name}")


class Player(Human):
    def __init__(self, name, xp):
        super().__init__(name)
        self.xp = xp

    def say_hello(self):
        super().say_hello()
        print(f"And my xp is {self.xp}")


class Fan(Human):
    def __init__(self, name, fav_team):
        super().__init__(name)
        self.fav_team = fav_team

    def favorite_team(self):
        print(self.fav_team)


bigPerson_player = Player("bigPerson_player", 1000)
bigPerson_player.say_hello()

bigPerson_fan = Fan("bigPerson_fan", "Arsenal")
bigPerson_fan.say_hello()
bigPerson_fan.favorite_team()
