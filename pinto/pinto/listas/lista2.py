# lista=[]

# for i in range(11):
#     lista.append(i*10)

# print(lista)

import random


def llenarListaFactorDiez(lista,cantidad):
    lista=[]
    for i in range(cantidad):
        lista.append(i*10)
    return lista

def llenarLista(lista,cantidad):
    lista=[]
    num=0
    for i in range(cantidad):
        num=int(input("ingrese numero"))
        lista.append(num)
    return lista

vector=[]
vector=llenarLista(vector,5)
print(vector)
# print("-"*20)
# llenarLista(10)
# print("-"*20)
# llenarLista(20)

import random
def llenarListaRandom(lista,cantidad):
    lista=[]
    num=0
    for i in range(cantidad):
        num=random.randint(1,100)
        lista.append(num)
    return lista

vec=[]
tam=int(input("Cuantos numeros ingreso a la lista"))
vec=llenarListaRandom(vec,tam)
print(vec)


slice1=vec[len(vec)//2:len(vec)]
#slice1=vec[len(vec)//2:9] #No toma el último
#slice1=vec[len(vec)//2:-1] #No toma el último
print(slice1)