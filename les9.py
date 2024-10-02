# проверка сложности пароля от 3 цифр , есть заглавная буква , 
# есть символ из набора !@#$%* и длинна от 10 символов
# oop - разделение кода на блоки / декомпозиция задачи 

def checkmunber(password):
    count = 0
    for i in password :
        if i.isdigit(): # если число = true, если нет то false
            count += 1  # функцию научили считать  числа
    if count >= 3:
        return True
    else : 
        return False


def checkupper(password):
    for i in password :
        if i.isupper():  # проверяю есть ли заглавная буква .isupper методом
            return True 
    return False


def simbols(password):
    nabor = "!@#$%*"
    for i in password:
        if i in nabor:
            return True
    return False


def checklen(password):
    if len(password) >= 10:
        return True
    return False

def checkpassword(password):
    if checkmunber(password) and checkupper(password) and simbols(password) and checklen(password):
        return True
    return False


password = input("введите пароль: ")
if checkpassword(password):
    print(" пароль подходит по критериям ")
else: 
    print(" ой придумай новый ")

# логгер - подсказывает когда что то не так 