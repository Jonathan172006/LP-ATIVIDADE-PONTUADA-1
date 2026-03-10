import os

os.system("cls")

nome_produto = input("Descrição do produto: ")
quantidade = int(input("Quantidade adquirida: "))
preco_unitario = float(input("Preço unitário: R$ "))

total_bruto = quantidade * preco_unitario

if quantidade <= 5:
    porcentagem_desconto = 0.02
elif quantidade <= 10:
    porcentagem_desconto = 0.03
else:
    porcentagem_desconto = 0.05

valor_desconto = total_bruto * porcentagem_desconto
total_a_pagar = total_bruto - valor_desconto

print("-" * 30)
print(f"Produto: {nome_produto}")
print(f"Total Bruto: R$ {total_bruto:.2f}")
print(f"Desconto: R$ {valor_desconto:.2f}")
print(f"Total a pagar: R$ {total_a_pagar:.2f}")
