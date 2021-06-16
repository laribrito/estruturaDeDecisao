#coding: UTF-8
import os

def limpar():
	os.system("clear" or "cls")

limpar()
print(" - Que produto devo comprar? -")
input("1. Qual o ponto forte do primeiro produto? \n > ")
v1 = float(input("1. Valor do primeiro produto: \n  > R$ "))
input("2. Qual o ponto forte do segundo produto? \n > ")
v2 = float(input("2. Valor do segundo produto: \n  > R$ "))
input("3. Qual o ponto forte do terceiro produto? \n > ")
v3 = float(input("3. Valor do terceiro produto: \n  > R$ "))

if v1<v2:
	if v1<v3:
		print("Com certeza o primeiro produto é o melhor!")
	else:
		print("Com certeza o terceiro produto é o melhor!")
elif v2<v3:
	print("Com certeza o segundo produto é o melhor!")
else:
	print("Com certeza o terceiro produto é o melhor!")