import streamlit as st
from datetime import datetime
import os
import uuid

from reportlab.platypus import (
    SimpleDocTemplate, Table, TableStyle,
    Paragraph, Spacer, Image
)
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# ---------------- CONFIGURACIÓN ----------------
st.set_page_config(page_title="Checklist Operativo", layout="wide")
st.title("📋 Checklist Básicos del Servicio")

os.makedirs("fotos", exist_ok=True)
os.makedirs("pdfs", exist_ok=True)

CALIFICACIONES = {
    "Seleccione...": None,
    "Bueno": 5,
    "Regular": 3,
    "Malo": 1
}

OPCIONES_CAL = ["Seleccione...", "Bueno", "Regular", "Malo"]

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
def generar_pdf(ruta_pdf, inspector, fecha, filas, promedio, semaforo):

    doc = SimpleDocTemplate(
        ruta_pdf,
        pagesize=letter,
        rightMargin=30,
        leftMargin=30,
        topMargin=30,
        bottomMargin=30
    )

    elementos = []
    styles = getSampleStyleSheet()

    # ---------- Encabezado ----------
    elementos.append(Paragraph("<b>CHECKLIST BÁSICOS DEL SERVICIO</b>", styles["Title"]))
    elementos.append(Spacer(1, 8))
    elementos.append(Paragraph(f"<b>Inspector:</b> {inspector}", styles["Normal"]))
    elementos.append(Paragraph(f"<b>Fecha:</b> {fecha}", styles["Normal"]))
    elementos.append(Spacer(1, 12))

    color_semaforo = colors.green if promedio >= 4 else colors.orange if promedio >= 3 else colors.red

    elementos.append(Paragraph(f"<b>Promedio:</b> {promedio}", styles["Normal"]))
    elementos.append(Paragraph(f"<b>Semáforo:</b> {semaforo}",
        ParagraphStyle("sem", parent=styles["Normal"], textColor=color_semaforo, alignment=1)))
    elementos.append(Spacer(1, 14))

    # ---------- Estilos ----------
    estilo = ParagraphStyle("tabla", fontSize=8, leading=10)
    estilo_sec = ParagraphStyle("sec", fontSize=9, alignment=1, backColor=colors.lightgrey)

    def estilo_cal(v):
        return ParagraphStyle(
            f"cal{v}",
            parent=estilo,
            alignment=1,
            backColor=colors.red if v == 1 else colors.yellow if v == 3 else None
        )

    # ---------- Tabla principal ----------
    data = [[
        Paragraph("<b>SECCIÓN</b>", estilo),
        Paragraph("<b>ITEM</b>", estilo),
        Paragraph("<b>CALIFICACIÓN</b>", estilo),
        Paragraph("<b>OBSERVACIONES</b>", estilo),
    ]]

    ultima = None
    for f in filas:
        fila = [
            Paragraph(f["Seccion"], estilo_sec) if f["Seccion"] != ultima else "",
            Paragraph(f["Tarea"], estilo),
            Paragraph(str(f["Calificación"]), estilo_cal(f["Calificación"])),
            Paragraph(f["Observaciones"] or "-", estilo)
        ]
        data.append(fila)
        ultima = f["Seccion"]

    tabla = Table(data, colWidths=[95, 185, 85, 165], repeatRows=1)

    spans = []
    inicio = 1
    for i in range(1, len(data)):
        if data[i][0] != "":
            spans.append(("SPAN", (0, inicio), (0, i - 1)))
            inicio = i
    spans.append(("SPAN", (0, inicio), (0, len(data) - 1)))

    tabla.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 0.5, colors.black),
        ("ALIGN", (2,1), (2,-1), "CENTER"),
        ("VALIGN", (0,1), (0,-1), "MIDDLE"),
    ] + spans))

    elementos.append(tabla)

    # ---------- Puntos a mejorar ----------
    elementos.append(Spacer(1, 16))
    elementos.append(Paragraph("<b>PUNTOS A MEJORAR</b>", styles["Heading2"]))
    elementos.append(Spacer(1, 8))

    criticos = [f for f in filas if f["Calificación"] in (1,3)]

    if criticos:
        data_pm = [[
            Paragraph("<b>SECCIÓN</b>", estilo),
            Paragraph("<b>ITEM</b>", estilo),
            Paragraph("<b>CALIFICACIÓN</b>", estilo),
            Paragraph("<b>OBSERVACIÓN</b>", estilo),
        ]]

        ultima = None
        for f in criticos:
            fila = [
                Paragraph(f["Seccion"], estilo_sec) if f["Seccion"] != ultima else "",
                Paragraph(f["Tarea"], estilo),
                Paragraph(str(f["Calificación"]), estilo_cal(f["Calificación"])),
                Paragraph(f["Observaciones"] or "-", estilo)
            ]
            data_pm.append(fila)
            ultima = f["Seccion"]

        tabla_pm = Table(data_pm, colWidths=[95,185,85,165], repeatRows=1)

        spans_pm = []
        inicio = 1
        for i in range(1, len(data_pm)):
            if data_pm[i][0] != "":
                spans_pm.append(("SPAN", (0,inicio), (0,i-1)))
                inicio = i
        spans_pm.append(("SPAN", (0,inicio), (0,len(data_pm)-1)))

        tabla_pm.setStyle(TableStyle([
            ("GRID", (0,0), (-1,-1), 0.5, colors.black),
            ("ALIGN", (2,1), (2,-1), "CENTER"),
            ("VALIGN", (0,1), (0,-1), "MIDDLE"),
        ] + spans_pm))

        elementos.append(tabla_pm)
    else:
        elementos.append(Paragraph("No se registraron puntos críticos.", styles["Normal"]))

    # ---------- Fotos ----------
    elementos.append(Spacer(1, 16))
    elementos.append(Paragraph("<b>REGISTRO FOTOGRÁFICO</b>", styles["Heading2"]))
    elementos.append(Spacer(1, 8))

    for f in filas:
        if f["Foto"]:
            elementos.append(Paragraph(f"{f['Seccion']} - {f['Tarea']}", styles["Normal"]))
            elementos.append(Image(f["Foto"], width=180, height=130))
            elementos.append(Spacer(1, 10))

    doc.build(elementos)

# ================= FORMULARIO =================
with st.form("checklist"):
    inspector = st.text_input("Nombre del inspector")
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")

    filas = []
    total = 0
    contador = 0
    error = False

    total_items = sum(len(v) for v in CHECKLIST.values())
    completados = 0

    for seccion, items in CHECKLIST.items():
        st.subheader(seccion)

        for item in items:
            c1, c2, c3, c4 = st.columns([3,1,3,2])

            with c1:
                st.write(item)
            with c2:
                cal = st.selectbox("Calificación", OPCIONES_CAL, key=f"{seccion}_{item}")
            with c3:
                obs = st.text_input("Observaciones", key=f"obs_{seccion}_{item}")
            with c4:
                foto = st.file_uploader("Foto", type=["jpg","png"], key=f"foto_{seccion}_{item}")

            if cal == "Seleccione...":
                error = True
                continue

            puntaje = CALIFICACIONES[cal]
            completados += 1

            if puntaje == 3 and not obs.strip():
                error = True

            ruta_foto = ""
            if puntaje == 1:
                if not foto:
                    error = True
                else:
                    nombre = uuid.uuid4().hex
                    ruta_foto = f"fotos/{fecha}_{nombre}.jpg"
                    with open(ruta_foto, "wb") as f:
                        f.write(foto.getbuffer())

            filas.append({
                "Seccion": seccion,
                "Tarea": item,
                "Calificación": puntaje,
                "Observaciones": obs,
                "Foto": ruta_foto
            })

            total += puntaje
            contador += 1

    st.progress(completados / total_items)
    guardar = st.form_submit_button("💾 Guardar y generar PDF")

# ================= RESULTADO =================
if guardar:
    if error or completados < total_items:
        st.error("❌ Checklist incompleto o con errores")
    else:
        promedio = round(total / contador, 2)
        semaforo = "🟢 VERDE" if promedio >= 4 else "🟡 AMARILLO" if promedio >= 3 else "🔴 ROJO"

        pdf_path = f"pdfs/Checklist_{fecha.replace(':','-')}.pdf"
        generar_pdf(pdf_path, inspector, fecha, filas, promedio, semaforo)

        with open(pdf_path, "rb") as f:
            st.download_button("📄 Descargar PDF", f, file_name="Checklist.pdf")
