#coding: UTF-8
import os

#função para limpar a tela
def limpar():
	os.system("clear" or "cls")

#QUESTÃO: Faça um Programa que peça um número correspondente a um determinado ano 
# e em seguida informe se este ano é ou não bissexto.

limpar()
print(" - É ou não um ano bissexto? -")
ano = str(input("Digite um ano e descubra se ele foi/será bissexto: \n  > "))
tamanho = len(ano)
ano=int(ano)

#as regras para um ano ser bissexto são:
# - Se os dois últimos dígitos forem 00 (ou seja, 100, 400, 1500), o ano tem que ser perfeitamente divisível por 400
# - Ou se o ano for perfeitamente divisível por 4

#para pegar somente os dois últimos números do ano digitado, essa fórmula matemática nos ajuda.
#aprendi isso no seguinte vídeo: https://www.youtube.com/watch?v=wD2aerLMBWA
oFinal=ano%100
#primeiro testamos se o ano é um multiplo de 100
if oFinal == 00:
	#se for o caso, testaremos se ele é divisível por 400
	#o operador % armazena o resto da divisão. se o resto for 0, então foi uma divisão perfeita!
	if ano%400 == 0:
		print("Esse ano foi/será bissexto!")
	else:
		print("Esse ano não foi/será bissexto!")
else:
	#o outro caso para o ano ser bissexto é ser divisível por 4
	if oFinal%4 == 0:
		print("Esse ano foi/será bissexto!")
	else:
		print("Esse ano não foi/será bissexto!")
	
	

