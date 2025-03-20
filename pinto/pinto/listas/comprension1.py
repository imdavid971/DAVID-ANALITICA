#lista=[10 for i in range(5)]
import random
lista=[i for i in range(5)]
print(lista)
lista=[i*i for i in range(1,6)]
print(lista)
#tam=random.randint(5,20)
lista=[random.randint(0,100) for i in range(random.randint(5,10))]
print(lista)

lista2=[i*i for i in lista]
print(f"lista2={lista2}")

lista3=[0 if x%2==0 else x for x in lista]

lista4=[1 if x<50 else 2 for x in lista]
print(f"lista4={lista4}")

lista5=[x*2 if x%2==0 else x/2 for x in lista]
print(f"lista5={lista5}")