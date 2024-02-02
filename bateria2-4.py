# Programa que pregunta la nota a l'usuari i segons la nota diu el resultat obtingut: 1 a 4 - Insuficient, 5 - Suficient, 6 - Bé, 7 a 8 - Notable, 9 a 10 - Excel·lent.
nota = float(input("Entreu la vostre nota d'examen per evaluar-la si us plau: "))
if nota <= 4 and nota > 0:
  print("Insuficient")
elif nota == 5:
  print("Suficient")
elif nota == 6:
  print("Bé")
elif nota == 7 or nota == 8:
  print("Notable")
elif nota == 9 or nota == 10:
  print("Excel·lent")
else:
  print("La nota no pot ser inferior a 0 ni superior a 10.")
