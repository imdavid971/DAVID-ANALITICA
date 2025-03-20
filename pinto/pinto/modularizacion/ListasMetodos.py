import module
vec=[]
vec2=[10,20,30,10,5]
print(f"vec2={vec2}")
vec=module.llenarListaRandom(vec)
#print(vec)
vec.extend(vec2)
vec.insert(1,1.5)
#print(vec)
#vec2.remove()

x=vec2.pop(2) 
print(f"vec2={vec2}")
print(f"x={x}")

indice=vec2.index(5)
print(f"indice={indice}")
print(f"vec={vec}")
print(vec.count(10))
vec.sort()
print(f"vec={vec}")
vec.reverse()
print(f"vec={vec}")
vec3=vec.copy()
print(f"vec3={vec3}")

