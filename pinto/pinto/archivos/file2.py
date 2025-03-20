# with open("archivos/texto.txt","a",encoding="utf-8") as pointer:
#     pointer.write("Parte 3 trabajo con archivos\n")

# with open("archivos/himno.txt","r") as pointer:
#     st=pointer.read()
#     print(type(st))
#     cont=0
#     for letra in st:
#         print(letra)
#         cont+=1
#         if cont==20:
#             break
    #print(st.upper())

#with open("archivos/himno.txt","r") as pointer:
    #result=pointer.readline()
    #print(type(result))
    #print(result)
    # line_counter=0
    # character_counter=0
    # line = pointer.readline()
    # while line != '':
    #     print(line)
    #     # line_counter += 1
    #     # for char in line:
    #     #     print(char, end='-')
    #     #     character_counter += 1
    #     line = pointer.readline()
    


# with open("archivos/himno.txt","r") as pointer:
#     result=pointer.readlines()
#     print(type(result))
#     print(result[0])

# for linea in result:
#     print(linea)

with open("archivos/himno.txt","r") as pointer:
    st=pointer.read()
    contma=0
    contmi=0
    for letra in st:
        if letra.isupper()==True:
            contma+=1
        elif letra.islower()==True:
            contmi+=1

print(f"cantidad mayusculas={contma}")
print(f"cantidad minusculas={contmi}")

s="amo la programacion"
print(s.split())


#lista3=[0 if x%2==0 else x for x in lista]

palabra="gloria"

st=st.split()
#repeticiones = [palabra for x in palabras if x == palabra.lower()]

#print(repeticiones)