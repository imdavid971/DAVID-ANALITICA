#import module
from module import sumar,restar,multiplicar,dividir
from module import llenarListaRandom
# n1=100
# n2=200
# print(sumar(n1,n2))
ppp=[]
ppp=llenarListaRandom(ppp)
print(ppp)





def sumar(a,b):
    return "dañé la función que suma"

sel=1
while sel !=5:
    print("1-sumar")
    print("2-restar")
    print("3-multiplicar")
    print("4-dividir")
    print("5-salir")

    sel=int(input("Seleccione Opción"))

    num1=int(input("Numero 1"))
    num2=int(input("Numero 2"))
    match sel:
        case 1:
            print(sumar(num1,num2))
        case 2:
            print(restar(num1,num2))
        case 3:
            print(multiplicar(num1,num2))
        case 4:
            print(dividir(num1,num2))
        case 5:
            break
        case _:
            print("Opción Equiviocada") 
    