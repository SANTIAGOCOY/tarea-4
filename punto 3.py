


def mezclar_diccionarios(diccionario1, diccionario2):
    # Crea un nuevo diccionario con una copia de diccionario1
    diccionario_mezclado = diccionario1.copy()
    
    # Agrega las claves y valores de diccionario2
    for clave, valor in diccionario2.items():
        if clave not in diccionario_mezclado:
            diccionario_mezclado[clave] = valor
    
    return diccionario_mezclado

def main():
    # Ejemplos de diccionarios con nombres y números de identificación
    diccionario1 = {
        101: "carlos",
        102: "manuel",
        103: "alberto",
        104: "santiago"
    }
    
    diccionario2 = {
        103: "David",  # Clave repetida
        104: "jose",
        105: "alejandro"
    }
    
    diccionario_mezclado = mezclar_diccionarios(diccionario1, diccionario2)
    
    print("Diccionario mezclado:")
    print(diccionario_mezclado)

if __name__ == "__main__":
    main()