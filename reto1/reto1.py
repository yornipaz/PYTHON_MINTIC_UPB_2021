# TODO RF1 impresion del mensaje de bienbenida del recto de la semana 1.
print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
# TODO RF2A ingreso y validacion de la variable de nombre_usuario.
nombre_usuario = input("Digite el nombre de usuario : ")
nombre_usuario = int(nombre_usuario)
if (nombre_usuario != 51619):
    print("Error")
    exit(0)

# TODO RF2B ingreso y validacion de la variable clave del clave_usuario.
clave_usuario = input("Digite la clave de usuario : ")
clave_usuario = int(clave_usuario)
if (clave_usuario != 91615):
    print("Error")
    exit(0)
# TODO RF3 creacion del captcha seguridad.
ultimos_digitos = 619
# TODO RF3A creacion de operaciones aritméticas para el antepenultimo numero.
penultimo_digito = 6-5/1+9 % 1
penultimo_digito = 9-(6+1+1)
penultimo_digito = 5*9 % 1 + 1
# TODO RF3B imprimir y leer el captcha.
valor_captcha = input("619 + 1 = ")
# TODO RF4 confirmacion de ingreso al sistema con un mensaje de éxito en el inicio de sesión.
if (int(valor_captcha) == (ultimos_digitos+penultimo_digito)):
    print("Sesión iniciada")
else:
    print("Error")
