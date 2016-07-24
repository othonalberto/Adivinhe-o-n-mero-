#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import os

chute = '' #se colocar chute igual 0 pode acontecer de automaticamente estar certo
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
		print("Erro. Rode o jogo novamente.")

os.system('clear')
print("BEM-VINDO AO GAME 'ADIVINHE O NÚMERO!'\n\n")
level = int(input("Escolha a dificuldade: \n\n1-Fácil\n2-Médio\n3-Difícil\n"))

dificuldade(level)
sorteado = random.randint(numeros[0], numeros[1])
os.system('clear')

print("Dica: o número está entre {0} e {1}. Boa sorte! \n\n" .format(numeros[0], numeros[1]))
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
		print("Hey, lembre-se que o número a ser adivinhado está entre {0} e {1}\n" .format(numeros[0], numeros[1]))

if contador != 1:
	print("Você deu {0} chutes para chegar ao número {1}." .format(contador, chute))
else:
	print("MENTIRA QUE VC ACERTOU DE PRIMEIRA!!!!!!1111111!!!!!")