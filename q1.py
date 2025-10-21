idade = int(input("Digite sua idade: "))
if idade > 0 and idade <= 12:
    print("Criança")
elif idade > 12 and idade <= 17:
    print("Adolescente")
else: 
    print("Adulto")