import random

conjunto={1}
#print(type(conjunto))
conjunto2=set(['a',1,2,4])
print(conjunto2.pop())
print(conjunto2)
print(conjunto2.remove(111))
print(conjunto2.discard(111)

lista=[random.randint(1,10) for i in range(20)]
#lista=(random.randint(1,10) for i in range(15))
print(lista)
print(type(lista))
conjunto3=set(lista)
print(type(conjunto3))
print(conjunto3)

conjunto.update(lista)
print(f"conjunto despues de update")
print(f"{conjunto}")
conjunto.add(100)
print(f"{conjunto}")
print(conjunto.pop())
print(f"{conjunto}")