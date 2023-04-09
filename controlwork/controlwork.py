class Person:
    name = ''
    health = 0
    mood = 0
    money = 0

    def __init__(self, name='', health=0,
                 mood=0, money=0,):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money

    def __str__(self):
        return \
            f' === {self.name} ===\n' \
            f' Здоровье: {self.health}\n' \
            f' Настроение: {self.mood}\n' \
            f' Капитал: {self.money}\n'

    def change_state(self, health=0, mood=0, money=0):
        self.health += health
        self.mood += mood
        self.money += money
        if health < 0:
            print('человек скончался')
        elif mood < 0:
            print('человек впал в депрессию')
        elif money < 0:
            print('человек обанкротился')

    def do(self, action):
        self.change_state(health=action.health, mood=action.mood, money=action.money)


class Action:
    name = ''
    health = 0
    mood = 0
    money = 0

    def __init__(self, name='', health=0,
                 mood=0, money=0,):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money


    def __str__(self):
        return \
            f' === {self.name} ===\n' \
            f' Здоровье: {self.health}\n' \
            f' Настроение: {self.mood}\n' \
            f' Капитал: {self.money}\n'

class Work(Action):
    name = ''
    health = 0
    mood = 0
    money = 0

    def type(self, mood, money):
        if mood > 90:
            money += (self.money*100)/10

class Rest(Action):
    name = ''
    health = 0
    mood = 0
    money = 0

    def type(self, mood, health):
        if health < 40:
            mood += (self.money*100)/20
