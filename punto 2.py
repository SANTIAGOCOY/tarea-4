


def verificar_diccionarios(diccionario1, diccionario2):
    # Verificamos que todas las clave:valor de diccionario1 estén en diccionario2
    for clave, valor in diccionario1.items():
        if clave not in diccionario2 or diccionario2[clave] != valor:
            return False
    return True

def main():
    # Ejemplos de diccionarios
    diccionario1 = {
        'a': 1,
        'b': 2,
        'c': 3
    }
    
    diccionario2 = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4
    }
    
    resultado = verificar_diccionarios(diccionario1, diccionario2)
    
    if resultado:
        print("Todas las claves y valores de diccionario1 están presentes en diccionario2.")
    else:
        print("No todas las claves y valores de diccionario1 están presentes en diccionario2.")

if __name__ == "__main__":
    main()
