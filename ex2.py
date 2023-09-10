"""
    JOGO DA VELHA COM CAMPO DINÂMICO
    ALUNO: WILLIAM DALLA STELLA DOS SANTOS

    ESTRUTURAS USADAS:
        Faz uso de listas e tuplas.
            Usa listas de listas.

    ETAPAS:
        Pede para o usuário colocar quantas colunas e quantas linhas ele quer.

        Pede para o usuário colocar a célula que ele quer jogar.

        Em seguida a máquina irá jogar.
            A máquina possui uma inteligência que segue a seguinte estratégia:
                Simula sua jogada em cada célula e verifica se ela irá ganhar com essa jogada, se sim, ela joga.

                Se não ganhar com a jogada, ela faz a mesma coisa porém simulando a jogada do jogador.
                    Se o jogador for ganhar com determinada jogada, a máquina joga nessa célula para bloquar o jogador.

                Se ela e nem o jogador ganhar, ela joga aleatoriamente.

        A cada jogada é verificado se houve vencedores ou empate. Se houver, o jogo acaba.
"""
from random import randint
from os import system



def inicia_matriz(linhas, colunas):
    """
    Inicia a matriz de acordo com a tamanho das linhas e das colunas
    Faz uso de list comprehension 

    Args:
        linhas (int): Quantidade de linhas da matriz.
        colunas (int): Quantidade de colunas da matriz.

    Retorna a matriz preenchida com valores '-'
    """
    matriz = [['-' for _ in range(colunas)] for _ in range(linhas)]
    return matriz



def mostra_matriz(matriz):
    """
    Printa cada elemento da matriz separadamente para que fique visível para o jogador
    Função chamada a cada vez que o usuário e a máquina jogadorem

    Args:
        matriz (list): A matriz que representa o tabuleiro do jogo.
    """
    system("cls")
    for x in matriz:
        for y in x:
            print(y + "  ", end='')
        print()



def jogador_joga(linha, coluna, matriz,ja_jogadas):
    """
    Realiza a jogada do jogador no jogo da velha, desde que a jogada ainda não tenha sido feita.
    Cria uma tupla contendo a linha e a coluna da jogada e a verifica em relação às jogadas já fei

    Args:
        linha (int): O índice da linha onde o jogador deseja fazer a jogada.
        coluna (int): O índice da coluna onde o jogador deseja fazer a jogada.
        matriz (list): A matriz que representa o tabuleiro do jogo. 
        ja_jogadas (list): Uma lista de tuplas que registra todas as jogadas já feitas.

    Returns:
        bool: True se a jogada foi feita com sucesso, False se a jogada já foi feita anteriormente.
    """
    # Verificação se as linhas e colunas estão dentro do tabuleiro
    if linha < 0 or linha >= len(matriz):
        return False

    if coluna < 0 or coluna >= len(matriz[0]):
        return False

    tupla = (linha, coluna)

    for x in ja_jogadas:
        if x == tupla:
            return False
    else:
        ja_jogadas.append(tupla)
        return True



def maquina_joga(matriz, ja_jogadas):
    """
    Realiza a jogada da máquina (computador) no jogo da velha.

    Percorre a matriz do jogo em busca de posições vazias ('-').
    Tenta fazer uma jogada vencedora para 'O' (máquina).
    Se não for possível vencer em uma jogada, tenta bloquear o jogador 'X' de vencer.
    Se não for possível nem vencer nem bloquear, faz uma jogada aleatória.

    Args:
        matriz (list): A matriz que representa o tabuleiro do jogo.
        ja_jogadas (list): Uma lista de tuplas que registra todas as jogadas já feitas.

    Returns:
        None: A função modifica a matriz diretamente para refletir a jogada da máquina.
    """
    # Tenta vencer com uma jogada
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if matriz[linha][coluna] == '-':
                matriz[linha][coluna] = 'O'
                if verifica_vencedor(matriz) == 'O':
                    ja_jogadas.append(tuple([linha,coluna]))
                    return
                matriz[linha][coluna] = '-'

    # Tenta bloquar o jogador se ele for vencer
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if matriz[linha][coluna] == '-':
                matriz[linha][coluna] = 'X'
                if verifica_vencedor(matriz) == 'X':
                    matriz[linha][coluna] = 'O'
                    ja_jogadas.append(tuple([linha,coluna]))
                    return
                matriz[linha][coluna] = '-'

    # Joga aleatóriamente
    while True:
        linha = randint(0, len(matriz) - 1)
        coluna = randint(0, len(matriz[0]) - 1)
        if matriz[linha][coluna] == '-':
            matriz[linha][coluna] = 'O'
            return



def verifica_vencedor(matriz):
    """
    Retorna o símbolo do vencedor com base na matriz do tabuleiro.
    Verifica se um dos jogadores ('X' ou 'O') venceu horizontalmente, verticalmente ou diagonalmente.

    Args:
        matriz (list): A matriz que representa o tabuleiro do jogo.

    Returns:
        str or None: O símbolo do vencedor ('X' ou 'O') ou None se não houver vencedor.
    """
    for linha in matriz:
        if all(val == linha[0] and val != '-' for val in linha):
            return linha[0]

    for col in range(len(matriz[0])):
        coluna = [matriz[linha][col] for linha in range(len(matriz))]
        if all(val == coluna[0] and val != '-' for val in coluna):
            return coluna[0]


    diagonal1 = [matriz[i][i] for i in range(len(matriz))]
    diagonal2 = [matriz[i][len(matriz) - 1 - i] for i in range(len(matriz))]
    if all(val == diagonal1[0] and val != '-' for val in diagonal1):
        return diagonal1[0]
    if all(val == diagonal2[0] and val != '-' for val in diagonal2):
        return diagonal2[0]

    return None



def verifica_empate(matriz):
    """
    Verifica se o jogo da velha terminou em empate com base na matriz do tabuleiro.

    A função verifica se todas as posições da matriz foram preenchidas (não contêm '-') para determinar se o jogo terminou em empate.

    Args:
        matriz (list): A matriz que representa o tabuleiro do jogo.

    Returns:
        bool: True se o jogo terminou em empate, False caso contrário.
    """
    for linha in matriz:
        if '-' in linha:
            return False
    return True



# Definindo o tamanho da matriz
while True:
    try:
        linhas = int(input("Entre com o número de linhas da tabela: "))
        colunas = int(input("Entre com o número de colunas da tabela: "))
    except ValueError:
        print("Insira um valor válido!")
    else:
        break

# Iniciando matriz e lista das jogadas já feitas
matriz = inicia_matriz(linhas, colunas)
ja_jogadas = []
jogo_acabou = False

# Iniciando o jogo
while True:
    mostra_matriz(matriz)

    # Jogador joga
    try:
        linha = int(input(f"Entre com a linha (1-{linhas}): "))
        coluna = int(input(f"Entre com a coluna (1-{colunas}): "))
    except ValueError:
        continue

    linha -= 1
    coluna -= 1

    if jogador_joga(linha, coluna, matriz, ja_jogadas):
        matriz[linha][coluna] = 'X'
    else:
        continue    # Caso a jogada não for válida!

    # Verificando se houve vencedores
    vencedor = verifica_vencedor(matriz)
    if vencedor == 'X':
        mostra_matriz(matriz)
        print("Jogador Ganhou!")
        jogo_acabou = True

    # Verificando se houve empate
    if verifica_empate(matriz):
        mostra_matriz(matriz)
        print("Empate!")
        jogo_acabou = True

    if jogo_acabou:
        break

    # Máquina joga
    maquina_joga(matriz, ja_jogadas)

    # Verificando se houve vencedores
    vencedor = verifica_vencedor(matriz)
    if vencedor == 'O':
        mostra_matriz(matriz)
        print("Máquina Ganhou!")
        jogo_acabou = True

    # Verificando se houve empate
    if verifica_empate(matriz):
        mostra_matriz(matriz)
        print("Empate!")
        jogo_acabou = True

    # Fechando o jogo caso  o jogo tenha terminado
    if jogo_acabou:
        break
print("Obrigado por jogar!  =)")
