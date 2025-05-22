
import streamlit as st
from datetime import datetime

# Diseño general
st.set_page_config(page_title="INFONA - Asistente Inteligente de Vivienda", page_icon="🏠", layout="wide")

# --- Diccionario de respuestas ---
respuestas = {
    "hola": "¡Hola! ¿En qué puedo ayudarte hoy?",
    "adiós": "Gracias por consultar a INFONA. ¿Quieres que los pendientes te los mande a tu correo o tu WhatsApp registrado?",
    "infona": "INFONA es tu asistente virtual para orientación sobre créditos, pagos, citas y trámites relacionados con vivienda.",
    "cuánto debo pagar": "Por favor indícame si deseas calcularlo con base en tu crédito actual o estado de cuenta.",
    "estado de cuenta": "Puedes consultar tu estado de cuenta ingresando a tu perfil Infonavit o solicitarlo aquí. ¿Deseas que lo solicitemos por ti?",
    "nss": "Tu Número de Seguridad Social (NSS) es importante para el trámite. ¿Deseas saber cómo obtenerlo?",
    "ayuda": "Claro, puedo ayudarte con créditos, simulaciones, pagos, citas y más. ¿Qué necesitas saber?",
    "requisitos crédito": "Para obtener un crédito necesitas estar dado de alta en el IMSS, tener relación laboral vigente y puntos suficientes.",
    "simulador": "Ve al apartado 'Simulador de Crédito' para estimar tu monto disponible.",
    "agendar cita": "Puedes agendar una cita en el apartado correspondiente. ¿Te ayudo a llenarlo?"
}

# --- Función para encontrar respuesta ---
def obtener_respuesta(pregunta):
    pregunta = pregunta.lower()
    for clave in respuestas:
        if clave in pregunta:
            return respuestas[clave]
    return "Gracias por tu consulta. Actualmente INFONA responde preguntas relacionadas con tu crédito de vivienda, pagos, citas y requisitos. Estamos mejorando cada día para ayudarte mejor."

# --- Menú lateral ---
st.sidebar.image("infona_avatar.jpg", width=150)
st.sidebar.markdown("## Menú de navegación")
opcion = st.sidebar.radio("", ["🏠 Inicio", "💬 Chatea con INFONA", "🧮 Simulador de Crédito", "🗓️ Agendar Cita", "❓ Preguntas Frecuentes"])

# --- Contenido por sección ---
if opcion == "🏠 Inicio":
    st.title("INFONA - Asistente Inteligente de Vivienda")
    st.markdown("Consulta, simula y agenda de forma sencilla.")
    st.image("infona_avatar.jpg", width=200)
    st.markdown("**¡Hola! Soy INFONA, tu asistente inteligente de vivienda.** Estoy aquí para ayudarte a consultar tu crédito, simular montos, agendar citas o resolver cualquier duda que tengas sobre trámites de vivienda. Selecciona una opción en el menú para comenzar.")

elif opcion == "💬 Chatea con INFONA":
    st.header("Chatea con INFONA")
    st.write("Escribe tu pregunta sobre créditos, pagos, citas o trámites:")
    pregunta = st.text_input("Tu mensaje:")
    if pregunta:
        respuesta = obtener_respuesta(pregunta)
        st.success(f"INFONA responde: {respuesta}")

elif opcion == "🧮 Simulador de Crédito":
    st.header("Simulador de Crédito")
    salario = st.number_input("Ingresa tu salario mensual:", min_value=0)
    puntos = st.slider("Selecciona tus puntos actuales Infonavit:", 0, 116, 90)
    if salario > 0:
        monto_credito = salario * (puntos / 116) * 20
        st.write(f"Monto estimado de crédito: ${monto_credito:,.2f}")

elif opcion == "🗓️ Agendar Cita":
    st.header("Agenda una cita")
    nombre = st.text_input("Nombre completo:")
    fecha = st.date_input("Selecciona la fecha:")
    hora = st.time_input("Selecciona la hora:")
    if nombre:
        st.success(f"Cita agendada para {nombre} el {fecha} a las {hora}")

elif opcion == "❓ Preguntas Frecuentes":
    st.header("Preguntas Frecuentes")
    st.markdown("""
**¿Qué necesito para tramitar mi crédito?**  
Necesitas estar dado de alta en el IMSS, contar con puntos suficientes y tener una relación laboral activa.

**¿Puedo usar INFONA sin registrarme?**  
Sí, INFONA está diseñado para darte asistencia básica sin necesidad de registro previo.

**¿Qué tipo de créditos existen?**  
Crédito tradicional, Cofinavit, Unamos Créditos y Mejoravit, entre otros.
""")

# --- Pie de página ---
st.markdown("<hr>", unsafe_allow_html=True)
st.caption("INFONA es un asistente digital no oficial. Para atención personalizada, consulta el portal oficial de Infonavit.")
