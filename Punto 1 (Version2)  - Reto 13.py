# Punto 1.  Diccionario establecido. 

dic = {'Bogota': 'Colombia', 'Tokyo ': 'Japon', 'Moscu': 'Rusia', 'Caracas ': 'Venezuela', 'Buenos Aires ': 'Argentina'} # Diccionario. 

def valoresEnOrden(*args): # defenimos la función. 
    valores = list(dic.values())  # Agrega los "values" del diccionario a una lista.
    valores.sort(reverse=False) # Organiza la lista en orden ascentende alfabeticamente. 
    for i in valores: # Itera los valores de la lista. 
        print(i) # Los imprime
    return ("La lista de los valores organizados del diccionario es: ", valores) # Devuleve. 
    



if __name__ == "__main__": # Inicializa las funciones. 
    print(valoresEnOrden(dic)) #Imprime