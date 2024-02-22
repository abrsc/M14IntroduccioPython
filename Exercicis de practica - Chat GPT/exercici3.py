# Pide al usuario un número e imprime su tabla de multiplicar del 1 al 10.
numero = int(input("Si us plau, entreu el número a multiplicar: "))
resultat = numero
for i in range(1, 11):
    resultat = numero * i
    print(numero, "x", i, "=", resultat)
    