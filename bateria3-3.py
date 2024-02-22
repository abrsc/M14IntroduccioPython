# Modifica el programa anterior per a que només sumi els números parells.
num = int(input("Si us plau introdueix un número: "))
resultat = 0
while num > 0:
    resultat = resultat + num
    if num % 2 == 0:
        num = num - 2
    else:
        num = num - 1
    print(resultat)