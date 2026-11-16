import json
import subprocess
from vosk import Model, KaldiRecognizer, SetLogLevel


class AudioProcessingError(Exception):
    """Excepción lanzada cuando el audio está vacío o ffmpeg no puede decodificarlo."""
    pass


class AudioTranscriber:
    def __init__(self, model_path: str = "/app/model", sample_rate: int = 16000):
        SetLogLevel(-1)
        self.sample_rate = sample_rate
        self.model = Model(model_path)

    def _convert_to_pcm(self, audio_bytes: bytes) -> bytes:
        """Convierte cualquier formato de audio (mp3, m4a, ogg, webm, wav) a PCM 16kHz mono."""
        process = subprocess.Popen(
            [
                "ffmpeg",
                "-loglevel", "quiet",
                "-i", "pipe:0",
                "-ar", str(self.sample_rate),
                "-ac", "1",
                "-f", "s16le",
                "pipe:1",
            ],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        pcm_data, _ = process.communicate(input=audio_bytes)

        if process.returncode != 0 or not pcm_data:
            raise AudioProcessingError("No se pudo procesar el formato de audio recibido.")

        return pcm_data

    def transcribe(self, audio_bytes: bytes) -> str:
        """Recibe bytes de audio y devuelve el texto transcrito en español."""
        if not audio_bytes:
            raise AudioProcessingError("El archivo de audio está vacío.")

        pcm_data = self._convert_to_pcm(audio_bytes)

        recognizer = KaldiRecognizer(self.model, self.sample_rate)
        recognizer.AcceptWaveform(pcm_data)
        result = json.loads(recognizer.FinalResult())

        return result.get("text", "")