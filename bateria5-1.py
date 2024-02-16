# Fes un programa que pregunta valors de números sencers a l'usuari i els guarda en una llista fins que l'usuari introdueix la paraula final, i després torna la suma de tots els números introduïts.
llista=[]
while True:
    num = input("Introdueix un numero o final per acabar si us plau: ")
    resultat = 0
    if num == "final":
        for i in llista:
            resultat += i
        print(resultat)
        break
    else:
        llista.append(int(num))


        