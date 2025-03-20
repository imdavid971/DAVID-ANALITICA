var="global"
def funcion():
    global var
    var="local"
    #print(var)
    return var

print(funcion())
#var1=funcion()
print(var)