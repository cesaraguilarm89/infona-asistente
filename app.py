
import streamlit as st
import sqlite3
import datetime

st.set_page_config(page_title="INFONA", layout="centered")
st.title("INFONA - Asistente Inteligente del Infonavit")
st.subheader("Tu asistente para consultar crédito, agendar citas y resolver dudas.")

menu = st.sidebar.selectbox("Menú", ["Inicio", "Simulador de Crédito", "Agendar Cita", "Chat con INFONA"])

# Función para guardar citas en SQLite
def guardar_cita(nombre, curp, fecha, sede):
    conn = sqlite3.connect("citas.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS citas
                 (nombre TEXT, curp TEXT, fecha TEXT, sede TEXT)''')
    c.execute("INSERT INTO citas VALUES (?, ?, ?, ?)", (nombre, curp, str(fecha), sede))
    conn.commit()
    conn.close()

if menu == "Inicio":
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/4b/Infonavit_logo.svg", width=120)
    st.markdown("**Bienvenido a INFONA.** Este asistente te ayudará a realizar consultas y trámites con Infonavit.")

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
    st.header("Asistente Virtual")
    user_input = st.text_input("Escribe tu duda:")
    if user_input:
        st.info("Respuesta simulada:")
        st.write("Gracias por tu pregunta. Pronto un asesor se pondrá en contacto contigo o visita nuestro portal oficial.")
