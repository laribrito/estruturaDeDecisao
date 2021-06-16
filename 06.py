#coding: UTF-8
import os

def limpar():
	os.system("clear" or "cls")

limpar()
print(" - Quem é o maior? -")
a = float(input("Digite o primeiro número: \n  > "))
b = float(input("Digite o segundo: \n  > "))
c = float(input("Mais um número: \n  > "))

if a>b:
	if a>c:
		print(f"{a} é o maior número.")
	else:
		print(f"{c} é o maior número.")
elif b>c:
	print(f"{b} é o maior número.")
else:
	print(f"{c} é o maior número.")