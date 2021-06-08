#coding: UTF-8
import os

def limpar():
	os.system("clear" or "cls")

limpar()
print(" - Negativo ou positivo? -")
n1 = int(input(" Digite um número: \n  > "))

if n1 > 0:
	print(f"{n1} é um número positivo.")
elif n1 < 0:
	print(f"{n1} é um número negativo.")
else: 
	print("Você é esperto! Digitou o número 0.")
