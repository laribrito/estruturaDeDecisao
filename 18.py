#coding: UTF-8
import os

#função para limpar a tela
def limpar():
	os.system("clear" or "cls")

#QUESTÃO: Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

limpar()
print(" - Data dd/mm/aaaa -")
print("Digite uma data qualquer:")
dia = int(input("Dia (dd): \n  > "))
mes = int(input("Mês (mm): \n  > "))
ano = int(input("Ano (aaaa): \n  > "))

#confesso que tive que pesquisar sobre a logica desse 
# extrai desse site: https://www.pythonprogressivo.net/2018/02/Determinar-Data-Valida-Invalida.html 
# (mas depois achei uma falta no código acima)
# para cada mês temos um número de dias válidos, então primeiro identificamos o mês, 
# depois testamos o dia, não se esqueçendo de testar o ano bissexto para determinar os dias que fevereiro tem

# um erro no código do site é que a pessoa pode digitar números negativos, que passarão como números válidos
# deve-se corrigir isso nos testes com a variável dia

valida = False

if(mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12):
	if dia <=31 and dia > 0:
		valida=True
elif mes != 2:
	if dia <=30  and dia > 0:
		valida = True
else:
	if ano%4==0 or ano%400==0:
		if dia<=29 and dia > 0:
			valida = True
	else:
		if dia<=28 and dia > 0:
			valida = True

if valida:
	print(f"Parabéns! Essa é uma data válida!\nQue a força esteja com você em {dia:02d}/{mes:02d}/{ano}")
else:
	print("Você digitou algo errado. Não é possível formar uma data com essas informações")