Num1= int(input("Ingrese el primer numero"))
Num2= int(input("Ingrese el segundo numero"))
Num3= int(input("Ingrese el tercer numero"))
if Num1 >= Num2 <=Num3:
    print("El numero del medio es :",Num1)
else:
    if Num1 <= Num2 >= Num3:
        print("El numero del medio es :",Num1)
    else:
        if Num2 <= Num1 >=Num3:
            print("El numero del medio es :",Num2)
        else:
            if Num2 >= Num1 <= Num3:
                print("El numero del medio es :",Num2)
            else:
                if Num3 <= Num1 >= Num2:
                    print("El numero del medio es :",Num3)
                else:
                    if Num3 >= Num1 <= Num2:
                        print("El numero del medio es :",Num3)
                        