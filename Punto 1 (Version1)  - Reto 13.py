# Punto 1.  Pide al usuario ingresar diccionario. 

def crearDiccionario(*args): # Definimos la función. 
    global dic # Declaramos la variable "dic" como una variable global. 
    dic = {} # Establecemos variable con diccionaro vacio. 
    for i in range(longitudDiccionario): # Itera desde 0 hasta la longitud del diccionario. 
        # Por cada iteración pide: 
        key = (input("Ingrese la llave del diccionario: ")) # Ingresar "key"
        value = (input("Ingrese el valor del diccionaro: ")) # Ingresar "value"
        dic.update({key:value}) # Los agrega al diccionario. 
    return dic # Devuelve el diccionario. 

def valoresEnOrden(*args): # defenimos la función. 
    valores = list(dic.values())  # Agrega los "values" del diccionario a una lista.
    valores.sort(reverse=False) # Organiza la lista en orden ascentende alfabeticamente. 
    for i in valores: # Itera los valores de la lista. 
        print(i) # Los imprime
    return ("La lista de los valores organizados del diccionario es: ", valores) # Devuleve. 
    



if __name__ == "__main__": # Inicializa las funciones. 
    longitudDiccionario = int(input("Ingrese la logitud del diccionario: ")) # Pide al usuario ingresar variable. 
    print("El diccionario ingresado fue: ", crearDiccionario(longitudDiccionario)) # Imprime. 
    print(valoresEnOrden(dic))