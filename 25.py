#coding: UTF-8
import os

def limpar():
	os.system("clear" or "cls")

#QUESTÃO: Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" 
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".


limpar()
lista=[]
print(" - Responda com sinceridade -")
resposta = input("Telefonou para a vítima? (S/N): \n  > ")
#se a resposta for positiva, ela será colocada na lista
#no fim do programa, de acordo com o tamanho da lista saberemos quantas 
#respostas positivas foram dadas
if resposta.lower() == "s":
    lista.append(resposta)
resposta = input("Esteve no local do crime? (S/N): \n  > ")
if resposta.lower() == "s":
    lista.append(resposta)
resposta = input("Mora perto da vítima? (S/N): \n  > ")
if resposta.lower() == "s":
    lista.append(resposta)
resposta = input("Devia para a vítima? (S/N): \n  > ")
if resposta.lower() == "s":
    lista.append(resposta)
resposta = input("Já trabalhou com a vítima? (S/N): \n  > ")
if resposta.lower() == "s":
    lista.append(resposta)

#receber o tamanho da lista com a função LEN
tamanho = len(lista)

#fazer os testes com essa nova variavel
if tamanho == 5:
    print(f"Por responder que sim a {tamanho} perguntas, você é considerado culpado!")
elif tamanho >=3:
    print(f"Por responder que sim a {tamanho} perguntas, você é considerado cúmplice!")
elif tamanho ==2:
    print(f"Por responder que sim a {tamanho} perguntas, você é considerado suspeito!")
else:
    print(f"Por responder que sim a {tamanho} perguntas, você está liberado!")