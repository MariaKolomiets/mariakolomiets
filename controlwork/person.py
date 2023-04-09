import random
from controlwork import Person
from controlwork import Action
from controlwork import Work
from controlwork import Rest

human1 = Person(name='Person1', health=100, mood=100, money=0,)

print(human1)

human1.change_state(health=random.randint(50, 100), mood=random.randint(10, 20), money=random.randint(-30, -20))
print(human1)

###########################№

human2 = Person(name='Person2', health=100, mood=100, money=0,)

print(human2)

human2.change_state(health=random.randint(-50, -20), mood=random.randint(-100, -50), money=random.randint(10, 20))
print(human2)

###########################

human3 = Person(name='Person3', health=100, mood=100, money=0,)

print(human3)

human3.change_state(health=random.randint(-5, 10), mood=random.randint(-20, -10), money=random.randint(-5, 20))
print(human3)

###########################

go_to_park = Action(name='Сходить в парк', health=3,
                    mood=15, money=0)

human1.do(go_to_park)
print(human1)

go_to_factory = Work(name='Пойти на завод', money=50, mood=-10, health=-3)
go_to_park = Rest(name='Сходить в парк', money=0, mood=15, health=3)
go_to_hospital = Action(name='Пойти в больницу', money=-20, mood=-5, health=20)
print(type(go_to_factory) == Work)
print(type(go_to_park) == Work)
print(type(go_to_hospital))