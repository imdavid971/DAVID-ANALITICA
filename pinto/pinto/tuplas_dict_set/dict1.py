midiccionario={}
print(type(midiccionario))
datos={
    "gender": "female",
    #"gender":"male",
    "date_of_birth": "05.08.02",
    "enrollment_semester": "Summer 2022",
    "semester_number": 6,
    "major": "Data Analytics",
    "number": 22100,
    "hobbies":["paint","music","sports"],
    "address":{"street":14,
               "number":"11-11",
               "county":"center"
        }
 }

print(datos["gender"])
print(datos["address"]["street"])
print(datos["hobbies"][0])

datos["email"]="mail@mail.com"
datos.update({"email2":"mail2@mail2.com"})
print(datos.get("number"))

datos["semester_number"]=datos["semester_number"]/2
#key, value, item
for clave in datos.keys():
    print(f"clave={clave} y valor={datos[clave]}")

for valor in datos.values():
    print(valor)
    
print("-"*50)
for item in datos.items():
    print(type(item))