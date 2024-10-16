# def function1(name, surname , otchestvo):
#     name = name.lower()
#     surname = surname.lower()
#     otchestvo = otchestvo.lower()
#     return name.capitalize()
import random
import time

slovarik = {
    "Konfetki" : 4,
    "Ananas" : 5,
    "Pirojenih" : 6
    }

peremennayanekaya = random.choice(list(slovarik.keys()))
print(peremennayanekaya, slovarik[peremennayanekaya] )


timer = input("введите секунды")
for i in range(int(timer), 0 , -1 ):
    time.sleep(1)
    print(i)
print("dzin!,dzin!")