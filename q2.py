media = int(input("Digite a média final (Entre 0 e 100): "))
if media >= 90:
    conceito = "A"
elif media >= 70:
    conceito = "B"
else:
    conceito = "C"
print(f"O conceito do aluno é: {conceito}")