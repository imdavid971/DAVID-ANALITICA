import csv
with open("archivos/employees.csv") as empfile:
    data=csv.reader(empfile)
    #print(type(data))
    emplist=list(data)
    #print(type(emplist))
    #print(len(emplist))
    emplist.pop(0)
    salarios=[]
    for emp in emplist:
        salarios.append(int(emp[7]))
    
    print(max(salarios))


# import csv

# with open('archivos/employees.csv', 'r') as file:
#     empleados = [line.strip().split(',') for line in file.readlines()]
# def obtener_salarios(empleados):
#     nombres = [
#         empleados[1] for empleado in empleados[1:] 
#     ]
#     salarios = [
#         float(empleado[7]) for empleado in empleados[1:]
#         if empleado[7].replace('.', '', 1).isdigit()
#     ]
#     return salarios
# salarios = obtener_salarios(empleados)