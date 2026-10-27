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
    requerimiento = req1
elif opcion == "2":
    requerimiento= req2
elif opcion == "3":
    requerimiento = req3
elif opcion == "4":
    requerimiento= req4
elif opcion == "5":
    requerimiento = req5
    print("Opción no válida. Debes ingresar un número del 1 al 5.")
    exit()

print(f"\nEvaluando Requerimiento {opcion}: '{requerimiento}'...")

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

