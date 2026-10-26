import ollama

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