from src.deepseekClient import consultar_deepseek
from src.models import Alarma


async def procesar_alarma(texto_usuario: str) -> dict:
    resultado = await consultar_deepseek(texto_usuario)

    if resultado["tipo"] != "accion":
        return {
            "accion": "chat",
            "mensaje": resultado["respuesta"],
        }

    datos = resultado["datos"]

    match resultado["accion"]:
        case "crear_alarma":
            hora = datos.get("hora")
            etiqueta = datos.get("etiqueta", "Alarma")

            # Guarda en MongoDB usando Beanie
            nueva_alarma = Alarma(hora=hora, etiqueta=etiqueta)
            await nueva_alarma.insert()

            return {
                "accion": "crear_alarma",
                "mensaje": f"Alarma programada a las {hora} ({etiqueta}).",
                "datos": {"hora": hora, "etiqueta": etiqueta},
            }

        case "listar_alarmas":
            # Busca todas las alarmas activas en MongoDB
            alarmas = await Alarma.find(Alarma.activa == True).to_list()

            if not alarmas:
                return {
                    "accion": "listar_alarmas",
                    "mensaje": "No tienes ninguna alarma activa ahora mismo.",
                    "datos": [],
                }

            lista = [
                {"hora": a.hora, "etiqueta": a.etiqueta} for a in alarmas
            ]
            resumen = ", ".join(
                [f"{a.hora} ({a.etiqueta})" for a in alarmas]
            )
            return {
                "accion": "listar_alarmas",
                "mensaje": f"Tienes estas alarmas activas: {resumen}.",
                "datos": lista,
            }

        case "borrar_alarma":
            hora = datos.get("hora")
            # Busca la alarma por hora y la borra de MongoDB
            alarma = await Alarma.find_one(Alarma.hora == hora)

            if not alarma:
                return {
                    "accion": "borrar_alarma",
                    "mensaje": f"No encontré ninguna alarma a las {hora}.",
                    "datos": {"hora": hora},
                }

            await alarma.delete()
            return {
                "accion": "borrar_alarma",
                "mensaje": f"Alarma de las {hora} eliminada.",
                "datos": {"hora": hora},
            }

        case _:
            return {
                "accion": "error",
                "mensaje": (
                    f"Acción no soportada todavía: {resultado['accion']}"
                ),
            }