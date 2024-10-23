import random
import time

def full_name(name, surname, otchestvo): # Функция для форматирования полного имени
    name = name.lower()
    surname = surname.lower()
    otchestvo = otchestvo.lower()
    return f"{surname.capitalize()} {name.capitalize()} {otchestvo.capitalize()}"

products = { # Пример словаря с продуктами и их количеством
    "Конфеты": 4,
    "Ананас": 5,
    "Пирожные": 6
}

def choose_product(products_dict): # Выбор случайного продукта
    chosen_product = random.choice(list(products_dict.keys()))
    return chosen_product, products_dict[chosen_product]


def countdown(seconds):  # Функция обратного отсчета времени
    for i in range(seconds, 0, -1):
        time.sleep(1)
        print(i)
    print("Время истекло!")


if __name__ == "__main__": # Основная программа
    name = input("Введите ваше имя: ")# Получаем данные пользователя
    surname = input("Введите вашу фамилию: ")
    otchestvo = input("Введите ваше отчество: ")

    formatted_name = full_name(name, surname, otchestvo)  # Форматируем и выводим полное имя
    print(f"Ваше полное имя: {formatted_name}")

    product, quantity = choose_product(products) # Выбираем случайный продукт и выводим его
    print(f"Вы выбрали: {product}, количество: {quantity}")
    
    timer = int(input("Введите количество секунд для таймера: ")) # Запрашиваем у пользователя время для таймера
    countdown(timer)
