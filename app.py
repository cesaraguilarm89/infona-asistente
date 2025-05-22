
import streamlit as st
import sqlite3
import datetime

st.set_page_config(page_title="INFONA", layout="centered")
st.image("logo_infona_redes.png", width=120)
st.title("INFONA - Asistente Inteligente de Vivienda")
st.caption("Soluciones accesibles, información clara.")

menu = st.sidebar.radio("Menú de navegación", [
    "Inicio",
    "Chatea con INFONA",
    "Simulador de Crédito",
    "Agendar Cita",
    "Preguntas Frecuentes"
])

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
    st.markdown(
        "Te damos la bienvenida a INFONA, el asistente virtual inteligente que te ayuda a conocer tu crédito de vivienda, "
        "agendar citas y resolver tus dudas de forma clara y profesional."
    )

elif menu == "Chatea con INFONA":
    st.subheader("Consulta con INFONA")
    st.markdown("Selecciona una pregunta frecuente para obtener una respuesta inmediata.")
    pregunta = st.selectbox("Selecciona una pregunta:", ['¿Qué es INFONA?', '¿Cómo saber cuánto crédito tengo disponible?', '¿Dónde puedo agendar una cita?', '¿INFONA es parte de Infonavit?', '¿Puedo hacer trámites oficiales desde aquí?', '¿Cuáles son los requisitos para obtener un crédito?', '¿Se pueden hacer pagos desde esta app?', '¿Mis datos están seguros en INFONA?', '¿INFONA cobra algún servicio?', '¿Qué pasa si tengo dudas adicionales?'])
    if pregunta:
        st.markdown("**Respuesta:**")
        st.info({'¿Qué es INFONA?': 'INFONA es un asistente inteligente diseñado para orientarte sobre temas relacionados con tu crédito de vivienda.', '¿Cómo saber cuánto crédito tengo disponible?': 'Puedes usar nuestro simulador de crédito ingresando tu salario mensual y años de cotización.', '¿Dónde puedo agendar una cita?': "Desde la pestaña 'Agendar cita' puedes registrar una fecha y lugar para tu atención presencial.", '¿INFONA es parte de Infonavit?': 'INFONA es una herramienta complementaria que orienta sobre temas de vivienda, basada en información pública.', '¿Puedo hacer trámites oficiales desde aquí?': 'No. INFONA es solo una guía. Los trámites oficiales se realizan directamente en Infonavit.', '¿Cuáles son los requisitos para obtener un crédito?': 'Necesitas tener relación laboral activa, al menos 116 puntos y una precalificación positiva.', '¿Se pueden hacer pagos desde esta app?': 'No. Esta plataforma es solo informativa. Para pagos, consulta directamente tu portal Infonavit.', '¿Mis datos están seguros en INFONA?': 'Sí. No almacenamos ni compartimos información sin consentimiento.', '¿INFONA cobra algún servicio?': 'No. Es una herramienta gratuita de consulta y orientación.', '¿Qué pasa si tengo dudas adicionales?': 'Puedes contactarnos por los canales oficiales de atención o visitar un CESI.'}[pregunta])

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
