# Modifica el programa anterior per a que només sumi els números parells. WIP
num = int(input("Si us plau introdueix un número: "))
resultat = 2
while num > 0:
    resultat = resultat + num
    num = num - 2
    print(resultat)