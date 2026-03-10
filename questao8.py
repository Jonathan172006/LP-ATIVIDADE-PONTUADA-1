import os

os.system("cls")

cor = input("Digite a cor do CD(verde, azul, amarelo, vermelho):")

if cor == "verde":
    preco = 10.00
elif cor == "azul":
    preco = 20.00
elif cor == "amarelo":
    preco = 30.00
elif cor == "vermelho":
    preco = 40.00
else:
    preco = None

if preco is not None:
    print(f"Preço do CD {cor}: R$ {preco:.2f}")
else:
    print("Cor do CD inválida.")