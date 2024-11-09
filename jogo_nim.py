# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 14:12:45 2024

@author: lfelipe
"""
## Primeira função:
def computador_escolhe_jogada(n,m):
## Recebe os parâmetros "n" e "m"
## Devolve um inteiro correspondente à próxima jogada do computador
    # Ou seja, quantas peças o computador deve retirar do tabuleiro, de acordo com a estratégia vencedora
    # Estratégia para ganhar o jogo: deixar sempre múltiplos de (m+1) peças ao jogador oponente
    # Um valor x é múltiplo de outro valor y, se x % y == 0
## Não precisa chamar outras funções do programa
## Deve devolver (return) o número de peças removidas pela jogada
## Não deve devolver o número de peças que restam no tabuleiro
    # Computador tem que retirar um valor de modo que (n-x)/(m+1) == 0
    # x é o inteiro que faz com que "n" seja múltiplo de "(m + 1)"
    x = 1
    while x <= m:
        if (n - x) % (m + 1) == 0:
            return x ## Inteiro que viabiliza a estratégia vencedora, não o valor retirado pelo computador
        x += 1
    return m ## Se não encontrar uma jogada que satisfaça a condição, escolhe retirar o limite "m"
    
## Segunda função:
def usuario_escolhe_jogada(n,m):
## (1) Recebe os parâmetros "n" e "m"
## (2) Solicita que o jogador informe a sua jogada
## (3) Verifica se o valor informado é válido
    # Não pode retirar mais do que as peças do tabuleiro, não pode retirar mais do que o limite estabelecido, não pode retirar valor negativo
## (4) Se a jogada é válida, retorna o valor informado
## (5) Se a jogada é inválida, repete passos (2) e (3)
## Não precisa chamar outras funções do programa
## Deve devolver (return) o número de peças removidas pela jogada
## Não deve devolver o número de peças que restam no tabuleiro
## Para checar se a entrada do usuário é válida, é só fazer um laço usando como condição um booleano
    # y é o valor a ser retirado pelo usuário
    while True:
        y = int(input("Quantas peças você vai tirar? "))
        if 1 <= y <= m and y <= n:
            return y
        else:
            print()
            print("Oops! Jogada inválida! Tente de novo.")
       
## Terceira função:
def partida():
## Função que pergunta os valores de n e m que valem na partida
## n é o número de peças inicial no tabuleiro
## m é o número máximo de peças que é possível retirar em uma rodada
## limite de retirada de peças: pelo menos 1 e no máximo m
## Função que decide quem começa o jogo
## Função responsável por chamar as funções "xxx_escolhe_jogada()" alternadamente
      # Para isso, precisa usar um laço
      # Em cada chamada, imprime (print) estado do jogo (n e m)
## Recebe o valor devolvido por essas funções e atualiza o valor de n de acordo
## Função que identifica que o jogo acabou (n==0)
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    usuario_jogada = False
    computador_jogada = False
    
    # Verifica a jogada inicial conforme a estratégia vencedora
    if n % (m + 1) == 0:
        print("Você começa!")
        usuario_jogada = True
    else:
        print("Computador começa!")
        computador_jogada = True
        
    # Inicia o loop do jogo
    while n > 0:
        if computador_jogada:
            c = computador_escolhe_jogada(n,m)
            n = n - c
            print ("O computador tirou",c,"peças")
            print ("Agora restam",n,"peças no tabuleiro")
            computador_jogada = False
        else:
            u = usuario_escolhe_jogada(n,m)
            n = n - u
            print ("Você tirou ",u,"peças")
            print ("Agora restam ",n,"peças no tabuleiro")
            computador_jogada = True

    if computador_jogada:
        print ("Fim de jogo! Você ganhou!")
    else:
        print ("Fim de jogo! O computador ganhou!")

## Quarta função:
def campeonato():
## Só precisa chamar a função partida() três vezes
    x = 1
    while x <= 3:
        print()
        print("**** Rodada", x, "****")
        return partida()
        x = x + 1
    print("**** Final do campeonato! ****")
    print("Placar: Você 0 X 3 Computador")
        
## Quinta função:
def main():
## Serve para iniciar o jogo
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print()
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    a = int(input("Digite a sua opção: "))
    if a == 1:
        print()
        print("Você escolheu uma partida isolada!")
        return partida()
    if a == 2:
        print()
        print("Voce escolheu um campeonato!")
        return campeonato()
    else:
        print()
        print("Opção inválida!")
        return main()

main()