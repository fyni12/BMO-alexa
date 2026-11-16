import argparse
from fastapi import FastAPI, UploadFile, File, HTTPException
import uvicorn
from src.transcriber import AudioTranscriber, AudioProcessingError

app = FastAPI()
transcriber = AudioTranscriber(model_path="/app/model")


@app.get("/health")
def health_status():
    return {"Status": "Ok"}


@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    audio_bytes = await file.read()

    try:
        text = transcriber.transcribe(audio_bytes)
    except AudioProcessingError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {
        "filename": file.filename,
        "text": text
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Iniciar servidor FastAPI")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Dirección IP del host")
    parser.add_argument("--port", type=int, default=8000, help="Puerto de escucha")
    parser.add_argument("--reload", action="store_true", help="Activar recarga automática")

    args = parser.parse_args()
    uvicorn.run("src.main:app", host=args.host, port=args.port, reload=args.reload)