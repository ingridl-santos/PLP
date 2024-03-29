#!/usr/bin/python3 

""" Uma sequência de parênteses e colchetes é considerada bem-formada caso os parenteses e colchetes
correspondentes são fechados na ordem inversa à que foram abertos. Por exemplo: A sequencia "(()())"
é bem-formada, pois todos os paresenteses e colchetes são fechados na ordem inversa que foram abertos. 
Por outro lado, a sequencia ")()(" não é bem formada.

Entrada
Cada linha da entrada será um caso de teste. Cada caso de teste conterá uma sequência de parênteses, sem espaços.
A entrada termina com uma linha contendo a sequência de caracteres '###'. Esse caso não deve ser processado.

Saída
Para cada caso de entrada, imprima uma linha contendo a palavra SIM ou a palavra NAO, indicando se a sequência 
está balanceada.

Restrições
Não use pilha, nem recursão.

    Entrada:    (()())
                ())
                (())
                )(
                ###
    Saída:      SIM
                NAO
                SIM
                NAO
 """
entrada = input()
while(entrada != '###'):
	aberto = 0
	fechado = 0
	for i in (entrada):
		if i == '(':
			aberto += 1
		if i == ')':
			fechado += 1
			if (aberto > 0):
				aberto -= 1
				fechado -= 1
	if aberto == 0 and fechado == 0:
		print('SIM')
	else:
		print('NAO')
	entrada = input()
