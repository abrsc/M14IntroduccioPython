import random

def dau_6():
    dau6 = random.randint(1,6)
    print(dau_6)

def daus_6():  
    pregunta = int(input("Quants daus has de llençar?: "))
    for i in range(0, pregunta):
        daus6 = random.randint(1,6)
        print(daus6)

def dau_x():
    cares = int(input("Quants cares té el dau?: "))
    daux = random.randint(1,cares)
    print(daux)

def daus_x():
    numerodaus = int(input("Quants daus has de llençar?: "))
    cares = int(input("Quants cares té el dau?: "))
    for i in range(0, numerodaus):
        dausx = random.randint(1,cares)
        print(dausx)

programa1 = random.randint(1,6)


