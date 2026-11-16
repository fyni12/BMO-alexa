FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instalamos wget, unzip y ffmpeg (necesario para convertir audios del móvil)
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    unzip \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Descargamos y descomprimimos el modelo ligero de Vosk en español (~40 MB)
RUN wget -q https://alphacephei.com/vosk/models/vosk-model-small-es-0.42.zip \
    && unzip -q vosk-model-small-es-0.42.zip \
    && mv vosk-model-small-es-0.42 /app/model \
    && rm vosk-model-small-es-0.42.zip

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./src ./src

EXPOSE 8000
CMD ["sh", "-c", "exec python -m src.main --host ${HOST_IP:-0.0.0.0} --port ${HOST_PORT:-8000}"]