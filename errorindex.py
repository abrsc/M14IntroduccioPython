llista = [1,5,15,78,456,87]
preguntaindex = input("Entreu un número enter per ver a que correspon en la llista: ")
try:
    print(llista[int(preguntaindex)])
except:
    print("Error, el número no exista a l'index o no has entrat un número enter.")