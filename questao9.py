import os

os.system("cls")

renda_mensal = float(input("Digite a renda mensal do solicitante: R$"))
valor_emprestimo = float(input("Digite o valor total do empréstimo: R$"))
num_prestacoes = int(input("Digite o número de prestações desejadas: "))

valor_prestacao = valor_emprestimo /num_prestacoes
limite_emprestimo = renda_mensal * 10
limite_prestacao = renda_mensal * 0.30

print("-" * 35)
print(f"Valor da prestação calculada: R$ {valor_prestacao:.2f}")

if valor_emprestimo <= limite_emprestimo and valor_prestacao <= limite_prestacao:
    print("SITUAÇÃO: emprestimo pode ser CONCEDIDO.")
else:
    print("SITUAÇÃO: Empréstimo NÃO CONCEDIDO.")

    if valor_emprestimo > limite_emprestimo:
        print("- Motivo: O valor total excede 10 vezes a renda.")
    if valor_prestacao > limite_prestacao:
        print("- Motivo: A prestação excede 30% da renda mensal.")
print("-" * 35)