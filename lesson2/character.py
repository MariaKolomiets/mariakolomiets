from colorama import Fore, Style

class Character:
    #Поля класа
    name = ''
    health = 100
    demage = 1
    defence = 0
    is_alive = True
    color = Fore.LIGHTWHITE_EX

    def fight(self, health, is_alive):
        if health > 0:
            is_alive == True
        elif health < 0:
            is_alive == False


    #Конструктор
    def __init__(self, name = '', health = 100, demage = 1, defence = 0,
                 is_alive = True, color = Fore.LIGHTWHITE_EX):
        self.name = name
        self. health = health
        self.demage = demage
        self.defence = defence
        self.color = color
        self.is_alive = is_alive

    def __str__(self):
        return self.get_ststs()

    def get_ststs(self):
        return \
            f'{self.color}' \
            f'Имя: {self.name}\n' \
            f'Здоровье: {self.health}\n' \
            f'Урон: {self.demage}\n' \
            f'Защита: {self.defence}\n'\
            f'{Style.RESET_ALL}'

    def take_demage(self, demage):
        self.health -= max(demage, 0)

    def attack(self, targer):
        targer.take_demage(self.demage)

