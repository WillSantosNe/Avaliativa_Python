"""
    SISTEMA DE BANCO DE USUÁRIOS
    ALUNO: WILLIAM DALLA STELLA DOS SANTOS

    ESTRUTURA USADAS:
        Esse código faz uso de listas, tuplas e dicionários.
            Faz uso de dicionários de dicionários para armazenar os usuários
        
        Uso de funções MAP para deixar todos os elementos em minúsculo.
        Uso da função ZIP para alinhar dados de listas diferentes.

    ETAPAS:
        Pede para o usuário digitar os campos obrigatórios que serão usados no cadastro.
            Posteriormente pode colocar campos adicionais para cada cadastro.

        Entra no menu principal e pede para o usuário escolher uma opção.

        No cadastro o usuário deve colocar os campos obrigatórios e se quiser os adicionais.

        Para imprimir os usuários, há 4 maneiras diferentes de filtrar a consulta:
            Opção 1: imprime todos os usuários e todos os campos
            Opção 2: imprime todos os usuários com determinados nomes
            Opção 3: imprime todos os usuários de acordo com os campos e valores estabelecidos
            Opção 4: imprime todos os usuários de acordo com o nome e campos e valores estabelecidos

"""


import os

# Dicionário global para armazenar os usuários cadastrados
BANCO_USUARIOS = {}


def cadastrar_usuario(campos_obrigatorios):
    """
    Função para cadastrar um usuário.

    Args:
        campos_obrigatorios (tuple): Uma tupla contendo os nomes dos campos obrigatórios.

    Returns:
        dict: Um dicionário contendo os dados do usuário cadastrado.
    """
    usuario = {}
    
    # Preenche os campos obrigatórios
    for campo in campos_obrigatorios:
        valor = input(f"{campo.upper()}: ")
        usuario[campo.lower()] = valor
    
    # Permite ao usuário adicionar campos adicionais
    while True:
        campo_adicional = input("Digite o nome de um campo adicional ou 'sair' para encerrar: ")
        if campo_adicional.lower() == 'sair':
            break
        valor_adicional = input(f"{campo_adicional.upper()}: ")
        usuario[campo_adicional.lower()] = valor_adicional
    
    # Gerar um identificador único para o usuário (pode ser um número sequencial)
    usuario_id = len(BANCO_USUARIOS) + 1
    
    # Adicionar o usuário ao banco de usuários usando o identificador como chave
    BANCO_USUARIOS[usuario_id] = usuario
    
    print("Usuário cadastrado com sucesso!")
    
    return usuario



def imprimir_usuarios(*args, **kwargs):
    """
    Função para imprimir usuários com diferentes opções de filtragem.

    Args:
        *args: Argumentos posicionais que podem conter nomes de usuários.
        **kwargs: Argumentos nomeados que podem conter critérios de filtragem.

    Returns:
        None

    Explicações das opções de filtragem:
    -   Se nenhum argumento for fornecido, imprime todos os usuários com todas as informações.
    -   Se *args for fornecido, imprime todos os dados dos usuários cujos nomes correspondem aos nomes especificados em *args.
    -   Se **kwargs for fornecido, filtra os usuários com base nos critérios especificados em **kwargs.
    """
    if not args and not kwargs:
        # Caso a função não receba argumentos, imprime todos os usuários com todas as infos
        for usuario_id, usuario in BANCO_USUARIOS.items():
            print(f"{usuario_id}: {usuario}")
    elif args:
        # Caso receba vários nomes, imprime todos os dados dos usuários com os nomes especificados
        for nome in args:
            for usuario_id, usuario in BANCO_USUARIOS.items():
                if usuario.get('nome') == nome:
                    print(f"{usuario_id}: {usuario}")
    elif kwargs:
        # Filtrar por campos usando kwargs
        for usuario_id, usuario in BANCO_USUARIOS.items():
            if all(usuario.get(campo.lower()) == valor for campo, valor in kwargs.items()):
                print(f"{usuario_id}: {usuario}")



def input_numero(mensagem):
    """
    Função auxiliar para obter uma entrada numérica válida do usuário.

    Args:
        mensagem (str): A mensagem a ser exibida ao usuário.

    Returns:
        int: O número inserido pelo usuário.
    """
    while True:
        try:
            numero = int(input(mensagem))
            return numero
        except ValueError:
            return False

# Pega e transforma os campos obrigatórios em minúsculo usando map
campos_obrigatorios = input("Digite os nomes dos campos obrigatórios separados por espaço: ").split()
campos_obrigatorios = list(map(str.lower, campos_obrigatorios))

# Laço principal do programa
while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("\nMenu:")
    print("1 - Cadastrar usuário")
    print("2 - Imprimir usuários")
    print("0 - Encerrar")
    
    opcao = input_numero("Escolha uma opção: ")
    if opcao is False:
        continue

    if opcao == 1:
        print("-"*30)
        cadastrar_usuario(tuple(campos_obrigatorios))
    elif opcao == 2:
        while True:
            # Laço para mostrar o menu de impressão do usuário
            os.system("cls" if os.name == "nt" else "clear")

            print("1 - Imprimir todos")
            print("2 - Filtrar por nomes")
            print("3 - Filtrar por campos")
            print("4 - Filtrar por nomes e campos")
            opcao2 = input_numero("Opção: ")

            if opcao2 is False:
                continue
            break

        # Saindo do laço se a opção for válida
        if opcao2 == 1:
            # Chamando imprimir_usuarios() sem parâmetros 
            print("-"*30)
            imprimir_usuarios()
            print("-"*30)
            input("Pressione qualquer tecla: ")

        elif opcao2 == 2:
            # Chamando imprimir_usuarios() com *args (nome dos usuários)
            print("-"*30)
            nomes = input("Digite os nomes separados por espaço: ").split()
            print("-"*30)
            imprimir_usuarios(*nomes)
            print("-"*30)
            input("Pressione qualquer tecla: ")

        elif opcao2 == 3:
            # Chamando imprimir_usuarios() com **kwargs (dicionário {campo:valor})
            print("-"*30)
            campos = input("Digite os campos e valores separados por espaço (ex: campo1 valor1 campo2 valor2): ").split()
            print("-"*30)

            # Transformando a var kwargs em um dicionário para ser mandada como parâmetro
            kwargs = dict(zip(map(str.lower, campos[::2]), campos[1::2]))
            imprimir_usuarios(**kwargs)
            print("-"*30)
            input("Pressione qualquer tecla: ")

        elif opcao2 == 4:
            # Chamando imprimir_usuarios() com *args e **kwargs
            print("-"*30)
            nomes = input("Digite os nomes separados por espaço: ").split()
            campos = input("Digite os campos e valores separados por espaço (ex: campo1 valor1 campo2 valor2): ").split()
            print("-"*30)

            # Transformando a var kwargs em um dicionário para ser mandada como parâmetro
            kwargs = dict(zip(map(str.lower, campos[::2]), campos[1::2]))
            imprimir_usuarios(*nomes, **kwargs)
            print("-"*30)
            input("Pressione qualquer tecla: ")
            
    elif opcao == 0:
        # Fecha o programa
        os.system("cls" if os.name == "nt" else "clear")
        print("Até mais! =)")
        break
    else:
        print("Opção inválida!")
        input("Pressione qualquer tecla: ")
