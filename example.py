import streamlit as st

# ==========================
# st.title()
# Muestra el título principal de la página
# ==========================

# Ejemplo básico
st.title("Este es un título")

# -----------------------------------
# body
# Texto que se mostrará como título
# Acepta Markdown
# -----------------------------------
st.title("Curso de *Streamlit* para Principiantes")

# -----------------------------------
# anchor
# Crea un identificador para acceder
# al título mediante una URL
# -----------------------------------
st.title(
    "Sección Principal",
    anchor="inicio"
)

# URL de ejemplo:
# http://localhost:8501/#inicio

# -----------------------------------
# anchor=False
# Oculta el ancla del título
# -----------------------------------
st.title(
    "Título sin ancla",
    anchor=False
)

# -----------------------------------
# help
# Muestra una ayuda emergente (tooltip)
# cuando el usuario pasa el mouse
# sobre el icono de ayuda
# -----------------------------------
st.title(
    "Título con Ayuda",
    help="Este título identifica la página principal."
)

# -----------------------------------
# width="stretch"
# Ocupa todo el ancho disponible
# (valor por defecto)
# -----------------------------------
st.title(
    "Título ancho completo",
    width="stretch"
)

# -----------------------------------
# width="content"
# El ancho se ajusta al contenido
# -----------------------------------
st.title(
    "Título Ajustado",
    width="content"
)

# -----------------------------------
# width=500
# Define un ancho fijo en píxeles
# -----------------------------------
st.title(
    "Título de 500px",
    width=500
)

# -----------------------------------
# text_alignment="left"
# Alinea el texto a la izquierda
# (valor por defecto)
# -----------------------------------
st.title(
    "Alineado a la Izquierda",
    text_alignment="left"
)

# -----------------------------------
# text_alignment="center"
# Centra el texto
# -----------------------------------
st.title(
    "Título Centrado",
    text_alignment="center"
)

# -----------------------------------
# text_alignment="right"
# Alinea el texto a la derecha
# -----------------------------------
st.title(
    "Título a la Derecha",
    text_alignment="right"
)

# -----------------------------------
# text_alignment="justify"
# Justifica el texto
# -----------------------------------
st.title(
    "Título Justificado",
    text_alignment="justify"
)







# ==========================
# st.header()
# Muestra un encabezado para
# organizar secciones dentro
# de la aplicación
# ==========================

# Ejemplo básico
st.header("Este es un encabezado")

# -----------------------------------
# body
# Texto que se mostrará como encabezado
# Acepta Markdown
# -----------------------------------
st.header("Curso de *Streamlit*")

# -----------------------------------
# anchor
# Crea un identificador para acceder
# al encabezado mediante una URL
# -----------------------------------
st.header(
    "Sección de Usuarios",
    anchor="usuarios"
)

# URL de ejemplo:
# http://localhost:8501/#usuarios

# -----------------------------------
# anchor=False
# Oculta el ancla del encabezado
# -----------------------------------
st.header(
    "Encabezado sin ancla",
    anchor=False
)

# -----------------------------------
# help
# Muestra una ayuda emergente (tooltip)
# al pasar el mouse sobre el icono
# -----------------------------------
st.header(
    "Gestión de Clientes",
    help="Esta sección permite administrar clientes."
)

# -----------------------------------
# divider=True
# Agrega una línea divisoria automática
# debajo del encabezado
# -----------------------------------
st.header(
    "Productos",
    divider=True
)

# -----------------------------------
# divider con color específico
# Colores disponibles:
# blue, green, orange, red,
# violet, yellow, gray, rainbow
# -----------------------------------
st.header(
    "Ventas",
    divider="blue"
)

st.header(
    "Reportes",
    divider="green"
)

st.header(
    "Configuración",
    divider="rainbow"
)

# -----------------------------------
# width="stretch"
# Ocupa todo el ancho disponible
# (valor por defecto)
# -----------------------------------
st.header(
    "Encabezado ancho completo",
    width="stretch"
)

# -----------------------------------
# width="content"
# Ajusta el ancho al contenido
# -----------------------------------
st.header(
    "Encabezado Ajustado",
    width="content"
)

# -----------------------------------
# width=500
# Define un ancho fijo en píxeles
# -----------------------------------
st.header(
    "Encabezado de 500px",
    width=500
)

# -----------------------------------
# text_alignment="left"
# Alinea el texto a la izquierda
# (valor por defecto)
# -----------------------------------
st.header(
    "Alineado a la Izquierda",
    text_alignment="left"
)

# -----------------------------------
# text_alignment="center"
# Centra el texto
# -----------------------------------
st.header(
    "Encabezado Centrado",
    text_alignment="center"
)

# -----------------------------------
# text_alignment="right"
# Alinea el texto a la derecha
# -----------------------------------
st.header(
    "Encabezado a la Derecha",
    text_alignment="right"
)

# -----------------------------------
# text_alignment="justify"
# Justifica el texto
# -----------------------------------
st.header(
    "Encabezado Justificado",
    text_alignment="justify"
)













# ==========================
# st.caption()
# Muestra texto pequeño para
# descripciones, notas o ayudas
# adicionales dentro de la aplicación
# ==========================

# Ejemplo básico
st.caption("Este es un título pequeño")

# -----------------------------------
# body
# Texto que se mostrará como caption
# Acepta Markdown
# -----------------------------------
st.caption(
    "Esta aplicación permite calcular el factorial de un número."
)

# Markdown permitido
st.caption(
    "Texto con *cursiva*, **negrita**, emojis :rocket: y :blue[colores]"
)

# -----------------------------------
# unsafe_allow_html=False
# (valor por defecto)
# Las etiquetas HTML se muestran
# como texto normal
# -----------------------------------
st.caption(
    "<b>Texto en negrita</b>",
    unsafe_allow_html=False
)

# Resultado:
# <b>Texto en negrita</b>

# -----------------------------------
# unsafe_allow_html=True
# Permite interpretar etiquetas HTML
# dentro del texto
# -----------------------------------
st.caption(
    "<b>Texto en negrita</b>",
    unsafe_allow_html=True
)

# Nota:
# Usar HTML puede afectar la seguridad
# y el diseño de la aplicación.

# -----------------------------------
# help
# Muestra una ayuda emergente
# al pasar el mouse sobre el icono
# -----------------------------------
st.caption(
    "Información adicional",
    help="Este texto proporciona detalles extra para el usuario."
)

# -----------------------------------
# width="stretch"
# Ocupa todo el ancho disponible
# (valor por defecto)
# -----------------------------------
st.caption(
    "Caption ancho completo",
    width="stretch"
)

# -----------------------------------
# width="content"
# Ajusta el ancho al contenido
# -----------------------------------
st.caption(
    "Caption Ajustado",
    width="content"
)

# -----------------------------------
# width=400
# Define un ancho fijo en píxeles
# -----------------------------------
st.caption(
    "Caption de 400px",
    width=400
)

# -----------------------------------
# text_alignment="left"
# Alinea el texto a la izquierda
# (valor por defecto)
# -----------------------------------
st.caption(
    "Texto alineado a la izquierda",
    text_alignment="left"
)

# -----------------------------------
# text_alignment="center"
# Centra el texto
# -----------------------------------
st.caption(
    "Texto centrado",
    text_alignment="center"
)

# -----------------------------------
# text_alignment="right"
# Alinea el texto a la derecha
# -----------------------------------
st.caption(
    "Texto alineado a la derecha",
    text_alignment="right"
)

# -----------------------------------
# text_alignment="justify"
# Justifica el texto
# -----------------------------------
st.caption(
    "Texto justificado",
    text_alignment="justify"
)






# ==========================================
# INPUTS DE STREAMLIT
# Ejemplos para estudiantes
# ==========================================

# ------------------------------------------
# st.text_input()
# Permite ingresar texto en una sola línea
# ------------------------------------------
nombre = st.text_input(
    "Ingrese su nombre",
    value="",
    placeholder="Escriba aquí..."
)

# ------------------------------------------
# st.text_area()
# Permite ingresar texto en múltiples líneas
# ------------------------------------------
descripcion = st.text_area(
    "Descripción",
    height=150
)

# ------------------------------------------
# st.number_input()
# Permite ingresar números
# ------------------------------------------
edad = st.number_input(
    "Edad",
    min_value=0,
    max_value=120,
    value=18,
    step=1
)

# ------------------------------------------
# st.slider()
# Permite seleccionar un valor mediante
# una barra deslizante
# ------------------------------------------
calificacion = st.slider(
    "Calificación",
    min_value=0,
    max_value=100,
    value=50
)

# ------------------------------------------
# st.select_slider()
# Slider con opciones personalizadas
# ------------------------------------------
nivel = st.select_slider(
    "Nivel",
    options=["Básico", "Intermedio", "Avanzado"]
)

# ------------------------------------------
# st.checkbox()
# Casilla de verificación
# ------------------------------------------
acepta = st.checkbox(
    "Acepto los términos y condiciones"
)

# ------------------------------------------
# st.radio()
# Permite seleccionar una única opción
# ------------------------------------------
genero = st.radio(
    "Seleccione su género",
    ["Masculino", "Femenino", "Otro"]
)

# ------------------------------------------
# st.selectbox()
# Lista desplegable de selección única
# ------------------------------------------
pais = st.selectbox(
    "Seleccione un país",
    ["Bolivia", "Perú", "Chile", "Argentina"]
)

# ------------------------------------------
# st.multiselect()
# Permite seleccionar varias opciones
# ------------------------------------------
lenguajes = st.multiselect(
    "Lenguajes favoritos",
    ["Python", "C#", "Java", "JavaScript", "Go"]
)

# ------------------------------------------
# st.toggle()
# Interruptor ON/OFF
# ------------------------------------------
modo_oscuro = st.toggle(
    "Activar modo oscuro"
)

# ------------------------------------------
# st.date_input()
# Permite seleccionar una fecha
# ------------------------------------------
fecha = st.date_input(
    "Seleccione una fecha"
)

# ------------------------------------------
# st.time_input()
# Permite seleccionar una hora
# ------------------------------------------
hora = st.time_input(
    "Seleccione una hora"
)

# ------------------------------------------
# st.color_picker()
# Permite seleccionar un color
# ------------------------------------------
color = st.color_picker(
    "Seleccione un color",
    "#0000FF"
)

# ------------------------------------------
# st.file_uploader()
# Permite subir archivos
# ------------------------------------------
archivo = st.file_uploader(
    "Suba un archivo",
    type=["pdf", "txt", "png", "jpg"]
)

# ------------------------------------------
# st.camera_input()
# Permite capturar una foto desde la cámara
# ------------------------------------------
foto = st.camera_input(
    "Tomar fotografía"
)

# ------------------------------------------
# st.button()
# Ejecuta una acción al hacer clic
# ------------------------------------------
btn_guardar = st.button(
    "Guardar"
)

# ------------------------------------------
# st.download_button()
# Permite descargar contenido generado
# ------------------------------------------
st.download_button(
    "Descargar Archivo",
    data="Hola Mundo",
    file_name="archivo.txt"
)

# ------------------------------------------
# st.form()
# Agrupa varios controles en un formulario
# ------------------------------------------
with st.form("frmUsuario"):

    usuario = st.text_input("Usuario")
    correo = st.text_input("Correo")

    enviar = st.form_submit_button(
        "Enviar"
    )

# ------------------------------------------
# st.chat_input()
# Entrada de texto para aplicaciones tipo chat
# ------------------------------------------
mensaje = st.chat_input(
    "Escriba un mensaje..."
)




# ==========================
# st.button()
# Crea un botón que permite ejecutar
# una acción cuando el usuario hace clic.
# ==========================

# -----------------------------------
# Ejemplo básico
# label: texto que se mostrará
# dentro del botón.
# key: identificador único del botón.
# -----------------------------------
st.button(
    "Guardar",
    key="btn_basico"
)

# -----------------------------------
# label
# Es el texto visible que aparece
# dentro del botón.
# -----------------------------------
st.button(
    "Registrar Usuario",
    key="btn_registrar"
)

# -----------------------------------
# key
# Identificador único del componente.
# Se recomienda utilizarlo siempre
# para evitar errores de elementos
# duplicados.
# -----------------------------------
st.button(
    "Guardar",
    key="btn_guardar"
)

# -----------------------------------
# help
# Muestra un mensaje de ayuda cuando
# el usuario pasa el mouse sobre el
# icono de información del botón.
# -----------------------------------
st.button(
    "Eliminar",
    key="btn_eliminar",
    help="Elimina el registro seleccionado."
)

# -----------------------------------
# type="secondary"
# Estilo secundario del botón.
# Es el valor por defecto.
# Se utiliza para acciones menos
# importantes.
# -----------------------------------
st.button(
    "Cancelar",
    key="btn_cancelar",
    type="secondary"
)

# -----------------------------------
# type="primary"
# Resalta visualmente el botón.
# Se utiliza para la acción principal
# de una pantalla o formulario.
# -----------------------------------
st.button(
    "Guardar Cambios",
    key="btn_guardar_cambios",
    type="primary"
)

# -----------------------------------
# icon
# Permite agregar un icono o emoji
# dentro del botón.
# -----------------------------------
st.button(
    "Buscar",
    key="btn_buscar",
    icon="🔍"
)

# -----------------------------------
# icon con Material Icons
# Streamlit también permite utilizar
# iconos de Material Design.
# -----------------------------------
st.button(
    "Configuración",
    key="btn_configuracion",
    icon=":material/settings:"
)

# -----------------------------------
# disabled=True
# Deshabilita el botón para impedir
# que el usuario pueda presionarlo.
# Útil durante procesos de carga.
# -----------------------------------
st.button(
    "Procesando...",
    key="btn_procesando",
    disabled=True
)

# -----------------------------------
# use_container_width=True
# Hace que el botón ocupe todo el
# ancho disponible del contenedor.
# -----------------------------------
st.button(
    "Botón Ancho Completo",
    key="btn_ancho",
    use_container_width=True
)

# -----------------------------------
# width="content"
# Ajusta el ancho del botón según
# el tamaño de su contenido.
# -----------------------------------
st.button(
    "Pequeño",
    key="btn_pequeno",
    width="content"
)

# -----------------------------------
# width="stretch"
# Hace que el botón se expanda y
# ocupe todo el ancho disponible.
# -----------------------------------
st.button(
    "Ancho Completo",
    key="btn_stretch",
    width="stretch"
)

# -----------------------------------
# width=300
# Define un ancho fijo en píxeles.
# -----------------------------------
st.button(
    "Botón de 300px",
    key="btn_300",
    width=300
)

# -----------------------------------
# Ejemplo práctico
# Cuando el usuario hace clic,
# st.button() devuelve True.
# -----------------------------------
if st.button(
    "Calcular",
    key="btn_calcular",
    type="primary",
    icon="🧮",
    help="Ejecuta el cálculo"
):
    st.success("Cálculo realizado correctamente.")



# ==========================
# st.radio()
# Crea un grupo de opciones
# donde el usuario puede
# seleccionar únicamente una.
# ==========================

# -----------------------------------
# Ejemplo básico
# label: texto que describe
# la selección.
# options: lista de opciones
# disponibles.
# -----------------------------------
st.radio(
    "Seleccione una opción",
    options=["A", "B", "C"],
    key="radio_basico"
)

# -----------------------------------
# label
# Es el texto visible que aparece
# encima del grupo de opciones.
# -----------------------------------
st.radio(
    "Seleccione su género",
    options=["Masculino", "Femenino", "Otro"],
    key="radio_genero"
)

# -----------------------------------
# options
# Lista de valores que el usuario
# podrá seleccionar.
# -----------------------------------
st.radio(
    "Seleccione un lenguaje",
    options=["Python", "Java", "C#"],
    key="radio_lenguaje"
)

# -----------------------------------
# key
# Identificador único del componente.
# Se recomienda utilizarlo siempre
# para evitar conflictos.
# -----------------------------------
st.radio(
    "Seleccione una opción",
    options=["A", "B", "C"],
    key="radio_key"
)

# -----------------------------------
# help
# Muestra un mensaje de ayuda cuando
# el usuario pasa el mouse sobre el
# icono de información.
# -----------------------------------
st.radio(
    "Seleccione una prioridad",
    options=["Alta", "Media", "Baja"],
    key="radio_prioridad",
    help="Indica el nivel de prioridad."
)

# -----------------------------------
# index
# Define la opción seleccionada
# por defecto.
# El índice comienza en 0.
# -----------------------------------
st.radio(
    "Seleccione una letra",
    options=["A", "B", "C"],
    index=1,
    key="radio_index"
)

# -----------------------------------
# horizontal=True
# Muestra las opciones de manera
# horizontal en una sola fila.
# -----------------------------------
st.radio(
    "Seleccione una opción",
    options=["A", "B", "C"],
    horizontal=True,
    key="radio_horizontal"
)

# -----------------------------------
# horizontal=False
# Muestra las opciones de forma
# vertical (valor por defecto).
# -----------------------------------
st.radio(
    "Seleccione una opción",
    options=["A", "B", "C"],
    horizontal=False,
    key="radio_vertical"
)

# -----------------------------------
# captions
# Permite mostrar descripciones
# debajo de cada opción.
# -----------------------------------
st.radio(
    "Seleccione un plan",
    options=["Básico", "Pro", "Premium"],
    captions=[
        "Funciones esenciales",
        "Más herramientas",
        "Acceso completo"
    ],
    key="radio_captions"
)

# -----------------------------------
# disabled=True
# Deshabilita el componente para
# impedir que el usuario cambie
# la selección.
# -----------------------------------
st.radio(
    "Estado",
    options=["Activo", "Inactivo"],
    disabled=True,
    key="radio_disabled"
)

# -----------------------------------
# label_visibility="visible"
# Muestra la etiqueta.
# -----------------------------------
st.radio(
    "Opción visible",
    options=["A", "B", "C"],
    label_visibility="visible",
    key="radio_visible"
)

# -----------------------------------
# label_visibility="hidden"
# Oculta la etiqueta pero conserva
# el espacio ocupado.
# -----------------------------------
st.radio(
    "Opción oculta",
    options=["A", "B", "C"],
    label_visibility="hidden",
    key="radio_hidden"
)

# -----------------------------------
# label_visibility="collapsed"
# Oculta completamente la etiqueta
# y elimina el espacio.
# -----------------------------------
st.radio(
    "Opción colapsada",
    options=["A", "B", "C"],
    label_visibility="collapsed",
    key="radio_collapsed"
)

# -----------------------------------
# width="content"
# Ajusta el ancho al contenido.
# -----------------------------------
st.radio(
    "Seleccione una opción",
    options=["A", "B", "C"],
    width="content",
    key="radio_content"
)

# -----------------------------------
# width="stretch"
# Ocupa todo el ancho disponible.
# -----------------------------------
st.radio(
    "Seleccione una opción",
    options=["A", "B", "C"],
    width="stretch",
    key="radio_stretch"
)

# -----------------------------------
# Ejemplo práctico
# st.radio() devuelve el valor
# seleccionado por el usuario.
# -----------------------------------
operacion = st.radio(
    "Seleccione una operación",
    options=["Sumar", "Restar", "Multiplicar"],
    key="radio_operacion",
    horizontal=True,
    help="Seleccione la operación matemática"
)

st.success(f"Operación seleccionada: {operacion}")







# ==========================
# st.checkbox()
# Crea una casilla de
# verificación que permite
# activar o desactivar una
# opción.
# ==========================

# -----------------------------------
# Ejemplo básico
# label: texto que aparece junto
# a la casilla.
# -----------------------------------
st.checkbox(
    "Acepto los términos y condiciones",
    key="chk_basico"
)

# -----------------------------------
# label
# Es el texto visible que describe
# la opción del checkbox.
# -----------------------------------
st.checkbox(
    "Recibir notificaciones por correo",
    key="chk_notificaciones"
)

# -----------------------------------
# key
# Identificador único del componente.
# Se recomienda utilizarlo siempre
# para evitar conflictos cuando se
# tienen múltiples checkboxes.
# -----------------------------------
st.checkbox(
    "Modo oscuro",
    key="chk_modo_oscuro"
)

# -----------------------------------
# value=True
# Define el estado inicial del
# checkbox como seleccionado.
# -----------------------------------
st.checkbox(
    "Recordar sesión",
    value=True,
    key="chk_recordar"
)

# -----------------------------------
# value=False
# Define el estado inicial del
# checkbox como desmarcado.
# Es el valor por defecto.
# -----------------------------------
st.checkbox(
    "Activar sonido",
    value=False,
    key="chk_sonido"
)

# -----------------------------------
# help
# Muestra un mensaje de ayuda cuando
# el usuario pasa el mouse sobre el
# icono de información.
# -----------------------------------
st.checkbox(
    "Acepto los términos",
    key="chk_terminos",
    help="Debe aceptar los términos para continuar."
)

# -----------------------------------
# disabled=True
# Deshabilita el checkbox para que
# el usuario no pueda modificarlo.
# -----------------------------------
st.checkbox(
    "Opción bloqueada",
    disabled=True,
    key="chk_bloqueado"
)

# -----------------------------------
# label_visibility="visible"
# Muestra la etiqueta.
# -----------------------------------
st.checkbox(
    "Etiqueta visible",
    key="chk_visible",
    label_visibility="visible"
)

# -----------------------------------
# label_visibility="hidden"
# Oculta la etiqueta pero conserva
# el espacio reservado.
# -----------------------------------
st.checkbox(
    "Etiqueta oculta",
    key="chk_hidden",
    label_visibility="hidden"
)

# -----------------------------------
# label_visibility="collapsed"
# Oculta completamente la etiqueta
# y elimina el espacio reservado.
# -----------------------------------
st.checkbox(
    "Etiqueta colapsada",
    key="chk_collapsed",
    label_visibility="collapsed"
)

# -----------------------------------
# width="content"
# Ajusta el ancho del componente
# al tamaño de su contenido.
# -----------------------------------
st.checkbox(
    "Checkbox pequeño",
    key="chk_content",
    width="content"
)

# -----------------------------------
# width="stretch"
# Hace que el componente ocupe
# todo el ancho disponible.
# -----------------------------------
st.checkbox(
    "Checkbox ancho completo",
    key="chk_stretch",
    width="stretch"
)

# -----------------------------------
# Ejemplo práctico
# st.checkbox() devuelve True
# cuando está marcado y False
# cuando está desmarcado.
# -----------------------------------
acepta = st.checkbox(
    "Acepto los términos y condiciones",
    key="chk_acepta",
    help="Debe aceptar para continuar."
)

if acepta:
    st.success("Términos aceptados.")
else:
    st.warning("Debe aceptar los términos.")