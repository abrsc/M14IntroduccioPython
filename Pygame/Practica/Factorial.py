num = int(input("Insereu un nùmero per saber el seu factorial si us plau: "))
resultat = 1
while True:
    resultat = resultat * num
    num = num - 1
    if num == 0:
        break
print("El factorial és", resultat)