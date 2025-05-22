
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
    for claves, respuesta in {('hola',): '¡Hola! ¿En qué puedo ayudarte hoy?', ('buenos dias',): 'Buenos días, ¿cómo puedo asistirte con tu crédito de vivienda?', ('buenas tardes',): 'Buenas tardes, ¿necesitas ayuda con tu crédito o citas?', ('adios',): 'Hasta pronto. ¿Quieres que los pendientes te los mande a tu correo o WhatsApp registrado?', ('hasta luego',): 'Nos vemos pronto. ¿Te gustaría que enviemos un resumen a tu correo?', ('cuanto', 'pagar'): 'Tu monto depende de tu crédito y aportaciones. ¿Quieres que te mostremos cómo consultarlo?', ('cuanto', 'debo'): 'Podemos ayudarte a revisar cuánto debes. ¿Te gustaría abrir el portal oficial?', ('estado', 'cuenta'): 'Tu estado de cuenta está disponible en tu sesión Infonavit. ¿Te muestro cómo acceder?', ('pago', 'bimestre'): 'Los pagos se calculan bimestralmente. ¿Te gustaría conocer tu calendario de pagos?', ('saldo', 'favor'): 'Tu saldo a favor lo puedes consultar con tu NSS. ¿Deseas que te expliquemos cómo?', ('nss', 'olvidado'): 'Puedes recuperar tu NSS en el portal del IMSS. ¿Quieres el enlace directo?', ('actualizar', 'datos'): 'Puedes actualizar tus datos desde tu perfil en el portal Infonavit. ¿Te muestro cómo hacerlo?', ('ayuda',): 'Estoy aquí para orientarte. ¿Sobre qué tema necesitas apoyo?', ('necesito', 'ayuda'): 'Claro, dime qué necesitas y te ayudaré lo mejor posible.'}.items():
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
    st.write("Escribe tu pregunta sobre créditos, pagos, citas o trámites:")
    pregunta = st.text_input("Tu pregunta")
    if pregunta:
        pregunta_limpia = pregunta.lower()
        respuesta = ""

        if any(p in pregunta_limpia for p in ["cuánto debo", "debo", "cuánto me falta", "liquidar", "terminar", "cuánto me queda"]):
            respuesta = "Tu saldo pendiente depende del monto original y tus pagos realizados. Podemos ayudarte a consultar tu estado actual."
        elif any(p in pregunta_limpia for p in ["fecha de pago", "cuando debo", "cuándo pago"]):
            respuesta = "Tu fecha de pago depende del esquema que tengas con tu patrón o banco. Podemos revisar tu calendario de pagos."
        elif any(p in pregunta_limpia for p in ["monto de mi crédito", "crédito total", "cuánto me prestaron"]):
            respuesta = "El monto de tu crédito original se puede consultar directamente desde tu perfil. ¿Quieres que lo revise contigo?"
        elif any(p in pregunta_limpia for p in ["recomiendas", "mejor opción", "aconsejas"]):
            respuesta = "Podemos ayudarte a elegir la mejor ruta: desde pagar anticipadamente hasta cambiar de esquema. ¿Quieres que analicemos tu caso?"
        elif any(p in pregunta_limpia for p in ["tiempo acabo", "cuándo termino", "cuando liquido"]):
            respuesta = "Con base en tu salario y pagos actuales, podemos estimar una fecha tentativa de liquidación."
        elif any(p in pregunta_limpia for p in ["simulación", "mejor escenario"]):
            respuesta = "Puedo ayudarte a simular diferentes escenarios para que elijas el que más te convenga."
        elif any(p in pregunta_limpia for p in ["incentivo", "programa", "apoyo", "beneficio"]):
            respuesta = "Infonavit tiene programas como Descuentos por Pago Anticipado o Responsabilidad Compartida. ¿Te gustaría conocerlos?"
        elif any(p in pregunta_limpia for p in ["ya pagó", "mi jefe pagó", "aportación patrón"]):
            respuesta = "Podemos revisar si tu patrón ha realizado la aportación reciente. ¿Te gustaría que te lo confirme?"
        else:
            respuesta = "Gracias por tu pregunta. Puedo ayudarte con temas como pagos, simulaciones o citas."

        st.success(f"INFONA responde: {respuesta} ¿Deseas que te lo mande por correo o WhatsApp registrado?")


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
