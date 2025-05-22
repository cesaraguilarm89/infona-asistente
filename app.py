
import streamlit as st
import datetime

# Configuración de la interfaz
st.set_page_config(page_title="INFONA", page_icon="🏠", layout="centered")
st.markdown('<style>body {background-color: #ffffff; color: #111;}</style>', unsafe_allow_html=True)

# Imagen de bienvenida
st.sidebar.image("infonavit_logo.PNG", width=150)
seccion = st.sidebar.radio("Menú de navegación", ["Inicio", "Chatea con INFONA", "Simulador de Crédito", "Agendar Cita", "Preguntas Frecuentes"])

# Diccionario de respuestas simuladas
respuestas = {
    "hola": "Hola, soy INFONA, tu asistente digital. ¿En qué puedo ayudarte hoy?",
    "adiós": "Gracias por usar INFONA. ¿Quieres que los pendientes te los mande a tu correo o WhatsApp registrado?",
    "cuánto debo": "Hola Carlos, tu saldo estimado para este bimestre es de **2,470.00 MXN** y el total pendiente de tu crédito es de **86,300.00 MXN**. ¿Quieres que esta información se envíe a tu correo o WhatsApp registrado?",
    "cuánto falta para pagar": "Te faltan aproximadamente 14 bimestres, considerando tus pagos actuales. ¿Deseas que calculemos un plan personalizado?",
    "me recomiendas": "Con base en tu historial, podrías considerar un pago anticipado este bimestre. ¿Quieres simularlo juntos?",
    "cuánto falta para terminar mi crédito": "Según los datos estimados, tu crédito se terminará en julio de 2028. ¿Te gustaría que lo enviemos a tu WhatsApp para seguimiento?",
    "cuántos días me faltan para pagar": "Faltan 17 días para tu próximo pago. ¿Deseas agendar un recordatorio?",
    "saldo": "Tu saldo acumulado pendiente es de **52,300.00 MXN**. ¿Deseas ver el desglose por bimestre?",
    "crédito": "Actualmente tu crédito está activo y con buen historial. ¿Te gustaría saber si puedes solicitar otro producto?",
}

def normalizar(texto):
    return texto.lower().replace("¿", "").replace("?", "").replace("¡", "").replace("!", "").strip()

# Secciones de la app
if seccion == "Inicio":
    st.title("INFONA - Asistente Inteligente de Vivienda")
    st.write("Consulta, simula y agenda de forma sencilla.")
    st.image("infonavit_logo.PNG", width=180)
    st.markdown("Hola, soy **INFONA**, tu asistente digital para créditos de vivienda. Estoy aquí para ayudarte con tus trámites, pagos y simulaciones.")

elif seccion == "Chatea con INFONA":
    st.header("Chatea con INFONA")
    pregunta = st.text_input("Escribe tu pregunta sobre créditos, pagos, citas o trámites:")
    if pregunta:
        clave = normalizar(pregunta)
        respuesta = "Gracias por tu mensaje. ¿Deseas que esta consulta sea revisada y enviada a tu contacto de seguimiento?"
        for k in respuestas:
            if k in clave:
                respuesta = respuestas[k]
                break
        st.success(f"INFONA responde: {respuesta}")
    st.caption("INFONA es un asistente digital no oficial. Para atención personalizada, consulta el portal oficial de Infonavit.")

elif seccion == "Simulador de Crédito":
    st.header("Simulador de Crédito")
    salario = st.number_input("Ingresa tu salario mensual:", min_value=0)
    puntos = st.slider("Selecciona tus puntos actuales Infonavit:", 0, 116, 90)
    if salario > 0:
        monto = salario * (puntos / 116) * 10
        st.info(f"INFONA estima que podrías acceder a un crédito de aproximadamente **{monto:,.2f} MXN**.")
        st.markdown("¿Te gustaría que esta simulación se envíe a tu correo o WhatsApp registrado?")

elif seccion == "Agendar Cita":
    st.header("Agenda una cita")
    nombre = st.text_input("Nombre completo:")
    curp = st.text_input("CURP:")
    fecha = st.date_input("Selecciona la fecha:", datetime.date.today())
    hora = st.time_input("Selecciona la hora:")
    if nombre and curp:
        st.success(f"Cita agendada para {nombre} el día {fecha} a las {hora}. Recibirás una confirmación vía correo o WhatsApp.")

elif seccion == "Preguntas Frecuentes":
    st.header("Preguntas Frecuentes")
    st.markdown("**¿Qué necesito para tramitar mi crédito?**")
    st.write("Necesitas estar dado de alta en el IMSS, contar con puntos suficientes y tener una relación laboral activa.")
    st.markdown("**¿Puedo usar INFONA sin registrarme?**")
    st.write("Sí, INFONA está diseñado para darte asistencia básica sin necesidad de registro previo.")
    st.markdown("**¿Qué tipo de créditos existen?**")
    st.write("Crédito tradicional, Cofinavit, Unamos Créditos y Mejoravit, entre otros.")



# === FLUJOS DE PREGUNTAS Y RESPUESTAS EXPANDIDAS PARA INFONA ===

chat_flows = {
    "consulta_credito": {
        "variantes": [
            "¿Cuánto tengo disponible de crédito?",
            "¿Cuánto me presta Infonavit?",
            "¿Qué crédito puedo obtener?",
            "¿Me alcanza para una casa?",
            "¿Tengo puntos suficientes?",
            "¿Puedo ver mis puntos?",
            "¿Ya junto los puntos?"
        ],
        "respuesta": "Carlos, tu crédito disponible depende de tus puntos acumulados y tu salario. Puedes consultarlo usando el simulador o tu precalificación actualizada.",
        "llamado_accion": "¿Quieres que te muestre tu precalificación o el simulador de crédito?"
    },
    "consulta_pagos": {
        "variantes": [
            "¿Cuánto debo?",
            "¿Cuál es el saldo de mi crédito?",
            "¿Cuánto me toca pagar este mes?",
            "¿Dónde puedo pagar?",
            "¿Puedo adelantar pagos?",
            "¿Cómo consulto mis pagos?"
        ],
        "respuesta": "Carlos, puedes consultar tu saldo actual accediendo con tu número de crédito. Los pagos pueden hacerse por transferencia, banco o vía patrón.",
        "llamado_accion": "¿Te gustaría ver tu saldo actual o recibir la lista de lugares donde puedes pagar?"
    },
    "trámites_documentos": {
        "variantes": [
            "¿Cómo saco mi aviso de retención?",
            "¿Qué papeles necesito para el crédito?",
            "¿Dónde subo mis documentos?",
            "¿Qué necesito llevar a mi cita?"
        ],
        "respuesta": "Carlos, para continuar con tu trámite necesitas subir tus documentos básicos: INE, comprobante de domicilio y precalificación. El aviso de retención se genera en línea.",
        "llamado_accion": "¿Quieres que te muestre el portal para subir tus documentos o para generar tu aviso de retención?"
    },
    "agendar_cita": {
        "variantes": [
            "¿Cómo agendo una cita?",
            "¿Hay citas disponibles?",
            "¿Dónde puedo ir en persona?",
            "¿Puedo reagendar mi cita?"
        ],
        "respuesta": "Carlos, puedes agendar tu cita directamente desde esta app en la sección 'Agendar Cita'. Las ubicaciones varían según tu ciudad.",
        "llamado_accion": "¿Deseas agendar tu cita ahora o ver las oficinas disponibles?"
    },
    "simulador_credito": {
        "variantes": [
            "Hazme una simulación",
            "¿Puedo hacer un simulador?",
            "¿Me alcanza con mi sueldo?",
            "¿Cuánto me presta Infonavit si gano $10,000?"
        ],
        "respuesta": "Carlos, con tu ingreso mensual, podemos hacer una simulación aproximada del crédito que puedes recibir, y cuánto pagarías al mes.",
        "llamado_accion": "¿Quieres iniciar el simulador ahora mismo?"
    },
    "atencion_contacto": {
        "variantes": [
            "¿Hay alguien que me atienda?",
            "¿Puedo hablar con alguien?",
            "¿Me puedes mandar la info a mi WhatsApp?",
            "¿Tienes un número de contacto?"
        ],
        "respuesta": "Carlos, puedo ayudarte desde aquí, pero si prefieres atención personalizada, puedo enviarte la información de contacto de Infonatel o del centro más cercano.",
        "llamado_accion": "¿Te envío los datos de contacto por correo o por WhatsApp registrado?"
    }
}
