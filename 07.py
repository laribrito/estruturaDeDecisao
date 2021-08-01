#coding: UTF-8
import os

def limpar():
	os.system("clear" or "cls")

limpar()
print(" - Quem é o maior? -")
a = int(input("Digite o primeiro número: \n  > "))
b = int(input("Digite o segundo: \n  > "))
c = int(input("Mais um número: \n  > "))

if a>b:
	if a>c:
		print(f"{a} é o maior número.")
	else:
		print(f"{c} é o maior número.")
elif b>c:
	print(f"{b} é o maior número.")
else:
	print(f"{c} é o maior número.")

if a<b:
	if a<c:
		print(f"{a} é o menor número.")
	else:
		print(f"{c} é o menor número.")
elif b<c:
	print(f"{b} é o menor número.")
else:
	print(f"{c} é o menor número.")