from ollama import chat

pregunta = input("En que te puedo ayudar: ")

response = chat(
    model='qwen2.5:0.5b',
    messages=[
        {
        'role': 'user', 
        'content': f"Responde la siguiente pregunta como si fueras Mario Bros: {pregunta}"
        }
    ],
)
#print(response.message.content)
print(response)