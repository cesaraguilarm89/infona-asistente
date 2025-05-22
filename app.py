
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
    respuestas = [
        (['hola', 'buenos dias', 'buenas tardes', 'buenas'], '¡Hola! ¿En qué puedo ayudarte hoy?'),
        (['adios', 'hasta luego', 'nos vemos'], 'Hasta pronto. ¿Quieres que los pendientes te los mande a tu correo o WhatsApp registrado?'),
        (['cuanto', 'debo', 'adeudo', 'saldo pendiente', 'resta pagar'], 'Tu monto actual depende de tu crédito. ¿Quieres abrir el portal para consultarlo o que te lo envíe?'),
        (['fecha de pago', 'cuando pago', 'fecha limite', 'pago siguiente'], 'Tu fecha de pago es el día 17 de cada bimestre. ¿Quieres agendar un recordatorio?'),
        (['monto de mi credito', 'cuanto me prestaron', 'total del credito'], 'Tu crédito total es de $550,000 MXN. ¿Te gustaría ver el desglose completo?'),
        (['cuanto me falta por pagar', 'cuanto me falta por liquidar'], 'Te falta por pagar aproximadamente $120,000 MXN. ¿Deseas una proyección detallada?'),
        (['haz una simulacion', 'simula', 'calculo rapido'], 'Simulando tu mejor escenario... podrías terminar en 5 años si aportas $3,000 adicionales al mes. ¿Te muestro cómo?'),
        (['ya pago mi jefe', 'aportacion patronal'], 'Tu patrón realizó la última aportación hace 15 días. ¿Quieres recibir notificaciones cada vez que lo haga?'),
        (['programa apoyo', 'incentivo', 'ayuda especial'], 'Actualmente hay un programa de apoyo para liquidaciones anticipadas. ¿Te interesa saber si aplicas?'),
        (['que me recomiendas', 'sugerencia', 'mejor opcion'], 'Puedo mostrarte un plan personalizado según tu capacidad de pago. ¿Te gustaría intentarlo?')
    ]
    for claves, respuesta in respuestas:
        if all(any(k in texto for k in grupo) for grupo in [claves]):
            return respuesta
    return "No entendí completamente tu pregunta, pero puedo ayudarte con créditos, pagos, citas o simulaciones. ¿Qué necesitas hoy?"
    return "Gracias por tu consulta. Actualmente INFONA responde temas sobre crédito, citas y requisitos. ¿Te gustaría que te ayudemos en algo específico?"

def guardar_cita(nombre, curp, fecha, sede):
    conn = sqlite3.connect("citas.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS citas
                 (nombre TEXT, curp TEXT, fecha TEXT, sede TEXT)''')
    c.execute("INSERT INTO citas VALUES (?, ?, ?, ?)", (nombre, curp, fecha, sede))
    conn.commit()
    conn.close()

# 🏠
if menu == "Inicio":
    st.subheader("Bienvenido a INFONA")
    st.markdown("Te damos la bienvenida a INFONA, tu asistente para conocer tu crédito de vivienda, agendar citas y resolver dudas de forma confiable.")

if menu == "Chatea con INFONA":
    st.subheader("Chatea con INFONA")
    st.write("Escribe tu pregunta sobre créditos, pagos, citas o trámites:")
    pregunta = st.text_input("Tu pregunta")
    if pregunta:
        pregunta_limpia = pregunta.lower()
        respuesta = ""

        if any(p in pregunta_limpia for p in ["cuánto debo", "debo", "cuánto me falta", "liquidar", "terminar", "cuánto me queda"]):
            respuesta = "Zuri actualmente tiene un saldo pendiente de $158,400 MXN. Este monto puede reducirse si realiza pagos anticipados."
        elif any(p in pregunta_limpia for p in ["fecha de pago", "cuando debo", "cuándo pago"]):
            respuesta = "La próxima fecha de pago de Zuri es el 5 de junio. El monto estimado es de $2,450 MXN."
        elif any(p in pregunta_limpia for p in ["monto de mi crédito", "crédito total", "cuánto me prestaron"]):
            respuesta = "Zuri recibió un crédito inicial por $435,000 MXN en el año 2022, bajo el esquema de crédito tradicional."
        elif any(p in pregunta_limpia for p in ["recomiendas", "mejor opción", "aconsejas"]):
            respuesta = "Para Zuri, lo más conveniente sería aplicar pagos dobles en los próximos 6 meses y beneficiarse del programa de descuento anticipado."
        elif any(p in pregunta_limpia for p in ["tiempo acabo", "cuándo termino", "cuando liquido"]):
            respuesta = "Si Zuri continúa con su ritmo de pagos actual, terminaría de liquidar su crédito en aproximadamente 6 años."
        elif any(p in pregunta_limpia for p in ["simulación", "mejor escenario"]):
            respuesta = "Simulando el mejor escenario, Zuri podría reducir su plazo a 3.5 años si duplica su pago mensual actual."
        elif any(p in pregunta_limpia for p in ["incentivo", "programa", "apoyo", "beneficio"]):
            respuesta = "Zuri puede aplicar al programa 'Descuento por Liquidación Anticipada', vigente hasta diciembre. ¿Quieres ver si aplicas tú también?"
        elif any(p in pregunta_limpia for p in ["ya pagó", "mi jefe pagó", "aportación patrón"]):
            respuesta = "El patrón de Zuri realizó la última aportación el 15 de mayo. Está al corriente en sus obligaciones."
        else:
            respuesta = "Gracias por tu pregunta. Puedo ayudarte con temas como pagos, simulaciones o citas."

        st.success(f"INFONA responde a Zuri: {respuesta} ¿Deseas que te lo mande por correo o WhatsApp registrado?")


if menu == "Simulador de Crédito":
    st.subheader("Simulador de Crédito INFONA")
    ingreso = st.number_input("¿Cuál es tu ingreso mensual?", min_value=1000)
    años = st.slider("¿Cuántos años has cotizado?", 0, 40, 5)
    if ingreso:
        credito = ingreso * 10 + años * 1000
        st.success(f"Crédito estimado: ${credito:,.2f} MXN")

if menu == "Agendar Cita":
    st.subheader("Agenda tu Cita en INFONA")
    nombre = st.text_input("Nombre completo")
    curp = st.text_input("CURP")
    fecha = st.date_input("Fecha deseada", min_value=datetime.date.today())
    sede = st.selectbox("Sede", ["Oaxaca", "CDMX", "Guadalajara", "Monterrey"])
    if st.button("Confirmar cita"):
        guardar_cita(nombre, curp, fecha, sede)
        st.success("Tu cita ha sido registrada correctamente.")

if menu == "Preguntas Frecuentes":
    st.subheader("Preguntas Frecuentes")
    st.markdown("""
**¿Qué es INFONA?**  
INFONA es un asistente virtual que te orienta sobre opciones de crédito para vivienda.  

**¿Puedo hacer trámites oficiales aquí?**  
INFONA es un asistente de orientación, los trámites deben formalizarse directamente en Infonavit.  

**¿Mis datos están seguros?**  
Sí. No almacenamos ni compartimos tus datos personales sin tu consentimiento.  
""")
