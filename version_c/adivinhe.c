#include <stdio.h>
#include <locale.h>
#include <stdlib.h>
#include <time.h> 

char *posicao(int chute, int sorteado);
int percorre(int chute, int *todos_chutes);
void desaloca(int **p);

int main(){
	int chute = 1001, sorteado, dificuldade, n=0, opc, cont = 0;
	int *todos_chutes = NULL;

	srand(time(NULL));

	system("clear");

	printf("BEM-VINDO AO GAME 'ADIVINHE O NÚMERO'. \n\n");
	
	do{
		printf("\nESCOLHA A DIFICULDADE: \n\n1-Fácil\n2-Médio\n3-Difícil\n");
		scanf("%d", &dificuldade);

		switch(dificuldade){
			case 1:
				n = 10;
				break;

			case 2:
				n = 50;
				break;

			case 3:
				n = 100;
				break;

			default:
				n = 0;
				printf("Erro!");
				break;
		}
	} while((float)dificuldade > 3.0 || (float)dificuldade<1.0);

	sorteado = rand()%n;
	system("clear");

	printf("Dica: O número está entre 0 e %d\n\n\n", n);

	todos_chutes = (int*)malloc(sizeof(int)*n);
	
	while(chute != sorteado){
		
		printf("Chute: ");
		scanf("%d", &chute);
		
		if(percorre(chute, todos_chutes) != 0){
			printf("Ei, esse número já foi chutado\n\n");
		} else{
			if(chute<0 || chute>n){
				printf("Lembre-se: o número sorteado está entre 0 e %d\n\n", n);
			} else{		
				printf("%s", posicao(chute, sorteado));	
			}

			todos_chutes[cont] = chute;
			cont++;
		}
	}

	if (cont != 1){
		printf("Você deu %d chutes para chegar ao número %d.\nDeseja ver todos os seus chutes? (1 - Sim 2 - Não)\n", cont, sorteado);
		scanf("%d", &opc);
		system("clear");
		if(opc == 1){
			cont = 0;
			while (todos_chutes[cont] != '\0'){
				printf("%d\n", todos_chutes[cont]);
				cont++;
			}
		}
	} else if(cont == 1) printf("MENTIRA DE VOCÊ ACERTOU DE PRIMEIRA!!!!!!!!!!!!!!!");

	desaloca(&todos_chutes);

	return 0;
}

char *posicao(int chute, int sorteado){
	if (chute == sorteado){
		return("Parabéns!\n");
	} else if(chute>sorteado){
		return("Alto\n\n");
	} else if(chute<sorteado){
		return("Baixo\n\n");
	} else{
		return NULL;
	}
}

int percorre(int chute, int *todos_chutes){
	int j = 0, contador = 0;
	
	while(todos_chutes[j] != '\0'){
		if(todos_chutes[j] == chute){
			contador++;
		}
		j++;
	}

	return contador;
}

void desaloca(int **p){
	free(*p);
	p = NULL;
}