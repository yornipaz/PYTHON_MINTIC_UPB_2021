x = int(input("ingrese el valor de la x : "))
y = int(input("ingrese el valor de la y : "))
z = int(input("ingrese el valor de la z : "))
part_one_one = pow(((x**2)+z), (1/3))
part_one = (2*(x**2)+part_one_one-pow(z, 3))
part_two_one = ((z+x)/(3*x*y*z))
part_two = 1+part_two_one+(3*z)
ecuacion = part_one/part_two

print("Solucion ala ecuacion es : ", ecuacion)
