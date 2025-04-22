import random
l1=[random.randint(1,100) for i in range(random.randint(5,10))]
l2=[random.randint(1,100) for i in range(random.randint(5,10))]
c1=set(l1)
c2=set(l2)
print(c1)
print(c2)
print(f"union{c1 | c2}")
print(f"interseccion{c1 & c2}")
print(f"diferencia{c1 - c2}")
print(f"dif simetrica{c1 ^ c2}")

