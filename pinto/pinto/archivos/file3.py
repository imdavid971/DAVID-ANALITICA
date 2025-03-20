def palabra_himno(palabra):
    try:
        with open('archivos/himno.txt', 'r', encoding='utf-8') as archivo:
            contenido = archivo.read().lower()                        
            ocurrencias = contenido.count(palabra.lower())  
            if ocurrencias > 0:
                print(f"Tu palabra elegida '{palabra}' aparece {ocurrencias} veces en el himno de Colombia.")
            else:
                print(f"Tu palabra '{palabra}' no está en el himno de Colombia.")
    except FileNotFoundError:
        print("El archivo 'himno.txt' no se encuentra en el directorio.")

palabra = input("Introduce la palabra que deseas buscar en el himno de Colombia: ")
palabra_himno(palabra)

# def buscar_palabra_en_archivo(palabra):
#     # Abrir el archivo himno.txt en modo lectura
#     try:
#         with open('himno.txt', 'r', encoding='utf-8') as archivo:
#             # Leer todo el contenido del archivo
#             contenido = archivo.read()
            
#             # Contar cuántas veces aparece la palabra en el contenido
#             cantidad = contenido.lower().count(palabra.lower())
            
#             if cantidad > 0:
#                 print(f"La palabra '{palabra}' aparece {cantidad} veces en el archivo.")
#             else:
#                 print(f"La palabra '{palabra}' no está en el archivo.")
    
#     except FileNotFoundError:
#         print("El archivo 'himno.txt' no se encuentra en el directorio.")

# # Ejemplo de uso:
# buscar_palabra_en_archivo('libertad')

