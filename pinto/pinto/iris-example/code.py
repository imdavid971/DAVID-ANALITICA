import random

def generarLista(n, minimo=1, maximo=10):
    return[random.randint(minimo, maximo) for _ in range(n)]

def frecuenciaAbsoluta(lista):
    frecuencia={}
    for elemento in lista:
        frecuencia[elemento] = frecuencia.get(elemento, 0) + 1
        return frecuencia
    
def frecuenciaRelativa(frecuencia):
    total = sum(frecuencia.values())
    return{k: v / total for k, v in frecuencia.items()}

def frecuenciaAcumulada():
    acumulada={}
    suma=0
    for clave in sorted(frecuencia):
        suma+=frecuencia[clave]
        acumulada[clave] = suma
        return acumulada

datos = generarLista(100, 1, 10)

fa = frecuenciaAbsoluta(datos)
fr = frecuenciaRelativa(fa)
fac = frecuenciaAcumulada(fa)


print(f"Frecuencia Absoluta")
for numero, conteo in sorted(fa.items()):
    print(f"{numero}: {conteo}")

for numero, frecuencia in sorted(fr.items()):
    print(f"{numero}: {frecuencia:.2f%}")

for numero, acumulado in sorted(fac.items()):
    print(f"{numero}: {acumulado}")