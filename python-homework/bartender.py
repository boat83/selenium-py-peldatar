kor = int(input('adja meg az eletkorat: '))
rendeles = input('mit iszik? van kola es sor: ')


if kor < 18 and rendeles == 'sor':
    print('sajnos nem adhatok!')
elif kor < 18 and rendeles == 'kola':
    print('tessek itt a kola!')
elif kor > 60 and rendeles == 'kola':
    print('a koffein artalmas az on koraban')
elif kor > 60 and rendeles == 'sor':
    print('parancsoljon a sore!')
elif rendeles != 'kola' or 'sor':
    print('nincs ilyen ital')

