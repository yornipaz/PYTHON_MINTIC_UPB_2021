n = input(
    "Digite el numero n:"
)
n = int(n)
i = 2
suma = 0
if n > 2:
    while i <= n:
        suma = suma+i
        i = i+2

    print("la suma de los par es :", suma)
elif n <= 2:
    print("n debe ser mayor que 2 ")
    n = input(
        "Digite el numero n:"
    )
