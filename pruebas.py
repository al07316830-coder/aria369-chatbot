from artroom_bot import ChatbotArtroom, conversar

CONVERSACIONES = [
    ("Conversación 1 · Prospecto explora servicios",
     ["Hola, buenas tardes", "¿Qué servicios ofrecen?", "Muchas gracias, hasta luego"]),
    ("Conversación 2 · Director de RR. HH. busca comunicación interna",
     ["Buenos días", "Necesito una campaña de comunicación interna para los empleados de planta",
      "¿Cómo trabajan?", "Gracias"]),
    ("Conversación 3 · Startup quiere crear su marca y cotizar",
     ["Queremos crear nuestra marca y el logotipo", "¿Cuánto cuesta?", "Sí, por favor",
      "laura.mendez@empresa.com"]),
    ("Conversación 4 · Gerente de marketing busca dirección creativa",
     ["Busco dirección creativa para que todas nuestras piezas sean coherentes",
      "¿Con quién han trabajado?", "Excelente, es todo"]),
    ("Conversación 5 · Producción de video y redes sociales",
     ["Hola", "Necesitamos un video institucional y contenido para redes sociales",
      "¿Cuánto tiempo tardan?"]),
    ("Conversación 6 · Evento corporativo",
     ["Estamos organizando un evento corporativo por el aniversario de la empresa",
      "¿Qué necesito para empezar?", "Quiero agendar una reunión con un asesor"]),
    ("Conversación 7 · Material de punto de venta",
     ["Hola, ¿hacen displays y exhibidores para punto de venta?",
      "¿Cuál es el precio de un exhibidor?", "No por ahora, gracias"]),
    ("Conversación 8 · Solicitud fuera de oferta (RP y BTL)",
     ["¿Hacen relaciones públicas?", "¿Y activaciones BTL?",
      "Entonces me interesa branding"]),
    ("Conversación 9 · Solicitud de interiorismo (marca hermana)",
     ["Necesito diseño de interiores para nuestras oficinas",
      "Mi correo es compras@industrias-norte.mx", "Gracias, adiós"]),
    ("Conversación 10 · Errores de escritura (tolerancia con edit_distance)",
     ["Quiero una cotisacion", "¿Ofresen fotografia?", "Bye"]),
    ("Conversación 11 · Consulta fuera de dominio (fallback)",
     ["¿Qué clima hará mañana?", "¿Venden computadoras?", "Ok, ¿qué servicios tienen?"]),
    ("Conversación 12 · Negación y consulta múltiple",
     ["No quiero un logo, quiero un video",
      "Necesito branding, un evento y material impreso, ¿cuánto cuesta todo?",
      "Sí, agendemos", "Gracias, es todo"]),
]

# Pruebas de límites: entradas diseñadas para encontrar dónde falla la versión 1.0
PRUEBAS_LIMITE = [
    "Quiero que la gente reconozca mi empresa",          # paráfrasis sin palabras clave
    "¿Cuánto cuesta el branding?",                        # dos intenciones en una pregunta
    "¿Y eso cuánto tarda?",                               # referencia a un turno anterior
    "No me gustó mi logo actual, ¿pueden renovarlo?",    # negación que no excluye el tema
    "Do you offer video production?",                     # consulta en inglés
]

if __name__ == "__main__":
    bot = ChatbotArtroom()
    for titulo, mensajes in CONVERSACIONES:
        conversar(bot, mensajes, titulo)
    print("\n\n##### PRUEBAS DE LÍMITES #####")
    for m in PRUEBAS_LIMITE:
        conversar(bot, [m])
