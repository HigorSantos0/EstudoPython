nome = input("Entre com o nome: ")
idade = int(input("Digite sua idade: "))
prioridade = input("Suspeita de doenca? ").upper()

if (idade >= 65):
    print("O paciente ", nome, "possui atendimento prioritario")
elif prioridade == "SIM":
    print("O paciente ", nome, "deve ser direcionada para a sala de agenda reservada")
else:
    print("O paciente ", nome,
          "nao possui agenda reservada e deve aguardar na sala de espera comum")
