#coding: UTF-8
import os

def limpar():
	os.system("clear" or "cls")

limpar()
print(" - Uma saudação adequada! -")
print("  Em que turno você estuda?")
print("""
	M - Matutino
	V - Vespertino
	N - Noturno
""")
turno = input(" > ")

if turno.lower() == "m":
	print("Bom dia para você!")
elif turno.lower() == "v":
	print("Uma boa tarde para você!")
elif turno.lower() == "n":
	print("Boa noite para você!")
else:
	print("Valor inválido. Sinto muito. Tente novamente!")