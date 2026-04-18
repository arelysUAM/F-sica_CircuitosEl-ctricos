#Analiza circuitos eléctricos de resistencias
def analizar_circuito(resistencias, voltaje, tipo):
    """
    resistencias: lista de valores en ohms [R1, R2, ...]
    voltaje: valor de la fuente (V)
    tipo: "serie" o "paralelo"
    """

    resultado = {} #Diccionario vacio

    # Serie
    if tipo.lower() == "serie":
        # Resistencia equivalente
        R_eq = sum(resistencias)

        # Corriente total ► Ley de Ohm
        I_total = voltaje / R_eq

        # Voltaje en cada resistor 
        voltajes = [I_total * R for R in resistencias] #Recorre cada resistencia R dentro de la lista resistencia

        resultado = {
            "tipo": "serie",
            "R_eq": R_eq,
            "I_total": I_total,
            "voltajes": voltajes
        }

    # Paralelo
    elif tipo.lower() == "paralelo":
        # Resistencia equivalente
        inversa = sum(1/R for R in resistencias) #suma de las inversas
        R_eq = 1 / inversa

        # Corriente total
        I_total = voltaje / R_eq

        # Corriente en cada resistor
        corrientes = [voltaje / R for R in resistencias]

        resultado = {
            "tipo": "paralelo",
            "R_eq": R_eq,
            "I_total": I_total,
            "corrientes": corrientes
        }

    else:
        return "Error: tipo debe ser 'serie' o 'paralelo'"

    return resultado


if __name__ == "__main__":
    print("\nAnálisis de Circuitos Eléctricos")
    print("--------------------------------------")
    
    while True:
        print("\nSeleccione el tipo de circuito:")
        print("1. Serie")
        print("2. Paralelo")
        print("3. Salir")
        
        opcion = input("Ingrese su opción (1-3): ").strip()
        
        if opcion == "3":
            print("\nBye...")
            break
        elif opcion in ["1", "2"]:
            tipo = "serie" if opcion == "1" else "paralelo"
            
            # Ingresar datos
            try:
                n = int(input("\nIngrese el número de resistencias: "))
                if n <= 0:
                    print("El número de resistencias debe ser mayor que 0.")
                    continue
                
                resistencias = []# Lista de resistencia
                for i in range(n):
                    r = float(input(f"Ingrese la resistencia R{i+1} (en ohms): "))
                    if r <= 0:
                        print("La resistencia debe ser mayor que 0.")
                        resistencias = []  #se guarda cada resistencia
                        break
                    resistencias.append(r) #agregar al final de la lista
                
                if not resistencias: #si la lista está vacía...
                    continue #volvemos al menú principal
                
                voltaje = float(input("Ingrese el voltaje de la fuente (en volts): "))
                if voltaje <= 0:
                    print("El voltaje debe ser mayor que 0.")
                    continue #Vuelve al inicio del menú
                
                # llamada a la función
                resultado = analizar_circuito(resistencias, voltaje, tipo)
                
                if isinstance(resultado, str): #Devolvió cadena de texto
                    print(resultado) #Hubo un error
                else:
                    print(f"\nResultado para circuito en {tipo}:")
                    print(f"Resistencia equivalente: {resultado['R_eq']:.4f} ohms")
                    print(f"Corriente total: {resultado['I_total']:.4f} A")
                    
                    if tipo == "serie":
                        for i, v in enumerate(resultado['voltajes'], 1):
                            print(f"Voltaje en R{i}: {v:.4f} V")
                    else:
                        for i, c in enumerate(resultado['corrientes'], 1):
                            print(f"Corriente en R{i}: {c:.4f} A")
            
            except ValueError: 
                print("Error: Ingrese un número válido.")
        else:
            print("Opción inválida. Intente de nuevo.")
