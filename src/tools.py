ALARMAS_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "crear_alarma",
            "description": "Programa una nueva alarma a una hora específica.",
            "parameters": {
                "type": "object",
                "properties": {
                    "hora": {
                        "type": "string",
                        "description": "Hora en formato 24h HH:MM (ej. 07:30)",
                    },
                    "etiqueta": {
                        "type": "string",
                        "description": (
                            "Motivo o nombre de la alarma (ej. Clase de"
                            " empotradas)"
                        ),
                    },
                },
                "required": ["hora"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "listar_alarmas",
            "description": (
                "Consulta todas las alarmas que están programadas actualmente."
            ),
            "parameters": {
                "type": "object",
                "properties": {},
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "borrar_alarma",
            "description": "Elimina o desactiva una alarma existente por su hora.",
            "parameters": {
                "type": "object",
                "properties": {
                    "hora": {
                        "type": "string",
                        "description": "Hora de la alarma a borrar en formato HH:MM",
                    },
                },
                "required": ["hora"],
            },
        },
    },
]