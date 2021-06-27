#coding: UTF-8
import os

def limpar():
	os.system("clear" or "cls")

#QUESTÃO: Faça um Programa para leitura de três notas parciais de um aluno. 

#RESOLUÇÃO: Só fiz copiar a questão 5 e adaptar. risos! As vezes a inteligência aplicada é reutilizar o código.

limpar()
print(" - Estou aprovado? -")
n1 = float(input("Digite a primeira nota: \n  > "))
n2 = float(input("Digite a segunda nota: \n  > "))
n3 = float(input("Digite a terceira nota: \n  > "))

media = (n1+n2+n3)/3
print(f"Sua média foi: {media:.2f}")
if media == 10:
	print("Aprovado com distinção! Não fez mais que sua obrigação.")
elif media < 7:
	print("Reprovado. Não fique triste, se esforce mais na próxima vez!")
else:
	print("Aprovado! Continue assim!")
