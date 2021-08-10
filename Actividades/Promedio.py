def mean_value(values_list):
    suma = 0
    for value in values_list:
        suma += value
    return suma/len(values_list)


iteration = 0
list_number = []
while iteration < 5:
    number = input("digite un number : ")
    number = int(number)
    list_number.append(number)
    iteration = iteration + 1
mean = mean_value(list_number)
print("EL promedio de los valores es : ", mean)
