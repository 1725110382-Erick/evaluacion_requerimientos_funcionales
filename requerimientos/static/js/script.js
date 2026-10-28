async function evaluacion() {
    try{

        const uri = "https://crowded-spooky-mummy-4q644jv9qxvjhj5qp-11434.app.github.dev/v1/systemone";
        const requerimiento = "El usuario ingresa su nombre y contraseña en el sistema evalua si es valido o no.";

        const data = {
            model : "d1-omni:600m",
            state : requerimiento,
            questions : {
                "condicion":{
                    "type":"noul",
                    "instructions": '¿Incluye una situacion que detona el evento?',
                    "criteria": {
                        "true": "Específica clamarente el evento o situación detonante",
                        "false": "No menciona qué situación dispara la acción"
            }
        }
    }
}

    const response = await fetch(uri, {
            method:"POST",
            headers:{
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }
    );

    const resultado = await response.json();

    console.log("Conexión con la API exitosa: ", resultado);
    console.log("Criterio: ", resultado.answers.condicion.noul);

    }catch (error){
        console.log("Ups, algo fallo", error.message);
        throw error;
    }
}

evaluacion();