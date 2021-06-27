#coding: UTF-8
import os

#função para limpar a tela
def limpar():
	os.system("clear" or "cls")

#QUESTÃO: Faça um Programa que leia um número inteiro menor que 1000 
# e imprima a quantidade de centenas, dezenas e unidades do mesmo

# IMPORTANTE: sugiro que aprender a usar árvore de decisões, para trabalhar melhor com 
#  "if's" aninhados

#RESOLUÇÃO: 
# primeiro eu separei os números das dezenas, centenas e unidades usando a matemática, como 
#  aprendi no exercicio 17 desse módulo
# depois, como o exercício especifica como devemos exibir os resultados, faço uma cadeia de testes
#  para armazenar a forma correta de exibir o texto. Ex.: centena = 1 exibir "uma centena", enquanto
#  centena = 4 exibir "4 centenas"
# por último, exibir na tela o resultado disso tudo. Sei que tem como fazer isso com laços de repetição
#  mas me desafiei a resolver somente com estruturas de decisões, pois me parece ser a temática 
#  desse módulo

SEP=", "
END=".\n"

limpar()
print(" - Centenas, dezenas e unidades -")
print("Para números com 3 dígitos")
num = int(input("Insira o número para ser analisado: \n  > "))

if num < 1000 and num > -1000:
	unidade = num % 10
	dezena = num //10 %10
	centena=num//100%10

	if centena == 0:
		c = None
	else:
		if centena == 1:
			c = " 1 centena"
		else:
			c = f" {centena} centenas"

	if dezena == 0:
		d = None
	else:
		if dezena == 1:
			d = "1 dezena"
		else:
			d = f"{dezena} dezenas"
		
	if unidade == 0:
		u = None
	else:
		if unidade == 1:
			u = "1 unidade"
		else:
			u = f"{unidade} unidades"

	if c:
		if d:
			if u:
				print(f"{num} = {c}", f"{d}", f"{u}", sep=SEP, end=END)
			else:
				print(f"{num} = {c}", f"{d}", sep=SEP, end=END)
		elif u:
			print(f"{num} = {c}", f"{u}", sep=SEP, end=END) 
		else:
			print(f"{num} = {c}", sep=SEP, end=END)
	elif d:
		if u:
			print(f"{num} = {d}", f"{u}", sep=SEP, end=END)
		else:
			print(f"{num} = {d}", sep=SEP, end=END)
	elif u:
		print(f"{num} = {u}", sep=SEP, end=END)
	else:
		print("O número digitado foi 0. Não tem nada.")

else:
	print("Número inválido. Tente novamente!")


