# Punto 5. 

import json
import requests

url1 = 'https://catfact.ninja/fact'
url2 = 'https://www.boredapi.com/api/activity'
url3 = 'https://official-joke-api.appspot.com/random_joke'

def datosAleatoriosDeGatos(*args): 
    petición = requests.get(url1)
    respuesta = petición.text
    return(respuesta)

def actividadeAleatorias(*args): 
    petición = requests.get(url2)
    respuesta = petición.text
    return(respuesta)

def chistesAleatorios(*args): 
    petición = requests.get(url3)
    respuesta = petición.text
    return(respuesta)

if __name__ == "__main__": # Inicializa las funciones. 
    print(datosAleatoriosDeGatos(url1)) # Imprime. 
    print(actividadeAleatorias(url2))
    print(chistesAleatorios(url3)) 