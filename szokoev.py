year = int(input('adja meg az evszamot: '))

def date_chechk(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


print(date_chechk(year))
