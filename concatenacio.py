# Fes un programa que pregunta una llista de paraules a l'usuari indefinidament (en bucle) i quan l'usuari introdueix la paraula "final" mostra la concatenació de totes les paraules (menys final).
while True:
    lletra = input("Si us plau entreu paraules: ")
    if "final" in lletra == True:
        print(lletra3)
        break
    else:
        lletra2 = lletra
        lletra3 = lletra2 +" "+ lletra
        
        
        