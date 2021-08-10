# TODO funcion para imprimir menu con las opciones
def print_menu(options_list):
    for option in options_list:
        print(option)
# TODO funcion para evaluar las opcion escojida pasandole el valor de las dos variables y la opcion del menu a realizar


# TODO arreglo con las opciones del menu
options = [
    "1. Saludar", "2. Es par", "3. Promedio ", "4.Módulo", "5.  Porcentaje ", "6. Potencia", "0.Salir"
]

sentry = -1

while sentry != 0:
    print_menu(options)
    sentry = input(" Escoja la operacion a realizar : ")
    sentry = int(sentry)
