

import time


def Atv01():
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

def Atv02():
    ini = int(input("Iniciar em: "))
    fim = int(input("Finalizar em: "))
    pulando = int(input("Pualando de: "))
    for i in range(ini,fim+1,pulando):
        print(i)
    print ("Fim")
    return

def Atv03():
    s = 0
    cont = ""
    while cont != "r":
        for i in range(0,4):
            cont = 0
            n = int(input("Digite um valor: "))
            s += n
        print("A soma dos valores é: {}".format(s))

    return 
 
def Atv4():
    for i in range(-10,0):
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
        
Atv6()
    