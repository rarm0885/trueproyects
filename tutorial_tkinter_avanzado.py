"""
==============================================================================
 TUTORIAL INTERACTIVO DE TKINTER - PROGRAMACIÓN IMPERATIVA (SIN CLASES)
==============================================================================
Este programa es un "Manual de Aprendizaje en Vivo" para entender los
conceptos básicos de Tkinter usando SOLO funciones (nada de "class").

Cada sección de la ventana explica y demuestra un concepto distinto:
 1. Configuración de la ventana principal
 2. Layout managers (pack y grid)
 3. Variables dinámicas (StringVar, IntVar, BooleanVar)
 4. Widgets esenciales (Label, Entry, Button, Checkbutton, Radiobutton)
 5. Manejo de eventos con .bind()
 6. Ventanas emergentes (messagebox)

No hay clases, ni objetos definidos por el usuario: todo son variables
globales y funciones normales con "def". Esto es programación imperativa:
el programa se ejecuta como una lista de instrucciones y funciones que
se van llamando una tras otra, según lo que el usuario hace en pantalla.
==============================================================================
"""

# ------------------------------------------------------------------------
# IMPORTACIONES
# ------------------------------------------------------------------------
# "tkinter" es la librería estándar de Python para crear ventanas gráficas.
# La importamos con el alias "tk" para escribir menos código.
import tkinter as tk

# De tkinter también necesitamos el submódulo "messagebox", que sirve
# para mostrar ventanas emergentes de alerta, información o advertencia.
from tkinter import messagebox

# El submódulo "ttk" (Themed Tkinter) nos da widgets con una apariencia
# un poco más moderna. Lo usamos solo para el Combobox de ejemplo extra.
from tkinter import ttk


# ==========================================================================
# 1. CREACIÓN Y CONFIGURACIÓN DE LA VENTANA PRINCIPAL
# ==========================================================================
# "Tk()" crea la ventana raíz (la ventana principal de toda la aplicación).
# En Tkinter SIEMPRE debe existir una sola ventana raíz, de la cual
# "cuelgan" todos los demás widgets (etiquetas, botones, campos, etc).
ventana_principal = tk.Tk()

# .title(texto) -> Cambia el texto que aparece en la barra superior
# de la ventana (la barra de título del sistema operativo).
ventana_principal.title("Manual de Aprendizaje en Vivo - Tkinter Imperativo")

# .geometry("anchoxalto+posX+posY") -> Define el tamaño inicial de la
# ventana en píxeles. Aquí decimos: 950 píxeles de ancho por 700 de alto.
ventana_principal.geometry("950x700")

# .minsize(ancho, alto) -> Establece el tamaño MÍNIMO al que el usuario
# puede reducir la ventana al arrastrar sus bordes. Evita que la
# interfaz se "rompa" visualmente si se hace demasiado pequeña.
ventana_principal.minsize(850, 600)

# .maxsize(ancho, alto) -> Establece el tamaño MÁXIMO al que el usuario
# puede agrandar la ventana. Útil si no queremos que los widgets queden
# con demasiado espacio vacío en pantallas gigantes.
ventana_principal.maxsize(1400, 900)

# .config(bg=color) -> Cambia el color de fondo ("bg" = background) de
# la ventana principal. Usamos un color suave para que se vea agradable.
ventana_principal.config(bg="#eef2f7")


# ==========================================================================
# 2. VARIABLES DINÁMICAS DE TKINTER (EL "CORAZÓN" DEL ESTADO)
# ==========================================================================
# Las variables normales de Python (como texto = "hola") NO se actualizan
# automáticamente en pantalla cuando cambian. Por eso Tkinter nos da unas
# variables especiales que SÍ están conectadas de forma "viva" con los
# widgets: cuando el usuario escribe o hace clic, la variable cambia sola,
# y cuando cambiamos la variable desde el código, el widget se actualiza.
#
# Estas variables deben crearse DESPUÉS de crear la ventana principal
# (tk.Tk()), porque necesitan "engancharse" a ella internamente.

# StringVar -> guarda texto (cadenas de caracteres). Ideal para Entry.
variable_texto_nombre = tk.StringVar()
variable_texto_nombre.set("")  # Valor inicial: vacío.

# IntVar -> guarda números enteros. Ideal para Radiobutton (opción única).
variable_opcion_radio = tk.IntVar()
variable_opcion_radio.set(1)  # Por defecto, la primera opción queda marcada.

# BooleanVar -> guarda True o False. Ideal para Checkbutton (sí/no).
variable_check_terminos = tk.BooleanVar()
variable_check_terminos.set(False)  # Por defecto, la casilla está desmarcada.

variable_check_noticias = tk.BooleanVar()
variable_check_noticias.set(False)


# ==========================================================================
# ETIQUETA DE RESULTADO GENERAL
# ==========================================================================
# Esta etiqueta se actualizará constantemente para mostrar en pantalla
# qué acción realizó el usuario (escribir, marcar, hacer clic, etc.).
# La creamos ahora como variable global de tipo StringVar para poder
# modificar su contenido desde cualquier función más abajo.
variable_resultado_general = tk.StringVar()
variable_resultado_general.set("Aquí verás el resultado de tus interacciones...")


# ==========================================================================
# FUNCIONES (LÓGICA DEL PROGRAMA)
# ==========================================================================
# En programación imperativa, cada acción del usuario (clic, tecla, etc.)
# se conecta a una función normal definida con "def". Estas funciones NO
# pertenecen a ninguna clase, son simplemente bloques de código reutilizable.

def mostrar_texto_ingresado():
    """
    Se ejecuta cuando el usuario presiona el botón "Mostrar texto".
    Lee el valor actual de la variable StringVar (lo que el usuario
    escribió en el Entry) y lo muestra en la etiqueta de resultado.
    """
    texto_actual = variable_texto_nombre.get()  # .get() = "leer" el valor
    if texto_actual == "":
        variable_resultado_general.set("No escribiste ningún texto todavía.")
    else:
        variable_resultado_general.set(f"Escribiste: '{texto_actual}'")


def al_presionar_enter(evento):
    """
    Esta función se conecta a un EVENTO de teclado usando .bind().
    Recibe automáticamente un parámetro llamado "evento" con información
    sobre lo que pasó (qué tecla, en qué widget, etc.), aunque aquí no
    lo usemos directamente, Tkinter siempre lo envía.
    Se dispara cuando el usuario presiona la tecla Enter dentro del Entry.
    """
    mostrar_texto_ingresado()  # Reutilizamos la misma función de arriba.


def al_pasar_mouse_sobre_boton(evento):
    """
    Función conectada al evento "<Enter>" del mouse (cuando el cursor
    ENTRA al área del botón, no confundir con la tecla Enter).
    Cambia el color de fondo del botón para dar una señal visual.
    """
    boton_saludo.config(bg="#ffd166")  # Cambiamos color al pasar el mouse.


def al_quitar_mouse_de_boton(evento):
    """
    Función conectada al evento "<Leave>" del mouse (cuando el cursor
    SALE del área del botón). Regresamos el botón a su color original.
    """
    boton_saludo.config(bg="#06d6a0")


def mostrar_saludo_con_alerta():
    """
    Función vinculada al botón "Saludar". Usa messagebox.showinfo()
    para mostrar una ventana emergente informativa.
    messagebox.showinfo(titulo, mensaje) recibe:
      - titulo: texto que aparece en la barra de la ventana emergente.
      - mensaje: el contenido/pregunta que se muestra al usuario.
    """
    nombre_actual = variable_texto_nombre.get()
    if nombre_actual == "":
        nombre_actual = "amigo(a)"
    messagebox.showinfo("Saludo", f"¡Hola, {nombre_actual}! Bienvenido a Tkinter.")


def verificar_casillas():
    """
    Función vinculada al botón "Verificar casillas".
    Lee el estado (True/False) de las dos variables BooleanVar y
    decide si mostrar una advertencia o una confirmación.
    """
    acepto_terminos = variable_check_terminos.get()  # True o False
    quiere_noticias = variable_check_noticias.get()  # True o False

    if not acepto_terminos:
        # messagebox.showwarning muestra una alerta de advertencia
        # (con un ícono distinto a showinfo, para llamar más la atención).
        messagebox.showwarning(
            "Falta un requisito",
            "Debes aceptar los términos y condiciones para continuar."
        )
        variable_resultado_general.set("No aceptaste los términos y condiciones.")
    else:
        mensaje = "Aceptaste los términos."
        if quiere_noticias:
            mensaje += " Además, quieres recibir noticias."
        else:
            mensaje += " No quieres recibir noticias."
        variable_resultado_general.set(mensaje)


def mostrar_opcion_radio_seleccionada():
    """
    Función vinculada al botón "Ver opción elegida".
    Lee el número guardado en la IntVar de los Radiobutton y muestra
    un texto distinto según cuál esté seleccionado.
    """
    opcion = variable_opcion_radio.get()  # Devuelve 1, 2 o 3

    # Usamos un diccionario para "traducir" el número a un texto legible.
    # Un diccionario es una estructura de datos que asocia una llave (key)
    # con un valor (value), aquí: número de opción -> texto descriptivo.
    textos_opciones = {
        1: "Elegiste la opción: Principiante",
        2: "Elegiste la opción: Intermedio",
        3: "Elegiste la opción: Avanzado"
    }

    # .get(opcion, "valor_por_defecto") busca la llave "opcion" en el
    # diccionario; si no la encuentra, usa el texto por defecto.
    texto_final = textos_opciones.get(opcion, "No se reconoce la opción")
    variable_resultado_general.set(texto_final)


def limpiar_todo():
    """
    Función vinculada al botón "Reiniciar todo".
    Vuelve todas las variables dinámicas a su valor inicial y limpia
    la etiqueta de resultado. Sirve para practicar cómo se modifican
    las variables de Tkinter con .set() desde el código.
    """
    variable_texto_nombre.set("")
    variable_opcion_radio.set(1)
    variable_check_terminos.set(False)
    variable_check_noticias.set(False)
    variable_resultado_general.set("Todo fue reiniciado. ¡Puedes volver a intentarlo!")


# ==========================================================================
# 3. CREACIÓN DE MARCOS (LabelFrame) PARA ORGANIZAR VISUALMENTE LA VENTANA
# ==========================================================================
# Un "LabelFrame" es un marco (contenedor) que además tiene un título
# visible en su borde superior. Sirve para agrupar widgets relacionados
# y hacer que la interfaz se vea más ordenada, como si fueran "cajas".
#
# Parámetros usados en cada LabelFrame:
#   - Primer argumento (ventana_principal): el "padre" o contenedor donde
#     vivirá este marco. Todo widget necesita indicar quién es su padre.
#   - text: el título que aparece en el borde del marco.
#   - bg: color de fondo del marco.
#   - padx, pady: espacio interno (relleno) horizontal y vertical, para
#     que los widgets de adentro no queden pegados al borde del marco.
#   - font: tipografía y tamaño de letra del texto del título.

marco_variables = tk.LabelFrame(
    ventana_principal,
    text="1) Variables dinámicas: StringVar, IntVar y BooleanVar",
    bg="#ffffff",
    padx=10,
    pady=10,
    font=("Arial", 10, "bold")
)
# .pack() es uno de los "administradores de diseño" (layout managers).
# Ordena los widgets uno tras otro (por defecto, de arriba hacia abajo).
#   - fill="x": el marco se estira para ocupar todo el ancho disponible.
#   - padx, pady: separación externa respecto a otros widgets/bordes.
marco_variables.pack(fill="x", padx=15, pady=(15, 8))


marco_eventos = tk.LabelFrame(
    ventana_principal,
    text="2) Eventos con .bind() (teclado y mouse)",
    bg="#ffffff",
    padx=10,
    pady=10,
    font=("Arial", 10, "bold")
)
marco_eventos.pack(fill="x", padx=15, pady=8)


marco_dialogos = tk.LabelFrame(
    ventana_principal,
    text="3) Ventanas emergentes (messagebox) y grid()",
    bg="#ffffff",
    padx=10,
    pady=10,
    font=("Arial", 10, "bold")
)
marco_dialogos.pack(fill="x", padx=15, pady=8)


marco_resultado = tk.LabelFrame(
    ventana_principal,
    text="Resultado de tus interacciones",
    bg="#ffffff",
    padx=10,
    pady=10,
    font=("Arial", 10, "bold")
)
marco_resultado.pack(fill="both", expand=True, padx=15, pady=(8, 15))


# ==========================================================================
# 4. SECCIÓN 1: VARIABLES DINÁMICAS (dentro de marco_variables)
# ==========================================================================
# Aquí usamos .grid() en lugar de .pack(). Grid organiza los widgets en
# una tabla invisible de filas (row) y columnas (column), como una hoja
# de cálculo. Es más preciso que pack cuando queremos alinear varias
# cosas en columnas, como etiquetas junto a campos de texto.

# --- Entry conectado a una StringVar ---
etiqueta_nombre = tk.Label(
    marco_variables,
    text="Escribe tu nombre (StringVar):",
    bg="#ffffff"
)
# row=0, column=0 -> ubica el widget en la fila 0, columna 0 de la tabla.
# sticky="w" -> alinea el widget hacia la izquierda ("w" = west) de su celda.
# padx, pady -> espacio de separación alrededor del widget.
etiqueta_nombre.grid(row=0, column=0, sticky="w", padx=5, pady=5)

# El parámetro "textvariable" es lo que ENLAZA el Entry con la StringVar.
# Cada letra que el usuario escribe actualiza automáticamente la variable.
entrada_nombre = tk.Entry(marco_variables, textvariable=variable_texto_nombre, width=25)
entrada_nombre.grid(row=0, column=1, padx=5, pady=5)

boton_mostrar_texto = tk.Button(
    marco_variables,
    text="Mostrar texto",
    command=mostrar_texto_ingresado,  # "command" indica la función a ejecutar al hacer clic (sin paréntesis).
    bg="#118ab2",
    fg="white"
)
boton_mostrar_texto.grid(row=0, column=2, padx=5, pady=5)


# --- Radiobuttons conectados a una IntVar ---
etiqueta_radio = tk.Label(
    marco_variables,
    text="Elige tu nivel (Radiobutton + IntVar):",
    bg="#ffffff"
)
etiqueta_radio.grid(row=1, column=0, sticky="w", padx=5, pady=5)

# Un "Frame" simple (sin título) se usa aquí solo para agrupar los tres
# Radiobutton en una misma celda de la tabla de grid, uno al lado del otro.
marco_radios = tk.Frame(marco_variables, bg="#ffffff")
marco_radios.grid(row=1, column=1, sticky="w")

# Cada Radiobutton comparte la MISMA variable (variable_opcion_radio),
# por eso solo uno puede estar seleccionado a la vez. El parámetro
# "value" es el número que se guarda en la variable si se elige esa opción.
radio_principiante = tk.Radiobutton(
    marco_radios, text="Principiante", variable=variable_opcion_radio, value=1, bg="#ffffff"
)
radio_intermedio = tk.Radiobutton(
    marco_radios, text="Intermedio", variable=variable_opcion_radio, value=2, bg="#ffffff"
)
radio_avanzado = tk.Radiobutton(
    marco_radios, text="Avanzado", variable=variable_opcion_radio, value=3, bg="#ffffff"
)
# Aquí usamos .pack() DENTRO de este sub-marco, para mostrarlos en fila.
# side="left" -> ordena los widgets de izquierda a derecha.
radio_principiante.pack(side="left", padx=3)
radio_intermedio.pack(side="left", padx=3)
radio_avanzado.pack(side="left", padx=3)

boton_ver_radio = tk.Button(
    marco_variables,
    text="Ver opción elegida",
    command=mostrar_opcion_radio_seleccionada,
    bg="#118ab2",
    fg="white"
)
boton_ver_radio.grid(row=1, column=2, padx=5, pady=5)


# --- Checkbuttons conectados a BooleanVar ---
etiqueta_check = tk.Label(
    marco_variables,
    text="Marca tus preferencias (Checkbutton + BooleanVar):",
    bg="#ffffff"
)
etiqueta_check.grid(row=2, column=0, sticky="w", padx=5, pady=5)

marco_checks = tk.Frame(marco_variables, bg="#ffffff")
marco_checks.grid(row=2, column=1, sticky="w")

# El parámetro "variable" enlaza el Checkbutton con la BooleanVar.
# Cuando el usuario marca/desmarca la casilla, la variable pasa a
# True o False automáticamente (a diferencia de Radiobutton, cada
# Checkbutton es independiente: se puede marcar más de uno a la vez).
check_terminos = tk.Checkbutton(
    marco_checks, text="Acepto términos", variable=variable_check_terminos, bg="#ffffff"
)
check_noticias = tk.Checkbutton(
    marco_checks, text="Quiero noticias", variable=variable_check_noticias, bg="#ffffff"
)
check_terminos.pack(side="left", padx=3)
check_noticias.pack(side="left", padx=3)

boton_verificar_checks = tk.Button(
    marco_variables,
    text="Verificar casillas",
    command=verificar_casillas,
    bg="#118ab2",
    fg="white"
)
boton_verificar_checks.grid(row=2, column=2, padx=5, pady=5)


# ==========================================================================
# 5. SECCIÓN 2: MANEJO DE EVENTOS CON .bind() (dentro de marco_eventos)
# ==========================================================================
# .bind("<Evento>", funcion) conecta un widget con una función que se
# ejecutará automáticamente cuando ocurra ese evento específico.
# La función conectada SIEMPRE recibe un parámetro (aquí llamado "evento")
# con detalles técnicos del suceso, aunque a veces no lo usemos.

etiqueta_evento_teclado = tk.Label(
    marco_eventos,
    text="Presiona Enter dentro de este campo para repetir la acción de 'Mostrar texto':",
    bg="#ffffff"
)
etiqueta_evento_teclado.pack(anchor="w", padx=5, pady=(5, 2))

entrada_para_enter = tk.Entry(marco_eventos, textvariable=variable_texto_nombre, width=30)
entrada_para_enter.pack(anchor="w", padx=5, pady=(0, 10))

# "<Return>" es el nombre que usa Tkinter para la tecla Enter.
# Cada vez que el usuario presiona Enter DENTRO de este Entry, se llama
# automáticamente a la función "al_presionar_enter".
entrada_para_enter.bind("<Return>", al_presionar_enter)


etiqueta_evento_mouse = tk.Label(
    marco_eventos,
    text="Pasa el mouse sobre este botón para ver un evento de mouse (<Enter>/<Leave>):",
    bg="#ffffff"
)
etiqueta_evento_mouse.pack(anchor="w", padx=5, pady=(0, 2))

boton_saludo = tk.Button(
    marco_eventos,
    text="Pasa el mouse aquí",
    command=mostrar_saludo_con_alerta,  # Un botón puede tener command Y bind al mismo tiempo.
    bg="#06d6a0",
    fg="white",
    width=20
)
boton_saludo.pack(anchor="w", padx=5, pady=(0, 5))

# "<Enter>" (evento de mouse) se dispara cuando el cursor ENTRA al widget.
# "<Leave>" se dispara cuando el cursor SALE del widget.
# Ojo: no confundir este "<Enter>" de mouse con la tecla "<Return>" de arriba.
boton_saludo.bind("<Enter>", al_pasar_mouse_sobre_boton)
boton_saludo.bind("<Leave>", al_quitar_mouse_de_boton)


# ==========================================================================
# 6. SECCIÓN 3: VENTANAS EMERGENTES Y BOTÓN DE REINICIO (marco_dialogos)
# ==========================================================================
etiqueta_dialogos = tk.Label(
    marco_dialogos,
    text="Estos botones muestran ventanas emergentes (messagebox) y reinician los valores:",
    bg="#ffffff"
)
etiqueta_dialogos.grid(row=0, column=0, columnspan=2, sticky="w", padx=5, pady=5)

boton_saludo_dialogo = tk.Button(
    marco_dialogos,
    text="Saludar (showinfo)",
    command=mostrar_saludo_con_alerta,
    bg="#ef476f",
    fg="white"
)
boton_saludo_dialogo.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

boton_reiniciar = tk.Button(
    marco_dialogos,
    text="Reiniciar todo",
    command=limpiar_todo,
    bg="#ffd166",
    fg="black"
)
boton_reiniciar.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

# Un pequeño extra: un Combobox (lista desplegable) de ttk, solo para
# mostrar otro widget común. No forma parte de los requisitos base, pero
# ayuda a que el estudiante conozca más opciones disponibles en Tkinter.
etiqueta_combo = tk.Label(marco_dialogos, text="Extra - Combobox (ttk):", bg="#ffffff")
etiqueta_combo.grid(row=2, column=0, sticky="w", padx=5, pady=(10, 5))

combo_extra = ttk.Combobox(marco_dialogos, values=["Python", "Tkinter", "Programación imperativa"])
combo_extra.set("Python")  # Valor mostrado por defecto.
combo_extra.grid(row=2, column=1, sticky="w", padx=5, pady=(10, 5))


# ==========================================================================
# 7. ETIQUETA DE RESULTADO FINAL (marco_resultado)
# ==========================================================================
# Esta es la etiqueta "viva" que muestra el resultado de TODAS las
# interacciones anteriores. Está conectada a "variable_resultado_general"
# mediante el parámetro "textvariable": cada vez que llamamos a
# variable_resultado_general.set(nuevo_texto) en cualquier función de
# arriba, este Label se actualiza solo, sin necesidad de tocarlo directamente.
etiqueta_resultado = tk.Label(
    marco_resultado,
    textvariable=variable_resultado_general,
    bg="#ffffff",
    fg="#073b4c",
    font=("Arial", 12, "bold"),
    wraplength=850,   # Si el texto es muy largo, se acomoda en varias líneas.
    justify="left"
)
etiqueta_resultado.pack(fill="both", expand=True, padx=5, pady=5)


# ==========================================================================
# 8. BUCLE PRINCIPAL DE LA APLICACIÓN
# ==========================================================================
# .mainloop() es la línea MÁS IMPORTANTE de cualquier programa Tkinter.
# Inicia un bucle infinito que:
#   1) Dibuja la ventana y todos sus widgets en pantalla.
#   2) Espera y "escucha" constantemente las acciones del usuario
#      (clics, teclas, movimientos de mouse, etc.).
#   3) Llama a las funciones correspondientes cuando ocurre un evento.
# El programa permanece abierto hasta que el usuario cierra la ventana.
ventana_principal.mainloop()