# Modifica el programa anterior per que sigui l'usuari si vol sumar els números parells o els senars.
num = int(input("Si us plau introdueix un número: "))
tria = input("Vols sumar els números parells o els senars? (p/s): ")
resultat = 0
while num > 0:
    if tria == "p":
        resultat = resultat + num
        if num % 2 == 0:
            num = num - 2
        else:
            num = num - 1
        print(resultat)
    elif tria == "s":
        resultat = resultat + num
        if num % 2 == 1:
            num = num - 2
        else:
            num = num - 1
        print(resultat)
    else:
        print("S'ha de triar entre p per parells i s per senar.")
        tria = input("Vols sumar els números parells o els senars? (p/s): ")

