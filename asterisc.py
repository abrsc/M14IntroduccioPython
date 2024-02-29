pos_x = 0
pos_y = 0
AMPLADA = 20
ALTURA = 6
cadena_buida = "|" + " " * AMPLADA + "|"
cadena_vora = "-" * (AMPLADA+2)
while True:
    #genero cadena de text amb l'asterisc a la seva posició:
    cadena_asterisc = "|"
    for i in range(AMPLADA):
        if pos_x == i:
            cadena_asterisc += "*"
        else:
            cadena_asterisc += " "
    cadena_asterisc += "|"
    #imprimerixo l'asterisc:
    print(cadena_vora)
    for e in range(ALTURA+1):
        if pos_y == e:
            print(cadena_asterisc)
        else:
            print(cadena_buida)
    print(cadena_vora)
    #demano el moviment al user:
    moviment = input("")

    #aplico el moviment de l'usuari:
    if moviment == 'a' and pos_x > 0:
            pos_x -= 1
    elif moviment == 'd' and pos_x < AMPLADA-1:
            pos_x += 1
    elif moviment == 'w' and pos_y > 0:
            pos_y -= 1
    elif moviment == 's' and pos_y < AMPLADA:
            pos_y += 1

