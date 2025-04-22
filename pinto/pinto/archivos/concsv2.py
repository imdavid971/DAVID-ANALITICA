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
    
    print(max(salarios)