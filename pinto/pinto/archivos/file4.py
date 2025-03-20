with open('archivos/himno.txt','r') as file:
    contenido = file.read()
    palabra = 'gloria'
    
contenido=contenido.split()
print(contenido)
repeticiones = [palabra for x in contenido if x == palabra.lower()]

print(repeticiones)
#palabras = contenido.lower().split()
#repeticiones = [palabra for palabra in palabras if palabra == palabra.lower()]

if repeticiones: 

    print(f'la palabra"{palabra}" se repite {len(repeticiones)} veces')
else:
    print(f'la palabra "{palabra}" no se encuentra en el archivo')



with open('archivos/himno.txt','r') as file:
    contenido = file.read()
    palabra = 'gloria'


def palabra():
    with open ('archivos/himno.txt' , 'rt',encoding='utf-8') as him :
            con=0
            pal=input('ingrese la palabra que desea buscar: ')
            no=him.read().lower()
            sep=no.split()
            for j in sep:
                if j == pal:
                    con+=1
            if con>0:
                return f'la palabra si se encuentra y se repite {con} de veces'
            else:
                return 'la palabra no se encuentra'

print(palabra())