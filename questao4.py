import os

os.system("cls")

morango_kg = float(input("Digite a quantidade de morangos em kg: "))
maca_kg = float(input("Digite a quantidade de maçãs em kg: "))

if morango_kg <= 5:
    preco_morango = morango_kg * 2.50
else:
    preco_morango = morango_kg * 2.50

if maca_kg <= 5:
    preco_maca = maca_kg * 1.8
else:
    preco_maca = maca_kg * 1.5

peso_total = morango_kg + maca_kg
valor_total = preco_morango + preco_maca

if peso_total > 10 or valor_total > 15.00:
    desconto = valor_total * 0.10
    valor_total = valor_total - desconto
else:
    valor_final = valor_total

print("-" * 30)
print(f"Peso total: {peso_total:.2f} kg")
print(f"Valor sem desconto: R$ {valor_total:.2f}")

if peso_total > 10 or valor_total > 15.00:
    print(f"Valor com desconto: R$ {desconto:.2f}")

print(f"Valor final a pagar: R$ {valor_total:.2f}")
print("-" * 30)