#!/usr/bin/python3 

""" Uma sequência de parênteses e colchetes é considerada bem-formada caso os parenteses e colchetes 
correspondentes são fechados na ordem inversa à que foram abertos. Por exemplo: A sequencia "(()[()])" 
é bem-formada, pois todos os paresenteses e colchetes são fechados na ordem inversa que foram abertos. 
Por outro lado, a sequencia "([)]" não é bem formada.

Entrada
Cada linha da entrada será um caso de teste. Cada caso de teste conterá uma sequência de parênteses e 
colchetes, sem espaços. A entrada termina com uma linha contendo a sequência de caracteres '###'. Esse 
caso não deve ser processado.

Saída
Para cada caso de entrada, imprima uma linha contendo a palavra SIM ou a palavra NAO, indicando se a
sequência está balanceada.

Restrições
Utilize uma lista para implementar a pilha. 

    Entrada:    (()[()])
                ([)]
                ([([])])
                (][)
                ###
    Saída:      SIM
                NAO
                SIM
                NAO
"""

def computando(entrada):
	if(len(entrada)%2!=0):
		return False
	lista = []
	for i in entrada:
		if (i == '(') or (i== '['):
			lista.append(i)
		else:
			if lista == []:
				return False
			if (lista[-1] == '(' and i == ')') or (lista[-1] == '[' and i == ']'):
				lista.pop()
	if lista == []:
		return True
	else:
		return False

	
	
entrada = input()
while(entrada != '###'):
	if(computando(entrada)==True):
		print("SIM")
	else:
		print("NAO")
	entrada = input()
