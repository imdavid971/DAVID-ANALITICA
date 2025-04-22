import csv
with open("archivos/employees.csv") as empfile:
    data=csv.reader(empfile)
    emplist=list(data)
    emplist.pop(0)
    salarios=[]
    for emp in emplist:
        salarios.append(int(emp[7]))
    
    print(max(salarios