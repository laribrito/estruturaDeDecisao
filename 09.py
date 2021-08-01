#coding: UTF-8
import os

def limpar():
	os.system("clear" or "cls")

limpar()
print(" - Ordenando do maior para o menor! -")

a = float(input("Digite um número: \n > "))
b = float(input("Digite outro número: \n > "))
c = float(input("Mais um número: \n > "))

if a>b:
	if a>c: 
		if b>c:
			print(f"Em ordem decrescente, ficarão:\n{a}\n{b}\n{c}")
		else:
			print(f"Em ordem decrescente, ficarão:\n{a}\n{c}\n{b}")
	else:
		print(f"Em ordem decrescente, ficarão:\n{c}\n{a}\n{b}")
elif b>c:
	if a>c:
		print(f"Em ordem decrescente, ficarão:\n{b}\n{c}\n{a}")
	else:
		print(f"Em ordem decrescente, ficarão:\n{b}\n{a}\n{c}")
else:
	print(f"Em ordem decrescente, ficarão:\n{c}\n{b}\n{a}")