from rich import print 

lista = [5,4,9,8,7,3]
##while True :
   # pgt = int(input("Digite um numero ---> (Valor negativo para cancelar):"))
   # if pgt >= 0:
        #lista.append(pgt)
    #elif pgt < 0 :
    # 
lista_crescente = []
lista_Dec = []

def decrescente() :
  
    while lista != []:
        maior_numero = max(lista, key=int)
        lista_crescente.append(maior_numero)
        lista.remove(maior_numero)
    return lista_crescente

def crescente() :
  
    while lista != []:
        menor_numero = min(lista, key=int)
        lista_Dec.append(menor_numero)
        lista.remove(menor_numero)
    return lista_Dec

escolha = input("Deseja ver a lista crescente(C) ou Decrescente (D)?")

if escolha =="D":
    print (decrescente())
   
elif escolha == "C":
    print(crescente())
elif escolha != "D" and escolha!="C":
    print("Digite D ou C ")



        



