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
    "Bueno": 5,
    "Regular": 3,
    "Malo": 1
}

OPCIONES_CAL = ["Bueno", "Regular", "Malo"]

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

    # ================== ENCABEZADO ==================
    elementos.append(Paragraph("<b>CHECKLIST BÁSICOS DEL SERVICIO</b>", styles["Title"]))
    elementos.append(Spacer(1, 8))
    elementos.append(Paragraph(f"<b>Inspector:</b> {inspector}", styles["Normal"]))
    elementos.append(Paragraph(f"<b>Fecha:</b> {fecha}", styles["Normal"]))
    elementos.append(Spacer(1, 12))

    # ================== RESULTADO ==================
    color_semaforo = (
        colors.green if "VERDE" in semaforo else
        colors.orange if "AMARILLO" in semaforo else
        colors.red
    )

    estilo_resultado = ParagraphStyle(
        name="Resultado",
        parent=styles["Normal"],
        textColor=color_semaforo,
        alignment=1,
        fontSize=10
    )

    elementos.append(Paragraph(f"<b>Promedio General:</b> {promedio}", styles["Normal"]))
    elementos.append(Paragraph(f"<b>Semáforo:</b> {semaforo}", estilo_resultado))
    elementos.append(Spacer(1, 14))

    # ================== ESTILOS ==================
    estilo_normal = ParagraphStyle(
        name="NormalTabla",
        fontSize=8,
        leading=10,
        wordWrap="CJK"
    )

    estilo_seccion = ParagraphStyle(
        name="SeccionTabla",
        fontSize=9,
        leading=11,
        alignment=1,
        backColor=colors.lightgrey,
        wordWrap="CJK"
    )

    def estilo_calificacion(valor):
        return ParagraphStyle(
            name=f"Cal_{valor}",
            parent=estilo_normal,
            alignment=1,
            backColor=(
                colors.red if valor == 1 else
                colors.yellow if valor == 3 else
                None
            )
        )

    # ================== TABLA PRINCIPAL ==================
    data = [[
        Paragraph("<b>SECCIÓN</b>", estilo_normal),
        Paragraph("<b>ITEM</b>", estilo_normal),
        Paragraph("<b>CALIFICACIÓN</b>", estilo_normal),
        Paragraph("<b>OBSERVACIONES</b>", estilo_normal),
    ]]

    ultima_seccion = None

    for f in filas:
        seccion = f["Seccion"]
        tarea = Paragraph(f["Tarea"], estilo_normal)
        cal_valor = f["Calificación"]
        cal = Paragraph(str(cal_valor), estilo_calificacion(cal_valor))
        obs = Paragraph(f["Observaciones"] or "-", estilo_normal)

        if seccion != ultima_seccion:
            data.append([Paragraph(seccion, estilo_seccion), tarea, cal, obs])
            ultima_seccion = seccion
        else:
            data.append(["", tarea, cal, obs])

    tabla = Table(
        data,
        colWidths=[100, 190, 85, 165],
        repeatRows=1
    )

    spans = []
    fila_inicio = 1
    seccion_actual = None

    for i in range(1, len(data)):
        if data[i][0] != "":
            if seccion_actual is not None:
                spans.append(("SPAN", (0, fila_inicio), (0, i - 1)))
            seccion_actual = data[i][0]
            fila_inicio = i

    spans.append(("SPAN", (0, fila_inicio), (0, len(data) - 1)))

    tabla.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),

        ("ALIGN", (0, 1), (0, -1), "CENTER"),
        ("VALIGN", (0, 1), (0, -1), "MIDDLE"),

        ("ALIGN", (2, 1), (2, -1), "CENTER"),
        ("VALIGN", (2, 1), (2, -1), "MIDDLE"),

        ("VALIGN", (1, 1), (-1, -1), "TOP"),
    ] + spans))

    elementos.append(tabla)

    # ================== PUNTOS A MEJORAR (TABLA) ==================
    elementos.append(Spacer(1, 18))
    elementos.append(Paragraph("<b>PUNTOS A MEJORAR</b>", styles["Heading2"]))
    elementos.append(Spacer(1, 8))

    criticos = [f for f in filas if f["Calificación"] in (1, 3)]

    if criticos:
        data_pm = [[
            Paragraph("<b>SECCIÓN</b>", estilo_normal),
            Paragraph("<b>ITEM</b>", estilo_normal),
            Paragraph("<b>CALIFICACIÓN</b>", estilo_normal),
            Paragraph("<b>OBSERVACIONES</b>", estilo_normal),
        ]]

        ultima_seccion = None

        for f in criticos:
            seccion = f["Seccion"]
            tarea = Paragraph(f["Tarea"], estilo_normal)
            cal = Paragraph(str(f["Calificación"]), estilo_calificacion(f["Calificación"]))
            obs = Paragraph(f["Observaciones"] or "-", estilo_normal)

            if seccion != ultima_seccion:
                data_pm.append([Paragraph(seccion, estilo_seccion), tarea, cal, obs])
                ultima_seccion = seccion
            else:
                data_pm.append(["", tarea, cal, obs])

        tabla_pm = Table(
            data_pm,
            colWidths=[100, 190, 85, 165],
            repeatRows=1
        )

        spans_pm = []
        fila_inicio = 1
        seccion_actual = None

        for i in range(1, len(data_pm)):
            if data_pm[i][0] != "":
                if seccion_actual is not None:
                    spans_pm.append(("SPAN", (0, fila_inicio), (0, i - 1)))
                seccion_actual = data_pm[i][0]
                fila_inicio = i

        spans_pm.append(("SPAN", (0, fila_inicio), (0, len(data_pm) - 1)))

        tabla_pm.setStyle(TableStyle([
            ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),

            ("ALIGN", (0, 1), (0, -1), "CENTER"),
            ("VALIGN", (0, 1), (0, -1), "MIDDLE"),

            ("ALIGN", (2, 1), (2, -1), "CENTER"),
            ("VALIGN", (2, 1), (2, -1), "MIDDLE"),

            ("VALIGN", (1, 1), (-1, -1), "TOP"),
        ] + spans_pm))

        elementos.append(tabla_pm)

    else:
        elementos.append(Paragraph("No se registraron puntos críticos.", styles["Normal"]))

    # ================== REGISTRO FOTOGRÁFICO ==================
    elementos.append(Spacer(1, 18))
    elementos.append(Paragraph("<b>REGISTRO FOTOGRÁFICO</b>", styles["Heading2"]))
    elementos.append(Spacer(1, 8))

    for f in filas:
        if f["Foto"]:
            elementos.append(Paragraph(f"{f['Seccion']} - {f['Tarea']}", styles["Normal"]))
            elementos.append(Image(f["Foto"], width=180, height=130))
            elementos.append(Spacer(1, 10))

    # ================== GENERAR PDF ==================
    doc.build(elementos)

# ---------------- FORMULARIO ----------------
with st.form("checklist"):
    c_inspector, c_fecha = st.columns([2, 1])

    with c_inspector:
        inspector = st.text_input("Nombre del inspector")

    with c_fecha:
        fecha_dt = st.datetime_input(
            "Fecha y hora",
            value=datetime.now()
        )

    fecha = fecha_dt.strftime("%Y-%m-%d %H:%M")

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
                cal = st.selectbox("Calificación", OPCIONES_CAL, key=f"cal_{seccion}_{item}")

            with c3:
                obs = st.text_input("Observaciones", key=f"obs_{seccion}_{item}")

            with c4:
                foto = st.file_uploader("Foto", type=["jpg","png"], key=f"foto_{seccion}_{item}")

            if cal == "Seleccione...":
                error = True
                st.error("Seleccione calificación")
                continue

            puntaje = CALIFICACIONES[cal]
            completados += 1

            if puntaje == 3 and not obs.strip():
                error = True
                st.warning("Observación obligatoria cuando es Regular")

            ruta_foto = ""
            if puntaje == 1:
                if not foto:
                    error = True
                    st.warning("Foto obligatoria cuando es Malo")
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

# ---------------- RESULTADO ----------------
if guardar:
    if error or completados < total_items:
        st.error("❌ Checklist incompleto o con errores")
    else:
        promedio = round(total / contador, 2)
        semaforo = "🟢 VERDE" if promedio >= 4 else "🟡 AMARILLO" if promedio >= 3 else "🔴 ROJO"

        pdf_path = f"pdfs/Checklist_{fecha}.pdf"
        generar_pdf(pdf_path, inspector, fecha, filas, promedio, semaforo)

        with open(pdf_path, "rb") as f:
            st.download_button("📄 Descargar PDF", f, file_name="Checklist.pdf")
