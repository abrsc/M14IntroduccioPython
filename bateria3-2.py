# Fes un programa que pregunti un número a l'usuari i retorni la suma de tots els números fins el que ha introduït l'usuari.
num = int(input("Si us plau introdueix un número: "))
resultat = 0
while num > 0:
    resultat = resultat + num
    num = num - 1
    print(resultat)