import random

print("'''''''''''''''''''''''''''''''''")
print("Bem vindo ao jogo de adivinhação")
print("''''''''''''''''''''''''''''''''")

nome = input("Qual é o seu nome? ")
random = random.randint(0, 20)

nivel = int(input(f"{nome}, digite o seu nível. 1 - FÁCIL. 2 - MÉDIO. 3 - DIFÍCIL: "))

if nivel == 1:
    tentativas = 10
    print(nome, f"Você escolheu o modo fácil com {tentativas} tentativas, boa sorte.")

elif nivel == 2:
    tentativas = 5
    print(f"{nome}, você escolheu o modo médio com {tentativas} tentativas, boa sorte.")

elif nivel == 3:
    tentativas = 3
    print(f"{nome}, você escolheu o modo difícil com {tentativas} tentativas")

if nivel < 1 or nivel > 3:
    print(f"{nome}, você digitou um nível incorreto")

while tentativas > 1:
    chute = int(input("Digite o seu chute: "))
    tentativas = tentativas - 1

    if chute > random:
        print("Chute muito alto, o número é menor")
        print(f"RESTAM APENAS {tentativas} TENTATIVAS")
    if chute < random:
        print("Chute muito baixo, o número é maior")
        print(f"RESTAM APENAS {tentativas} TENTATIVAS")
    if chute == random:
        print("PARABÉNS, VOCÊ ACERTOU")
        break

while tentativas == 1 and chute != random:
    print("ESSA É A ÚLTIMA CHANCE")
    novoChute = int(input("Digite o valor: "))
    if novoChute == random:
        print("Certo")
        tentativas = tentativas - 1
    else:
        print(f"O jogo acabou e o número era {random}")
    break
