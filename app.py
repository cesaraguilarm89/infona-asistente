
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="INFONA - Asistente Inteligente de Vivienda",
    page_icon=":house:",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Estilos personalizados
st.markdown(
    """
    <style>
    body, .stApp {
        background-color: white;
        color: black;
    }
    .css-18e3th9 {
        padding: 1rem;
    }
    .stButton>button {
        background-color: #d32f2f;
        color: white;
    }
    .st-bf {
        background-color: #f5f5f5;
    }
    .st-af {
        color: #d32f2f;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Diccionario extendido en el mismo archivo
respuestas = {
    "hola": "Hola, ¿en qué puedo ayudarte hoy?",
    "adiós": "Gracias por tu visita. ¿Quieres que los pendientes te los mande a tu correo o WhatsApp registrado?",
    "¿qué es infona?": "INFONA es un asistente inteligente para ayudarte con trámites de vivienda, citas y simulación de crédito.",
    "¿cómo saco mi crédito?": "Para tramitar tu crédito necesitas estar dado de alta en Infonavit y cumplir con ciertos requisitos. ¿Quieres que te los mande?",
    "cuánto debo pagar": "Para conocer tu pago exacto del bimestre, accede con tu número de crédito. ¿Quieres que lo calculemos juntos?",
    "estado de cuenta": "Puedes consultar tu estado de cuenta ingresando tu número de crédito. ¿Deseas que te lo mande?",
    "mi nss": "Tu Número de Seguridad Social lo puedes encontrar en tu registro del IMSS. ¿Quieres que lo verifiquemos?",
    "ayuda": "Claro, dime tu duda y con gusto te apoyo.",
    "simular crédito": "Accede a la pestaña de Simulador para conocer el monto estimado que podrías recibir.",
    "agendar cita": "Ingresa a la pestaña 'Agendar Cita' para escoger la fecha y hora disponibles."
}

# Sidebar
st.sidebar.image("logo_infona_redes.png", width=150)
menu = st.sidebar.radio("Menú de navegación", ["Inicio", "Chatea con INFONA", "Simulador de Crédito", "Agendar Cita", "Preguntas Frecuentes"])

if menu == "Inicio":
    st.title("INFONA - Asistente Inteligente de Vivienda")
    st.markdown("Consulta, simula y agenda de forma sencilla.")
    st.image("infona_logo.PNG", width=200)

elif menu == "Chatea con INFONA":
    st.header("Chatea con INFONA")
    st.markdown("Escribe tu pregunta sobre créditos, pagos, citas o trámites:")

    pregunta = st.text_input("Tu mensaje:")
    if pregunta:
        respuesta = "Gracias por tu consulta. Estamos mejorando cada día para ayudarte mejor."
        for clave in respuestas:
            if clave in pregunta.lower():
                respuesta = respuestas[clave]
                break
        st.success(f"INFONA responde: {respuesta}")

elif menu == "Simulador de Crédito":
    st.header("Simulador de Crédito")
    ingreso = st.number_input("Ingresa tu salario mensual:", min_value=0)
    puntos = st.slider("Selecciona tus puntos actuales Infonavit:", 0, 116, 90)
    if ingreso > 0:
        monto = ingreso * (puntos / 100) * 20
        st.info(f"El monto estimado de tu crédito es: ${monto:,.2f}")

elif menu == "Agendar Cita":
    st.header("Agenda una cita")
    nombre = st.text_input("Nombre completo:")
    fecha = st.date_input("Selecciona la fecha:")
    hora = st.time_input("Selecciona la hora:")
    if nombre:
        st.success(f"Cita registrada para {nombre} el {fecha} a las {hora}")

elif menu == "Preguntas Frecuentes":
    st.header("Preguntas Frecuentes")
    st.markdown("""
    **¿Qué necesito para tramitar mi crédito?**  
    Necesitas estar dado de alta en el IMSS, contar con puntos suficientes y tener una relación laboral activa.

    **¿Puedo usar INFONA sin registrarme?**  
    Sí, INFONA está diseñado para darte asistencia básica sin necesidad de registro previo.

    **¿Qué tipo de créditos existen?**  
    Crédito tradicional, Cofinavit, Unamos Créditos y Mejoravit, entre otros.
    """)
