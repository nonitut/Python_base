spisok = [ "яблоки", "груши" , "cherry" , "banana" , "potato" ]
spisok.append ( "tomato" )
# .append - добавить данные в список
# print (spisok[2:6])
spisok[1] = "огрурцы"
del spisok[4]
# del удалить эллемент 
# Списки и Картежи

# print (spisok)
# minuta%60  - находим так остаток от деления 

minuta = 136
secunda = minuta%60 
znachenie = minuta // 60
# // - что бы убрать дробные результаты
# // - используется для целочисленного деления без остатка
print(znachenie, secunda)