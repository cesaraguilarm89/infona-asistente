
import streamlit as st
import sqlite3
import datetime
import openai

# Configura tu clave de OpenAI
openai.api_key = "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"

st.set_page_config(page_title="INFONA", layout="centered")
st.title("INFONA - Asistente Inteligente del Infonavit")
st.subheader("Consulta tu crédito, agenda citas y chatea con IA.")

menu = st.sidebar.selectbox("Menú", ["Inicio", "Simulador de Crédito", "Agendar Cita", "Chat con INFONA"])

# Base de datos local para guardar citas
def guardar_cita(nombre, curp, fecha, sede):
    conn = sqlite3.connect("citas.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS citas
                 (nombre TEXT, curp TEXT, fecha TEXT, sede TEXT)''')
    c.execute("INSERT INTO citas VALUES (?, ?, ?, ?)", (nombre, curp, str(fecha), sede))
    conn.commit()
    conn.close()

# Chatbot con GPT
def responder_con_gpt(pregunta):
    try:
        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": pregunta}],
            temperature=0.6
        )
        return respuesta.choices[0].message["content"]
    except Exception as e:
        return f"Ocurrió un error al consultar la IA: {e}"

if menu == "Inicio":
    st.image("infonavit_logo.svg", width=120)
    st.markdown("**Bienvenido a INFONA**: tu asistente confiable para trámites con Infonavit.")

elif menu == "Simulador de Crédito":
    st.header("Simulador de Crédito")
    ingreso = st.number_input("¿Cuál es tu ingreso mensual?", min_value=1000)
    años = st.slider("¿Cuántos años has cotizado al Infonavit?", 0, 40, 5)
    if ingreso:
        credito = ingreso * 10 + años * 1000
        st.success(f"Crédito estimado: ${credito:,.2f} MXN")

elif menu == "Agendar Cita":
    st.header("Agenda una Cita en el CESI")
    nombre = st.text_input("Nombre completo")
    curp = st.text_input("CURP")
    fecha = st.date_input("Fecha deseada", min_value=datetime.date.today())
    sede = st.selectbox("Sede", ["Oaxaca", "CDMX", "Monterrey", "Guadalajara"])
    if st.button("Agendar"):
        guardar_cita(nombre, curp, fecha, sede)
        st.success(f"Cita registrada para {nombre} el {fecha} en {sede}.")

elif menu == "Chat con INFONA":
    st.header("Asistente Virtual con IA")
    user_input = st.text_input("Escribe tu duda:")
    if user_input:
        st.info("INFONA responde:")
        respuesta = responder_con_gpt(user_input)
        st.write(respuesta)
