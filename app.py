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
def generar_pdf(ruta_pdf, inspector, fecha, filas):
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib import colors

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(
        ruta_pdf,
        pagesize=letter,
        rightMargin=30,
        leftMargin=30,
        topMargin=30,
        bottomMargin=30
    )

    elementos = []

    # -------- TÍTULO --------
    elementos.append(Paragraph("<b>INFORME CHECKLIST OPERATIVO</b>", styles["Title"]))
    elementos.append(Spacer(1, 12))

    elementos.append(Paragraph(f"<b>Inspector:</b> {inspector}", styles["Normal"]))
    elementos.append(Paragraph(f"<b>Fecha:</b> {fecha}", styles["Normal"]))
    elementos.append(Spacer(1, 12))

    # -------- ESTILOS TABLA --------
    estilo_normal = ParagraphStyle(
        name="NormalTabla",
        fontSize=8,
        leading=10
    )

    estilo_seccion = ParagraphStyle(
        name="SeccionTabla",
        fontSize=8,
        leading=10,
        alignment=1  # Centrado
    )

    # -------- CABECERA TABLA --------
    data = [
        [
            Paragraph("<b>SECCION</b>", estilo_normal),
            Paragraph("<b>ITEM</b>", estilo_normal),
            Paragraph("<b>CALIFICACIÓN</b>", estilo_normal),
            Paragraph("<b>OBSERVACIONES</b>", estilo_normal),
        ]
    ]

    ultima_seccion = None
    inicio_merge = 1

    # -------- FILAS --------
    for f in filas:
        seccion = f["Seccion"]
        item = Paragraph(f["Tarea"], estilo_normal)
        cal = Paragraph(str(f["Calificación"]), estilo_normal)
        obs = Paragraph(f["Observaciones"] or "-", estilo_normal)

        if seccion != ultima_seccion:
            if ultima_seccion is not None:
                data_span_fin = len(data) - 1
                tabla_temp = Table(data)
                tabla_temp.setStyle(TableStyle([
                    ("SPAN", (0, inicio_merge), (0, data_span_fin))
                ]))
                inicio_merge = len(data)

            data.append([
                Paragraph(seccion, estilo_seccion),
                item,
                cal,
                obs
            ])
            ultima_seccion = seccion
        else:
            data.append([
                "",
                item,
                cal,
                obs
            ])

    # -------- TABLA FINAL --------
    tabla = Table(
        data,
        colWidths=[90, 180, 70, 180],
        repeatRows=1
    )

    tabla.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 0.5, colors.black),
        ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("ALIGN", (2,1), (2,-1), "CENTER"),
    ]))

    # Combinar última sección
    tabla.setStyle(TableStyle([
        ("SPAN", (0, inicio_merge), (0, len(data)-1))
    ]))

    elementos.append(tabla)

    # -------- FOTOS --------
    elementos.append(Spacer(1, 12))
    elementos.append(Paragraph("<b>REGISTRO FOTOGRÁFICO</b>", styles["Heading2"]))
    elementos.append(Spacer(1, 8))

    for f in filas:
        if f["Foto"]:
            elementos.append(Paragraph(f["Seccion"] + " - " + f["Tarea"], styles["Normal"]))
            elementos.append(Image(f["Foto"], width=180, height=130))
            elementos.append(Spacer(1, 10))

    # -------- GENERAR PDF --------
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
    generar_pdf(pdf_path, inspector, fecha, filas)

    with open(pdf_path, "rb") as f:
        st.download_button("📄 Descargar PDF", f, file_name="Checklist.pdf")

if guardar and error:
    st.error("❌ Hay ítems en MAL estado sin foto")
