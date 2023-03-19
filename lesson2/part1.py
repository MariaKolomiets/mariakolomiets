from character import Character
from colorama import Fore

player1 = Character(name='Vasya', health=70,
                    demage=2, is_alive=True,
                    color=Fore.LIGHTRED_EX)
print(player1)

player2 = Character(name= 'Petya', health=90,
                    demage=1, is_alive=True,
                    color=Fore.LIGHTBLUE_EX)
print(player2)



while player1.is_alive() and player2.is_alive():
    player1.attack(player2)
    player2.attack(player1)
    print(player1)
    print(player2)

