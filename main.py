"""
Jogo - Pedra, Papel e Tesoura

Programa que joga pedra, papel e tesoura com o usuário.
Versão: 1.0
"""
from random import choice

TITULO = 'Jogo - Pedra, Papel e Tesoura'
TAMANHO_LINHA = 78
OPCOES = ('pedra', 'papel', 'tesoura')


def verificar_resultado(escolha_jogador: str, escolha_computador: str) -> str:
    """
    Compara as escolhas do jogador e do computador e retorna o resultado da partida.

    Args:
        escolha_jogador (str): Escolha do jogador.
        escolha_computador (str): Escolha do computador.

    Returns:
        str: resultado da partida.
    """
    if escolha_jogador == escolha_computador:
        return 'Empate!'
    elif ((escolha_jogador == OPCOES[0] and escolha_computador == OPCOES[2]) or
          (escolha_jogador == OPCOES[1] and escolha_computador == OPCOES[0]) or
          (escolha_jogador == OPCOES[2] and escolha_computador == OPCOES[1])
    ):
        return 'Você venceu!'
    else:
        return 'Você perdeu!'


def main():
    """
    Função que executa o fluxo do programa.
    """
    print(TAMANHO_LINHA * "=")
    print(TITULO.center(TAMANHO_LINHA))
    print(TAMANHO_LINHA * "=")

    escolha_computador = choice(OPCOES)
    escolha_usuario = input('Escolha: Pedra, Papel ou Tesoura? ').lower()

    while escolha_usuario not in OPCOES:
        print('Opção inválida. Tente novamente.')
        print(TAMANHO_LINHA * "=")
        escolha_usuario = input('Escolha: Pedra, Papel ou Tesoura? ').lower()

    resultado = verificar_resultado(escolha_usuario, escolha_computador)

    print(TAMANHO_LINHA * "=")
    print(f'O computador escolheu: {escolha_computador.title()}')
    print(resultado)
    print(TAMANHO_LINHA * "=")


if __name__ == '__main__':
    main()
