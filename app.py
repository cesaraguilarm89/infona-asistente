
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
    for claves, respuesta in {('que es', 'infona'): 'INFONA es tu asistente inteligente en vivienda. ¿Quieres que te explique cómo empezar a usarlo?', ('cuanto', 'credito'): 'Puedes estimar tu crédito con nuestro simulador. ¿Quieres que lo calculemos juntos?', ('credito', 'disponible'): 'Podemos ayudarte a estimar cuánto crédito tienes. ¿Te gustaría simularlo ahora?', ('simulador', 'credito'): 'Nuestro simulador te ayuda a calcular tu crédito de manera fácil. ¿Deseas usarlo?', ('agendar', 'cita'): 'Puedes agendar tu cita desde el menú correspondiente. ¿Te ayudo a registrarla ahora?', ('sacar', 'cita'): 'Claro, puedes sacar una cita rápidamente. ¿Quieres que lo hagamos ya?', ('infona', 'infonavit'): 'INFONA es una herramienta complementaria, no oficial, para ayudarte con orientación de vivienda.', ('tramite', 'oficial'): 'Aquí no se realizan trámites oficiales, pero podemos orientarte. ¿Te gustaría saber cómo iniciar?', ('requisitos', 'credito'): 'Para obtener crédito necesitas relación laboral activa, al menos 116 puntos y precalificación positiva.', ('pago', 'credito'): 'Los pagos se realizan desde tu portal Infonavit. ¿Quieres saber cómo acceder?', ('hacer', 'pago'): 'INFONA te puede guiar para hacer tu pago correctamente. ¿Quieres que te explique cómo?', ('dato', 'seguro'): 'Tus datos están protegidos. No los almacenamos sin tu consentimiento. ¿Quieres revisar nuestra política?', ('infona', 'cobra'): 'INFONA es gratuito. No tiene ningún costo para los usuarios.', ('duda', 'adicional'): 'Puedes acudir al CESI o consultar los canales oficiales. ¿Te ayudo a buscar el más cercano?', ('puntos', 'infonavit'): 'Puedes consultar tus puntos en el portal oficial. ¿Te muestro cómo hacerlo?', ('precalificacion',): 'La precalificación se obtiene en línea con tus datos. ¿Te gustaría que te guiemos paso a paso?', ('aportaciones', 'patronales'): 'Puedes revisar tus aportaciones en tu estado de cuenta Infonavit. ¿Te muestro dónde acceder?', ('trabajo', 'informal'): 'Por el momento no hay créditos para trabajo informal, pero existen opciones como Unamos Créditos. ¿Quieres conocerlas?', ('unamos', 'creditos'): 'Unamos Créditos permite juntar créditos con un familiar o pareja. ¿Te interesa esta opción?', ('credito', 'construir'): 'El crédito para construir está disponible si tienes un terreno propio. ¿Te gustaría simularlo?', ('cesi',): 'El CESI es el Centro de Servicio Infonavit más cercano. ¿Te gustaría ubicar uno?'}.items():
        if all(palabra in texto for palabra in claves):
            return respuesta
    return "Gracias por tu consulta. Actualmente INFONA responde temas sobre crédito, citas y requisitos. ¿Te gustaría que te ayudemos en algo específico?"

def guardar_cita(nombre, curp, fecha, sede):
    conn = sqlite3.connect("citas.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS citas
                 (nombre TEXT, curp TEXT, fecha TEXT, sede TEXT)''')
    c.execute("INSERT INTO citas VALUES (?, ?, ?, ?)", (nombre, curp, fecha, sede))
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
