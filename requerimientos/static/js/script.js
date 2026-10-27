async function evaluacion() {
    try{

        const uri = "https://crowded-spooky-mummy-4q644jv9qxvjhj5qp-11434.app.github.dev/api/chat";
        const requerimiento = "El usuario ingresa su nombre y contraseña en el sistema evalua si es valido o no.";

        const data = {
            model : "qwen2.5:1.5b",
            state : requerimiento,
            questions : {
                "condicion":{
                    "type":"noul",
                    "instructions": '¿Incluye una situacion que detona el evento?',
                    "criteria": {
                        "true": "Específica claramente el evento o situación detonante",
                        "false": "No menciona qué situación dispara la acción"
            }
        }
    }
};

data.messages = [
    {
        role: "user",
        content: 'Requerimiento: ${data.state}\n\nEvalúa esta pregunta: ${JSON.stringify}(data.questions)}\n\nResponde SOLO con JSON en este formato: {"condicion": {"noul": true}} o {"condicion": {"noul": false}}'
    }
];
data.stream = false;
data.format = "json";

    const response = await fetch(uri, {
            method:"POST",
            headers:{
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });
        
        if (!response.ok){
            throw new Error('HTTP ${response.status}: ${response.status.Text}');
        }

    const resultado = await response.json();

    resultado.answers = JSON.parse(resultado.message.content);

    console.log("Conexión con la API exitosa: ", resultado);
    console.log("Criterio: ", resultado.answers.condicion.noul);

    }catch (error){
        console.log("Ups, algo fallo", error.message);
    }
}

evaluacion();