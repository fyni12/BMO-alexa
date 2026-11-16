FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./src ./src

EXPOSE 8000
CMD ["sh", "-c", "exec python -m src.main --host ${HOST_IP:-0.0.0.0} --port ${HOST_PORT:-8000}"]
