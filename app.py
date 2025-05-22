# === FUNCIONES DE NAVEGACIÓN PLACEHOLDER ===
def mostrar_inicio():
    st.write("Bienvenido a INFONA. Elige una opción del menú para comenzar.")

def mostrar_chat():
    st.write("Puedes escribir tu duda sobre créditos, pagos, citas o trámites.")

def mostrar_simulador():
    st.write("Simula tu crédito aquí. Ingresa tus datos para continuar.")

def mostrar_agendar():
    st.write("Agenda tu cita seleccionando la fecha y módulo disponible.")

def mostrar_preguntas():
    st.write("Aquí encontrarás respuestas a las preguntas más frecuentes.")



import streamlit as st
import datetime

# Configuración de la interfaz
st.set_page_config(page_title="INFONA", page_icon="🏠", layout="centered")
st.markdown('<style>body {background-color: #ffffff; color: #111;}</style>', unsafe_allow_html=True)

# Imagen de bienvenida
st.sidebar.image("infonavit_logo.PNG", width=150)
seccion = 

if seleccion == menu_opciones["Inicio"]:
    mostrar_inicio()
elif seleccion == menu_opciones["Chat"]:
    mostrar_chat()
elif seleccion == menu_opciones["Simulador"]:
    mostrar_simulador()
elif seleccion == menu_opciones["Cita"]:
    mostrar_agendar()
elif seleccion == menu_opciones["FAQ"]:
    mostrar_preguntas()


# === MENÚ LATERAL CON CLAVES SEGURAS Y KEY ÚNICA ===
menu_opciones = {
    "Inicio": "🏠 Inicio",
    "Chat": "💬 Chatea con INFONA",
    "Simulador": "📊 Simulador de Crédito",
    "Cita": "📅 Agendar Cita",
    "FAQ": "❓ Preguntas Frecuentes"
}

seleccion = st.sidebar.radio(
    "Menú de navegación",
    list(menu_opciones.values()),
    key="menu_navegacion"
)

if seleccion == menu_opciones["Inicio"]:
    mostrar_inicio()
elif seleccion == menu_opciones["Chat"]:
    mostrar_chat()
elif seleccion == menu_opciones["Simulador"]:
    mostrar_simulador()
elif seleccion == menu_opciones["Cita"]:
    mostrar_agendar()
elif seleccion == menu_opciones["FAQ"]:
    mostrar_preguntas()


# === MENÚ LATERAL CON CLAVES SEGURAS Y KEY ÚNICA ===
menu_opciones = {
    "Inicio": "🏠 Inicio",
    "Chat": "💬 Chatea con INFONA",
    "Simulador": "📊 Simulador de Crédito",
    "Cita": "📅 Agendar Cita",
    "FAQ": "❓ Preguntas Frecuentes"
}

seleccion = st.sidebar.radio(
    "Menú de navegación",
    list(menu_opciones.values()),
    key="menu_navegacion"
)

if seleccion == menu_opciones["Inicio"]:
    mostrar_inicio()
elif seleccion == menu_opciones["Chat"]:
    mostrar_chat()
elif seleccion == menu_opciones["Simulador"]:
    mostrar_simulador()
elif seleccion == menu_opciones["Cita"]:
    mostrar_agendar()
elif seleccion == menu_opciones["FAQ"]:
    mostrar_preguntas()


# === MENÚ LATERAL CON CLAVES SEGURAS Y KEY ÚNICA ===
menu_opciones = {
    "Inicio": "🏠 Inicio",
    "Chat": "💬 Chatea con INFONA",
    "Simulador": "📊 Simulador de Crédito",
    "Cita": "📅 Agendar Cita",
    "FAQ": "❓ Preguntas Frecuentes"
}

seleccion = st.sidebar.radio(
    "Menú de navegación",
    list(menu_opciones.values()),
    key="menu_navegacion"
)

if seleccion == menu_opciones["Inicio"]:
    mostrar_inicio()
elif seleccion == menu_opciones["Chat"]:
    mostrar_chat()
elif seleccion == menu_opciones["Simulador"]:
    mostrar_simulador()
elif seleccion == menu_opciones["Cita"]:
    mostrar_agendar()
elif seleccion == menu_opciones["FAQ"]:
    mostrar_preguntas()
