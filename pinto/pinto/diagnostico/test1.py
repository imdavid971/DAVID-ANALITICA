
contador = 0
numero_anterior = None

while True:
    try:
        numero = int(input("Ingresa un número: "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue
    
    if numero_anterior is not None and numero <= numero_anterior:
        break  
   

    numero_anterior = numero
    contador += 1

print(f"Se ingresaron {contador} números.")
