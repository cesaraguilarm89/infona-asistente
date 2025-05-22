
import streamlit as st
import datetime

st.set_page_config(page_title="INFONA - Asistente Infonavit", layout="centered")

st.title("INFONA - Asistente Inteligente del Infonavit")
st.subheader("Consulta tu crédito, agenda una cita y recibe asistencia personalizada.")

menu = st.sidebar.selectbox("Menú", ["Inicio", "Simulador de Crédito", "Agendar Cita", "Chat con INFONA"])

if menu == "Inicio":
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/4b/Infonavit_logo.svg", width=150)
    st.markdown("**Bienvenido a INFONA.** Esta herramienta te ayudará a interactuar con el Infonavit de forma simple y rápida.")

elif menu == "Simulador de Crédito":
    st.header("Simulador de Crédito")
    ingreso = st.number_input("¿Cuál es tu ingreso mensual?", min_value=1000, step=500)
    años = st.slider("¿Cuántos años has cotizado?", 0, 40, 1)
    if ingreso and años:
        credito = ingreso * 10 + (años * 1000)
        st.success(f"Tu crédito estimado es de: ${credito:,.2f} MXN")

elif menu == "Agendar Cita":
    st.header("Agenda una Cita")
    nombre = st.text_input("Nombre completo")
    curp = st.text_input("CURP")
    fecha = st.date_input("Selecciona una fecha", min_value=datetime.date.today())
    sede = st.selectbox("Selecciona la sede", ["Oaxaca", "CDMX", "Guadalajara", "Monterrey"])
    if st.button("Enviar"):
        st.success(f"Cita registrada para {nombre} el día {fecha} en {sede}. Te llegará una confirmación.")

elif menu == "Chat con INFONA":
    st.header("Chat con INFONA")
    user_input = st.text_input("Escribe tu duda:")
    if user_input:
        st.info("Respuesta simulada:")
        st.write(f"Has preguntado: {user_input}")
        st.write("Por el momento INFONA está en modo demostración. Pronto responderé con IA.")
