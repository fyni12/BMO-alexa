import argparse
from fastapi import FastAPI
import uvicorn
import src.services as procesar_alarma
from pydantic import BaseModel

app = FastAPI()

class AlarmaRequest(BaseModel):
    texto: str

@app.get("/health")
def health_status():
    return {"Status": "Ok"}

@app.post("/alarma")
async def ejecutar_alarma(peticion: AlarmaRequest):
    return await procesar_alarma(peticion.texto)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Iniciar servidor FastAPI")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Dirección IP del host (ej. 0.0.0.0)")
    parser.add_argument("--port", type=int, default=8000, help="Puerto de escucha (ej. 8000)")
    parser.add_argument("--reload", action="store_true", help="Activar recarga automática en desarrollo")

    args = parser.parse_args()

    uvicorn.run("src.main:app", host=args.host, port=args.port, reload=args.reload)