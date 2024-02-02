# Programa que pregunta un número a l'usuari i diu si és senar o parell
num = int(input("Insereu un número si us plau: "))
resultat = num % 2
if resultat == 1:
  print("El número és senar.")
else:
  print("El número és parell.")
      
