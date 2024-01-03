from identificacao_de_funcao import *

minhaLista = []
print("Preenchendo")
preencherInvetario(minhaLista)
print("Exibindo!")
exibirInventario(minhaLista)

print("Pesquisando")
localizaPorNome(minhaLista)
print("Alterando")
depreciacaoPorNome(minhaLista, 20)

print("Excluindo por série!")
excluirPorSerial(minhaLista)

print("Resumindo")
resumirValores(minhaLista)
