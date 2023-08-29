# Função para Criar uma lista ordenada:
def listaOrdenada(filename):
    # defino a quantidade:
    quantidade = int(input('Informe a quantidade: '))

    # abro/crio arquivo:
    arquivo = open(filename, 'w')

    # escrevo dentro do arquivo, através do laço FOR:
    for elemento in range(1, quantidade + 1):
        arquivo.write(str(elemento) + ' ; ')

    # fecho o arquivo:
    arquivo.close()

    # chamo a função lerArquivo:
    lerArquivo(filename)


# Função para leitura do arquivo:
def lerArquivo(filename):
    # abrir o arquivo:
    arquivo = open(filename, 'r')

    # atribuir a leitura do arquivo a uma variável:
    conteudo = arquivo.read()

    # exibir o conteúdo na tela
    print(conteudo)

    # fecho arquivo:
    arquivo.close()


# Chamada da função.
listaOrdenada('crescente.txt')
