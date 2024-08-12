numeros = [24, 47, 14, 85, 15, 74, 36]

minimo = numeros[0]

for numero in numeros:
    if numero < minimo:
        minimo = numero

print("El valor mínimo es:", minimo)