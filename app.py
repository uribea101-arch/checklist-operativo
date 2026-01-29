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

    # ===== ENCABEZADO =====
    elementos.append(Paragraph("<b>CHECKLIST BÁSICOS DEL SERVICIO</b>", styles["Title"]))
    elementos.append(Spacer(1, 8))
    elementos.append(Paragraph(f"<b>Inspector:</b> {inspector}", styles["Normal"]))
    elementos.append(Paragraph(f"<b>Fecha:</b> {fecha}", styles["Normal"]))
    elementos.append(Spacer(1, 12))

    # ===== RESULTADO =====
    color_semaforo = colors.green if promedio >= 4 else colors.orange if promedio >= 3 else colors.red

    elementos.append(Paragraph(f"<b>Promedio General:</b> {promedio}", styles["Normal"]))
    elementos.append(
        Paragraph(
            f"<b>Semáforo:</b> {semaforo}",
            ParagraphStyle("res", textColor=color_semaforo, alignment=1)
        )
    )
    elementos.append(Spacer(1, 14))

    # ===== ESTILOS =====
    estilo_normal = ParagraphStyle("normal", fontSize=8, leading=10)
    estilo_seccion = ParagraphStyle("seccion", fontSize=9, alignment=1, backColor=colors.lightgrey)

    def estilo_cal(valor):
        return ParagraphStyle(
            f"cal_{valor}",
            alignment=1,
            backColor=colors.red if valor == 1 else colors.yellow if valor == 3 else None
        )

    # ===== TABLA PRINCIPAL =====
    data = [[
        Paragraph("<b>SECCIÓN</b>", estilo_normal),
        Paragraph("<b>ITEM</b>", estilo_normal),
        Paragraph("<b>CALIFICACIÓN</b>", estilo_normal),
        Paragraph("<b>OBSERVACIONES</b>", estilo_normal),
    ]]

    ultima = None
    inicio = 1

    for f in filas:
        sec = f["Seccion"]
        fila = [
            Paragraph(sec, estilo_seccion) if sec != ultima else "",
            Paragraph(f["Tarea"], estilo_normal),
            Paragraph(str(f["Calificación"]), estilo_cal(f["Calificación"])),
            Paragraph(f["Observaciones"], estilo_normal)
        ]
        data.append(fila)
        ultima = sec

    tabla = Table(data, colWidths=[110, 200, 90, 160], repeatRows=1)

    spans = []
    start = 1
    for i in range(1, len(data)):
        if data[i][0] != "":
            spans.append(("SPAN", (0, start), (0, i - 1)))
            start = i
    spans.append(("SPAN", (0, start), (0, len(data) - 1)))

    tabla.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 0.5, colors.black),
        ("ALIGN", (2,1), (2,-1), "CENTER"),
        ("VALIGN", (0,1), (0,-1), "MIDDLE"),
    ] + spans))

    elementos.append(tabla)

    # ===== PUNTOS A MEJORAR (TABLA) =====
    elementos.append(Spacer(1, 16))
    elementos.append(Paragraph("<b>PUNTOS A MEJORAR</b>", styles["Heading2"]))
    elementos.append(Spacer(1, 8))

    criticos = [f for f in filas if f["Calificación"] in (1, 3)]

    if criticos:
        data2 = [[
            "SECCIÓN", "ITEM", "CALIFICACIÓN"
        ]]

        ultima = None
        for f in criticos:
            data2.append([
                f["Seccion"] if f["Seccion"] != ultima else "",
                f["Tarea"],
                f["Calificación"]
            ])
            ultima = f["Seccion"]

        tabla2 = Table(data2, colWidths=[150, 260, 90], repeatRows=1)
        tabla2.setStyle(TableStyle([
            ("GRID", (0,0), (-1,-1), 0.5, colors.black),
            ("ALIGN", (2,1), (2,-1), "CENTER"),
        ]))
        elementos.append(tabla2)
    else:
        elementos.append(Paragraph("No se registraron puntos críticos.", styles["Normal"]))

    doc.build(elementos)


# ---------------- FORMULARIO ----------------
hora_cliente = st_javascript("new Date().toLocaleString()")
fecha = hora_cliente if hora_cliente else datetime.now().strftime("%Y-%m-%d %H:%M")

total_items = sum(len(v) for v in CHECKLIST.values())

with st.form("checklist"):

    inspector = st.text_input("Nombre del inspector")

    progreso = st.progress(0)
    texto_prog = st.empty()

    filas = []
    completados = 0
    total = 0
    error = False

    for seccion, items in CHECKLIST.items():
        st.subheader(seccion)

        for item in items:
            c1, c2, c3, c4 = st.columns([3,1,3,2])

            with c1:
                st.write(item)

            with c2:
                cal_txt = st.selectbox(
                    "Calificación",
                    CALIFICACIONES.keys(),
                    key=f"{seccion}_{item}"
                )

            with c3:
                obs = st.text_input("Observaciones", key=f"obs_{seccion}_{item}")

            with c4:
                foto = st.file_uploader("Foto", type=["jpg","png"], key=f"foto_{seccion}_{item}")

            if CALIFICACIONES[cal_txt] is None:
                error = True
                st.warning("⚠️ Debe seleccionar calificación")
                continue

            puntaje = CALIFICACIONES[cal_txt]

            if puntaje == 3 and not obs:
                error = True
                st.warning("⚠️ Observación obligatoria cuando es Regular")

            if puntaje == 1 and not foto:
                error = True
                st.warning("⚠️ Foto obligatoria cuando es Malo")

            ruta_foto = ""
            if foto:
                ruta_foto = f"fotos/{uuid.uuid4().hex}.jpg"
                with open(ruta_foto, "wb") as f:
                    f.write(foto.getbuffer())

            filas.append({
                "Seccion": seccion,
                "Tarea": item,
                "Calificación": puntaje,
                "Observaciones": obs,
                "Foto": ruta_foto
            })

            completados += 1
            total += puntaje

            porcentaje = int((completados / total_items) * 100)
            progreso.progress(porcentaje)
            texto_prog.markdown(f"**Progreso:** {porcentaje}%")

    guardar = st.form_submit_button(
        "💾 Guardar y generar PDF",
        disabled=(completados < total_items or error)
    )


# ---------------- RESULTADO ----------------
if guardar and not error:
    promedio = round(total / completados, 2)
    semaforo = "🟢 VERDE" if promedio >= 4 else "🟡 AMARILLO" if promedio >= 3 else "🔴 ROJO"

    st.subheader("🚦 Resultado final")
    st.success(semaforo)

    pdf_path = f"pdfs/Checklist_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    generar_pdf(pdf_path, inspector, fecha, filas, promedio, semaforo)

    with open(pdf_path, "rb") as f:
        st.download_button("📄 Descargar PDF", f, file_name="Checklist.pdf")
