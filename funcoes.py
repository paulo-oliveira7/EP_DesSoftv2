# Definindo a posição dos navios
def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    for i in range(tamanho):
        if orientacao == 'horizontal':
            posicoes.append([linha,coluna+i])
        else:
            posicoes.append([linha+i, coluna])
    return posicoes

# Preenchendo a frota (armazenando as posições dos navios)
def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    if nome_navio in frota:
        frota[nome_navio].append(define_posicoes(linha, coluna, orientacao, tamanho))
    else:
        frota[nome_navio] = [define_posicoes(linha, coluna, orientacao, tamanho)]
    return frota

# Função da jogada
def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = '-'
    elif tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    return tabuleiro

# Função que posiciona a frota no tabuleiro
def posiciona_frota(frota):
    tabuleiro = [[0]*10]
    for i in range(9):
        tabuleiro.append([0]*10)
    for valores in frota.values():
        for embarcacao in valores:
            for i in range(len(embarcacao)):
                tabuleiro[embarcacao[i][0]][embarcacao[i][1]] = 1
    return tabuleiro

# Função que conta quantos navios já foram afundados
def afundados(frota, tabuleiro):
    resultado = 0
    for valores in frota.values():
        for embarcacao in valores:
            count = 0
            for i in range(len(embarcacao)):
                if tabuleiro[embarcacao[i][0]][embarcacao[i][1]] == 'X':
                    count += 1
                if count == len(embarcacao):
                    resultado += 1
    return resultado
