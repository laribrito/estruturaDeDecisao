#coding: UTF-8
import os

def limpar():
	os.system("clear" or "cls")

limpar()
print(" - É ou não um triângulo? -")
lado1 = float(input("Digite o valor do primeiro lado: \n  > "))
lado2 = float(input("O valor do segundo: \n  > "))
lado3 = float(input("Do terceiro agora: \n  > "))

if lado1 == lado2 and lado2 == lado3:
	print("Esses dados são de um triângulo equilátero.")
elif lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado3 + lado1 > lado2:
	if lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
		print("Esses dados são de um triângulo isósceles.")
	else:
		print("Esses dados são de um triângulo escaleno.")
else:
	print("Esses dados não podem formar um triângulo.")
		