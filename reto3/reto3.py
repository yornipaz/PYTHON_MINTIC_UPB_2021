import os
# Funcion para limpiar la consola de comando en los dos sistemas operativos linux y windows
# Declaracion de variable globales para
current_password = 91615
user_id = 51619
ultimos_digitos = 619
column = 2
row = 3

latitud_sup = 6.284
latitud_inf = 6.077
longitud_sup = -75.841
longitud_inf = -76.049
iterator = -1
count_sessions = 0
start_coordinated = True
mesagge = ""
matrix_coordinates = []
menu_options_list = ["Cambiar contraseña",
                     "Ingresar coordenadas actuales",
                     "Ubicar zona wifi más cercana",
                     "Guardar archivo con ubicación cercana",
                     "Actualizar registros de zonas wifi desde archivo",
                     "Elegir opción de menú favorita",
                     "Cerrar sesión"]


def clear_console():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
# Funcion con el primer reto de sistema de inicio de sesión


def print_exit():
    print("Error")
    exit(0)


def print_lotecation_coordinates(matrix, long_pro, lat_pro):

    locations_sur = 0
    locations_oriente = 0
    for index_loc, coordinateds in enumerate(matrix):
        lat_current = coordinateds[0]
        long_current = coordinateds[1]
        if lat_current >= lat_pro and long_current <= long_pro:
            lat_pro = lat_current
            long_pro = long_current
            locations_oriente = index_loc
        if lat_current <= lat_pro and long_current <= long_pro:
            lat_pro = lat_current
            long_pro = long_current
            locations_sur = index_loc

    print("Coordenada ubicada más al sur ", (locations_sur+1))
    print("Coordenada ubicada más al oriente ", (locations_oriente+1))


def location_coordinates(matrix_locations):
    sum_latitudes = 0
    sum_longitudes = 0
    for locations in matrix_locations:
        for coordinates in locations:
            if coordinates % 2 == 0:
                sum_latitudes = sum_latitudes+coordinates
            else:
                sum_longitudes = sum_longitudes+coordinates

    pro_lat = sum_latitudes/3
    pro_lon = sum_longitudes/3
    print_lotecation_coordinates(matrix_locations, pro_lat, pro_lon)


def session_start():

    # TODO RF1.1 impresion del mensaje de bienbenida del recto de la semana 1.
    print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
    # TODO RF1.2A ingreso y validacion de la variable de nombre_usuario.
    nombre_usuario = input("Digite el nombre de usuario : ")
    nombre_usuario = int(nombre_usuario)
    if (nombre_usuario != user_id):
        print_exit()

    # TODO RF1.2B ingreso y validacion de la variable clave del clave_usuario.
    clave_usuario = input("Digite la clave de usuario : ")
    clave_usuario = int(clave_usuario)
    if (clave_usuario != current_password):
        print_exit()
    # TODO RF1.3 creacion del captcha seguridad.
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


def created_matrix_coordinates():
    new_coordinateds = []
    for i in range(row):
        new_coordinateds.append([])

        for j in range(column):
            if j % 2 == 0:
                coordinated = validate_coordinates(
                    "latitud", latitud_sup, latitud_inf)

            else:
                coordinated = validate_coordinates(
                    "longitud", longitud_sup, longitud_inf)

            new_coordinateds[i].append(coordinated)
    return new_coordinateds


def print_coordinateds(matrix_coordinates):
    for index, coordinated in enumerate(matrix_coordinates):
        print(f"coordenada [latitud,longitud] {index+1} : ", coordinated)


def update_password(current_password):
    new_password = input("Ingrese su nueva contraseña : ")
    new_password = int(new_password)
    if new_password != current_password and new_password > 0:
        pass_code = input("Confirmar la contraseña actual ")
        pass_code = int(pass_code)
        if pass_code == current_password and pass_code > 0:
            return new_password
        else:
            print_exit()
    elif new_password == 0:
        print_exit()
    else:
        print("Error")


def update_matrix_coordinates(matrix_update, index_update):
    for index in range(len(matrix_update[index_update])):
        if index % 2 == 0:
            matrix_update[index_update][index] = validate_coordinates(
                "latitud", latitud_sup, latitud_inf)
        else:
            matrix_update[index_update][index] = validate_coordinates(
                "longitud", longitud_sup, longitud_inf)
    return matrix_update


def validate_coordinates(type_coordinate, limit_sup, limit_inf):
    coordinated_input = float(input(f"Ingrese la {type_coordinate} : "))
    if coordinated_input >= limit_inf and coordinated_input <= limit_sup:
        pass

    else:
        print("Error coordenada")
        exit(0)
    return coordinated_input


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


while iterator != 7:
    # TODO CA2.1.2 El menú debe mostrarse en una lista ordenada por números.
    print_options_list(menu_options_list)
    # TODO CA2.1.3 El sistema debe mostrar el mensaje “Elija una opción” al final del menú para recibir las instrucciones del usuario.
    print("Elija una opción")
    iterator = input()
    iterator = int(iterator)
    count_sessions = count_sessions + 1
    # print("El contador esta :", count_sessions)

    # TODO RF2.2: El programa permite elegir una opción del menú como favorito.
    # El usuario solo podrá reordenar las primeras 5 opciones del menú
    if(iterator == 1):
        current_password = update_password(current_password)
        # print("New password : ", current_password)

    if iterator == 2:
        if start_coordinated:
            matrix_coordinates = created_matrix_coordinates()
            start_coordinated = False
        else:
            print_coordinateds(matrix_coordinates)
            location_coordinates(matrix_coordinates)
            print(
                "Presione 1, 2 ó 3 para actualizar la respectiva coordenada. Presione 0 para regresar al menú")
            select_up = input("")
            select_up = int(select_up)
            if select_up < 0 or select_up > 3:
                print("Error actualización")
                exit(0)
            elif select_up == 0:
                continue
            else:
                matrix_coordinates = update_matrix_coordinates(
                    matrix_coordinates, (select_up-1))
                print_coordinateds(matrix_coordinates)

    if(iterator == 3 or iterator == 4 or iterator == 5):
        pass
        # continue
    if iterator == 6:
        # TODO CA2.2.2 El programa deberá mostrar el mensaje “Seleccione opción favorita” después de acceder a esta funcionalidad.
        print("Seleccione opción favorita")
        index = input()
        index = int(index)
        if index >= 1 and index <= 5:
            # count_sessions = count_sessions + 1
            if count_sessions == 3:
                print_exit()

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
                # count_sessions = count_sessions + 1
                if count_sessions == 3:
                    print_exit()
                print("Error")
                print("Elija una opción")
                option = input()
                option = int(option)
                if option < 1 or option > 5:
                    print_exit()

            else:
                print(f"Usted ha elegido la opción {option}")
                exit(0)
            #  TODO CA2.2.3 El programa deberá mostrar el mensaje “Error” si el usuario elige una opción incorrecta(número diferente entre 1 y 5) y finalizar la ejecución del programa.
        if index < 1 or index > 5:
            print("Error")
            break
        # TODO RF2.5: El programa permite al usuario salir del menú.
    if count_sessions > 3:
        print_exit()


if iterator == 7:
    print("Hasta pronto")
    exit(0)
