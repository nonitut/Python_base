def is_palindrome(number):
    num_str = str(number)
    return num_str == num_str[::-1] # Проверяем, равна ли строка своему обратному значению

number = input("Введите число для проверки: ")

if number.isdigit():
    result = is_palindrome(number)
    if result: 
        print("Число является палиндромом")
    else:   print("Число не является палиндромом")
else:
    print("Пожалуйста, введите корректное число")
