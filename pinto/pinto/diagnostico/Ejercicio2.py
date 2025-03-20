print("A continuacion digite tres numeros")
Num1=int(input("Ingrese el primer numero"))
Num2=int(input("Ingrese el segundo numero"))
Num3=int(input("Ingrese el tercer numero"))

if Num1==Num2==Num3:
    print("Los tres numeros son iguales")
else:
    if Num1==Num2>Num3:
        print("Hay dos numero iguales")
    else:
        if Num1==Num2<Num3:
            print("Hay dos numeros iguales")
        else:
            if Num1==Num3>Num2:
                print("Hay dos numeros iguales")
            else:
                if Num1==Num3<Num2:
                    print("Hay dos numeros iguales")
                else:
                    if Num2==Num1>Num3:
                        print("Hay dos numero iguales")
                    else:
                        if Num2==Num1<Num3:
                            print("Hay dos numeros iguales")
                        else:
                            if Num2==Num3>Num1:
                                print("Hay dos numeros iguales")
                            else:
                                if Num2==Num3<Num1:
                                    print("Hay dos numeros iguales")
                                else:
                                    if Num3==Num2>Num1:
                                        print("Hay dos numeros iguales")
                                    else:
                                        if Num3==Num2<Num1:
                                            print("Hay dos numeros iguales")
                                        else:
                                            if Num3==Num1>Num2:
                                                print("Hay dos numeros iguales")
                                            else:
                                                if Num3==Num1<Num2:
                                                    print("Hay dos numeros iguales")
                                                else:
                                                    if Num1>Num2<Num3:
                                                        print("Todos los numeros son distintos")
                                                    else:
                                                        if Num1<Num2>Num3:
                                                            print("Todos los numeros son diferentes")
                                                        else:
                                                            if Num2>Num1<Num3:
                                                                print("Todos los numeros son diferentes")
                                                            else:
                                                                if Num2<Num1>Num3:
                                                                    print("Todos los numeros son diferentes")
                                                                else:
                                                                    if Num3>Num1<Num2:
                                                                        print("Todos los numeros son diferentes")
                                                                    else:
                                                                        if Num3<Num1>Num2:
                                                                            print("Todos los numeros son diferentes")