
import streamlit as st
from datetime import datetime, timedelta
import unicodedata
import re

st.set_page_config(page_title="INFONA - Asistente Inteligente de Vivienda", page_icon="🏠", layout="wide")

# Función de limpieza de texto para que entienda frases genéricas
def limpiar_texto(texto):
    texto = texto.lower()
    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )
    texto = re.sub(r"[¿?!¡.,;:]", "", texto)
    return texto

# Función de respuesta con llamados a la acción
def responder_chat(texto):
    t = limpiar_texto(texto)

    if "cuanto debo" in t or "debo algo" in t:
        return "Hola Carlos, tu saldo estimado para este bimestre es de **$2,470.00 MXN** y el total pendiente de tu crédito es de **$86,300.00 MXN**. ¿Quieres que esta información se envíe a tu correo o WhatsApp registrado?"
    elif "cuantos dias faltan" in t or "cuanto falta para mi pago" in t:
        dias = (datetime(2025, 6, 17) - datetime.today()).days
        return f"Faltan **{dias} días** para tu próximo pago programado el **17 de junio de 2025**. ¿Deseas recibir un recordatorio automático por WhatsApp?"
    elif "cuanto tiempo me falta" in t or "cuantos bimestres" in t:
        return "Te restan **24 bimestres**, equivalentes a aproximadamente **4 años de pago**. ¿Te gustaría recibir un plan personalizado para reducir este plazo?"
    elif "que me recomiendas" in t:
        return "Te recomiendo hacer aportaciones voluntarias de $1,000 al mes para reducir el plazo en 1 año y ahorrar intereses. ¿Quieres que calculemos un escenario más preciso para ti?"
    elif "como pago" in t:
        return "Puedes realizar pagos desde el portal Infonavit, ventanilla bancaria o tiendas autorizadas. ¿Deseas que te mande el enlace directo para pagar?"
    elif "estado de cuenta" in t:
        return "Tu estado de cuenta más reciente refleja un pago puntual. ¿Quieres que te envíe el resumen a tu correo?"
    elif "cuanto me prestan" in t or "credito estimado" in t:
        return "Con tu salario registrado de $10,000, podrías acceder a un crédito de aproximadamente **$350,000 MXN**. ¿Deseas ver una simulación más detallada?"
    elif "nss" in t or "curp" in t:
        return "Puedes consultar tu NSS en el portal del IMSS. ¿Te mando el enlace para hacerlo de inmediato?"
    elif "hola" in t:
        return "¡Hola! Soy INFONA, tu asistente de vivienda. ¿Quieres conocer tu saldo, agendar una cita o simular tu crédito?"
    elif "adios" in t or "gracias" in t or "nos vemos" in t:
        return "Aún tenemos pendientes. ¿Quieres que te los mande a tu correo o tu WhatsApp registrado?"
    else:
        return "Gracias por tu mensaje. ¿Deseas que esta consulta sea revisada y enviada a tu contacto de seguimiento?"

# Menú
st.sidebar.image("logo_infona_redes.png", width=150)
opcion = st.sidebar.radio("Menú de navegación", ["🏠 Inicio", "💬 Chatea con INFONA", "🧮 Simulador de Crédito", "🗓️ Agendar Cita", "❓ Preguntas Frecuentes"])

# Contenido
if opcion == "🏠 Inicio":
    st.title("INFONA - Asistente Inteligente de Vivienda")
    st.markdown("**¡Hola! Soy INFONA.** Te ayudo a consultar tu crédito, agendar citas o resolver cualquier duda sobre vivienda.")
    st.image("logo_infona_redes.png", width=200)

elif opcion == "💬 Chatea con INFONA":
    st.header("Chatea con INFONA")
    mensaje = st.text_input("Tu mensaje:")
    if mensaje:
        respuesta = responder_chat(mensaje)
        st.success(f"INFONA responde: {respuesta}")

elif opcion == "🧮 Simulador de Crédito":
    st.header("Simulador de Crédito")
    ingreso = st.number_input("Tu ingreso mensual:", min_value=0)
    puntos = st.slider("Tus puntos Infonavit:", 0, 116, 90)
    if ingreso > 0:
        monto = ingreso * (puntos / 116) * 20
        st.info(f"**Crédito estimado:** ${monto:,.2f} MXN")

elif opcion == "🗓️ Agendar Cita":
    st.header("Agendar una Cita")
    nombre = st.text_input("Nombre completo:")
    curp = st.text_input("CURP:")
    fecha = st.date_input("Fecha deseada:")
    hora = st.time_input("Hora deseada:")
    if nombre and curp:
        st.success(f"Cita registrada para **{nombre}** con CURP **{curp}**, el día **{fecha}** a las **{hora}**.")

elif opcion == "❓ Preguntas Frecuentes":
    st.header("Preguntas Frecuentes")
    st.markdown("""
- ¿Qué necesito para tramitar mi crédito?
  Estar dado de alta en el IMSS, tener puntos suficientes y una relación laboral activa.

- ¿Puedo usar INFONA sin registrarme?
  Sí, puedes realizar consultas sin registro.

- ¿Qué tipo de créditos existen?
  Tradicional, Cofinavit, Unamos Créditos, Mejoravit y otros.
""")

# Pie
st.markdown("<hr>", unsafe_allow_html=True)
st.caption("INFONA es un asistente digital no oficial. Para atención personalizada, consulta el portal oficial de Infonavit.")
