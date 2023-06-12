# Punto 2. Diccionarios Establecidos

dic1 = {'Alemania': 'Berlin', 'Suecia': 'Estocolmo ', 'Colombia': 'Bogotá'} # Diccionario. 
dic2 = {'Colombia': 'Medellin', 'China': 'Pekin', 'Vaticano': 'Vaticano', 'Venezuela': 'Caracas'}
dic3 = {}

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
    print("La mezcla de los diccionarios ingresados es: ", mezclarDiccionarios(dic1, dic2)) # Imprime. 
