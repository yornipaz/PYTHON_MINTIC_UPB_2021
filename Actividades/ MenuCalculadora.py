# TODO funcion para imprimir menu con las opciones
def print_menu(options_list):
    for option in options_list:
        print(option)
# TODO funcion para evaluar las opcion escojida pasandole el valor de las dos variables y la opcion del menu a realizar


def evaluate_operation(val1, val2, option):
    if option == 1:
        sum_values = val1 + val2
        print(f"La suma de los dos valores es :  {sum_values}")
    elif option == 2:
        res = val1-val2
        print(f"La resta de los dos valores es : {res}")
    elif option == 3:
        mul = val1*val2
        print("La multiplicación de los dos valores es : ", mul)
    elif option == 4:
        div = val1/val2
        print(f"La division de los dos valores es : {div}")
    elif option == 5:
        pot = val1**val2
        print(f"La potencia del valor 1 elevado al valor 2  es :  {pot}", )
    elif option == 6:
        print("                 ..: : : : ..          .., ; ; , , .")
        print("       ::::::::::::.    .::t$$$$$$$$bu:,.                .zn$$$$k")
        print("      ::::d$$$$bi::::.,::::$$$$$$$$$$$$i::.            ur:d$$$$$$F")
        print("     ::::$$$$$$$$$L::::::::3$$$$$'zec`$$$d$,           ?$,\"bd$$$$.")
        print("     `:::3$$$$$$$$$;::::::::?$$$$ `\"$$`$$$$?,           4='$b'ue$\"")
        print("      ::::$$$$$$$$$$:::::uee$$$$$L. `?:$$$$`?k           4$bedP\"")
        print("       ::::$$$$$\"""?:::z$$$$$$$$$$$$bu$$P""-.?,      zMMbu'""")
        print("        `:::\"'.;::::::d$$$$$$$$$C73$$$$$$;    `b ,MUMMMMMMMM")
        print("          ueeeeec, i." "$$$$$$$$$$$ `?$$$$$$; , ., d$F; MMMMMMMMF")
        print("      ,eMMMMMMMMMMMc`!;\"$$$$$$$$$.   \"?$$$$$$$$F,MMMMMMMP\"")
        print(",eM6\"TMMMMMMMMMMMMb`!i; \"$$$$$$$$ %,   .ueeP\',dMMMMMM\"")
        print("zMMMMMMc'MMMMP,c,_??Mk`!!;.?$$$$F$$buued$$F,dM?MMMMM\"")
        print("MMMMMMMMMP\"MM\"d$$(?$b'ML`!!!;`?$$$bCCCdP\"; MMM'dMMP\"")
        print("TMMMMMF,d\"ze$$$$?be ;MML`!!!!;`?$$P\",;!!'dMM\"P\"")
        print(".\"?PP,$'$$$$$$$LF\";MMMMb`!!!!!i;,,;i!!\'dMMF")
        print("',dMMMF")
        print(". +dMMMMMMMMMMMMMeeeeedMMMMMM\"")
        print(":!!!!!!  `!!!!!'''` c,\"TMMMMMMMMMMMMMMMMMMPF\"")
        print(":!!!!!!'     `!'udNu`>.\"$br`TMMMMMMMMPP""\",")
        print("!!!!!!         :MMMMb`!!;,'     ;""ii!>;i!")
        print("'!!!!'          4MMMMM, JMMMMMM`!!!!!!>'     i!!'")
        print("!         :!! 4MMMMMMMh..zeee'    i!!'")
        print(":!!!:`MMMMMMP:MMMM\"")
        print("!!!!! `TMMP,dMMP\"")
        print("'''  \`?bdMMP\"")
        print("  ;!!!;.'\"")
        print(" ;!!!!!!\'")
        print("''!!'`")
    elif option == 7:
        print("Chauuuu")
        exit(0)
    else:
        print("Digite una opcion valida")


# TODO arreglo con las opciones del menu
options_calculated = [
    "1. Sumar", "2. Restar", "3. Multiplica ", "4. Dividir", "5. Potenciar ", "6. Decoracion", "7.Salir"
]
option = 0
# TODO ciclo para evaluar las operacion a realizar
while option != 7:
    # TODO lectura entradas de las dos variables a evaluar
    val1 = input("Ingrese un numero a evaluar : ")
    val2 = input("Ingrese otro numero a evaluar : ")
    # TODO conversion de las entradas a numero flotante
    val2 = float(val2)
    val1 = float(val1)
    # TODO imprimir el menu
    print_menu(options_calculated)
    # lectura de la opcion escojida
    option = input(" Escoja la operacion a realizar : ")
    # TODO conversion de las entradas a numero entero
    option = int(option)
    # TODO llamado de la funcion para evaluar la opcion y sus valores de sus variables
    evaluate_operation(val1, val2, option)
