
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="INFONA - Asistente Inteligente de Vivienda", page_icon="🏠", layout="wide")

# Diccionario integrado
respuestas_extensas = {
    # Saludos
    "hola": "¡Hola! Soy INFONA, tu asistente virtual. ¿En qué puedo ayudarte hoy?",
    "buenos días": "¡Buenos días! Estoy lista para ayudarte con cualquier trámite o consulta de vivienda.",
    "buenas tardes": "¡Buenas tardes! ¿Te ayudo con tu crédito o alguna cita?",
    "buenas noches": "¡Buenas noches! ¿Necesitas orientación sobre tu crédito de vivienda?",

    # Despedidas con llamado a la acción
    "adiós": "Aún tenemos pendientes. ¿Quieres que te los mande a tu correo o WhatsApp registrado?",
    "nos vemos": "Nos vemos. ¿Te gustaría que guarde esta conversación o la envíe a tu contacto?",
    "gracias": "¡Con gusto! ¿Deseas que esta información se te envíe por correo o WhatsApp?",

    # Identidad
    "¿qué es infona?": "INFONA es un asistente virtual que te apoya con trámites, simulaciones y dudas sobre tu crédito de vivienda.",
    "¿quién eres?": "Soy INFONA, un asistente inteligente de vivienda listo para ayudarte.",
    "¿para qué sirves?": "Te ayudo a conocer tu crédito, pagos, puntos, requisitos y a agendar tus citas.",

    # Consultas comunes
    "¿cuánto debo?": "**Tu saldo estimado es de:** $48,230 MXN. ¿Quieres un desglose completo por bimestre?",
    "¿cuándo debo pagar?": "**Tu próximo pago vence el:** 17 de junio de 2025. ¿Te gustaría recibir un recordatorio?",
    "¿cuánto me toca pagar este bimestre?": "**Pago bimestral estimado:** $2,407. ¿Deseas realizar este cálculo con tus datos reales?",
    "¿tengo deudas?": "**Detectamos 2 bimestres pendientes.** ¿Deseas recibir un resumen detallado?",
    "estado de cuenta": "Tu último estado de cuenta indica saldo a favor por $1,250. ¿Te gustaría enviarlo por correo?",
    "mi nss": "Tu NSS es un dato esencial para consultas. ¿Quieres que te muestre cómo recuperarlo?",

    # Requisitos y procesos
    "¿qué necesito para un crédito?": "Debes estar dado de alta en el IMSS, tener relación laboral activa y al menos 1080 puntos.",
    "¿cómo obtengo un crédito?": "Puedes iniciar con una precalificación. ¿Te gustaría simularlo ahora?",
    "puntos": "Tu puntaje actual estimado es de 985. ¿Quieres saber cuántos necesitas para alcanzar un crédito?",
    "simulador": "Accede al simulador en el menú lateral. ¿Deseas ir ahora?",
    "agendar cita": "Ve al apartado correspondiente y llena tus datos. ¿Quieres que te guíe paso a paso?"
}

# Función para obtener respuestas
def obtener_respuesta(pregunta):
    pregunta = pregunta.lower()
    for clave, respuesta in respuestas_extensas.items():
        if clave in pregunta:
            return respuesta
    return "Gracias por tu consulta. ¿Te gustaría que te envíe la información a tu correo o WhatsApp?"

# Sidebar
st.sidebar.image("logo_infona_redes.png", width=150)
st.sidebar.markdown("## Menú de navegación")
opcion = st.sidebar.radio("", ["🏠 Inicio", "💬 Chatea con INFONA", "🧮 Simulador de Crédito", "🗓️ Agendar Cita", "❓ Preguntas Frecuentes"])

# Contenido de la app
if opcion == "🏠 Inicio":
    st.title("INFONA - Asistente Inteligente de Vivienda")
    st.markdown("**¡Hola! Soy INFONA.** Tu asistente inteligente de vivienda. Te ayudo a consultar tu crédito, agendar citas o resolver cualquier duda.")
    st.image("logo_infona_redes.png", width=200)

elif opcion == "💬 Chatea con INFONA":
    st.header("Chatea con INFONA")
    st.write("Escribe tu pregunta sobre créditos, pagos, citas o trámites:")
    pregunta = st.text_input("Tu mensaje:")
    if pregunta:
        respuesta = obtener_respuesta(pregunta)
        st.success(f"INFONA responde: {respuesta}")

elif opcion == "🧮 Simulador de Crédito":
    st.header("Simulador de Crédito")
    ingreso = st.number_input("Ingresa tu salario mensual:", min_value=0)
    puntos = st.slider("Selecciona tus puntos actuales Infonavit:", 0, 116, 90)
    if ingreso > 0:
        monto_credito = ingreso * (puntos / 116) * 20
        st.info(f"**Crédito estimado:** ${monto_credito:,.2f} MXN")

elif opcion == "🗓️ Agendar Cita":
    st.header("Agenda una cita")
    nombre = st.text_input("Nombre completo:")
    fecha = st.date_input("Selecciona la fecha:")
    hora = st.time_input("Selecciona la hora:")
    if nombre:
        st.success(f"Cita agendada para **{nombre}** el **{fecha}** a las **{hora}**")

elif opcion == "❓ Preguntas Frecuentes":
    st.header("Preguntas Frecuentes")
    st.markdown("""
**¿Qué necesito para tramitar mi crédito?**  
Necesitas estar dado de alta en el IMSS, tener puntos suficientes y una relación laboral activa.

**¿Puedo usar INFONA sin registrarme?**  
Sí, puedes consultar y simular sin necesidad de registrarte.

**¿Qué tipo de créditos existen?**  
Crédito tradicional, Cofinavit, Unamos Créditos y Mejoravit.
""")

# Pie de página
st.markdown("<hr>", unsafe_allow_html=True)
st.caption("INFONA es un asistente digital no oficial. Para atención personalizada, consulta el portal oficial de Infonavit.")
