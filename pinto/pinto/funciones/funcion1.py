def divisores(num):
    #indentación
    for i in range(1,num+1):
        if num%i==0:
            print(i)

#divisores(10)
#divisores(20)
print(divisores(15))

def sumDivisores(num):
    sum=0
    for i in range(1,num):        
        if num%i==0:
            sum+=i
    return sum

def perfectos(num):
    if num==sumDivisores(num):
        return "perfecto"
    else:
        return "no es perfecto"

def primos(num):
    if sumDivisores(num)==1:
        return "es primo"
    else: 
        return "no es primo"

#print(sumDivisores(10))
#print(perfectos(28))
print(len(perfectos(28)))

print(primos(9))