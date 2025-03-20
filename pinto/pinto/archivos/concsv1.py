import csv

with open("C:\\Users\\usuario\\Dropbox\\sena2025\\Trimestre1-Febrero10-Abril25\\2996881_Analitica\\datos2.csv") as mycsv:
    data=csv.reader(mycsv)
    #print(data)
    #print(type(data))
    for x in data:
        print(x[2])