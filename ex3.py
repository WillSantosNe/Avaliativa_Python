"""
    JOGO TERMO
    ALUNO: WILLIAM DALLA STELLA DOS SANTOS

    REQUISITOS:
        Ter instalado a biblioteca COLORAMA em seu terminal.
            Usar: pip install colorama

        Preferência de usar o Python 3.10 por conta do colorama

        Ter na pasta do programa o arquivo lista_palavras.txt
        
    ESTRUTURAS USADAS:
        Esse código prioriza o uso de listas e de listas de listas.
    
        
    ETAPAS:
        Puxa de um arquivo uma lista de palavras e faz uma tratativa para selecionar palavras sem acento.

        Inicia 6 listas onde cada uma representa uma tentativa do jogador.
            Todas inicialmente são preenchidas com traços.

        A cada tentativa o usuário tenta escrever uma palavra completa:
            COR ROXA        :quando a letra está no local correto da palavra
            COR AMARELA     :quando a letra não está no local correto da palavra.
            SEM COR         :quando a letra não está na palavra.

        Na próxima tentativa, o usuário não consegue repetir as letras que não existem na palavra.

        Ao acertar a palavra, o usuário vence e o programa mostra em qual tentativa ele acertou.
            Se o número de tentativas acabar, o jogo acaba também.
"""
from random import choice
import os
from colorama import Fore, init

# Inicializa o colorama
init(autoreset=True)

def le_arquivo(arq):
    """
    Lê um arquivo de texto e retorna uma lista de palavras.

    Args:
        arq (str): O nome do arquivo a ser lido.

    Returns:
        list: Uma lista de palavras lidas do arquivo.
    """
    with open(arq, encoding="UTF-8") as f:
        return [linha.strip() for linha in f]


def possui_acentos(palavra):
    """
    Verifica se uma palavra possui caracteres acentuados.

    Args:
        palavra (str): A palavra a ser verificada.

    Returns:
        bool: True se a palavra possui acentos, False caso contrário.
    """
    for char in palavra:
        if char in 'áàãâéèêíìîóòõôúùûÁÀÃÂÉÈÊÍÌÎÓÒÕÔÚÙÛ':
            return True
    return False


def possui_caracteres_especiais(palavra):
    """
    Verifica se uma palavra possui caracteres especiais (não alfanuméricos).

    Args:
        palavra (str): A palavra a ser verificada.

    Returns:
        bool: True se a palavra possui caracteres especiais, False caso contrário.
    """
    for char in palavra:
        if not char.isalnum():
            return True
    return False


def seleciona_palavra_sem_acentos_especiais(lista):
    """
    Seleciona aleatoriamente uma palavra da lista que não possui acentos nem caracteres especiais.

    Args:
        lista (list): A lista de palavras disponíveis.

    Returns:
        str: Uma palavra sem acentos e caracteres especiais.
    """
    while True:
        palavra = choice(lista)
        if not possui_acentos(palavra) and not possui_caracteres_especiais(palavra) and len(palavra) < 6:
            return palavra


def mostra_lista(palavra_random, lista_jogador):
    """
    Mostra uma lista de tentativas do jogador com cores.

    Args:
        palavra_random (str): A palavra que o jogador está tentando adivinhar.
        lista_jogador (list): A lista de letras do jogador.
    """
    letras_certas = []  # Lista para armazenar as letras que já foram acertadas no local certo

    for letra_oculta, letra_jogador in zip(palavra_random, lista_jogador):
        if letra_jogador.upper() == letra_oculta.upper():
            print(Fore.BLUE + letra_jogador + ' ' + Fore.RESET, end="")
            letras_certas.append(letra_jogador.upper())
        elif letra_jogador in palavra_random and letra_jogador.upper() not in letras_certas:
            print(Fore.YELLOW + letra_jogador + ' ' + Fore.RESET, end="")
        else:
            print(letra_jogador + ' ', end="")
    print()




def adiciona_letras_usadas(palavra_random, palpite, lista_usadas_teclado):
    """
    Adiciona as letras do palpite do jogador à lista de letras usadas no teclado.

    Args:
        palavra_random (str): A palavra que o jogador está tentando adivinhar.
        palpite (str): O palpite do jogador.
        lista_usadas_teclado (list): A lista de letras usadas no teclado (devem ser bloqueadas).
    """
    for letra in palpite:
        if letra not in palavra_random:
            lista_usadas_teclado.append(letra)


def mostra_teclado(letras_testadas):
    """
    Mostra o teclado com as letras já testadas pelo jogador.

    Args:
        letras_testadas (list): A lista de letras já testadas.
    """
    teclado = [
        ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
        ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
        ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
    ]

    for linha in teclado:
        for letra in linha:
            if letra in letras_testadas:
                print(f"{Fore.LIGHTBLACK_EX + letra + Fore.RESET} ", end="")
            else:
                print(letra + ' ', end="")
        print()
    print("-"*30)


def inicia_listas(palavra):
    """
    Inicializa uma lista de tentativas com traços.

    Args:
        palavra (str): A palavra a ser adivinhada.

    Returns:
        list: Uma lista de listas contendo traços para cada tentativa.
    """
    lista = [['-' for _ in range(len(palavra))] for _ in range(6)]
    return lista


# Realiza leitura do arquivo e escolhe a palavra
arquivo = "lista_palavras.txt"
lista = le_arquivo(arquivo)
palavra_random = seleciona_palavra_sem_acentos_especiais(lista)

# Inicia variáveis usadas durante o laço principal
listas_jogador = inicia_listas(palavra_random)
letras_testadas = []
lista_usadas_teclado = []
contador = 0

while contador < 6:
    for lista_tentativa in listas_jogador:
        mostra_lista(palavra_random.upper(), lista_tentativa)

    mostra_teclado(letras_testadas)

    # Pegando palpite do jogador
    palpite = input("Palavra: ").upper()
    if len(palpite) != len(palavra_random):
        os.system("cls" if os.name == "nt" else "clear")
        continue

    for x in palpite:
        # Caso o usuário tente usar uma letra já usada anteriormente
        if x in lista_usadas_teclado:
            os.system("cls" if os.name == "nt" else "clear")
            print("Por favor, insira apenas letras válidas que ainda não foram usadas ou que estão na palavra.")
            break
    else:
        # Atualiza a lista que representa a tentativa atual do jogador
        listas_jogador[contador] = list(palpite)
        letras_testadas.extend(palpite)
        adiciona_letras_usadas(palavra_random.upper(), palpite, lista_usadas_teclado)

        os.system("cls" if os.name == "nt" else "clear")
        contador += 1

        # Verifica se o usuário ganhou
        if list(palpite.upper()) == list(palavra_random.upper()):
            for x in range(contador):
                mostra_lista(palavra_random.upper(), listas_jogador[x])
            print(f"Parabéns! Você ganhou na {contador}º tentativa!")
            print(f"A palavra é {palavra_random.upper()}")
            break
else:
    # Caso as tentativas tenham acabado
    os.system("cls" if os.name == "nt" else "clear")
    for x in range(contador):
        mostra_lista(palavra_random.upper(), listas_jogador[x])
    print("Fim de jogo! Você usou todas as tentativas.")
    print(f"A palavra correta era {palavra_random.upper()}")
