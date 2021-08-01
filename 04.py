#coding: UTF-8
import os

def limpar():
	os.system("clear" or "cls")

limpar()
print(" - Vogais ou consoantes? -")
letra = input(" Digite uma letra: \n  > ")

if letra.lower() == "a" or letra.lower() == "e" or letra.lower() == "i" or letra.lower() == "0" or letra.lower() == "u":
	print(f"'{letra}' é uma vogal.")
elif letra.isnumeric():
	print(f"Você é esperto. '{letra}' é um número.")
else:
	print(f"'{letra}' é uma consoante.")
