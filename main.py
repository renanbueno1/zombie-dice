import random

print("ZOMBIE DICE (Protótipo Semana 4)")
print("Seja bem-vindo ao jogo Zombie Dice!")
print()
# Iniciando a variável com 0
numJogadores = 0
# Criando a estrutura enquando, dependendo do valor especificado
while numJogadores < 2:
    # Programação defensiva. Exemplo: caso o usuário insira uma letra, apresentar msg de valor inválido.
    try:
        numJogadores = int(input("Informe a quantidade de jogadores: "))
        if numJogadores < 2:
            print("AVISO: Você precisa de pelo menos 2 jogadores!\n")
    except ValueError:
        print("Valor inválido")
print() # Pulando linha
# Criando lista de jogadores
listaJogadores = []
# Adicionando na lista, n jogadores, que contém na variável numJogadores
for i in range(numJogadores):
    nome = input("Informe o nome do jogador " + str(i + 1) + ": ")
    listaJogadores.append(nome)

print("Jogadores:")
for i, item in enumerate(listaJogadores):
    print(str(i+1) + " " + item)

dadoVerde = "CPCTPC"
dadoAmarelo = "TPCTPC"
dadoVermelho = "TPTCPT"

listaDados = [dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde,
              dadoAmarelo, dadoAmarelo, dadoAmarelo, dadoAmarelo,
              dadoVermelho, dadoVermelho, dadoVermelho]
print() # Pulando linha
print("Iniciando o jogo...")
print() # Pulando linha
jogadoAtual = 0
dadosSorteados = []
tiros = 0
cerebros = 0
passos = 0

while True:

    print("TURNO DO JOGADOR", listaJogadores[jogadoAtual])
    # Como são 3 dados a ser retirados, cria-se um for com condição 3.
    inicio = input("Pressione enter para jogar os dados:")

    for i in range(0, 3, 1):
        # Sorteando um número de 0 a 11. 12 possibilidades no total.
        numSorteado = random.randrange(0, 12)
        dadosSorteado = listaDados[numSorteado]

        if dadosSorteado == "CPCTPC":
            corDado = "VERDE"
        elif dadosSorteado == "TPCTPC":
            corDado = "AMARELO"
        else:
            corDado = "VERMELHO"
        print("Dado sorteado: ", corDado)
        dadosSorteados.append(dadosSorteado)

    print("As faces sorteadas foram: ")

    for dadosSorteado in dadosSorteados:

        numFaceDado = random.randrange(0, 5)

        if dadosSorteado[numFaceDado] == "C":
            print("- CÉREBRO (Você comeu um cérebro)")
            cerebros += 1
        elif dadosSorteado[numFaceDado] == "T":
            print("- TIRO (Você levou um tiro)")
            tiros += 1
        else:
            print("- PASSOS (Uma vítima escapou)")
            passos += 1

    print("SCORE ATUAL: ")
    print("CÉREBROS: ", cerebros)
    print("TIROS: ", tiros)
    print("PASSOS: ", passos)

    continuarTurno = input("Aviso: Você deseja continuar jogando dados? (s=sim / n=não)")

    if continuarTurno == "n":

        jogadoAtual += 1
        dadosSorteados = []
        tiros = 0
        cerebros = 0
        passos = 0

        if jogadoAtual == listaJogadores[2]:
            print("Finalizando protótipo do jogo...")
            break
    else:
        print("Iniciando mais uma rodada do turno atual...")
        dadosSorteados = []


