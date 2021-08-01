#coding: UTF-8
import os

def limpar():
	os.system("clear" or "cls")

#QUESTÃO: Faça um Programa que peça um número inteiro e determine 
# se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

#RESOLUÇÃO: É como a própria questão disse. Um número par é divisível por 2.
# se o resto for 0, é par. A excessão é o número 0.

limpar()
print(" - Par ou ímpar? -")
nmr = float(input("Digite um número para ser analisado: \n  > "))

if nmr == 0:
	par = True
else:
	if nmr%2==0:
		par=True
	else:
		par=False

if par:
	print("Esse número é par!")
else:
	print("Esse número é ímpar!")

