pares = 0
impares = 0
for i in range(1, 16): 
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"Total de números pares: {pares}") 
print(f"Total de números ímpares: {impares}")