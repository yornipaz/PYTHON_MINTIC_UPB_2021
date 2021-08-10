import os
# Funcion para limpiar la consola de comando en los dos sistemas operativos linux y windows


def clear_console():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
# Funcion con el primer reto de sistema de inicio de sesión


def session_start():
    # TODO RF1.1 impresion del mensaje de bienbenida del recto de la semana 1.
    print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
    # TODO RF1.2A ingreso y validacion de la variable de nombre_usuario.
    nombre_usuario = input("Digite el nombre de usuario : ")
    nombre_usuario = int(nombre_usuario)
    if (nombre_usuario != 51619):
        print("Error")
        exit(0)

    # TODO RF1.2B ingreso y validacion de la variable clave del clave_usuario.
    clave_usuario = input("Digite la clave de usuario : ")
    clave_usuario = int(clave_usuario)
    if (clave_usuario != 91615):
        print("Error")
        exit(0)
    # TODO RF1.3 creacion del captcha seguridad.
    ultimos_digitos = 619
    # TODO RF1.3A creacion de operaciones aritméticas para el antepenultimo numero.
    penultimo_digito = (6-5/1+9 % 1)+(9-(6+1+1))-(5*9 % 1 + 1)
    # TODO RF1.3B imprimir y leer el captcha.
    valor_captcha = input("619 + 1 = ")
    # TODO RF1.4 confirmacion de ingreso al sistema con un mensaje de éxito en el inicio de sesión.
    if (int(valor_captcha) == (ultimos_digitos+penultimo_digito)):
        print("Sesión iniciada")
    else:
        print("Error")

# funcion para imprimir las opciones del menu


def print_options_list(lists_options):

    for index, option in enumerate(lists_options):
        print((index+1), ".", option)


def organize_list_favorite(list_favorites, index):
    first_option = list_favorites[0]
    index_option = list_favorites[index]
    list_favorites[0] = index_option
    list_favorites[index] = first_option
    return list_favorites

# TODO Recto 2: Son los reauqrimientos asociados al recto 2, en el cual se toma en cuenta el primer recto
# TODO RF2.1 El programa muestra el siguiente menú de opciones en consola para el uso del programa


# TODO CA2.1.1 El menú debe visualizarse completo en consola después de iniciar sesión(Reto  # 1).
session_start()
# clear_console()
iterator = -1
count_sessions = 0
menu_options_list = ["Cambiar contraseña",
                     "Ingresar coordenadas actuales",
                     "Ubicar zona wifi más cercana",
                     "Guardar archivo con ubicación cercana",
                     "Actualizar registros de zonas wifi desde archivo",
                     "Elegir opción de menú favorita",
                     "Cerrar sesión"]

while iterator != 7:
    # TODO CA2.1.2 El menú debe mostrarse en una lista ordenada por números.
    print_options_list(menu_options_list)
    # TODO CA2.1.3 El sistema debe mostrar el mensaje “Elija una opción” al final del menú para recibir las instrucciones del usuario.
    print("Elija una opción")
    iterator = input()
    iterator = int(iterator)
    count_sessions = count_sessions + 1
   #print("El contador esta :", count_sessions)

    # TODO RF2.2: El programa permite elegir una opción del menú como favorito.
    # El usuario solo podrá reordenar las primeras 5 opciones del menú
    if(iterator == 1 or iterator == 2 or iterator == 3 or iterator == 4 or iterator == 5):
        pass
        # continue
    if iterator == 6:
        # TODO CA2.2.2 El programa deberá mostrar el mensaje “Seleccione opción favorita” después de acceder a esta funcionalidad.
        print("Seleccione opción favorita")
        index = input()
        index = int(index)
        if index >= 1 and index <= 5:
            #count_sessions = count_sessions + 1
            if count_sessions == 3:
                print("Error")
                exit(0)
            # TODO CA2.2.1 El usuario solo podrá reordenar las primeras 5 opciones del menú; elegir opción favorita y cerrar sesión siempre deben aparecer al final.
            print(
                "Si tengo 3  peces y regalo dos y suelto uno en mi pecera ¿ cuantos peces me quedan?")
            question_one = input()
            question_one = int(question_one)
            if question_one != 1:
                print("Error")
                continue
            print(
                "Si tengo 9  peces y se me ahogan los nueve peces  ¿ cuantos peces me quedan?")
            question_two = input(
            )
            question_two = int(question_two)
            if question_two != 9:
                print("Error")
                continue
            menu_favorite = organize_list_favorite(
                menu_options_list, (index+1))
            clear_console()
            print_options_list(menu_favorite)
            print("Elija una opción")
            option = input()
            option = int(option)
            if option < 1 or option > 5:
                ##count_sessions = count_sessions + 1
                if count_sessions == 3:
                    print("Error")
                    exit(0)
                print("Error")
                print("Elija una opción")
                option = input()
                option = int(option)
                if option < 1 or option > 5:
                    print("Error")
                    exit(0)

            else:
                print(f"Usted ha elegido la opción {option}")
                exit(0)
            #  TODO CA2.2.3 El programa deberá mostrar el mensaje “Error” si el usuario elige una opción incorrecta(número diferente entre 1 y 5) y finalizar la ejecución del programa.
        if index < 1 or index > 5:
            print("Error")
            break
        # TODO RF2.5: El programa permite al usuario salir del menú.
    if count_sessions > 3:
        print("Error")
        exit(0)

if iterator == 7:
    print("Hasta pronto")
    exit(0)
