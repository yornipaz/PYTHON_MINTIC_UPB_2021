from random import choices

frases = []
actores = ["schwarzenegger", "pacino", "gibson", "Gadot"]
frutas = ["mango", "pera", "manzana", "fresa"]
deportes = ["futbol", "baloncesto", "ciclismo", "natacion"]
frases.append(actores)
frases.append(frutas)
frases.append(deportes)

# Este programa solo funciona con una palabra
secreto = None  # "Cafe Tacuba" #"Metallica"
progreso = None
letra = None
temp = None
cont = 0
bandera = False

while True:

    opcion = input(
        "Seleccione la categoria asi:\n1. Actores\n2. Frutas\n3. Deportes\n4. Salir\n>")

    if opcion == "1":
        bandera = True
        secreto = choices(frases[0])[0]

    if opcion == "2":
        bandera = True
        secreto = choices(frases[1])[0]

    if opcion == "3":
        bandera = True
        secreto = choices(frases[2])[0]

    if opcion == "4":
        break

    if bandera:
        secreto = secreto.lower()
        progreso = (len(secreto)*"_ ").split()

        while True:
            letra = input("Ingrese una letra ")

            if len(letra) == 1:
                if secreto.find(letra) != -1:
                    temp = ""
                    cont = 0

                    for i in secreto:
                        if i == letra:
                            progreso[cont] = i
                        cont += 1
                    print(" ".join(progreso))

                    if "".join(progreso) == secreto:
                        print("¡Gano!")
                        break
                else:
                    print("Mostrar error")
            else:
                print("Letra no valida")
