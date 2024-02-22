import random

def dau_6():
    dau6 = random.randint(1,6)
    print("El result és: ", dau6)

def daus_6():  
    pregunta = int(input("Quantes daus has de llençar?: "))
    print("Els results són: ")
    for i in range(0, pregunta):
        daus6 = random.randint(1,6)
        print(daus6)

def dau_x():
    cares = int(input("Quantes cares té el dau?: "))
    daux = random.randint(1,cares)
    print("El result del vostre dau a",cares, "cares és: ", daux)

def daus_x():
    numerodaus = int(input("Quantes daus has de llençar?: "))
    cares = int(input("Quantes cares té el dau?: "))
    print("Els results són: ")
    for i in range(numerodaus):
        print(random.randint(1,cares))

programa1 = random.randint(1,6)

