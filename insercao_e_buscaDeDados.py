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

busca = input("Digite qual equipamento deseja buscar: ")
for i, equipamento in enumerate(equipamentos):
    if busca.upper() == equipamento:
        print("Valor: ", valores[i])
        print("Serial: ", seriais[i])
