# Fes un programa que imprimeixi per pantalla els números primers.
num = 1
i = 2
while i < num and num % i != 0:
    i += 1
    if i == num:
        print(num)
        num += 1
    else:
        num += 1