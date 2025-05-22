
import streamlit as st
from diccionario_extendido import respuestas_extensas

st.set_page_config(page_title="INFONA - Asistente Inteligente", page_icon="🏠", layout="centered")

# Menú lateral
seccion = st.sidebar.radio("🏛️ Menú de navegación", [
    "🏠 Inicio",
    "💬 Chatea con INFONA",
    "📊 Simulador de Crédito",
    "📅 Agendar Cita",
    "❓ Preguntas Frecuentes"
])

st.title("INFONA - Asistente Inteligente de Vivienda")

if seccion == "🏠 Inicio":
    st.subheader("Bienvenido a INFONA")
    st.write("Consulta, simula y agenda de forma sencilla cualquier trámite relacionado con tu crédito de vivienda.")

elif seccion == "💬 Chatea con INFONA":
    st.subheader("Chatea con INFONA")
    st.write("Escribe tu pregunta sobre créditos, pagos, citas o trámites:")

    user_input = st.text_input("Tu mensaje:")

    if user_input:
        respuesta = "Gracias por tu consulta. Actualmente INFONA responde preguntas relacionadas con tu crédito de vivienda, citas y requisitos."
        for claves, r in respuestas_extensas.items():
            if all(palabra in user_input.lower() for palabra in claves):
                respuesta = r
                break
        st.success(f"INFONA responde:
{respuesta}")

elif seccion == "📊 Simulador de Crédito":
    st.subheader("Simulador de Crédito")
    ingreso = st.number_input("Ingresa tu ingreso mensual (MXN):", min_value=1000, step=500)
    if ingreso:
        estimado = ingreso * 12 * 0.3
        st.write(f"Podrías obtener aproximadamente: ${estimado:,.2f} MXN en crédito.")

elif seccion == "📅 Agendar Cita":
    st.subheader("Agenda tu Cita")
    nombre = st.text_input("Nombre completo")
    correo = st.text_input("Correo electrónico")
    fecha = st.date_input("Selecciona una fecha")
    if st.button("Agendar"):
        st.success("Tu cita ha sido agendada. Recibirás confirmación por correo.")

elif seccion == "❓ Preguntas Frecuentes":
    st.subheader("Preguntas Frecuentes")
    st.markdown("""
    - ¿Cuántos puntos necesito para un crédito?
    - ¿Cómo obtengo mi NSS?
    - ¿Dónde consulto mi saldo?
    - ¿Qué documentos debo llevar a mi cita?
    - ¿Cómo simulo mi crédito?
    """)

# Fin del archivo
