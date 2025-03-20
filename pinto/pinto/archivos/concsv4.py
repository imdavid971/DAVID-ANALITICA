import csv
diccio=[
    {'name':'Alice','age':18},
    {'name':'Bob','age':19},
    {'name':'John','age':17}
]
zzz=['name','age']

with open('archivos/people.csv','w') as csvfile:
    writer=csv.DictWriter(csvfile,fieldnames=zzz)
    writer.writeheader()
    writer.writerows(diccio)
