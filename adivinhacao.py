print("***************************************************************")
print("Bem vindo ao jogo de adivinhação!")
print("O número secreto é um inteiro entre 0 e 10, com ambos inclusos.")
print("***************************************************************")

import random

rodada = 1
numerosecreto = round(random.random() * 10)
nivel = int(input("Digite 1, para fácil, 2, para médio e 3, para díficil: "))

if nivel == 1:
    print("Nível fácil, 10 tentativas")
    tentativas = 10

if nivel == 2:
    print("Nível médio, 5 tentativas")
    tentativas = 5

if nivel == 3:
    print("Nível dífiicl, 3 tentativas")
    tentativas = 3

while rodada <= tentativas:
    print("Rodada ", rodada, " de ", tentativas)
    chute = int(input("Qual é o seu chute "))
    print("Você digitou ", chute)

    certo = numerosecreto == chute
    maior = numerosecreto > chute
    menor = numerosecreto < chute

    if certo:
        print("Parabéns, você acertou!!!")
        print("fim de jogo")
        break

    else:
        if maior:
            print("Você errou, o  número secreto é maior do que esse")
        elif menor:
            print("Você errou, o número secreto é menor do que esse")

    rodada = rodada + 1
    while rodada > tentativas:
        print("O número secreto era", numerosecreto)
        print("Fim do jogo")
        break
