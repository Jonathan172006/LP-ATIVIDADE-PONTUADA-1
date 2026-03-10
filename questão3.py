import os

os.system("cls")

a = int(input("Digite o valor A: "))
b = int(input("Digite o valor B: "))


if a == b:

    c = a + b
    operacao = "soma"
else:

    c = a * b
    operacao = "multiplicação"

print("-" * 30)
print(f"Como os valores são {'iguais' if a == b else 'diferentes'}, o resultado da {operacao} é C 3= {c}")