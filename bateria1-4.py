# Programa que demana un pes en kg a l'usuari i retorna el mateix pes convertit en lliures.
MASSALLIURES = 0.45359237
peskg = input("Si us plau, entreu un pes en KG: ")
resultat = float(peskg) / MASSALLIURES
print(peskg, "fa", resultat, "lliures.")
