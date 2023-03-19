from lesson2.character import Character
from colorama import Fore, Style

class Berserk(Character):
    def __init__(self, name='',
                 health=100,
                 demage=1, defence = 0,
                 color=Fore.LIGHTWHITE_EX):
        Character.__init__(self, name, health,
                           demage, defence, color)
        self.max_health = health

    def get_additional_damage(self):
        return int(self.demage * (1 - self.health /
                                 self.max_health))


    def attack(self, targer):
        targer.take_demage(self.demage +
                           self.get_additional_damage())




    def get_ststs(self):
        return \
            f'{self.color}' \
            f'Имя: {self.name}\n' \
            f'Здоровье: {self.max_health}\n' \
            f'Урон: {self.demage} (+{self.get_additional_damage()})\n' \
            f'Защита: {self.defence}\n'\
            f'{Style.RESET_ALL}'














#    def healsy(self):
        #return int((self.get_additional_damage() / 100) * 10)



