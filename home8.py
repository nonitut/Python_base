# Напиши функцию, которая будет складывать все значения из списка в одну строку. 
# На вход функция будет принимать список, а возвращать строку

def per(list):
    result = ''  # Инициализируем пустую строку для накопления результатов
    for element in list:  # Проходит по каждому элементу в списке
        result += str(element)  # Преобразуем элемент в строку и добавляем к результату
    return result

my_list = [1," ", 'Нона'," ", 'думает'," ", 'все', " ", 'ясно']
print(per(my_list)) 

# Когда используешь return, как бы "возвращаешь" результат функции обратно в точку, 
# откуда она была вызвана. Это позволяет сохранить результат и использовать его дальше в программе