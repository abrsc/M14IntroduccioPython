# Fes un programa que pregunti un número i et tregui la seva taula de multiplicar.
numero = float(input("Si us plau, entreu el número a multiplicar: "))
resultat = numero
for i in range(1, 11):
    resultat = numero * i
    print(resultat)
