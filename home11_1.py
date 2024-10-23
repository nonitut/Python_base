# 1. Напишите программу, которая запрашивает у пользователя радиус круга 
# и вычисляет его площадь и длину окружности с использованием модуля math.
import math

radius = float(input("Введите радиус круга: "))# Запрашиваем радиус у пользователя
area = math.pi * radius ** 2 # Вычисляем площадь круга
circumference = 2 * math.pi * radius # Вычисляем длину окружности

print(f"Площадь круга: {area:.2f}")
print(f"Длина окружности: {circumference:.2f}")


# 2. Напишите программу, которая запрашивает у пользователя диапазон чисел (минимальное и максимальное) 
# и выводит случайное число из этого диапазона с использованием модуля random.

import random

min_value = int(input("Введите минимальное число: "))# Запрашиваем минимальное
max_value = int(input("Введите максимальное число: "))# и максимальное значения
random_number = random.randint(min_value, max_value) # Генерируем случайное число в диапазоне

print(f"Случайное число: {random_number}")


# 3. Напишите программу, которая выводит текущую дату и время, 
# а также запрашивает у пользователя количество дней и выводит дату, 
# которая будет через это количество дней

from datetime import datetime, timedelta

current_date_time = datetime.now()
print(f"Текущая дата и время: {current_date_time}") # Получаем текущую дату и время
days = int(input("Введите количество дней: ")) # Запрашиваем количество дней
future_date = current_date_time + timedelta(days=days) # Вычисляем дату через указанное количество дней

print(f"Дата через {days} дней: {future_date.strftime('%Y-%m-%d')}")


# Напишите программу, которая создает новую папку с именем "NewFolder" в текущей директории, 
# а затем выводит список всех файлов и папок в этой директории


import os

folder_name = "Nonitestit" # Создаем новую папку
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Папка создана: {folder_name}")
else:
    print(f"Папка уже существует: {folder_name}")

print("Содержимое текущей директории:")
for item in os.listdir():
    print(f"- {item}")


# Напишите программу, которая создает словарь с данными о пользователе (имя, возраст, город) 
# и сохраняет его в файл в формате JSON с помощью модуля json

import json

name = input("Введите имя: ") # Запрашиваем данные пользователя
age = int(input("Введите возраст: "))
city = input("Введите город: ")

user_data = { # Создаем словарь с данными
    "name": name,
    "age": age,
    "city": city
}

with open('user_data.json', 'w') as file: # Сохраняем данные в файл в формате JSON
    json.dump(user_data, file)

print("Данные сохранены в файл user_data.json")

