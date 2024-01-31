# Programa que pregunta el nom de l'usuari i només dona la benvinguda si l'usuari es diu "Amilcar" o "Sila".
usuari1 = "Amilcar"
usuari2 = "Sila"
usuariusuari = input("Si us plau entreu el vostre nom d'usuari: ")
if usuariusuari == usuari1:
  print("Benvingut", usuari1)
elif usuariusuari == usuari2:
  print("Benvingut", usuari2)
else:
  print("Usuari incorrecte, reinicia el programa.")
