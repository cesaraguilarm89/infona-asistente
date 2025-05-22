
import streamlit as st
import sqlite3
import datetime
import re
import unicodedata

st.set_page_config(page_title="INFONA", layout="centered")

st.image("logo_infona_redes.png", width=120)
st.title("INFONA - Asistente Inteligente de Vivienda")
st.caption("Consulta, simula y agenda de forma sencilla.")

# Menú lateral único y limpio
menu = st.sidebar.radio("Menú de navegación", [
    "Inicio",
    "Chatea con INFONA",
    "Simulador de Crédito",
    "Agendar Cita",
    "Preguntas Frecuentes"
])

# Secciones condicionales
if menu == "Inicio":
    st.subheader("Bienvenido a INFONA")
    st.write("Este asistente digital te ayuda a consultar tu crédito, agendar citas y resolver dudas sobre Infonavit.")

elif menu == "Chatea con INFONA":
    st.subheader("Chatea con INFONA")
    st.write("Escribe tu pregunta sobre créditos, pagos, citas o trámites:")
    pregunta = st.text_input("Tu pregunta")
    if pregunta:
        st.success("INFONA responde: Actualmente tu crédito está activo y con buen historial. ¿Te gustaría saber si puedes solicitar otro producto?")

elif menu == "Simulador de Crédito":
    st.subheader("Simulador de Crédito")
    st.write("Ingresa tu salario mensual para simular tu crédito.")
    salario = st.number_input("Salario mensual", min_value=0)
    if salario > 0:
        st.info(f"Con un salario de ${salario:.2f}, podrías acceder a un crédito estimado de ${salario * 35:.2f}.")

elif menu == "Agendar Cita":
    st.subheader("Agendar Cita")
    fecha = st.date_input("Selecciona una fecha")
    hora = st.time_input("Selecciona una hora")
    if st.button("Agendar"):
        st.success(f"Cita agendada para el {fecha} a las {hora}.")

elif menu == "Preguntas Frecuentes":
    st.subheader("Preguntas Frecuentes")
    st.write("- ¿Cómo consulto mi saldo?")
    st.write("- ¿Qué necesito para tramitar un crédito?")
    st.write("- ¿Dónde puedo pagar?")
