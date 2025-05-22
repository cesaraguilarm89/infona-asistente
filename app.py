
import streamlit as st
import sqlite3
import datetime
import re
import unicodedata

st.set_page_config(page_title="INFONA", layout="centered")
st.image("logo_infona_redes.png", width=120)
st.title("INFONA - Asistente Inteligente de Vivienda")
st.caption("Consulta, simula y agenda de forma sencilla.")

menu = st.sidebar.radio("Menú de navegación", [
    "Inicio",
    "Chatea con INFONA",
    "Simulador de Crédito",
    "Agendar Cita",
    "Preguntas Frecuentes"
])

def limpiar_texto(texto):
    texto = texto.lower()
    texto = ''.join(c for c in unicodedata.normalize('NFD', texto)
                    if unicodedata.category(c) != 'Mn')
    texto = re.sub(r'[¿?¡!.,;:]', '', texto)
    return texto

def responder_mensaje(mensaje):
    texto = limpiar_texto(mensaje)
    for claves, respuesta in {('que es', 'infona'): 'INFONA es un asistente inteligente diseñado para orientarte sobre temas relacionados con tu crédito de vivienda.', ('cuanto', 'credito'): 'Puedes usar nuestro simulador de crédito ingresando tu salario mensual y años de cotización.', ('agendar', 'cita'): "Desde la pestaña 'Agendar cita' puedes registrar una fecha y lugar para tu atención presencial.", ('infona', 'infonavit'): 'INFONA es una herramienta complementaria que orienta sobre temas de vivienda, basada en información pública.', ('tramite', 'oficial'): 'No. INFONA es solo una guía. Los trámites oficiales se realizan directamente en Infonavit.', ('requisito', 'credito'): 'Necesitas tener relación laboral activa, al menos 116 puntos y una precalificación positiva.', ('pago',): 'No. Esta plataforma es solo informativa. Para pagos, consulta directamente tu portal Infonavit.', ('dato', 'seguro'): 'Sí. No almacenamos ni compartimos información sin consentimiento.', ('infona', 'cobra'): 'No. Es una herramienta gratuita de consulta y orientación.', ('duda', 'adicional'): 'Puedes contactarnos por los canales oficiales de atención o visitar un CESI.'}.items():
        if all(palabra in texto for palabra in claves):
            return respuesta
    return "Gracias por tu consulta. Actualmente INFONA responde preguntas relacionadas con tu crédito de vivienda, citas y requisitos. Estamos mejorando cada día para ayudarte mejor."

def guardar_cita(nombre, curp, fecha, sede):
    conn = sqlite3.connect("citas.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS citas
                 (nombre TEXT, curp TEXT, fecha TEXT, sede TEXT)''')
    c.execute("INSERT INTO citas VALUES (?, ?, ?, ?)", (nombre, curp, str(fecha), sede))
    conn.commit()
    conn.close()

if menu == "Inicio":
    st.subheader("Bienvenido a INFONA")
    st.markdown("Te damos la bienvenida a INFONA, tu asistente para conocer tu crédito de vivienda, agendar citas y resolver dudas de forma confiable.")

elif menu == "Chatea con INFONA":
    st.subheader("Chatea con INFONA")
    st.markdown("Escribe tu pregunta sobre créditos, citas o requisitos:")
    pregunta = st.text_input("Tu mensaje:")
    if pregunta:
        respuesta = responder_mensaje(pregunta)
        st.markdown("**INFONA responde:**")
        st.success(respuesta)

elif menu == "Simulador de Crédito":
    st.subheader("Simulador de Crédito INFONA")
    ingreso = st.number_input("¿Cuál es tu ingreso mensual?", min_value=1000)
    años = st.slider("¿Cuántos años has cotizado?", 0, 40, 5)
    if ingreso:
        credito = ingreso * 10 + años * 1000
        st.success(f"Crédito estimado: ${credito:,.2f} MXN")

elif menu == "Agendar Cita":
    st.subheader("Agenda tu Cita en INFONA")
    nombre = st.text_input("Nombre completo")
    curp = st.text_input("CURP")
    fecha = st.date_input("Fecha deseada", min_value=datetime.date.today())
    sede = st.selectbox("Sede", ["Oaxaca", "CDMX", "Guadalajara", "Monterrey"])
    if st.button("Confirmar cita"):
        guardar_cita(nombre, curp, fecha, sede)
        st.success("Tu cita ha sido registrada correctamente.")

elif menu == "Preguntas Frecuentes":
    st.subheader("Preguntas Frecuentes")
    st.markdown("""
**¿Qué es INFONA?**  
INFONA es un asistente virtual que te orienta sobre opciones de crédito para vivienda.  

**¿Puedo hacer trámites oficiales aquí?**  
INFONA es un asistente de orientación, los trámites deben formalizarse directamente en Infonavit.  

**¿Mis datos están seguros?**  
Sí. No almacenamos ni compartimos tus datos personales sin tu consentimiento.  
""")
