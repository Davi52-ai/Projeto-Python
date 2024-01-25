def mostrar_tabuleiro():
    """
    UNIÃO DAS LISTAS CHAMADAS DE LINHA(1 A 3), FORMANDO O "TABULEIRO". USADO EM TODAS JOGADAS E AO IMPRIMIR O RESULTADO DA PARTIDA."
    """

    print('\n')
    print(''.join(linha_1))
    print(''.join(linha_2))
    print(''.join(linha_3))


def inicio_de_jogo():
    """
    "NÚCLEO" DO JOGO, LOOP ATIVO ATÉ QUE ALGUM JOGADOR SE TORNE O VENCEDOR OU ACABE EM EMPATE
    """

    print('\nBem vindo ao jogo da velha! Vamos começar!')

    mostrar_tabuleiro()

    print('\nEste é o nosso tabuleiro!\n')

    contador_jogadas = 0

    while True:

        joga_o()
        if (checar_o(venceu_o) == True):
            fim_de_jogo()
            break
        mostrar_tabuleiro()
        contador_jogadas += 1

        if contador_jogadas == 9:
            print('\nDeu velha!\n')
            fim_de_jogo()
            break

        joga_x()
        if (checar_x(venceu_x) == True):
            fim_de_jogo()
            break
        mostrar_tabuleiro()
        print(venceu_o, venceu_x)
        contador_jogadas += 1


def fim_de_jogo():
    """
    FUNÇÃO CHAMADA APÓS O PROGRAMA OBTER O RESULTADO DA PARTIDA, PEDINDO SE O USUÁRIO DESEJA JOGAR NOVAMENTE
    """
    restart = input('\n\nA partida acabou! Deseja jogar novamente? Digite "s" ou "n": ')
    restart = restart.lower()
    while True:
        if restart == 'n':
            print('\nObrigado por jogar! Até a próxima!')
            break
        elif restart == 's':
            limpar_linhas()
            inicio_de_jogo()


def limpar_linhas():
    """
    FUNÇÃO PARA LIMPAR O TABULEIRO E DEIXÁ-LO PRONTO PARA UMA NOVA PARTIDA
    """
    for i in range(3):
        for j in range(0, len(linha_1), 2):
            linhas[i][j] = ' '


def joga_o():
    """
    FUNÇÃO PARA ATRIBUIR AS JOGADAS "O" NO TABULEIRO, TAMBÉM INCLUIDO CHECAGEM DE POSIÇÃO PARA NÃO SOBREPOR UMA QUE JÁ ESTEJA OCUPADA
    """
    jogada_linha = int(input('\nJogador "O", selecione a linha da jogada: '))
    jogada_coluna = int(input('\nJogador "O", selecione a coluna da jogada: '))

    # Váriavel jogada_coluna se transforma na posição da jogada na linha selecionada, existem "barras" intercalando as posições da lista linha então as possíveis posições para o jogador são 0,2 e 4.

    if jogada_coluna == 1:
        jogada_coluna = 0
    elif jogada_coluna == 2:
        jogada_coluna = 2
    elif jogada_coluna == 3:
        jogada_coluna = 4

    if jogada_linha == 1:
        while linha_1[jogada_coluna] == 'X' or linha_1[jogada_coluna] == 'O':
            print('\nJogada inválida! Posição já ocupada! Tente novamente: \n')
            joga_o()
            break
        else:
            linha_1[jogada_coluna] = 'O'
    elif jogada_linha == 2:
        while linha_2[jogada_coluna] == 'X' or linha_2[jogada_coluna] == 'O':
            print('\nJogada inválida! Posição já ocupada! Tente novamente: \n')
            joga_o()
            break
        else:
            linha_2[jogada_coluna] = 'O'

    elif jogada_linha == 3:
        while linha_3[jogada_coluna] == 'X' or linha_3[jogada_coluna] == 'O':
            print('\nJogada inválida! Posição já ocupada! Tente novamente: \n')
            joga_o()
            break
        else:
            linha_3[jogada_coluna] = 'O'


def joga_x():
    """
    FUNÇÃO PARA ATRIBUIR AS JOGADAS "O" NO TABULEIRO, TAMBÉM INCLUIDO CHECAGEM DE POSIÇÃO PARA NÃO SOBREPOR UMA QUE JÁ ESTEJA OCUPADA
    """
    jogada_linha = int(input('\nJogador "X", selecione a linha da jogada: '))
    jogada_coluna = int(input('\nJogador "X", selecione a coluna da jogada: '))

    if jogada_coluna == 1:
        jogada_coluna = 0
    elif jogada_coluna == 2:
        jogada_coluna = 2
    elif jogada_coluna == 3:
        jogada_coluna = 4

    if jogada_linha == 1:
        while linha_1[jogada_coluna] == 'X' or linha_1[jogada_coluna] == 'O':
            print('\nJogada inválida! Posição já ocupada! Tente novamente: \n')
            joga_x()
            break
        else:
            linha_1[jogada_coluna] = 'X'
    elif jogada_linha == 2:
        while linha_2[jogada_coluna] == 'X' or linha_2[jogada_coluna] == 'O':
            print('\nJogada inválida! Posição já ocupada! Tente novamente: \n')
            joga_x()
            break
        else:
            linha_2[jogada_coluna] = 'X'

    elif jogada_linha == 3:
        while linha_3[jogada_coluna] == 'X' or linha_3[jogada_coluna] == 'O':
            print('\nJogada inválida! Posição já ocupada! Tente novamente: \n')
            joga_x()
            break
        else:
            linha_3[jogada_coluna] = 'X'


def checar_o(venceu_o):
    """
    FUNÇÃO PARA CHECAR LINHAS, COLUNAS E DIAGONAIS DO TABULEIRO COM O SÍMBOLO "O"
    CASO ENCONTRE 3 SÍMBOLOS NA MESMA LISTA, RETORNA QUE venceu_o É VERDADEIRO E O RESULTADO DA PARTIDA
    """
    coluna_1 = [linha_1[0], linha_2[0], linha_3[0]]
    coluna_2 = [linha_1[2], linha_2[2], linha_3[2]]
    coluna_3 = [linha_1[4], linha_2[4], linha_3[4]]

    diagonal_1 = [linha_1[0], linha_2[2], linha_3[4]]
    diagonal_2 = [linha_3[0], linha_2[2], linha_1[4]]

    linhas = [linha_1, linha_2, linha_3]

    colunas = [coluna_1, coluna_2, coluna_3]

    diagonais = [diagonal_1, diagonal_2, '']

    for i in range(3):

        x = linhas[i].count('O')
        y = colunas[i].count('O')
        z = diagonais[i].count('O')
        if x == 3 or y == 3 or z == 3:
            print('\nJogador "O" venceu!\n')
            mostrar_tabuleiro()
            venceu_o = True
            return venceu_o


def checar_x(venceu_x):
    """
    FUNÇÃO PARA CHECAR LINHAS, COLUNAS E DIAGONAIS DO TABULEIRO COM O SÍMBOLO "X"
    CASO ENCONTRE 3 SÍMBOLOS NA MESMA LISTA, RETORNA QUE venceu_x É VERDADEIRO E O RESULTADO DA PARTIDA
    """
    coluna_1 = [linha_1[0], linha_2[0], linha_3[0]]
    coluna_2 = [linha_1[2], linha_2[2], linha_3[2]]
    coluna_3 = [linha_1[4], linha_2[4], linha_3[4]]

    diagonal_1 = [linha_1[0], linha_2[2], linha_3[4]]
    diagonal_2 = [linha_3[0], linha_2[2], linha_1[4]]

    linhas = [linha_1, linha_2, linha_3]

    colunas = [coluna_1, coluna_2, coluna_3]

    diagonais = [diagonal_1, diagonal_2, '']

    for i in range(3):
        x = linhas[i].count('X')
        y = colunas[i].count('X')
        z = diagonais[i].count('X')
        if x == 3 or y == 3 or z == 3:
            print('\nO jogador "X" venceu!\n')
            mostrar_tabuleiro()
            venceu_x = True
            return venceu_x


# Váriaveis para uso de checagem
venceu_o = True
venceu_x = False

# Listas para refêrencia de tabuleiro, colunas e diagonais
linha_1 = [' ', '|', ' ', '|', ' ']
linha_2 = [' ', '|', ' ', '|', ' ']
linha_3 = [' ', '|', ' ', '|', ' ']
linhas = [linha_1, linha_2, linha_3]

# Começo da partida
inicio_de_jogo()