szum = 0
while True:
    szam = int(input('adjon meg eg szamot: '))
    if szam < 10:
        szum = szum + szam
    elif szam > 10:
        print(f'A beirt szamok osszege: {szum}')
        break







