import os
os.system("cls")

PRECO_GASOLINA = 6.59
PRECO_ALCOOL = 3.79

litros = float(input("Digite o número de litros vendidos: "))
tipo = input("Digite o tipo de combustível (A-álcool, G-gasolina): ").strip().upper()

valor_total = 0

if tipo == 'A':
    if litros <= 25:
        valor_total = litros * (PRECO_ALCOOL * 0.98)
    else:
        valor_total = litros * (PRECO_ALCOOL * 0.96)

elif tipo == 'G':
    if litros <= 25:
        valor_total = litros * (PRECO_GASOLINA * 0.97)
    else:
        valor_total = litros * (PRECO_GASOLINA * 0.95)

else:
    print("Tipo de combustível inválido!")

if valor_total > 0:
    print("-" * 30)
    combustivel_nome = "Álcool" if tipo == 'A' else "Gasolina"
    print(f"Combustível: {combustivel_nome}")
    print(f"Quantidade: {litros} litros")
    print(f"VALOR A SER PAGO: R$ {valor_total:.2f}")
    print("-" * 30)