import ollama

req1 = "El usuario o administrador ingresa la información de una nueva prenda/lote"
req2 = "Registro y control de caducidad de medicamentos"
req3 = "El sistema envía una notificación cuando el stock está por debajo del mínimo"
req4 = "Generar reporte de ventas mensuales en formato PDF"
req5 = "El usuario inicia sesión con su correo electrónico y contraseña"

print("--- SELECCIONA UN REQUERIMIENTO ---")
print(f"1. {req1}")
print(f"2. {req2}")
print(f"3. {req3}")
print(f"4. {req4}")
print(f"5. {req5}")

opcion = input("\nIngresa el número a evaluar (1-5): ").strip()

if opcion == "1":
    requerimiento_seleccionado = req1
elif opcion == "2":
    requerimiento_seleccionado = req2
elif opcion == "3":
    requerimiento_seleccionado = req3
elif opcion == "4":
    requerimiento_seleccionado = req4
elif opcion == "5":
    requerimiento_seleccionado = req5
else:
    print("Opción no válida. Debes ingresar un número del 1 al 5.")
    exit()

print(f"\nEvaluando Requerimiento {opcion}: '{requerimiento_seleccionado}'...")

requerimiento = input("El usuario o administrador ingrasa la información de una nueva prenda/lote ")
response = ollama.systemone(
    model = "d1-omni:600m",
    state = requerimiento,
    questions = {
        "condicion":{
            "type":"noul",
            "instructions": '¿Incluye una situacion que detona el evento?',
            "criteria": {
                "true": "Específica clamarente el evento o situación detonante",
                "false": "No menciona qué situación dispara la acción"
            }
        }
    }
)

condicion = response.answers['condicion'].noul

if condicion >= 0.05:
    print(f"1. Cumple con la condición: {condicion}")
else:
    print(f"1. No cumple con la condición: {condicion}")

requerimiento2 = input("Registro y control de caducidad de medicamentos ")
response = ollama.systemone(
    model = "d1-omni:600m",
    state = requerimiento,
    questions = {
        "condicion":{
            "type":"noul",
            "instructions": '¿Incluye una situacion que detona el evento?',
            "criteria": {
                "true": "Específica clamarente el evento o situación detonante",
                "false": "No menciona qué situación dispara la acción"
            }
        }
    }
)

condicion = response.answers['condicion'].noul

if condicion >= 0.05:
    print(f"1. Cumple con la condición: {condicion}")
else:
    print(f"1. No cumple con la condición: {condicion}")

requerimiento3 = input("Consulta general de inventario disponible ")
response = ollama.systemone(
    model = "d1-omni:600m",
    state = requerimiento,
    questions = {
        "condicion":{
            "type":"noul",
            "instructions": '¿Incluye una situacion que detona el evento?',
            "criteria": {
                "true": "Específica clamarente el evento o situación detonante",
                "false": "No menciona qué situación dispara la acción"
            }
        }
    }
)

condicion = response.answers['condicion'].noul

if condicion >= 0.05:
    print(f"1. Cumple con la condición: {condicion}")
else:
    print(f"1. No cumple con la condición: {condicion}")

requerimiento4 = input("Verificación y filtrado de disponibilidad de productos ")
response = ollama.systemone(
    model = "d1-omni:600m",
    state = requerimiento,
    questions = {
        "condicion":{
            "type":"noul",
            "instructions": '¿Incluye una situacion que detona el evento?',
            "criteria": {
                "true": "Específica clamarente el evento o situación detonante",
                "false": "No menciona qué situación dispara la acción"
            }
        }
    }
)

condicion = response.answers['condicion'].noul

if condicion >= 0.05:
    print(f"1. Cumple con la condición: {condicion}")
else:
    print(f"1. No cumple con la condición: {condicion}")

requerimiento5 = input("Registro de apoyo para zonas o personas marginadas ")
response = ollama.systemone(
    model = "d1-omni:600m",
    state = requerimiento,
    questions = {
        "condicion":{
            "type":"noul",
            "instructions": '¿Incluye una situacion que detona el evento?',
            "criteria": {
                "true": "Específica clamarente el evento o situación detonante",
                "false": "No menciona qué situación dispara la acción"
            }
        }
    }
)

condicion = response.answers['condicion'].noul
print(f"\nResultado para requerimiento {opcion}:")
if condicion >= 0.05:
    print(f"1. Cumple con la condición: {condicion}")
else:
    print(f"1. No cumple con la condición: {condicion}")

