#coding: UTF-8
import os

def limpar():
	os.system("clear" or "cls")

# #QUESTÃO: O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
# porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o 
# cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo 
# e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: 
# tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

limpar()
#preços em caixa alta como constantes
#   PREÇOS ATÉ 5 QUILOS
PRECO_FD_1 = 4.90
PRECO_A_1 = 5.90
PRECO_P_1 = 6.90
#   PREÇOS ACIMA DE 5 QUILOS 
PRECO_FD_2 = 5.80
PRECO_A_2 = 6.80
PRECO_P_2 = 7.80

#outras variáveis
desconto = 0
emitirCupom = True

#inicio
print(" - Hipermercado Tapajara -")
print("  * PROMOÇÃO DE CARNES  *")
print("Qual tipo de carne foi comprado?")
print('[1] - Filé duplo')
print('[2] - Alcatra')
print('[3] - Picanha')
opCarne = int(input(' > '))
limpar()

quant = int(input('Quantos quilos foram comprados? \n > '))
limpar()

print("Qual a forma de pagamento?")
print('[1] - Cartão Tabajara')
print('[2] - Dinheiro')
print('[3] - Cartão de crédito')
print('[4] - Cartão de débito')
opPag = int(input(' > '))
limpar()

#variáveis trabalhadas
# opCarne - recebe o tipo da carne comprada, através de números (menu)
# quant - recebe a quantidade em quilos
# opPag - recebe a forma de pagamento, através de números (menu)


#identificar o tipo de carne comprado
if opCarne == 1:
   # caso Filé duplo
   #  testar a quantidade
   tipo = "Filé duplo" #importante para o cupom fiscal
   if quant <= 5:
      valor = quant * PRECO_FD_1 #preço 1 será sempre, nesse código, a menor quantidade
   else:
      valor = quant * PRECO_FD_2
   #  testar a forma de pagamento
   # eu faria somente um teste, para poder calcular o desconto, porém terei que fazer os outros testes para colocar a informação correta no cupom fiscal
   if opPag == 1:
      desconto = valor*0.05 #desconto de 5%
      pag = "Cartão Tabajara"
   elif opPag == 2:
      pag = "Dinheiro"
   elif opPag == 2:
      pag = "Cartão de crédito"
   else:
      pag = "Cartão de débito"

#identificar o tipo de carne comprado
elif opCarne == 2:
   # caso Alcatra
   #  testar a quantidade
   tipo = "Alcatra" #importante para o cupom fiscal
   if quant <= 5:
      valor = quant * PRECO_A_1 #preço 1 será sempre, nesse código, a menor quantidade
   else:
      valor = quant * PRECO_A_2
   #  testar a forma de pagamento
   # eu faria somente um teste, para poder calcular o desconto, porém terei que fazer os outros testes para colocar a informação correta no cupom fiscal
   if opPag == 1:
      desconto = valor*0.05 #desconto de 5%
      pag = "Cartão Tabajara"
   elif opPag == 2:
      pag = "Dinheiro"
   elif opPag == 2:
      pag = "Cartão de crédito"
   else:
      pag = "Cartão de débito"

#poderia colocar um else aqui, mas esse programa entenderá se não for digitado um número correto
# ver linha 126

#identificar o tipo de carne comprado
elif opCarne == 3:
   # caso Picanha
   #  testar a quantidade
   tipo = "Picanha" #importante para o cupom fiscal
   if quant <= 5:
      valor = quant * PRECO_P_1 #preço 1 será sempre, nesse código, a menor quantidade
   else:
      valor = quant * PRECO_P_2
   #  testar a forma de pagamento
   # eu faria somente um teste, para poder calcular o desconto, porém terei que fazer os outros testes para colocar a informação correta no cupom fiscal
   if opPag == 1:
      desconto = valor*0.05 #desconto de 5%
      pag = "Cartão Tabajara"
   elif opPag == 2:
      pag = "Dinheiro"
   elif opPag == 2:
      pag = "Cartão de crédito"
   else:
      pag = "Cartão de débito"

else:
   print("Tipo de carne não válido. Verifique o menu e tente novamente")
   emitirCupom = False #como eu não consigo parar o programa aqui, já que ele não está dentro de um loop, vou criar essa variável para parar o programa. ver o último if do programa

if emitirCupom:
   #para emitir o cupom exigido pela questão é necessário criar variáveis e armazenar o devido valor nela
   # por isso eu criei a variável tipo e a pag
   print(" - Hipermercado Tapajara -")
   print('       CUPOM FISCAL       ')
   print(f"| TIPO DE CARNE: {tipo}")
   print(f"| QUANTIDADE (kg): {quant}")
   print(f"| FORMA DE PAGAMENTO: {pag}")
   print(f"| PREÇO TOTAL: R$ {valor}")
   print(f"| DESCONTO: R$ {desconto:.12f}")
   print(f"| PREÇO FINAL: R$ {valor-desconto}")
else:
   pass
                     


