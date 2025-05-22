import streamlit as st
from diccionario_extendido import respuestas_extensas

# Estilo personalizado
st.set_page_config(page_title="INFONA - Asistente Inteligente de Vivienda", page_icon=":house:", layout="wide")

st.markdown("""
    <style>
        .main {
            background-color: white;
            color: black;
        }
        .stApp {
            background-color: #ffffff;
        }
        header, footer {visibility: hidden;}
        .css-1v3fvcr {
            background-color: #e10600 !important;
        }
        .stButton>button {
            background-color: #e10600 !important;
            color: white !important;
        }
        .stTextInput>div>div>input {
            border: 1px solid #e10600;
        }
    </style>
""", unsafe_allow_html=True)

menu = st.sidebar.radio("Menú de navegación", ["Inicio", "Chatea con INFONA", "Simulador de Crédito", "Agendar Cita", "Preguntas Frecuentes"])

if menu == "Inicio":
    st.image("logo_infona_redes.png", width=100)
    st.title("INFONA - Asistente Inteligente de Vivienda")
    st.write("Consulta, simula y agenda de forma sencilla.")

elif menu == "Chatea con INFONA":
    st.header("Chatea con INFONA")
    pregunta = st.text_input("Escribe tu pregunta sobre créditos, pagos, citas o trámites:")
    if pregunta:
        respuesta = respuestas_extensas.get(pregunta.lower(), "Gracias por tu consulta. Actualmente INFONA responde preguntas relacionadas con tu crédito de vivienda, citas y requisitos.")
        st.success(f"INFONA responde: {respuesta}")

elif menu == "Simulador de Crédito":
    st.header("Simulador de Crédito")
    ingreso = st.number_input("¿Cuál es tu ingreso mensual aproximado?", min_value=0)
    if ingreso:
        estimado = ingreso * 40
        st.write(f"Con un ingreso mensual de ${ingreso}, podrías tener acceso a un crédito aproximado de ${estimado}")

elif menu == "Agendar Cita":
    st.header("Agendar una Cita")
    st.date_input("Selecciona la fecha deseada")
    st.time_input("Selecciona la hora deseada")
    st.text_input("Nombre completo")
    st.text_input("Correo electrónico")
    st.button("Agendar")

elif menu == "Preguntas Frecuentes":
    st.header("Preguntas Frecuentes")
    st.write("1. ¿Cómo obtengo mi crédito INFONAVIT?")
    st.write("2. ¿Qué requisitos necesito?")
    st.write("3. ¿Dónde puedo agendar una cita?")
    st.write("4. ¿Cómo consulto mi saldo?")