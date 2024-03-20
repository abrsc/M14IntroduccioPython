# Fes un programa que pregunta un número i et retorna tots els números que són divisors del número (els que la seva divisió no té residu).
num = int(input("Si us plau, escriu un número: "))
divisor = num
print("Els divisors de", num,"són: ")
for i in range(num):
    if num % divisor == 0:
        print(divisor)
        divisor -= 1
    else:
        divisor -= 1
