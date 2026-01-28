import streamlit as st
from datetime import datetime
import os

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

# ---------------- CONFIGURACIÓN ----------------
st.set_page_config(page_title="Checklist Operativo", layout="wide")
st.title("📋 Checklist Básicos del Servicio")

os.makedirs("fotos", exist_ok=True)
os.makedirs("pdfs", exist_ok=True)

CALIFICACIONES = {
    "Bueno": 5,
    "Regular": 3,
    "Malo": 1
}

CHECKLIST = {

    "PUNTOS DE INFORMACIÓN PISO 1": [
        "Estado y aseo sillas de rueda",
        "Estado y aseo coches de bebé",
        "Estado y aseo mobiliario",
        "Estado herramientas tecnológicas (Computadores, teclado, mouse, impresoras)"
    ],

    "BAÑOS PISO 1": [
        "Aseo espejos",
        "Aseo orinales",
        "Estado dispensador de jabón",
        "Estado secador de manos",
        "Estado papeleras",
        "Papel higiénico en cabinas",
        "Jabón en dispensador",
        "Bolsas en papeleras",
        "Aseo baño familiar",
        "Lavamanos funcionales",
        "Aseo lavamanos",
        "Olor"
    ],

    "PASILLOS PISO 1": [
        "Estado y aseo ingreso",
        "Estado de los pisos",
        "Aseo de los pisos",
        "Ubicación óptima de mobiliario",
        "Estado papeleras",
        "Aseo papeleras",
        "Aseo mobiliario",
        "Estado mobiliario"
    ],

    "PUNTOS DE INFORMACIÓN PISO 2": [
        "Estado y aseo juegos de mesa",
        "Estado y aseo mobiliario",
        "Estado herramientas tecnológicas (Computadores, teclado, mouse, impresoras)"
    ],

    "BAÑOS PISO 2": [
        "Aseo espejos",
        "Aseo orinales",
        "Estado dispensador de jabón",
        "Estado secador de manos",
        "Estado papeleras",
        "Papel higiénico en cabinas",
        "Jabón en dispensador",
        "Bolsas en papeleras",
        "Aseo baño familiar",
        "Lavamanos funcionales",
        "Aseo lavamanos",
        "Olor"
    ],

    "PASILLOS PISO 2": [
        "Estado y aseo ingreso",
        "Estado de los pisos",
        "Aseo de los pisos",
        "Ubicación óptima de mobiliario",
        "Estado papeleras",
        "Aseo papeleras",
        "Aseo mobiliario",
        "Estado mobiliario"
    ],

    "PUNTOS DE INFORMACIÓN PISO 3": [
        "Estado y aseo mobiliario",
        "Estado herramientas tecnológicas (Computadores, teclado, mouse, impresoras)"
    ],

    "BAÑOS PISO 3": [
        "Aseo espejos",
        "Aseo orinales",
        "Estado dispensador de jabón",
        "Estado secador de manos",
        "Estado papeleras",
        "Papel higiénico en cabinas",
        "Jabón en dispensador",
        "Bolsas en papeleras",
        "Aseo baño familiar",
        "Lavamanos funcionales",
        "Aseo lavamanos",
        "Olor"
    ],

    "PASILLOS PISO 3": [
        "Estado de los pisos",
        "Aseo de los pisos",
        "Ubicación óptima de mobiliario",
        "Estado papeleras",
        "Aseo papeleras",
        "Aseo mobiliario",
        "Estado mobiliario"
    ],

    "CENTRALAB PISO 4": [
        "Estado mesas",
        "Estado sillas",
        "Aseo baño",
        "Estado tomas energía",
        "Estado herramientas tecnológicas (Computadores, teclado, mouse, impresoras)"
    ],

    "BAÑOS PISO 4": [
        "Aseo espejos",
        "Aseo orinales",
        "Estado dispensador de jabón",
        "Estado secador de manos",
        "Estado papeleras",
        "Papel higiénico en cabinas",
        "Jabón en dispensador",
        "Bolsas en papeleras",
        "Aseo baño familiar",
        "Lavamanos funcionales",
        "Aseo lavamanos",
        "Olor"
    ],

    "PASILLOS PISO 4": [
        "Estado de los pisos",
        "Aseo de los pisos",
        "Ubicación óptima de mobiliario",
        "Estado papeleras",
        "Aseo papeleras",
        "Aseo mobiliario",
        "Estado mobiliario"
    ],

    "BAÑOS PISO 5": [
        "Aseo espejos",
        "Aseo orinales",
        "Estado dispensador de jabón",
        "Estado secador de manos",
        "Estado papeleras",
        "Papel higiénico en cabinas",
        "Jabón en dispensador",
        "Bolsas en papeleras",
        "Aseo baño familiar",
        "Lavamanos funcionales",
        "Aseo lavamanos",
        "Olor"
    ],

    "PASILLOS PISO 5": [
        "Estado de los pisos",
        "Aseo de los pisos",
        "Ubicación óptima de mobiliario",
        "Estado papeleras",
        "Aseo papeleras",
        "Aseo mobiliario",
        "Estado mobiliario"
    ],

    "ZONA DE COMIDAS PISO 5": [
        "Estado mesas",
        "Estado sillas",
        "Aseo mesas",
        "Aseo sillas",
        "Recepción de bandejas",
        "Papeleras"
    ],

    "CENTRAL DEL BEBÉ PISO 5": [
        "Agua",
        "Aire acondicionado",
        "Microondas",
        "Cambiadero",
        "Aseo",
        "Papeleras",
        "Mobiliario",
        "Toallas de manos",
        "Estado dispensador de jabón",
        "Jabón"
    ],

    "BAÑOS PISO 6": [
        "Aseo espejos",
        "Aseo orinales",
        "Estado dispensador de jabón",
        "Estado secador de manos",
        "Estado papeleras",
        "Papel higiénico en cabinas",
        "Jabón en dispensador",
        "Bolsas en papeleras",
        "Aseo baño familiar",
        "Lavamanos funcionales",
        "Aseo lavamanos",
        "Olor"
    ],
    
    "PASILLOS PISO 6": [
        "Estado de los pisos",
        "Aseo de los pisos",
        "Ubicación óptima de mobiliario",
        "Estado papeleras",
        "Aseo papeleras",
        "Aseo mobiliario",
        "Estado mobiliario"
    ],

    "PARQUEADEROS": [
        "Estado talanqueras",
        "Se evidencia personal de apoyo",
        "Atención personal",
        "Señalética",
        "Aseo en las celdas",
        "Estado máquina pago automático"
    ],

    "SERVICIO AL CLIENTE": [
        "Servicio al cliente de Alpha",
        "Servicio al cliente de Beta",
        "Servicio al cliente de Anfitriones",
        "Conocimiento agenda Alpha",
        "Conocimiento agenda Beta",
        "Conocimiento agenda Anfitriones",
        "Atención de locatarios"
    ]
}

styles = getSampleStyleSheet()

# ---------------- PDF ----------------
def generar_pdf(path, inspector, fecha, filas, promedio, semaforo):
    doc = SimpleDocTemplate(path, pagesize=letter)
    elementos = []

    elementos.append(Paragraph("<b>INFORME CHECKLIST OPERATIVO</b>", styles["Title"]))
    elementos.append(Spacer(1, 12))
    elementos.append(Paragraph(f"Inspector: {inspector}", styles["Normal"]))
    elementos.append(Paragraph(f"Fecha: {fecha}", styles["Normal"]))
    elementos.append(Paragraph(f"Promedio: {promedio}", styles["Normal"]))
    elementos.append(Paragraph(f"Semáforo: {semaforo}", styles["Normal"]))
    elementos.append(Spacer(1, 12))

    data = [["Sección", "Ítem", "Puntaje", "Observaciones"]]
    for f in filas:
        data.append([f["seccion"], f["item"], f["puntaje"], f["obs"]])
        
tabla = Table(data, repeatRows=1)
    tabla.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
        ("GRID", (0,0), (-1,-1), 0.5, colors.grey)
    ]))
    elementos.append(tabla)

    elementos.append(Spacer(1, 12))
    for f in filas:
        if f["foto"]:
            elementos.append(Paragraph(f"<b>{f['item']}</b>", styles["Normal"]))
            elementos.append(Image(f["foto"], 200, 150))
            elementos.append(Spacer(1, 10))

    doc.build(elementos)

# ---------------- FORMULARIO ----------------
with st.form("checklist"):
    inspector = st.text_input("Nombre del inspector")
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")

    filas = []
    total = 0
    contador = 0
    error = False

    for seccion, items in CHECKLIST.items():
        st.subheader(seccion)
        for item in items:
            c1, c2, c3, c4 = st.columns([3,1,3,2])

            with c1:
                st.write(item)
            with c2:
                cal = st.selectbox("Calificación", CALIFICACIONES.keys(), key=f"{seccion}{item}")
            with c3:
                obs = st.text_input("Observaciones", key=f"obs{seccion}{item}")
            with c4:
                foto = st.file_uploader("Foto", type=["jpg","png"], key=f"foto{seccion}{item}")

            puntaje = CALIFICACIONES[cal]
            ruta_foto = ""

            if puntaje == 1 and not foto:
                error = True
                st.warning("⚠️ Foto obligatoria cuando es Malo")

            if foto:
                ruta_foto = f"fotos/{fecha}_{item}.jpg"
                with open(ruta_foto, "wb") as f:
                    f.write(foto.getbuffer())

            filas.append({
                "seccion": seccion,
                "item": item,
                "puntaje": puntaje,
                "obs": obs,
                "foto": ruta_foto
            })

            total += puntaje
            contador += 1

    guardar = st.form_submit_button("💾 Guardar y generar PDF")

# ---------------- RESULTADO ----------------
if guardar and not error:
    promedio = round(total / contador, 2)

    if promedio >= 4:
        semaforo = "🟢 VERDE"
    elif promedio >= 3:
        semaforo = "🟡 AMARILLO"
    else:
        semaforo = "🔴 ROJO"

    st.subheader(f"Resultado: {semaforo}")
    st.write(f"**Promedio:** {promedio}")

    pdf_path = f"pdfs/Checklist_{fecha}.pdf"
    generar_pdf(pdf_path, inspector, fecha, filas, promedio, semaforo)

    with open(pdf_path, "rb") as f:
        st.download_button("📄 Descargar PDF", f, file_name="Checklist.pdf")

if guardar and error:
    st.error("❌ Hay ítems en MAL estado sin foto")
