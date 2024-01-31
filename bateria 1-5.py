# Programa que demana una temperatura en graus Celsius a l'usuari i retorna la temperatura en graus Fahrenheit.
FORMULAFAHRENHEIT1 = 1.8
FORMULAFAHRENHEIT2 = 32
celsius = input("Si us plau, entreu la temperatura en Celsius: ")
resultat = float(celsius) * FORMULAFAHRENHEIT1 + FORMULAFAHRENHEIT2
print(celsius, "fa", resultat, "en Fahrenheit.")
