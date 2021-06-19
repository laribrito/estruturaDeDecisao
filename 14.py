#coding: UTF-8
import os

def limpar():
	os.system("clear" or "cls")

limpar()
print(" - Estou aprovado? 2.0 -")
n1 = float(input("Digite a primeira nota: \n  > "))
n2 = float(input("Digite a segunda nota: \n  > "))

media = (n1+n2)/2
print(f"Sua média foi: {media}")
if media <=4:
	conceito = "E"
elif media <= 6:
	conceito = "D"
elif media <=7.5:
	conceito = "C"
elif media <=9:
	conceito = "B"
else:
	conceito="A"

if conceito=="E" or conceito =="D":
	print(f"Seu conceito foi {conceito}, portanto, você foi reprovado.")
else:
	print(f"Seu conceito foi {conceito}, portanto, você foi aprovado.")