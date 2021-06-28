''' Írj egy Python programot, amely a felhasználótól pozitív számokat kér be mindaddig,
amíg a felhasználó nullát nem ad be! A program az összes értéket tárolja egy listában,
majd írja ki a képernyőre a lista elemeit fordított sorrendben!
A megoldást egy fordito.py nevű file-ban kell beadnod.


'''

number = 1
numbers = []

while (number != 0):
    number = int(input("adjon meg egy pozitiv szamot szamot: "))
    if number > 0:
        numbers.append(number)
    elif number < 0:
        print('nope')
        break
    else:

        print(numbers[::-1])
