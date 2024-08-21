def ordenar_diccionario(diccionario):
    # Obtenemos las claves del diccionario ordenadas
    claves_ordenadas = sorted(diccionario, key=diccionario.get)
    
    # Creamos un nuevo diccionario con las claves en orden
    diccionario_ordenado = {clave: diccionario[clave] for clave in claves_ordenadas}
    
    return diccionario_ordenado

def main():
    
    diccionario = {
        'x': 5,
        'y': 1,
        'z': 8,
        'w': 3
    }
    
    print("Diccionario original:")
    print(diccionario)
    
    diccionario_ordenado = ordenar_diccionario(diccionario)
    
    print("\nDiccionario ordenado por valores (ascendente):")
    print(diccionario_ordenado)

if __name__ == "__main__":
    main()