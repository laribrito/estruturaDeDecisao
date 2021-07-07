#coding: UTF-8
import os

def limpar():
	os.system("clear" or "cls")

#QUESTÃO: Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
#   até 20 litros, desconto de 3% por litro
#   acima de 20 litros, desconto de 5% por litro
# Gasolina:
#   até 20 litros, desconto de 4% por litro  
#   acima de 20 litros, desconto de 6% por litro 
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível 
# (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor 
# a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 e o 
# preço do litro do álcool é R$ 1,90.


limpar()
#valores dos combustivel como "constantes"
VALORA = 1.9
VALORG = 2.5
print(" - Posto Ipiranga -")
#o tipo do combustível é armazenado em "tipo"
print("Qual o combustível vendido?:")
print("Digite A para Álcool")
print("Digite G para Gasolina")
tipo = input(" > ")
#a quantidade de litros vendida vai para "quant"
quant = int(input("Quantos litros foram vendidos?: \n  > "))

#primeiro deve-se identificar o combustível vendido
if tipo.lower() == "g":
    #sendo gasolina, vamos identificar o desconto obtido pelo cliente
    if quant > 20:
        desconto = 0.06 # acima de 20 litros, desconto de 6% por litro 
    else:
        desconto = 0.04 # até 20 litros, desconto de 4% por litro
    #vamos calcular o desconto/litro
    desconto = desconto * VALORG
    # e o valor do litro com o desconto
    valorL=VALORG - desconto
elif tipo.lower() == "a":
    if quant > 20:
        desconto = 0.05 # acima de 20 litros, desconto de 5% por litro
    else:
        desconto = 0.03 # até 20 litros, desconto de 3% por litro
    #vamos calcular o desconto/litro
    desconto = desconto * VALORA
    # e o valor do litro com o desconto
    valorL=VALORA - desconto
else:
    #se não for informado um tipo de combustivel válido, o "valorL" recebe 0, para que 
    # não ocorra um erro na linha 60
    print("Erro. Tente novamente.")
    valorL = 0

#o valor final será o "valorL" multiplicado pelos litros vendidos
valorFinal = valorL * quant

print(f"Valor final: R$ {valorFinal:.2f}")



