# функция со строкой , и функция должна считать заглавные и строчные 

def countletter(letter):
    count_upper, countlower = 0 , 0 
    for i in letter:
        if i.isupper():
            count_upper += 1
        if i.islower():
            countlower += 1
    print(count_upper, countlower)
countletter(input(" write here some text"))


# посчитать символы которые ввел челик 
def poiski(search, letter):
    count = 0
    for i in search:
        if i == letter:
            count += 1
    return count
print(poiski("zaika" , "k"))

