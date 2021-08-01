#coding: UTF-8
import os

def limpar():
	os.system("clear" or "cls")

limpar()
print(" - Ordenando do maior para o menor! -")

semana = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
count = 1
num = float(input("Digite um número: \n > "))

if num < 0 or num > 8:
	print("Valor inválido!")
else:
	for dia in semana:
		if count == num:
			print(f"O número que você digitou corresponde a esse dia da semana: {dia}.")
		count += 1