# Fes un programa que pregunta un número de telèfon i contesta "El número és vàlid" si té 9 caràcters i "El número no és vàlid" en cas contrari.
while True:
    numero = input("Si us plau, entres el teu numero de tel.: ")
    if len(numero) == 9:
        print("El nùmero és correcte!")
        break
    else:
        print("El nùmero NO és correcte, verifica que hi ha 9 nùmeros.")