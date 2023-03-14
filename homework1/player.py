import datetime
from datetime import date

class Character:
    #Поля класа
    name = ''
    year = ''
    group = ''
    mark = ''
    age = ''


    #Конструктор
    def __init__(self, name = '', year = '', group = '', mark = '',
                 age = ''):
        self.name = name
        self.year = year
        self.group = group
        self.mark = mark
        self.age = age

    def get_age(self):
        today = datetime.date.today().year
        birth = int(self.year)
        return \
            f'{today - birth}\n'\

    def __str__(self):
        return self.get_ststs()

    def get_ststs(self):
        return \
            f'Имя: {self.name}\n' \
            f'год рождения: {self.year}\n' \
            f'група: {self.group}\n' \
            f'средний бал: {self.mark}\n' \
            f'возраст: {self.age}\n'

    #fgbgbf