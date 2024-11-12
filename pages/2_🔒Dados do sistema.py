def inicializar_tabuleiro():
    return [[' ' for _ in range(3)] for _ in range(3)]

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print('|'.join(linha))
        print('-' * 5)

def verificar_vencedor(tabuleiro, jogador):
    # Verifica linhas, colunas e diagonais
    for i in range(3):
        if all([tabuleiro[i][j] == jogador for j in range(3)]) or \
           all([tabuleiro[j][i] == jogador for j in range(3)]):
            return True

    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador or \
       tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True

    return False

def jogo_da_velha():
    tabuleiro = inicializar_tabuleiro()
    jogador_atual = 'X'
    movimentos = 0

    while movimentos < 9:
        imprimir_tabuleiro(tabuleiro)
        print(f"Jogador {jogador_atual}, escolha uma linha (0-2) e uma coluna (0-2):")
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))

        if tabuleiro[linha][coluna] == ' ':
            tabuleiro[linha][coluna] = jogador_atual
            movimentos += 1

            if verificar_vencedor(tabuleiro, jogador_atual):
                imprimir_tabuleiro(tabuleiro)
                print(f"Jogador {jogador_atual} venceu!")
                return

            jogador_atual = 'O' if jogador_atual == 'X' else 'X'
        else:
            print("Posição já ocupada. Tente novamente.")

    imprimir_tabuleiro(tabuleiro)
    print("O jogo terminou empatado!")

# Iniciar o jogo
jogo_da_velha()
