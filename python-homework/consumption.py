print("Adja meg a kert adatokat a kalkulaciohoz:")

fogyasztas_strada = float(input("orszaguti fogyasztas literben:"))
fogyasztas_varos = float(input("varosi fogyasztas literben:"))
ut_strada = float(input("orszaguton megtett ut km-ben:"))
ut_varos = float(input("varosban megtett ut km-ben:"))
benzin_ar = float(input("Az uzemanyag ara per L:"))
kalkulacio_oda = ((ut_strada / 100 * fogyasztas_strada) + (ut_varos / 100 * fogyasztas_varos)) * benzin_ar
kalkulacio_return = kalkulacio_oda * 2
print(f"Az utikoltseg csak oda:{kalkulacio_oda}, return ut eseten:{kalkulacio_return}")


