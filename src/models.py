from datetime import datetime
from typing import Optional
from beanie import Document
from pydantic import Field


class Alarma(Document):
    hora: str  # Ejemplo: "08:30" (formato HH:MM)
    etiqueta: str = "Alarma"  # Ejemplo: "Clase de empotradas"
    activa: bool = True
    creada_en: datetime = Field(default_factory=datetime.now)

    class Settings:
        name = "alarmas"  # Nombre de la colección en MongoDB