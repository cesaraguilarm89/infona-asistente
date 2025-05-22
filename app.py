
import streamlit as st
import sqlite3
import datetime

st.set_page_config(page_title="INFONA", layout="centered")
st.title("INFONA - Asistente Inteligente del Infonavit")
st.subheader("Consulta tu crédito, agenda una cita y revisa tus opciones.")

menu = st.sidebar.selectbox("Menú", ["Inicio", "Simulador de Crédito", "Agendar Cita"])

def guardar_cita(nombre, curp, fecha, sede):
    conn = sqlite3.connect("citas.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS citas
                 (nombre TEXT, curp TEXT, fecha TEXT, sede TEXT)''')
    c.execute("INSERT INTO citas VALUES (?, ?, ?, ?)", (nombre, curp, str(fecha), sede))
    conn.commit()
    conn.close()

if menu == "Inicio":
    st.image("infonavit_logo.PNG", width=150)
    st.markdown("**Bienvenido a INFONA.** Este asistente te ayuda a simular tu crédito y agendar citas con Infonavit.")

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
    fecha = st.date_input("Fecha deseada", min_value=datetime.date.today())
    sede = st.selectbox("Sede", ["Oaxaca", "CDMX", "Guadalajara", "Monterrey"])
    if st.button("Agendar"):
        guardar_cita(nombre, curp, fecha, sede)
        st.success("Tu cita fue registrada con éxito.")
