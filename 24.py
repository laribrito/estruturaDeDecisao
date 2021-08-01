#coding: UTF-8
import os

def limpar():
	os.system("clear" or "cls")

#QUESTÃO: Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação 
# ele deseja realizar. O resultado da operação deve ser acompanhado de uma 
# frase que diga se o número é:
#   par ou ímpar;
#   positivo ou negativo;
#   inteiro ou decimal.


limpar()
print(" - Compare dois números -")
a = float(input("Digite um número para ser analisado: \n  > ")) #recebe o primeiro número
b = float(input("Digite outro número para ser analisado: \n  > ")) # recebe o segundo
limpar()
#exibe o menu
print(f" | Os números foram: {a} e {b}    ") 
print(" | Escolha o teste a ser feito:  ")
print(" | [1] - Par ou Ímpar             |")
print(" | [2] - Positivo ou Negativo     |")
print(" | [3] - Inteiro ou decimal       |")
#recebe a opção escolhida
opc = int(input("\n > "))

#encaminhar para a opção desejada
if opc == 1:
    #par ou ímpar
    #teste para variavel 'a'
    if a == 0:
        par = True
    else:
        if a%2==0:
            par=True
        else:
            par=False

    if par:
        print(f"{a} é par!")
    else:
        print(f"{a} é ímpar!")
    #teste para variavel 'b'
    if b == 0:
        par = True
    else:
        if b%2==0:
            par=True
        else:
            par=False

    if par:
        print(f"{b} é par!")
    else:
        print(f"{b} é ímpar!")
elif opc==2:
    #positivo ou negativo
    #teste para variavel 'a'
    if a > 0:
        print(f"{a} é um número positivo.")
    elif a < 0:
        print(f"{a} é um número negativo.")
    else: 
        print("Você é esperto! Digitou o número 0.")
    #teste para variavel 'b'
    if b > 0:
        print(f"{b} é um número positivo.")
    elif b < 0:
        print(f"{b} é um número negativo.")
    else: 
        print("Você é esperto! Digitou o número 0.")
elif opc==3:
    #inteiro ou decimal
    #teste para variavel 'a'
    aux=int(a)
    if a==aux:
        print(f"{a} é um número inteiro.")
    else:
        print(f"{a} é um número decimal.")
    #teste para variavel 'b'
    aux=int(b)
    if b==aux:
        print(f"{b} é um número inteiro.")
    else:
        print(f"{b} é um número decimal.")
else:
    #valor invalido
    print("Opção não disponível. Tente novamente.")

