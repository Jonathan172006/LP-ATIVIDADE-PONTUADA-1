import os

os.system("cls")

valor_A = input("Digite o valor A: ")
valor_B = input("Digite o valor B: ")
valor_C = input("Digite o valor C:")

soma = valor_A + valor_B 

if soma <= valor_C:
    print("A soma de A e B é menor que o valor C")
else:
    print("A soma é maior que o valor C")
