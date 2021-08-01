#coding: UTF-8
import os

def limpar():
	os.system("clear" or "cls")

limpar()
print(" - Veja quanto foi seu aumento! -")

salBruto = float(input("Informe seu salário atual: \n > R$ "))

if salBruto<=280:
	percent = 0.2
	aumento = salBruto * percent
	salNovo = salBruto + aumento

elif salBruto <=700:
	percent = 0.15
	aumento = salBruto * percent
	salNovo = salBruto + aumento

elif salBruto < 1500:
	percent = 0.1
	aumento = salBruto * percent
	salNovo = salBruto + aumento
else:
	percent = 0.05
	aumento = salBruto * percent
	salNovo = salBruto + aumento

print(f"""
Salário antigo:                    : R$ {salBruto:.2f}
Percentual aplicado                :    {percent * 100} %
Valor do aumento                   : R$ {aumento:.2f}
Novo salário                       : R$ {salNovo:.2f}
""")