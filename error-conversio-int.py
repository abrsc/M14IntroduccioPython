# Demana a l'usuari que introdueixi un número, i intenta convertir aquesta entrada en un enter. Utilitza try i except per capturar qualsevol error de conversió.
num = input("Si us plau entreu un numero enter: ")
try:
    int(num)
    print(num, "és un enter valid!")
except:
    print("Error, s'ha de ser un nùmero enter.")
