#coding: UTF-8
import os

def limpar():
	os.system("clear" or "cls")

limpar()
print(" - Quem é o maior? -")
n1 = int(input(" Digite um número: \n  > "))
n2 = int(input(" Digite outro número: \n  > "))
if n1 > n2:
	print(f"O primeiro número é o maior. O primeiro número foi: {n1}")
elif n2 > n1:
	print(f"O segundo número é o maior. O segundo número foi: {n2}")
else: 
	print("Você é esperto! Digitou números iguais.")
