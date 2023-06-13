import json

archivo = {
    "jadiazcoronado": {
        "nombres": "Juan Antonio",
        "apellidos": "Diaz Coronado",
        "edad": 19,
        "colombiano": True,
        "deportes": ["Futbol", "Ajedrez", "Gimnasia"]
    },
    "dmlunasol": {
        "nombres": "Dorotea Maritza",
        "apellidos": "Luna Sol",
        "edad": 25,
        "colombiano": False,
        "deportes": ["Baloncesto", "Ajedrez", "Gimnasia"]
    }
}

file = open('archivo.json', 'w')  # Creamos un archivo para escribir datos en este. 
json.dump(archivo, file)  # Guardamos el archivo como un archivo tipo JSON. 
file.close() # Cerramos el archivo. 

file = open('archivo.json', 'r')  # Abrimos el archivo en modo lectura
diccionario = json.load(file)  # Convierte el archivo tipo JSON a un diccionario en python. 
file.close() # Cerramos el archivo. 

def nombresDeporte(*args): # Definimos función. 
    for key, value in diccionario.items(): # Itera tanto las llaves con los valores del diccionario. 
        if deporte in value["deportes"]: # Condición.
            # Si el deporte ingresado por el usuario se encuentra dentro de la lista del "value" deportes. 
            nombres = value["nombres"] # Guarda variable del valor del "value"
            apellidos = value["apellidos"]
            print(nombres, apellidos) # Imprime
        else: # Si no cumple la condición. 
            print("El deporte ingresado no se encontro") # Imprime

def nombresEdad(*args): # Definimos función. 
    for key, value in diccionario.items():  # Itera tanto las llaves como los valores del diccionario. 
        edad = value["edad"] # Guarda en una variable el valor del "value"
        edad = int(edad) # Convierte dicho valor a un entero.
        if edadMinima <= edad <= edadMaxima: # Condición.
            # Que la edad se encuentre en el rango de edad ingresado por el usuario. 
            nombres = value["nombres"] # Guarda variable del valor del "value"
            apellidos = value["apellidos"]
            print(nombres, apellidos) # Imprime
        else: # Si no cumple la condición. 
            print("Las edades no se encuentran en el rango establecido.")  # Imprime. 


if __name__ == "__main__": # Inicializa las funciones.
    deporte = str(input("Ingrese el deporte: "))
    print("Nombres completos de personas que practican", deporte)
    print(nombresDeporte(diccionario, deporte))
    edadMinima = int(input("Ingrese la edad minima: "))
    edadMaxima = int(input("Ingrese edad maxima: "))
    print("Nombres completos de las personas que tienen el rango de edad entre", edadMinima, "-", edadMaxima)
    print(nombresEdad(edadMaxima, edadMinima, diccionario))