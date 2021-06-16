#coding: UTF-8
import os

def limpar():
	os.system("clear" or "cls")

limpar()
print(" - Estou aprovado? -")
n1 = float(input("Digite a primeira nota: \n  > "))
n2 = float(input("Digite a segunda nota: \n  > "))

media = (n1+n2)/2
print(f"Sua média foi: {media}")
if media == 10:
	print("Aprovado com distinção! Não fez mais que sua obrigação.")
elif media < 7:
	print("Reprovado. Não fique triste, se esforce mais na próxima vez!")
else:
	print("Aprovado! Continue assim!")
