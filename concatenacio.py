# Fes un programa que pregunta una llista de paraules a l'usuari indefinidament (en bucle) i quan l'usuari introdueix la paraula "final" mostra la concatenació de totes les paraules (menys final).
concatenar = ""
while True:
    lletra = input("Si us plau introdueix una paraula o final per acabar: ")
    if "final" in lletra:
        break
    else:
        concatenar = concatenar + lletra + " "
print(concatenar)
        
        