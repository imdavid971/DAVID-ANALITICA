
x=int(input("ingrese un numero"))
if x>0:
    print("positivo")
elif x<0:
    print("negativo")
else :
    print("neutro")

est=int(input("ingrese estrato"))
match est:
    case 1:
        print("Estrato 1")     
    case 2:
        print("Estrato 2")
    case 3:
        print("Estrato 3")
    case 4:
        print("Estrato 4")
    case 5:
        print("Estrato 5")
    case 6:
        print("Estrato 6")
    case _:
        print("opcion no existe")
    

def ppp():
    print("hola")
    #return 1

print(ppp())
# x=ppp()
# print(x)

