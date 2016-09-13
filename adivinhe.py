#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import os

chute = ''  # se colocar chute igual 0 pode acontecer de automaticamente estar certo
contador = 0
nivel = 0
numeros = [0]
todos_chutes = []  # vetor para guardar todos os chutes dado pelo usuario


def dificuldade(nivel): #funcao que define a dificuldade
    global numeros
    if nivel == 1:
        numeros.append(10)
    elif nivel == 2:
        numeros.append(50)
    elif nivel == 3:
        numeros.append(100)
    elif nivel == 4:
        numeros.append(1000)
    else:
        nivel = "Erro, rode o jogo novamente!"
    return nivel


# função para mostrar se o chute foi o correto, está alto ou baixo.
def posicao(chute, sorteado):
    if chute == sorteado:
        os.system('clear')
        return("Parabéns! Acertô, Miseravi.")
    elif chute > sorteado:
        return("Alto.\n")
    else:
        return("Baixo.\n")

os.system('clear')
print("BEM-VINDO AO GAME 'ADIVINHE O NÚMERO!'\n\n")
level = int(
    input("Escolha a dificuldade: \n\n1-Fácil\n2-Médio\n3-Difícil\n4-Ultra\n"))

dificuldade(level)
os.system('clear')

if type(dificuldade(level)) == int:
    sorteado = random.randint(numeros[0], numeros[1])
    print("Dica: o número está entre {} e {}. Boa sorte! \n\n" .format(
        numeros[0], numeros[1]))
    input("Pressione ENTER para iniciar.")

    while chute != sorteado:
        chute = int(input("Chute: "))
        todos_chutes.append(chute)
        contador += 1
        if chute in range(numeros[0], numeros[1] + 1):
            print(posicao(chute, sorteado))
        else:
            print(
                "Hey, lembre-se que o número a ser adivinhado está entre {} e {}\n" .format(
                    numeros[0], numeros[1]))

    if contador != 1:
        print("Você deu {} chutes para chegar ao número {}.\n" .format(
            contador, chute))
        escolha = int(input("Deseja ver todos os chutes? \n\n1-Sim\n2-Não\n"))
        os.system('clear')
        # mostra todos os chutes dado pelo usuário
        if escolha == 1:
            for x in range(len(todos_chutes)):
                print(todos_chutes[x])
    else:
        print("MENTIRA QUE VC ACERTOU DE PRIMEIRA!!!!!!1111111!!!!!\n")

else:
    print(dificuldade(level))
