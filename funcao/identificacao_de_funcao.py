def preencherInvetario(lista):
    resposta = "S"
    while resposta == "S":
        equipamentos = [
            input("Equipamento: "),
            float(input("Valor: ")),
            int(input("Numero social: ")),
            input("Departamento: ")]

        lista.append(equipamentos)
        resposta = input("Digite \"S\" para continuar: ").upper()


def exibirInventario(lista):
    for elemento in lista:
        print("Nome..........: ", elemento[0])
        print("Valor.........: ", elemento[1])
        print("Serial........: ", elemento[2])
        print("Departamento..: ", elemento[3])


def localizaPorNome(lista):
    busca = input("Digite qual equipamento deseja buscar: ")
    for elemento in lista:
        if busca == elemento[0]:
            print("Valor: ", elemento[1])
            print("Serial: ", elemento[2])


def depreciacaoPorNome(lista, porc):
    depreciacao = input("\nDigite o nome do equipamento que será depreciado: ")
    for elemento in lista:
        if depreciacao == elemento[0]:
            print("Valor antigo: ", elemento[1])
            elemento[1] = elemento[1] * (1-porc/100)
            print("Novo valor: ", elemento[1])


def excluirPorSerial(lista):
    serial = int(input("\nDigite o serial do equipamento que será excluido: "))
    for elemento in lista:
        if elemento[2] == serial:
            lista.remove(elemento)
    return "itens excluidos!"


def resumirValores(lista):
    valores = []
    for elemento in lista:
        valores.append(elemento[1])
    if len(valores) > 0:
        print("O equipamento mais caro custa: ", max(valores))
        print("O equipamento mais barato custa: ", min(valores))
        print("O total de equipamentos é de: ", sum(valores))
    else:
        print("Feito, agora sua lista está vazia!")
