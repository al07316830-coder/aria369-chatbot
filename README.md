# ARIA 369 · Asistente de orientación a clientes de Artroom 369

Chatbot basado en reglas para atender las consultas iniciales de prospectos de **Artroom 369 Worldwide**, consultoría boutique de comunicación con sede en la Ciudad de México.

**Proyecto Fase 1 · MBIA2602 · Maestría en Inteligencia Artificial · Universidad Tecmilenio**
Autora: Valeria Giselle Uribe Pérez

## Qué hace
- Explica las seis líneas de servicio: Corporate & Industrial Communications · Branding · Brand Visual Strategy & Creative Direction · Content & Audiovisual Production · Events · Print & POP.
- Orienta sobre el proceso de trabajo, cotizaciones, tiempos y experiencia.
- Canaliza solicitudes fuera de oferta y las de diseño de espacios a la marca hermana Atenea 369.
- Registra el correo del prospecto y lo turna a un consultor.

## Tecnología
- Python 3.10 o superior
- NLTK: `word_tokenize`, stopwords en español, `SnowballStemmer("spanish")` y `edit_distance`
- Desarrollo en Google Colab

## Archivos
| Archivo | Contenido |
|---|---|
| `ARIA369_Chatbot_Artroom.ipynb` | Notebook de Colab con el chatbot, las 12 conversaciones de prueba y las pruebas de límites |
| `artroom_bot.py` | Código fuente del chatbot (base de conocimiento, intenciones y motor) |
| `pruebas.py` | Conversaciones de prueba y pruebas de límites |
| `requirements.txt` | Dependencias |

## Cómo ejecutarlo
**En Google Colab:** abre el notebook y elige *Entorno de ejecución → Ejecutar todas*.

**En local:**
```bash
pip install -r requirements.txt
python pruebas.py        # corre las pruebas
python artroom_bot.py    # chat interactivo
```

## Arquitectura
Usuario → Chatbot (preprocesamiento NLTK → identificación de intención por reglas → selección de respuesta) ↔ Base de conocimiento, con un estado de conversación que permite continuar el diálogo (acción pendiente, datos del prospecto).

## Próximas fases
Clasificador de intenciones con PLN, clasificación de imágenes de piezas de marca e integración web.
