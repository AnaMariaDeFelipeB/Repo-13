# Punto 5. 

import json # Llama la función
import requests

url1 = 'https://catfact.ninja/fact'  # Variable que guarda el API
url2 = 'https://www.boredapi.com/api/activity'
url3 = 'https://official-joke-api.appspot.com/random_joke'

def datosAleatoriosDeGatos(*args): # Definimos función. 
    petición = requests.get(url1)  # Extrae la infromación del API
    respuesta = petición.text  # Devuelve el contenido como un string
    dict_data = petición.json()  # El ".json()" convierte la info del API y lo convierte en un archivo json/diccionario. 
    for key, value in dict_data.items(): # Itera el diccionario. 
            print(key, ":", value) # Imprime 
    return(respuesta) # Devuelve

def actividadeAleatorias(*args): 
    petición = requests.get(url2)
    respuesta = petición.text
    dict_data = petición.json()
    for key, value in dict_data.items():
            print(key, ":", value)
    return(respuesta)

def chistesAleatorios(*args): 
    petición = requests.get(url3)
    respuesta = petición.text
    dict_data = petición.json()
    for key, value in dict_data.items():
            print(key, ":", value)
    return(respuesta)

if __name__ == "__main__": # Inicializa las funciones.
    print("    ♥ Json y datos key and value del primer API: ") 
    print(datosAleatoriosDeGatos(url1)) # Imprime.
    print("    ♥ Json y datos key and value del segundo API: ")  
    print(actividadeAleatorias(url2))
    print("    ♥ Json y datos key and value del tercer API: ") 
    print(chistesAleatorios(url3)) 