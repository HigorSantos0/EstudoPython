equipamentos = []
valores = []
seriais = []
departamento = []

resposta = "S"

while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Numero social: ")))
    departamento.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

# for i in range (0, len(equipamentos)):

for i, equipamento in enumerate(equipamentos):
    print("\nEquipamento...: ", (i+1))
    print("Nome: ", equipamento)
    print("Valor: ", valores[i])
    print("Serial ", seriais[i])
    print("Departamento: ", departamento[i])
