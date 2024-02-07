# Fes un programa que demana un número a l'usuari i imprimeix la seva taula de multiplicar (del 1 al 10).
num = int(input("Si us plau entreu un número: "))
resultat = 1
print("La tabla de multiplicar de", num, "és: ")
while resultat <=10:
    print(num, "x", resultat, "=", num * resultat)
    resultat = resultat + 1