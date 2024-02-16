# Fes un programa com l'anterior que mostra el valor màxim i mínim de la llista.
llista=[]
while True:
    num = input("Introdueix un numero o final per acabar si us plau: ")
    resultat = -1
    if num == "final":        
        break
    else:
        llista.append(int(num))
        resultat += 1
llista.sort()
print(llista[0])
print(llista[resultat])


        