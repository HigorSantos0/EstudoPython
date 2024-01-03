# Inventário

inventário = []
resposta = "S"

# Inserindo dados na lista
while resposta == "S":
    inventário.append(input("Equipamento: "))
    inventário.append(float(input("Valor: ")))
    inventário.append(int(input("Numero social: ")))
    inventário.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

print(" Elementos da lista ")
for lista in inventário:
    print(lista)
