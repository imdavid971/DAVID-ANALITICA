# Inicializamos el contador y la variable para el primer número
contador = 0
numero_anterior = None

# Bucle que solicita números
while True:
    # Solicitamos el número al usuario
    try:
        numero = int(input("Ingresa un número: "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue
    
    # Verificamos si es mayor que el número anterior
    if numero_anterior is not None and numero <= numero_anterior:
        break  # Si no es mayor, finalizamos el bucle
    
    # Actualizamos el número anterior y el contador
    numero_anterior = numero
    contador += 1

# Mostramos cuántos números fueron ingresados
print(f"Se ingresaron {contador} números.")
