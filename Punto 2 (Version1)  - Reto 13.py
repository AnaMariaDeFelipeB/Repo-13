# Punto 2. Pide ingresar al usuario los diccionarios. 

def crearDiccionario(*args): # Definimos la función. 
    global dic1 # Declaramos la variable "dic" como una variable global. 
    dic1 = {} # Establecemos variable con diccionaro vacio. 
    for i in range(longitudDiccionario1): # Itera desde 0 hasta la longitud del diccionario. 
        # Por cada iteración pide: 
        key = (input("Ingrese la llave del primer diccionario: ")) # Ingresar "key"
        value = (input("Ingrese el valor del primer diccionaro: ")) # Ingresar "value"
        dic1.update({key:value}) # Los agrega al diccionario. 
    return dic1 # Devuelve el diccionario. 

def crearDiccionario2(*args): 
    global dic2
    dic2 = {} 
    for i in range(longitudDiccionario2): 
        key = (input("Ingrese la llave del segundo diccionario: ")) 
        value = (input("Ingrese el valor del segundo diccionaro: ")) 
        dic2.update({key:value}) 
    return dic2 

def mezclarDiccionarios(*args): # Definimos función. 
    dic3 = {} # Creamos diccionario vacio. 
    if dic1 == dic2: # Condición: Que los diccionarios 1 y 2 sean igulaes. 
        dic3 = dic1.copy() # Si cumple la condición: Copia el diccionario 1 en el 3. 
    
    else: # Si no cumple la condición. 
        dic3 = dic2.copy() # Copia el diccionaro 2 en el 3. 
        for keys, values in dic1.items(): # Itera tanto las llaves como los valores del diccionario 1. 
            dic3.update({keys:values}) # Actualiza. 
            
    return(dic3) # Devuelve. 



if __name__ == "__main__": # Inicializa las funciones. 
    longitudDiccionario1 = int(input("Ingrese la logitud del primer diccionario: ")) # Pide al usuario ingresar variable. 
    longitudDiccionario2 = int(input("Ingrese la logitud del segundo diccionario: ")) # Pide al usuario ingresar variable. 
    print("El primer diccionario ingresado fue: ", crearDiccionario(longitudDiccionario1)) # Imprime. 
    print("El segundo diccionario ingresado fue: ", crearDiccionario2(longitudDiccionario2)) 
    print("La mezcla de los diccionarios ingresados es: ", mezclarDiccionarios(dic1, dic2))