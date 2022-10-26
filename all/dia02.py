
import os
import time
from turtle import clear


def Atv1():
    resposta = "S"
    while resposta == "S":
       valor = int(input("Digite um valor: "))
       resposta = str(input("Deseja sair[S/N]: ")).upper()
    print("Saindo...")
    print(valor)
    
def Atv2():
    feminino = "F"
    masculino = "M"
    sair = 1
    while sair != 0 :
        sexo = str(input("Digite Seu sexo [F] para feminino e [M] masculino: ")).upper()
        if sexo == feminino:
            print("Seu sexo é Feminino")
        if sexo == masculino:
            print("Seu sexo é Masculino")
            
        if sexo != feminino and sexo != masculino:
            print("Opção Inválida")
        sair = int(input("Para sair aperte [0] Para continuar aperte [1]"))

        if sair != 1 and sair != 0 and sair != int:
             print("Opção Inválida")
    print("Saindo...")


def Atv3():
    try:
        os.system('clear')
        opcao = 0
        while opcao == 0:
            valor1 = int(input("Digite um Número: "))
            valor2 = int(input("Digite outro Número: "))
            if valor1 < 0 or valor2 < 0:
                print("Números negativos não é valido")
                time.sleep(2)
                Atv3()
                return
            opcao = int(input(
            """\nSelecione uma opção\n
        |   [1] Somar          |
        |   [2] Multiplicar    |
        |   [3] Dividir        |
        |   [4] Novos números  |
        |   [5] Sair           |
        |                      | 
        """"R: """))
        
        if opcao == 1:
            print("{} + {} = {}".format(valor1, valor2,valor1+valor2))
            return
        if opcao == 2:
            print ("{} X {} = {}".format(valor1, valor2, valor1*valor2))
            return
        if opcao == 3:
            print ("{} ÷ {} = {}".format(valor1, valor2, valor1/valor2))
            return
        if opcao == 4:
            Atv3()
            return
        os.system('clear')
        if opcao == 5:
            print("Saindo...")
            return
        if opcao >= 0 or opcao <= 6:
            print( "{} Não é uma opção valida:".format(opcao))
            time.sleep(2)
            Atv3()
            return
    except:
        print("Não é um número tente novamente.")
        time.sleep(2)
        Atv3()
        return
Atv3()
#OBS: ao escolher o numero do menu executar ele. 


