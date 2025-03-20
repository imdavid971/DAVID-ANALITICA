import random

def media(lista):
    sum=0
    for n in lista:
        sum+=n
    return sum/len(lista)

def mitades(lista):
    tam=len(lista)
    print(tam)
    if tam%2!=0:
        m=media(lista)        
        lista.append(int(m))
        tam=len(lista)
        print(lista)
    r1=lista[:int(tam/2)]
    r2=lista[int(tam/2):]
    print(f"mitad1= {r1}")
    print(f"mitad2= {r2}")


def rebanadas(lista, ini,fin):
    if ini>len(lista) or fin<len(lista)*-1:
        return "Fuera del rango de la lista"
    else:
        return lista[ini:fin]

def llenarListaRandom(lista):
    lista=[]
    cantidad=random.randint(5,20)
    num=0
    for i in range(cantidad):
        num=random.randint(1,100)
        lista.append(num)
    return lista

vector=[]
vector=llenarListaRandom(vector)
print(vector)
# reb1=rebanadas(vector,-4,-2)
# print(reb1)
mitades(vector)