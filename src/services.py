from src.ai import consultar_deepseek


async def procesar_alarma(texto_usuario: str) -> dict:
    resultado = await consultar_deepseek(texto_usuario)

    if resultado["tipo"] == "accion":
        accion = resultado["accion"]
        datos = resultado["datos"]

        if accion == "crear_alarma":
            hora = datos.get("hora")
            etiqueta = datos.get("etiqueta", "Alarma")
            # TODO (ODM): await Alarma(hora=hora, etiqueta=etiqueta).insert()
            return {
                "accion": "crear_alarma",
                "mensaje": f"Alarma programada a las {hora} ({etiqueta}).",
                "datos": {"hora": hora, "etiqueta": etiqueta},
            }

        if accion == "listar_alarmas":
            # TODO (ODM): alarmas = await Alarma.find(Alarma.activa == True).to_list()
            return {
                "accion": "listar_alarmas",
                "mensaje": "Consultando alarmas activas...",
                "datos": [],
            }

        if accion == "borrar_alarma":
            hora = datos.get("hora")
            # TODO (ODM): alarma = await Alarma.find_one(Alarma.hora == hora); await alarma.delete()
            return {
                "accion": "borrar_alarma",
                "mensaje": f"Alarma de las {hora} eliminada.",
                "datos": {"hora": hora},
            }

    return {
        "accion": "chat",
        "mensaje": resultado["respuesta"],
    }