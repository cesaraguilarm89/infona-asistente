
import streamlit as st

st.set_page_config(page_title="INFONA - Asistente Inteligente", layout="centered")

# Diccionario de respuestas por tema
respuestas = {
    "cuánto debo": "Hola Carlos, tu saldo estimado para este bimestre es de $2,470.00 MXN y el total pendiente de tu crédito es de $86,300.00 MXN. ¿Quieres que esta información se envíe a tu correo o WhatsApp registrado?",
    "cuándo debo pagar": "Tu siguiente pago vence el 17 de junio. ¿Deseas agendar un recordatorio?",
    "cuánto tiempo me falta": "Te faltan 24 bimestres, aproximadamente 4 años. ¿Te gustaría recibir un plan personalizado?",
    "qué me recomiendas": "Te recomiendo realizar un pago anticipado este mes para reducir intereses. ¿Quieres ver cómo impactaría en tu plazo?",
    "estado de cuenta": "Tu estado de cuenta está disponible. ¿Quieres que lo enviemos a tu correo electrónico registrado?"
}

# Variaciones por tema
variaciones = {
    "cuánto debo": [f"cuánto debo {i}" for i in range(1, 201)] + [
        "cuánto debo", "cuál es mi saldo", "cuánto tengo que pagar", "mi deuda actual", "cuánto me falta por pagar",
        "cuanto devo", "saldo pendiente", "qué cantidad adeudo", "cuanto debo pagar", "cuanto es mi deuda"
    ],
    "cuándo debo pagar": [f"cuándo debo pagar {i}" for i in range(1, 201)] + [
        "cuándo pago", "cuándo vence mi pago", "fecha de pago", "próximo vencimiento", "día de pago",
        "cuando debo abonar", "cuando es el pago", "me puedes decir cuando pago"
    ],
    "cuánto tiempo me falta": [f"cuánto tiempo me falta {i}" for i in range(1, 201)] + [
        "cuántos bimestres me restan", "cuántos años faltan", "cuánto para terminar", "cuánto me queda", "terminar crédito",
        "cuánto resta", "cuántas mensualidades", "cuánto es el tiempo restante"
    ],
    "qué me recomiendas": [f"qué me recomiendas {i}" for i in range(1, 201)] + [
        "alguna sugerencia", "qué puedo hacer", "qué pasos sigo", "cómo mejorar mi crédito", "me das un consejo",
        "me ayudas a decidir", "sugerencia personalizada", "tienes una recomendación"
    ],
    "estado de cuenta": [f"estado de cuenta {i}" for i in range(1, 201)] + [
        "ver movimientos", "ver pagos", "resumen de cuenta", "descargar historial", "consulta estado de cuenta",
        "ver mi cuenta", "checar estado de cuenta", "descargar estado"
    ]
}

# Limpieza básica de texto
def normalizar(texto):
    return texto.lower().replace("¿", "").replace("?", "").replace("¡", "").replace("!", "").strip()

# Motor de búsqueda interno
def buscar_respuesta(pregunta):
    normal = normalizar(pregunta)
    for tema, lista in variaciones.items():
        for variante in lista:
            if variante in normal:
                return respuestas[tema]
    return "Gracias por tu consulta. ¿Deseas que esta respuesta se envíe por correo o WhatsApp registrado?"

# Interfaz principal
st.title("INFONA - Asistente Inteligente de Vivienda")
st.write("Consulta, simula y agenda de forma sencilla.")

opcion = st.sidebar.radio("Menú", ["Inicio", "Chatea con INFONA"])

if opcion == "Inicio":
    st.image("infonavit_logo.PNG", width=160)
    st.markdown("**Hola, soy INFONA.** Estoy aquí para ayudarte con tus trámites, pagos, simulaciones y dudas sobre tu crédito Infonavit.")
elif opcion == "Chatea con INFONA":
    st.subheader("Chatea con INFONA")
    pregunta = st.text_input("¿Cuál es tu duda?")
    if pregunta:
        st.success(f"INFONA responde: {buscar_respuesta(pregunta)}")
