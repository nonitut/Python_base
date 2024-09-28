# def calc():
#     print()

# calc()

# def calc(a):
#     print(a ** 7)

# calc(4)

# def calc(a: int,  b: int, c: int, d: int)-> int:
#     print(a ** 7)

# calc(a=5, b=6, c=70, d=80)

# b: int, c: int, d: int для примера 

# def calc(a,  b, c, d):
#     return a + b / c

# result = calc(a=4, b=6, c=3, d=80)
# print(result)

# def math(a):
#     return a ** 7

# num = int(input("write here"))
# result = math(a=num)
# print(result)

# Площадь=длина×ширина

# def main(w,h):
#     return int(w) * int(h)
# shirina = input("write here width:")
# dlinna = input("write here height:")

# peremennaya = main(w = shirina, h = dlinna)
# print(peremennaya)
# задаю функцию ,  присваиваю значения, дальше вызываю функцию и вывожу ее результат


def main(w,h):
    return int(w) * int(h)
def function(w):
    p = main(w,w)
    return int(p)*6

shirina = input("write here width:")

peremennaya =  function(w = shirina)
print(peremennaya)
# анатации

