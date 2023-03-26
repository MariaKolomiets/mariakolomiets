from random import randint
from lesson2.character import Character
from colorama import Fore, Style


class Assassin(Character):
    def __init__(self, name='',
                 health=100,
                 demage=1, defence = 0,
                 color=Fore.LIGHTWHITE_EX):
        Character.__init__(self, name, health,
                           demage, defence, color)



    def attack(self, targer):
        if randint(1, 10) == 1:
            targer.take_demage(1000)
        else:
            targer.take_demage(self.demage)


    #def assassinn(self, targer):
     #   targer.take_demage(self.roll(30) => self.demage = 1000)





    def get_ststs(self):
        return \
            f'{self.color}' \
            f'Имя: {self.name}\n' \
            f'Здоровье: {self.health}\n' \
            f'Урон: {self.demage}\n' \
            f'Защита: {self.defence}\n'\
            f'{Style.RESET_ALL}'


