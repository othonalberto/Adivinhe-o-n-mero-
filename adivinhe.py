#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import os

chute = ''  # se colocar chute igual 0 pode acontecer de automaticamente estar certo
contador = 0
nivel = 0
numeros = [0]


def dificuldade(nivel):
    global numeros
    if nivel == 1:
        numeros.append(10)
    elif nivel == 2:
        numeros.append(50)
    elif nivel == 3:
        numeros.append(100)
    else:
        nivel = "Erro, rode o jogo novamente!"
    return nivel

os.system('clear')
print("BEM-VINDO AO GAME 'ADIVINHE O NÚMERO!'\n\n")
level = int(input("Escolha a dificuldade: \n\n1-Fácil\n2-Médio\n3-Difícil\n"))

dificuldade(level)
os.system('clear')

if type(dificuldade(level)) == int:
    sorteado = random.randint(numeros[0], numeros[1])
    print("Dica: o número está entre {} e {}. Boa sorte! \n\n" .format(
        numeros[0], numeros[1]))
    input("Pressione ENTER para iniciar.")

    while chute != sorteado:
        chute = int(input("Chute: "))
        contador += 1
        if chute in range(numeros[0], numeros[1] + 1):
            if chute == sorteado:
                os.system('clear')
                print("Parabéns! Acertô, Miseravi.")
            elif chute > sorteado:
                print("Alto.\n")
            else:
                print("Baixo.\n")
        else:
            print(
                "Hey, lembre-se que o número a ser adivinhado está entre {} e {}\n" .format(
                    numeros[0], numeros[1]))

    if contador != 1:
        print("Você deu {} chutes para chegar ao número {}." .format(
            contador, chute))
    else:
        print("MENTIRA QUE VC ACERTOU DE PRIMEIRA!!!!!!1111111!!!!!")
else:
    print(dificuldade(level))
