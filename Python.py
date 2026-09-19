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

while i < N and vehiculos < 30:
    print(f"\n--- Registro del vehículo {i + 1} ---")
    
    placa = input("Ingrese la placa del vehículo: ")
    tipo_usuario = input("Tipo de usuario (E: Estudiante, D: Docente, V: Visitante): ").upper().strip()
    hora_entrada = int(input("Hora de entrada (0-23): "))
    horas_permanencia = float(input("Horas de permanencia: "))

    if (hora_entrada < 0 or hora_entrada > 23) or horas_permanencia <= 0:
        print("ERROR: Hora de entrada fuera de rango o tiempo de permanencia no válido. Registro rechazado.")
    else:
        # Validación de tipo de usuario 
        if tipo_usuario not in ("E", "D", "V"):
            print("ADVERTENCIA: Tipo de usuario no válido. Se asignará como Visitante (V).")
            tipo_usuario = "V"

        # Cálculo de tarifa 
        if tipo_usuario == "E":
            if horas_permanencia <= 2:
                costo_base = 0.0
            else:
                costo_base = (horas_permanencia - 2) * 800.0
            estudiantes += 1

        elif tipo_usuario == "D":
            costo_base = horas_permanencia * 500.0
            docentes += 1

        else:  # Visitante ('V')
            # Nivel extra: si es sábado, la tarifa de visitante se reduce un 20%
            if es_sabado:
                tarifa_primera_hora = 1500.0 * 0.8  
                tarifa_hora_adicional = 1200.0 * 0.8  
            else:
                tarifa_primera_hora = 1500.0
                tarifa_hora_adicional = 1200.0

            if horas_permanencia <= 1:
                costo_base = horas_permanencia * tarifa_primera_hora
            else:
                costo_base = tarifa_primera_hora + (horas_permanencia - 1) * tarifa_hora_adicional
            visitantes += 1

        # Descuento nocturno 
        if not es_sabado and (hora_entrada >= 19 or hora_entrada < 6):
            total_vehiculo = costo_base * 0.90  # 10% de descuento
        else:
            total_vehiculo = costo_base

        total_vehiculo = round(total_vehiculo, 2)

        # Acumulación de estadísticas de vehículos válidos
        vehiculos += 1
        total_recaudado += total_vehiculo
        suma_horas_permanencia += horas_permanencia

        print(f"Vehículo registrado con éxito. Total a pagar: ${total_vehiculo}")

    i += 1  # Incremento de iteración

# Control de cupos máximos
if vehiculos == 30:
    print("\nPARQUEADERO LLENO")

# Cálculos finales
ocupacion = (vehiculos / 30) * 100
promedio_permanencia = (suma_horas_permanencia / vehiculos) if vehiculos > 0 else 0.0