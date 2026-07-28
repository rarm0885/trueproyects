#CLASE GUI (Grafic User Interface)
#Libreria Python Tkinter
#GUI Ventana, input, Radio Botones, Cajitas de seleccion, Label (etiquetas), Botones -> Evento
#Entorno Virtual (Venv), pip
#Ejecutable .app

import tkinter as tk #El "as" es como un alias, como llamo la libreria

def add(num1,num2):
    return num1 + num2

def execute():
    try:
        num1 = float(input1.get())
        num2 = float(input2.get())
    except ValueError:
        result.config(text=f"ERROR: No se pueden ingresar strings...",fg="red")

    result_add = add (num1,num2)
    result.config(text=f"Result: {result_add}")


window = tk.Tk()
window.title("App Suma")
window.geometry("320x500")
window.minsize(320,500)
window.maxsize(320,500)
tk.Label(window,text = "Ingresa un numero:\n").pack()
input1 = tk.Entry(window)
input1.pack()
tk.Label(window,text = "Ingresa otro numero:\n").pack()
input2 = tk.Entry(window)
input2.pack()

tk.Button(window, text="Calcular",command=execute).pack()

result = tk.Label(window,text = "Result:")
result.pack()


window.mainloop()


#CREAR ENTORNO VIRTUAL
#python3 -m venv venv
#source venv/bin/activate

#CREAR EJECUTABLE
#pyinstaller --noconsole --onefile suma.py
