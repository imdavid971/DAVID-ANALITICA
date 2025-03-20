def saludar():
    return 'Hola'

datos={
    "gender": "female",
    "date_of_birth": "05.08.02",
    "enrollment_semester": "Summer 2022",
    "semester_number": 6,
    "major": "Data Analytics",
    "number": 22100,
    "saludo":saludar()
 }

print(datos['saludo'])

def nuevaClave(dict,clave,valor):
    flag=False
    for key in dict.keys():
        if key==clave:            
            return("La clave ya existe") 
                       
        else:
            flag=True

    if flag==True:
        dict[clave]=valor        
    return dict
            


miclave=input("ingrese la nueva clave")
mivalor=input("ingrese valor asociado a la clave")
print(nuevaClave(datos,miclave,mivalor))
print("-"*50)
print(datos)