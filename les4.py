# slovar = {
#     "mykey" : "mango",
#     "mysecret" : "coin",
#     "cozyhouse" : "slice",
# }

# slovar["ferrary"] = "candy"
# # slovar["ferrary"] = "candy" добавитли в словарь новую пару значений

# slovar["mysecret"] = "notcoin"
# # slovar["mysecret"] = "notcoin" мы заменили значение ключа

# del slovar["cozyhouse"]
# # del slovar["cozyhouse"] удалили и ключ и его значение  

# slovar.clear()
# # slovar.clear() - удалили весь словарь {} 

# print (slovar)
# # print (slovar["mykey"])


slovarik ={
    "Ivanos" : 89266170000,
    "Belov" : 89266177777,
    "Ocunev" : 89266178888,
    "Ostrov" : 89266179999,
    "Krasev" : 89266173333,
}

vopros = input("Введите вашу фамилию")

if vopros in list(slovarik.keys())  : # если фамилия есть в словаре , то ... 
    print(slovarik[vopros])
# при условии верного = соответствующего нашему списку ответу мы его проверяем по словарю и только потом выводим

else :
    print(" Такого неть")
