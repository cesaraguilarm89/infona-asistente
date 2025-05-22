
import streamlit as st
import openai
import sqlite3
import datetime

# Seguridad: API Key tomada desde secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="INFONA", layout="centered")
st.title("INFONA - Asistente Inteligente del Infonavit")
st.subheader("Consulta tu crédito, agenda una cita y chatea con IA.")

menu = st.sidebar.selectbox("Menú", ["Inicio", "Simulador de Crédito", "Agendar Cita", "Chat con INFONA"])

def guardar_cita(nombre, curp, fecha, sede):
    conn = sqlite3.connect("citas.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS citas
                 (nombre TEXT, curp TEXT, fecha TEXT, sede TEXT)''')
    c.execute("INSERT INTO citas VALUES (?, ?, ?, ?)", (nombre, curp, str(fecha), sede))
    conn.commit()
    conn.close()

def responder_con_gpt(pregunta):
    try:
        respuesta = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": pregunta}],
            temperature=0.7
        )
        return respuesta.choices[0].message.content
    except Exception as e:
        return f"Ocurrió un error al consultar la IA: {e}"

if menu == "Inicio":
    st.image("infonavit_logo.svg", width=120)
    st.markdown("**Bienvenido a INFONA.** Tu asistente para trámites con Infonavit.")

elif menu == "Simulador de Crédito":
    st.header("Simulador de Crédito")
    ingreso = st.number_input("¿Cuál es tu ingreso mensual?", min_value=1000)
    años = st.slider("¿Cuántos años has cotizado?", 0, 40, 5)
    if ingreso:
        credito = ingreso * 10 + años * 1000
        st.success(f"Crédito estimado: ${credito:,.2f} MXN")

elif menu == "Agendar Cita":
    st.header("Agenda una Cita")
    nombre = st.text_input("Nombre completo")
    curp = st.text_input("CURP")
    fecha = st.date_input("Fecha", min_value=datetime.date.today())
    sede = st.selectbox("Sede", ["Oaxaca", "CDMX", "Guadalajara", "Monterrey"])
    if st.button("Agendar"):
        guardar_cita(nombre, curp, fecha, sede)
        st.success("¡Tu cita ha sido agendada!")

elif menu == "Chat con INFONA":
    st.header("Asistente Virtual con IA")
    pregunta = st.text_input("Escribe tu duda:")
    if pregunta:
        respuesta = responder_con_gpt(pregunta)
        st.write("INFONA responde:")
        st.write(respuesta)
