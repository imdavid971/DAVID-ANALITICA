#excepciones
try:
    print(10/0)
except Exception as fallo:
    print(fallo)
    print("No puedo dividir por cero")

#print("Hola \n Soacha")
lista=[]
#stream1=open()
file="archivos\prueba1.txt"
stream = open(file, mode='w', encoding="utf-8")

#p=IOBase()
