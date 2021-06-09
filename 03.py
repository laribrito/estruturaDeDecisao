#coding: UTF-8
import os

def limpar():
	os.system("clear" or "cls")

limpar()
print(" - Sexo biológico -")
sexo = input(" Digite uma letra: \n  > ")

if sexo.lower() == "f":
	print(f"Informação digitada foi: F - Feminino.")
elif sexo.lower() == "m":
	print(f"Informação digitada foi: M - Masculino")
else: 
	print("Você digitou um sexo inválido.")
