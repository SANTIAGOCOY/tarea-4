def filtro_por_edad(lista_personas, edad_min, edad_max):
    for persona in lista_personas:
        if edad_min <= persona["edad"] <= edad_max:
            print(f"{persona['nombres']} {persona['apellidos']}")

def main():
    
    lista_personas = [
        {"nombres": "mario", "apellidos": "torres", "edad": 101},
        {"nombres": "Ana María", "apellidos": "Pérez García", "edad": 45},
        {"nombres": "Luis Alberto", "apellidos": "Gómez Rodríguez", "edad": 33},
        {"nombres": "María Fernanda", "apellidos": "López Martínez", "edad": 60}
    ]
    
    # Rango de edades
    edad_min = 30
    edad_max = 60
    
    print(f"Personas con edades entre {edad_min} y {edad_max}:")
    filtro_por_edad(lista_personas, edad_min, edad_max)

if __name__ == "__main__":
    main()
