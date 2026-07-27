"""
==============================================================================
 TUTORIAL BÁSICO DE TKINTER - PRIMEROS PASOS (PARA PRINCIPIANTES)
==============================================================================
Este es un programa MUY sencillo para aprender lo mínimo indispensable
de Tkinter. Si nunca has creado una ventana con Python, empieza por aquí.

No usamos "class" (clases), ni cosas avanzadas. Solo:
  - Crear una ventana.
  - Poner texto, un campo para escribir y un botón.
  - Que al hacer clic en el botón, pase algo (se actualice un texto).
  - Mostrar una alerta simple.

Todo el código está comentado línea por línea, explicado con palabras
simples, como si fuera la primera vez que ves esto (¡porque probablemente
lo es!).
==============================================================================
"""

# ------------------------------------------------------------------------
# PASO 1: IMPORTAR LO NECESARIO
# ------------------------------------------------------------------------
# "tkinter" ya viene instalado con Python, no hay que instalar nada.
# Lo importamos como "tk" para no tener que escribir "tkinter" cada vez.
import tkinter as tk

# "messagebox" es una parte extra de tkinter que sirve para mostrar
# pequeñas ventanas de alerta o mensaje, como un "pop-up".
from tkinter import messagebox


# ------------------------------------------------------------------------
# PASO 2: CREAR LA VENTANA PRINCIPAL
# ------------------------------------------------------------------------
# Esto crea la ventana vacía. Es como el "lienzo" donde vamos a poner
# todo lo demás (textos, botones, etc). SIEMPRE se necesita esta línea.
ventana = tk.Tk()

# Le ponemos un título, que se ve arriba en la barra de la ventana.
ventana.title("Mi primera ventana con Tkinter")

# Le damos un tamaño inicial: 400 píxeles de ancho por 300 de alto.
# Se escribe como texto: "anchoxalto".
ventana.geometry("400x300")

# Le damos un color de fondo a la ventana, para que no sea gris por defecto.
ventana.config(bg="#f0f8ff")


# ------------------------------------------------------------------------
# PASO 3: UNA VARIABLE ESPECIAL PARA GUARDAR TEXTO (StringVar)
# ------------------------------------------------------------------------
# En Tkinter, si queremos que un texto en pantalla cambie automáticamente,
# no usamos una variable normal de Python. Usamos "StringVar", que es
# una cajita especial de texto que Tkinter sabe "vigilar" y actualizar.
mensaje = tk.StringVar()

# Le damos un valor inicial (el texto que se ve al abrir el programa).
mensaje.set("Escribe tu nombre y presiona el botón")


# ------------------------------------------------------------------------
# PASO 4: UNA FUNCIÓN QUE SE EJECUTA AL HACER CLIC
# ------------------------------------------------------------------------
# Una función es un bloque de código con un nombre, que podemos "llamar"
# (ejecutar) cuando queramos. Aquí la usamos para decir qué debe pasar
# cuando el usuario haga clic en el botón.
def saludar():
    # .get() sirve para "leer" lo que el usuario escribió en el campo de texto.
    nombre = campo_texto.get()

    # Si el usuario no escribió nada, mostramos un mensaje por defecto.
    if nombre == "":
        mensaje.set("¡No escribiste tu nombre!")
    else:
        # .set() cambia el texto de la variable "mensaje", y como está
        # conectada a una etiqueta (Label), el texto en pantalla cambia solo.
        mensaje.set("¡Hola, " + nombre + "! Bienvenido a Python.")

    # Además, mostramos una ventanita emergente de saludo.
    # messagebox.showinfo(titulo, texto) crea una alerta simple con un botón "OK".
    messagebox.showinfo("Saludo", "Mensaje enviado correctamente.")


# ------------------------------------------------------------------------
# PASO 5: CREAR LOS WIDGETS (LOS ELEMENTOS VISUALES)
# ------------------------------------------------------------------------
# Un "widget" es cualquier elemento visual: un texto, un botón, un campo
# para escribir, etc. Todos se crean parecido: se le dice a qué ventana
# pertenecen (aquí "ventana"), y luego algunas opciones extra.

# --- Un texto (Label) que explica qué hacer ---
etiqueta_instruccion = tk.Label(
    ventana,                     # Va dentro de "ventana" (la ventana principal).
    text="¿Cómo te llamas?",     # El texto que se muestra.
    bg="#f0f8ff",                 # Color de fondo (igual al de la ventana, para que combine).
    font=("Arial", 12)            # Tipo y tamaño de letra.
)
# ".pack()" es la forma más simple de "colocar" un widget en la ventana.
# Por defecto, apila los widgets uno debajo del otro, de arriba hacia abajo.
etiqueta_instruccion.pack(pady=10)  # pady = espacio arriba y abajo (en píxeles).


# --- Un campo de texto (Entry) para que el usuario escriba ---
campo_texto = tk.Entry(
    ventana,
    width=25,        # Ancho del campo (cuántos caracteres se ven aproximadamente).
    font=("Arial", 12)
)
campo_texto.pack(pady=5)


# --- Un botón (Button) que ejecuta la función "saludar" al hacer clic ---
boton = tk.Button(
    ventana,
    text="Saludar",       # Texto que aparece dentro del botón.
    command=saludar,      # La función que se ejecuta al hacer clic (SIN paréntesis).
    bg="#4caf50",          # Color de fondo del botón.
    fg="white",            # Color del texto (fg = "foreground").
    font=("Arial", 11, "bold")
)
boton.pack(pady=10)


# --- Una etiqueta (Label) que muestra el resultado y se actualiza sola ---
etiqueta_resultado = tk.Label(
    ventana,
    textvariable=mensaje,  # Aquí está la magia: se conecta con la variable "mensaje".
    bg="#f0f8ff",
    fg="#1a1a1a",
    font=("Arial", 11),
    wraplength=350          # Si el texto es largo, se acomoda en varias líneas.
)
etiqueta_resultado.pack(pady=15)


# ------------------------------------------------------------------------
# PASO 6: MANTENER LA VENTANA ABIERTA (MUY IMPORTANTE)
# ------------------------------------------------------------------------
# Sin esta línea, la ventana se abriría y se cerraría de inmediato.
# ".mainloop()" hace que el programa se quede "esperando" a que el
# usuario haga algo (escribir, hacer clic, cerrar la ventana, etc.).
ventana.mainloop()