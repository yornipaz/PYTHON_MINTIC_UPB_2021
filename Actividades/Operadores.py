import random
x = 23
y = 10
edges = 131
is_employ = True
name = "Andres"
ready = False
generate = 'H'
salary = 1500.34
discount_help = 100

suma = (x+y+edges+100)
print("Suma : ", suma)
rest = suma - 2334
print("Resta : ", rest)
part = random(1, 432)
if part % 2 == 0:
    print("es par el numero : ", part)
else:
    print("es inpar el numero : ", part)
division = salary/20
print(" El valor de su dia de trabajo es : ", division)
compared = ready or is_employ
print(compared)
compared = is_employ and ready
print(compared)

mutipicacion = (division*salary)
print("el salario  de este mes es : ", mutipicacion)

print("el salario  de este mes es : ", mutipicacion**y)
print("el salario  de este mes es : ", (mutipicacion/x)-(x**y))
print("el salario  de este mes es : ", (mutipicacion)-(x**y))
print("el salario  de este mes es : ", (mutipicacion % x)+(discount_help**y))
print("el salario  de este mes es : ", (8/x)/(y))

print("el la solucion es : ", mutipicacion**y)
print("el la solucion es : ", (mutipicacion/x) % (x**y))
print("el la solucion es : ", (56 % 3)+(x**y))
print("el la solucion es : ", (676 % x)+(discount_help**y))
print("el la solucion es : ", (8/x)/(y))


print("el la solucion es : ", x*y-division+salary)
print("el la solucion es : ", (mutipicacion/x-78)-(x**y))
print("el  la solucion es  ", (5-x/y+salary)-(x**y))
print("el la solucion es : ", (is_employ or ready) and ready)
print("el la solucion es : ", not ready)
