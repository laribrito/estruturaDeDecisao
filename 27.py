#coding: UTF-8
import os

def limpar():
	os.system("clear" or "cls")

# #QUESTÃO: Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar
#  R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo
#  para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas 
# e escreva o valor a ser pago pelo cliente.

limpar()
#preços em caixa alta como constantes
PRECO_MO_1 = 2.5
PRECO_MO_2 = 2.2
PRECO_MA_1 = 1.8
PRECO_MA_2 = 1.5
print(" - Quitanda da dona Paulina -")
ma = float(input("Quantos quilos de maçã foram comprados? \n > "))
mo = float(input("Quantos quilos de morango foram comprados? \n > "))

#testes referentes ao morango
if mo <= 5:
    valorMO = mo * PRECO_MO_1
else:
    valorMO = mo * PRECO_MO_2

#testes referentes à maçã
if ma <= 5:
    valorMA = ma * PRECO_MA_1
else:
    valorMA = ma * PRECO_MA_2

#testes referentes ao desconto de 10%
valorTotal = valorMO + valorMA
quantTotal = ma + mo
if quantTotal > 8 or valorTotal > 25:
    valorTotal = valorTotal - (valorTotal*0.1)

#exibindo o resultado
print(f'Valor total da compra: R$ {valorTotal:.2f}') #Variável valorTotal formatada para apresentar somente duas casas decimais
