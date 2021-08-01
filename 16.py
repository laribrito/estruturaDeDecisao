#coding: UTF-8
import os
import math

def limpar():
	os.system("clear" or "cls")

limpar()
print(" - Calculadora # EQUAÇÃO DO SEGUNDO GRAU -")
print("Informe os valores de A, B, e C, seguindo esta ordem.")
a = float(input("Valor de A: \n  > "))
if a == 0:
	print("Se o valor de A é zero, essa não é uma equação de segundo grau,\ne portanto não será resolvida aqui.")
else:
	b = float(input("Valor de B: \n  > "))
	c = float(input("Valor de C: \n  > "))

	delta=math.pow(b,2)-(4*a*c)

	if delta < 0:
		print("Essa equação não tem resultados reais. Delta deu um valor negativo. ")
		print(f"Delta = {delta}")
	elif delta ==0:
		print("Essa equação terá somente um resultado real.")
		print(f"Delta = {delta}")
		raiz = ((-b) - math.sqrt(delta))/(2*a)
		print(f"A raiz dessa equação é:\nR1 = {raiz}\nR2 = R1")
	else:
		print("Essa equação terá dois resultados reais. Delta deu um valor positivo. ")
		print(f"Delta = {delta}")
		raiz1 = ((-b) - math.sqrt(delta))/(2*a)
		raiz2 = ((-b) + math.sqrt(delta))/(2*a)
		print(f"As raizes dessa equação são:\nR1 = {raiz1}\nR2 = {raiz2}")
		
