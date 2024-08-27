# Спрашиваем у пользователя оценку
question = int(input("введите оценку"))

# Проверяем, чему равна оценка
if question == 2:
    print("Ох надо поучиться еще")
elif question == 3:
    print("ну не 2 и на том спасибо")
elif question == 4:
    print("о отлично, ты молодец")
elif question == 5:
    print("вау, да ты умничка!")
# Здесь можно добавить проверку на некорректные значения, например:
# elif question > 5 or question < 2:
#     print("ой ошибка")
else:
    print("эх не подходит")

# Работаем с текстом
text = "fvbtmgrienwdef9gjn4ie9fjevr9bni4ej0cvr9n143d0ecjv9nir" \
       "fvrin49e8vkrjb9in4feok@cvrj9nigmf403dkBejrv9nmg14fo30kevrj" \
       "4jgvrb9jmefin4gvr9j0km9oeinf4gvrkefmni4fegvr9jm9eoinf4gv" \
       "in4fgvr9jmno1 f4erv9jemfni4vr9jme9nief4vr9jk8efj9omnie@4gr" \
       "3ni4rv9jmenif4vr9j0k9emnif4vr9jekm9ndw9jd0kc9ovmrin end"

# Ищем позицию первого символа "@" в тексте
print(text.find("@"))

# Ищем позицию последнего символа "@" в тексте
print(text.rfind("@"))

# Работаем с текстом "У Лукоморья дуб зелёный"
mybooktext = "У Лукоморья дуб зелёный"

# Извлекаем символы со 2-го по 4-й (включительно)
look = mybooktext[2:5]
print(look)

# Извлекаем последние 7 символов строки
green = mybooktext[-7:]
print(green)

# Извлекаем символы с 12-го по 14-й (включительно)
tree = mybooktext[12:15]
print(tree)

# Извлекаем первый символ строки
y = mybooktext[0]
print(y)

# Извлекаем 6-й по 8-й символы и добавляем 10-й символ
sea = mybooktext[6:9] + mybooktext[10]
print(sea)

# Переменная пробела
probel = " "

# Объединяем подстроки и пробел
print(look + probel + green)

# Работа со штрих-кодами
na = "101202245"
nb = "105202244"
nc = "912202333"
nd = "509202235"
ni = "001202309"

# Извлекаем даты (с 3-й по 8-ю цифру для каждого штрих-кода)
cleardatena = na[2:8]
cleardatenb = nb[1:7]
cleardatenc = nc[1:7]
cleardatend = nd[1:7]
cleardateni = ni[2:8]

# Комментарий к вашему коду:
# Первое, что вы сделали - получили чистую дату из каждого штрих-кода.
# Необходимо написать программу, которая будет проверять свежесть продукта по его штрих-коду.
# Со 2-ой по 8-ю цифры кода означают месяц и год производства.

# Преобразуем даты в целые числа
ournumber1 = int(cleardatena)
ournumber2 = int(cleardatenb)
ournumber3 = int(cleardatenc)
ournumber4 = int(cleardatend)
ournumber5 = int(cleardateni)

# Текущая дата (в формате ГГММДД)
today = 270824

# Рассчитываем разницу между текущей датой и датой производства
print(today - ournumber1)
print(today - ournumber2)
print(today - ournumber3)
print(today - ournumber4)
print(today - ournumber5)

# Вы получили числа - теперь их нужно отсортировать по убыванию

# Работа со штрих-кодами
na = "101202245"
nb = "105202244"
nc = "912202333"
nd = "509202235"
ni = "001202309"

# Извлекаем даты (с 3-й по 8-ю цифру для каждого штрих-кода)
cleardatena = int(na[2:8])
cleardatenb = int(nb[1:7])
cleardatenc = int(nc[1:7])
cleardatend = int(nd[1:7])
cleardateni = int(ni[2:8])

# Текущая дата
today = 270824

# ################################# вот до сюда норм а дальше сложно

# Рассчитываем разницу между текущей датой и датами производства
diff_na = today - cleardatena
diff_nb = today - cleardatenb
diff_nc = today - cleardatenc
diff_nd = today - cleardatend
diff_ni = today - cleardateni

# Собираем разницы в список
differences = [diff_na, diff_nb, diff_nc, diff_nd, diff_ni]

# Сортируем по убыванию
sorted_differences = sorted(differences, reverse=True)

# Выводим отсортированные разницы
print(sorted_differences)

# Проверка просрочки на конкретных числах
nashichisla = [218802, 178802, 150600, 150594, 148801]

# Текущая дата
today = 270823

# Проверяем каждое число в списке
for number in nashichisla:
    if number < today:
        print(f"{number} — просрочка")

# Типы данных
# int — целое число, например, 5, -2, 42
# str — строка, последовательность символов, например, "Hello"
# bool — логический тип данных, который может быть True или False
# float — число с плавающей точкой, например, 3.14, -0.001
