# Entrada para saber si es sábado 
es_sabado_input = input("¿Es sábado? (si/no): ").lower().strip()
es_sabado = es_sabado_input == "si" or es_sabado_input == "s" or es_sabado_input == "true"

# Cantidad total de vehículos a procesar inicialmente
N = int(input("Ingrese la cantidad de vehículos a procesar (N): "))

# Variables para estadísticas acumuladas
vehiculos = 0
total_recaudado = 0.0
estudiantes = 0
docentes = 0
visitantes = 0
suma_horas_permanencia = 0.0

i = 0  # Contador de iteraciones del ciclo

print(f"\n--- Registro del vehículo {i + 1} ---")
    
placa = input("Ingrese la placa del vehículo: ")
