import daus

def menu():
    print("""----------------------------------
Que vols fer?
1. Llençar un dau de 6 cares.
2. Llençar més d'un dau de 6 cares.
3. Llençar un dau de cares definides per usuari.
4. Llençar més d'un dau de cares definides per usuari.
0. Sortir.
""")
while True:
    menu()
    opcio  = input("Tria la vostre opció: ")
    if opcio == "1":
        daus.dau_6()
    elif opcio == "2":
        daus.daus_6()
    elif opcio == "3":
        daus.dau_x()
    elif opcio == "4":
        daus.daus_x()
    elif opcio == "0":
        break
    else:
        print("S'ha de triar una opció entre 0 i 4!")


            
