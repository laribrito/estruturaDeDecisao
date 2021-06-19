#coding: UTF-8
import os

def limpar():
	os.system("clear" or "cls")

limpar()
print(" - Folha de pagamento -")
quantHoras = float(input("Quantidade de horas trabalhadas por mês: \n > "))
valorHora = float(input("Valor da hora: \n > R$ "))
sind = input("É adepto do sindicato? (S/N) \n > ")

salbruto = valorHora * quantHoras
somador = 0
print(f"\n\nSalário Bruto: ({valorHora} * {quantHoras})      : R$ {salbruto:.2f}")

#IR (-)
ir = 0
if salbruto <=900:
	pass
elif salbruto <=1500:
	percent = 0.05
	ir=salbruto * percent
	print(f"(-) IR ({percent*100}%)                     : R$ {ir:.2f}  ")
elif salbruto <=2500:
	percent = 0.1
	ir=salbruto * percent
	print(f"(-) IR ({percent*100}%)                     : R$ {ir:.2f}  ")
else:
	percent = 0.2
	ir=salbruto * percent
	print(f"(-) IR ({percent*100}%)                     : R$ {ir:.2f}  ")
somador = somador + ir

#Sindicato
s=0
if sind.lower() == "s":
	percent = 0.3
	s = salbruto * percent
	print(f"(-) Sindicato ({percent*100}%)              : R$ {s:.2f}  ")
somador = somador + s

#INSS (-)
percent = 0.1
inss= salbruto * percent
print(f"(-) INSS ({percent*100}%)                  : R$ {inss:.2f}")
somador = somador + inss

#FGTS
percent = 0.11
fgts= salbruto * percent
print(f"FGTS ({percent*100}%)                      : R$ {fgts:.2f}")


salL = salbruto - somador
print(f"""Total dos descontos               : R$ {somador:.2f}
Salário Liquido                   : R$ {salL:.2f}
""")