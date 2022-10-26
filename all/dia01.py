

from functools import reduce
import re
import time


def Atv1():
    for i in range(0,3):
        a = "Passo"
        b = "Pega"
        c = "pula"
        if i >=0:
            print(a)
    print(b)
    print(c)
    for i in range(0,2):
        print(a)
    return

def Atv2():
    ini = int(input("Iniciar em: "))
    fim = int(input("Finalizar em: "))
    pulando = int(input("Pualando de: "))
    for i in range(ini,fim+1,pulando):
        print(i)
    print ("Fim")
    return

def Atv3():
    s = 0
    for i in range(0,4):
        n = int(input("Digite um valor: "))
        s += n
    print("A soma dos valores é: {}".format(s))
    return 
 
def Atv4():
    for i in range(10,-1,-1):
        print(i)
        time.sleep(1)
    print("""
         ☆┌─┐　─┐☆ 
          │▒│ /▒/
          │▒│/▒/
          │▒ /▒/─┬─┐
          │▒│▒|▒│▒│
         ┌┴─┴─┐-┘─┘
         │▒┌──┘▒▒▒│
         └┐▒▒▒▒▒▒┌┘
          └┐▒▒▒▒┌
                 KBOMMM!!""") 
    return

def Atv5():
    pulando = 2
    for i in range(1,51,pulando):
     print(i)
     time.sleep(1)
    return
  
def Atv6():
    numero = int(input('Número: '))
    if (numero % 2) == 0:
            print ("{} é Par".format(numero))
    else:
         print("{} é Impar".format(numero))
    return
        
def Atv7():
    numero = int(input("Número para saber sua tabuada? \n "))
    for i in range(1,11):
         print("{} X {} = {}".format(numero, i, (numero * i)))
    return

def Atv8():
    s = 0
    for i in range(0,6):
        numero = int(input("Digite um valor: "))
        if (numero % 2) == 0:
            s += numero
    print("A soma dos valores ímpares é: {}".format(s))
    
    return 

def Atv9():
    nome1 = str(input("Nome: "))
    ano1 = int(input("Ano: "))
    nome2 = str(input("Nome: "))
    ano2 = int(input("Ano: "))
    nome3 = str(input("Nome: "))
    ano3 = int(input("Ano: "))
    dados = [ano1, nome1, ano2, nome2, ano3, nome3]
    print ("AQUI",dados)
    for i in range(len(dados)):
        maior = 2005
        if dados[0] <= maior:
            print(dados[0],dados[1],"é maior de idade")
            
        if dados[2]<= maior:
            print(dados[2],dados[3],"é maior de idade")
            
        if dados[4] <= maior:
            print(dados[4],dados[5],"é maior de idade") 
    
        return
    
''' def Atv10():
    soma = 0
    maioridadehomen = 0
    nomevelho = ""
    totalmulher = 0
    for i  in range(1,4):
        nome  = str(input("Nome: "))
        idade = int(input("Idade: "))
        sexo  = str(input("Sexo[M/F]: ")).strip()
        soma += idade
    if i == 1 and sexo in "Mn":
        maioridadehomen = idade
        nomevelho = nome
    if sexo in "Mm" and idade > maioridadehomen:
        maioridadehomen = idade
        nomevelho = nome
    maioridade = soma /4
    print("A media de idades é {}".format(soma/4))
    print("O homen mais velho é {} e tem {}".format(nomevelho,maioridade)) '''
        #aqui ja deu a media 
    
        #Falta o nome do homen mais velho
        #quantas mulheres tem mais de 20 anos 