from datetime import datetime
import json
import os
from openai import AsyncOpenAI
from src.tools import ALARMAS_TOOLS

client = AsyncOpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)


async def consultar_deepseek(texto_usuario: str) -> dict:
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M")

    response = await client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "system",
                "content": (
                    "Eres BMO, un asistente de voz empotrado. "
                    f"Hora actual: {ahora}. "
                    "Responde de forma breve y natural."
                ),
            },
            {"role": "user", "content": texto_usuario},
        ],
        tools=ALARMAS_TOOLS,
        tool_choice="auto",
    )

    mensaje = response.choices[0].message

    if mensaje.tool_calls:
        llamada = mensaje.tool_calls[0].function
        return {
            "tipo": "accion",
            "accion": llamada.name,
            "datos": json.loads(llamada.arguments),
        }

    return {
        "tipo": "chat",
        "respuesta": mensaje.content,
    }