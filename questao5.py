import os

os.system("cls")

operacao = input("Digite a operação desejada (+, -, *, /): ")
a = int(input("Digite o valor A: "))
b = int(input("Digite o valor B: "))

if operacao == "+":
    resultado = a + b
elif operacao == "-":
    resultado = a - b
elif operacao == "*":
    resultado = a * b
elif operacao == "/":
    resultado = a / b
else:
    print("Operação inválida.")
    resultado = None

if resultado is not None:
    print(f"O resultado da operação {operacao} entre {a} e {b} é: {resultado}")