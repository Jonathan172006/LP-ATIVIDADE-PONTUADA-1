import os 

os.system("cls")

nome = (input("Digite o nome da pessoa:"))
sexo = (input("Digite o sexo da pessoa: "))
estado_civil = (input("Digite o estado civil da pessoa: "))

tempo_casada = ""

if sexo == "Feminino" and estado_civil == "Casada":
    tempo_casada = input("Digite o tempo de casada: ")

print(f"Nome: {nome}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estado_civil}")

if tempo_casada != "":
    print(f"Tempo de Casada: {tempo_casada}")