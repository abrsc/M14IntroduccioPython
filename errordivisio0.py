# Pregunta a l'usuari dos nombres i divideix-los. Utilitza un bloc try i except per evitar l'error de divisió per zero.
while True:
    num1 = input("Si us plau entreu el primer número a dividir: ")
    num2 = input("Si us plau entreu el segon número a dividir: ")
    try:
        print(num1, "/",num2,"= ", float(num1)/float(num2))
        break
    except:
        print("No es pot dividir per zero i s'ha de escrir números!")