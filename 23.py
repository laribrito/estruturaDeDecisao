#coding: UTF-8
import os

def limpar():
	os.system("clear" or "cls")

#QUESTÃO: Faça um Programa que peça um número e informe 
# se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

#RESOLUÇÃO: Vou receber em float, transformar 
# o número em int(), comparar os dois. Se for diferente, 
# é porque o número tem casas decimais que sumiram na 
# transformação.

limpar()
print(" - Tem casa decimal ou não? -")
a = float(input("Digite um número para ser analisado: \n  > "))

b=int(a)
if a==b:
	print("É um número inteiro.")
else:
	print("É um número decimal.")