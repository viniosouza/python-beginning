from random import randint

print('********************************')
print('*      Jogo da adivinhação      *')
print('********************************')

numero_secreto = randint(0, 30)
total_de_tentativas = 3
rodada = 1


while (rodada <= total_de_tentativas):
    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
    chute = int(input('Insira um número de 0-100: '))
    print('Você digitou: ', chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if chute == numero_secreto:
        print('Você	acertou')
        break
    elif(maior):
        print('Você errou! O seu chute foi maior que o número secreto, o número correto é o {}'.format(
            numero_secreto))
    elif(menor):
        print('Você errou! O seu chute foi menor que o número secreto, o número correto é o {}'.format(
            numero_secreto))
    rodada = rodada + 1
print('Fim do jogo')
