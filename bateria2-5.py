# Fes un programa que pregunti quants anys portes treballant de programador i et digui que ets junior si portes menys de 5 anys i senior si portes més de 5.
antiguitat = int(input("Entreu el número d'anys d'expèriencia que tens: "))
if antiguitat < 5:
    print("Ets junior!")
else:
    print("Ets senior.")