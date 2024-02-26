# Pregunta a l'usuari dos valors i intenta sumar-los. Utilitza try i except per capturar errors quan els valors no són números.
num1 = input("Entreu el primer nùmero per la suma: ")
num2 = input("Entreu el segon nùmero per la suma: ")
try:
    print("El resultat és: ", float(num1)+float(num2))
except:
    print("Error, s'ha de entrar números.")