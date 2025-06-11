import os
from openai import OpenAI

# Configuración de la API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

print(f"Usando API key: {OPENAI_API_KEY[:6]}...{OPENAI_API_KEY[-4:]}")

# Inicializar el cliente de OpenAI
try:
    client = OpenAI(api_key=OPENAI_API_KEY)
    print("Cliente OpenAI inicializado correctamente")
    
    # Hacer una petición de prueba
    try:
        print("Enviando petición de prueba a OpenAI...")
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un asistente de emergencias médicas."},
                {"role": "user", "content": "Test de conexión. Responde con 'OK'"}
            ],
            temperature=0.2,
            max_tokens=50
        )
        
        # Extraer respuesta
        content = response.choices[0].message.content
        print(f"Respuesta recibida: {content}")
        print("La conexión con OpenAI funciona correctamente!")
        
    except Exception as e:
        print(f"Error al hacer la petición a OpenAI: {str(e)}")
        import traceback
        print(f"Traceback: {traceback.format_exc()}")
        
except Exception as e:
    print(f"Error al inicializar el cliente OpenAI: {str(e)}")
    print("Asegúrate de tener la librería openai instalada correctamente con 'pip install openai'")