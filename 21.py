#coding: UTF-8
import os

def limpar():
	os.system("clear" or "cls")

#QUESTÃO: Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque 
# e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 
# 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.

#RESOLUÇÃO: Usando a matemática a meu favor. Começo testando a nota de maior valor com a funçao valor//100. 
# se o resultado for diferente de zero, significa que será necessario alguma nota de 100. Sendo esse o caso,
# calculo o que sobra do valor, passo a quantidade de notas para uma lista e ai finaliza a lógica. Agora é fazer 
# o mesmo para as próximas notas. No final, para exibir o resultado, so percorrer a lista. Exibi com cadeia de 
# "ifs" na questão 19 então farei de outra forma agora  

notas=[]

limpar()
print(" __ Caixa eletrônico - Somente saque __")
print("- Notas disponíveis: 1, 5, 10, 50 e 100 -")
valor = int(input("Valor para saque: \n  > "))
resto=valor #sem essa linha, valores menores que 100 dão erro

if valor >= 10 and valor <=600:
	quant = valor//100
	if quant!=0:
		resto = valor%100
		if quant ==1:
			notas.append(f"1 nota de 100")
		else:
			notas.append(f"{quant} notas de 100")
		
	quant = resto//50
	if quant!=0:
		resto = valor%50
		if quant ==1:
			notas.append(f"1 nota de 50")
		else:
			notas.append(f"{quant} notas de 50")
		
	quant = resto//10
	if quant!=0:
		resto = valor%10
		if quant ==1:
			notas.append(f"1 nota de 10")
		else:
			notas.append(f"{quant} notas de 10")

	quant = resto//5
	if quant!=0:
		resto = valor%5
		if quant ==1:
			notas.append(f"1 nota de 5")
		else:
			notas.append(f"{quant} notas de 5")

	quant = resto//1
	if quant!=0:
		resto = valor%1
		if quant ==1:
			notas.append(f"1 nota de 1")
		else:
			notas.append(f"{quant} notas de 1")

	#me desafiei a exibir o resultado lendo a lista, mas em somente uma linha. 
	# usando o backspace (\b) e o atributo "end" consegui fazer uma lógica 
	# de escrever e apagar que funcionasse
	x=1
	print("Você receberá:", end=" ")
	for i in notas:
		if x==1:
			print(i, end=".")
		else:
			print("\b, ",i, end=".")
		x+=1
	print("")
else: 
	print("Valor inválido! Tente novamente.")

