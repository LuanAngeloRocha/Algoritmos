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

lista_vdd = []
if escolha =="D":
    lista_vdd = decrescente()
    print (decrescente())

   
elif escolha == "C":
    lista_vdd = crescente()
    print(crescente())
elif escolha != "D" and escolha!="C":
    print("Digite D ou C ")


qtd_lista = len(lista_vdd)
while True :
    pilha = int(input("voce quer remove o valor de qual posição : [valor negativo para cancelar]:"))
    if pilha > qtd_lista:
            input("Não esxite esta posição, por faor digite uma posição válida(enter para continuar):")
    
    elif pilha >= 0 :
        pilha -= 1
        lista_vdd.pop(pilha)
        print(lista_vdd)
        
    elif pilha < 0 :
        break 
        








