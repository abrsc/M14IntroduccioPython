#És una calculadora amb selecció etc..
from colorama import Fore, Back, Style
while True:
    print(Style.RESET_ALL)
    print("""Benvinguts a pycalc, introduiu una de les següents opcions:
0. Sortir
1. Sumar
2. Restar
3. Multiplicar
4. Dividir""")
    seleccio = input("La vostre opció: ") #Lo que l'usuari ha d'entrar per seleccionar entre un metodi de càlcul.
    if seleccio == "0": #Permet de decidir quina acció fer en funció de l'input que l'usuari va introduir abans.
        print("Adeu!")
        break
    elif seleccio == "1":
        numero1 = float(input(Fore.CYAN + "Introdueix el primer número: ")) #Pregunta el primer número del calcul (Fore.Color per poner en color el foreground).
        numero2 = float(input("Introdueix el segon número: ")) #Pregunta el segon número del calcul
        print("La suma de", numero1, "+", numero2, "és: ", numero1 + numero2) #Fa el calcul necessari i lo mostra a l'usuari.
    elif seleccio == "2":
        numero1 = float(input(Fore.LIGHTGREEN_EX + "Introdueix el primer número: "))
        numero2 = float(input("Introdueix el segon número: "))
        print("La suma de", numero1, "-", numero2, "és: ", numero1 - numero2)
    elif seleccio == "3":
        numero1 = float(input(Fore.MAGENTA + "Introdueix el primer número: "))
        numero2 = float(input("Introdueix el segon número: "))
        print("La suma de", numero1, "*", numero2, "és: ", numero1 * numero2)
    elif seleccio == "4":
        while True: #Permet de tornar a elegir números si el usuari decide de dividir per 0.
            numero1 = float(input(Fore.YELLOW + "Introdueix el primer número: ")) 
            numero2 = float(input( "Introdueix el segon número: "))
            if numero2 == 0: #Comprova que l'usuari no intenta de dividir per 0.
                print(Fore.RED + "No es pot dividir per 0!")
            else:
                print("La suma de", numero1, "/", numero2, "és: ", numero1 / numero2)
                break #Permet de tornar al primer bucle.
    else:
        print(Fore.RED + "Assegureu-vos que heu escrit un número vàlid.") #Codi d'error si el usuari sel·lecionna un número invalid.
