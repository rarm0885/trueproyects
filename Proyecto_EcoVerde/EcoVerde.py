#=====================================================================================================================================
#Aca se importa las libreria Tkinter y Se declaran listas Globales.
#=====================================================================================================================================
import os #este os es meramente para que el logo funcione XD
import tkinter as tk 
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk #Esto porque nada que me salia ese logo en la Mac 🫩

# Listas globales para guardar las entregas y los montos pagados
lista_entregas = []
MontosEntregados = []


#=====================================================================================================================================
#ACA SE DEFINEN LAS VERIFICACIONES; Esta def limita lo que se tiene que agregar en los (entry) asi como previene y maneja errores.
#Calcula un total (por usuario) Y Tambien hace un diccionario donde guarda Todos los datos del usuario y los guarda en listas_entregas.
#Y guarda cada total de cada usuario en la lista MontosEntregados.
#=====================================================================================================================================

def verificaciones():
            
    HasCedula = cedula.get().strip()
    HasTipoDeMaterial = TipoDeMaterial.get().strip()
    HasTipoDeMaterial = HasTipoDeMaterial.lower().strip()
    HasKg = kg.get().strip()
    HasTarifaPorKg = TarifaPorKg.get().strip()

    HasMaterialVerificado = MaterialClasificado.get()

    if not HasCedula or not HasTipoDeMaterial or not HasKg or not HasTarifaPorKg:
        messagebox.showwarning("ERROR","Tienes que rellenar todos los campos para continuar...")
        return
        
    if not HasCedula.isdigit():
        messagebox.showerror("ERROR", "El campo 'C.C' debe contener solo números enteros...")
        return
    
    if len(str(HasCedula))<5 or len(str(HasCedula))>10:
        messagebox.showerror("ERROR","La cedula no puede tener menos de 5 digitos, o mas de 10 digitos ...")
        return

    try:
        HasKg = float(HasKg)
        if HasKg <= 0:
            messagebox.showerror("ERROR","No puedes rellenar el campo 'Cantidad Kg' con cero, o numeros negativos")
            return 
        
    except ValueError:
        messagebox.showerror("ERROR","El campo 'Cantidad Kg' debe ser rellenado solo con numeros...")
        return

    try:
        HasTarifaPorKg = float(HasTarifaPorKg)
        if HasTarifaPorKg <= 0:
            messagebox.showerror("ERROR","No puedes rellenar el campo 'Tarifas por Kilo' con cero, o numeros negativos")
            return
    except ValueError:
        messagebox.showerror("ERROR","El campo 'Tarifa por Kg' debe ser rellenado solo con numeros...")
        return


    if HasMaterialVerificado == True:
        HasMaterialVerificado = "Si"
    else:
        HasMaterialVerificado = "No"


    TotalUsuario = calcular_total_usuario(HasKg,HasTarifaPorKg,HasMaterialVerificado)

    # Crea el diccionario con toda la informacion cargada en las entradas
    datos_recolectores_urbanos = {
        "C.C": HasCedula,
        "Tipo Material": HasTipoDeMaterial,
        "Kg": HasKg,
        "Tarifa Kg": HasTarifaPorKg,
        "Material Verificado": HasMaterialVerificado,
        "Total": TotalUsuario
    }

    # Guarda los datos en las listas globales
    MontosEntregados.append(TotalUsuario)
    lista_entregas.append(datos_recolectores_urbanos)

    UsuariosIngresados.delete(0, tk.END)# Limpiael listbox para que no repita elementos anteriores
    MeterUsuariosIngresados(lista_entregas) #Y se vuelve a cargar toda la lista

    messagebox.showinfo("SUCCES",f"Usuario Guardado Correctamente en la Base de Datos, el total fue: {TotalUsuario}")

    #Limpio loas formularios
    cedula.delete(0, tk.END)
    TipoDeMaterial.delete(0, tk.END)
    kg.delete(0, tk.END)
    TarifaPorKg.delete(0, tk.END)
    MaterialClasificado.set(False)


#=====================================================================================================================================
#ESTA DEF RECURSIVA CALCULA EL TOTAL DE CADA USUARIO; esto le ayuda a la anterior funcion a hacer ese total sin tanto complique.
#=====================================================================================================================================
      
def calcular_total_usuario(HasKg,HasTarifaPorKg,HasMaterialVerificado):

    TotalUsuario = HasKg * HasTarifaPorKg
    if HasMaterialVerificado == "Si":
        TotalUsuario += TotalUsuario*0.1
    
    return TotalUsuario


#=====================================================================================================================================
#ESTA DEF RECURSIVA METE LOS USUARIOS A LA LISTBOX; la funcion de esta def es recursivamente agregar cada nuevo usuario a la listbox.
#De hecho la funcion (verificaciones) borra todos los usuarios ingresados (lista) y hace un llamado a esta def para volverlos a poner
# y/o actualizar la listbox y asi evitar bugs.
#=====================================================================================================================================

def MeterUsuariosIngresados(lista_entregas):

    if len(lista_entregas) == 0:
        return

    entrega_actual = lista_entregas[0]
    linea = f"C.C: {entrega_actual['C.C']} | Material: {entrega_actual['Tipo Material']} | Kg: {entrega_actual['Kg']} | Total: ${entrega_actual['Total']}"
    UsuariosIngresados.insert(tk.END,linea)   # agrega la fila al final del listbox
    
    MeterUsuariosIngresados(lista_entregas[1:])


#=====================================================================================================================================
#FUNCION RECURSIVA PARA CALCULAR UN TOTAL; Esta funcion le ayuda a la def totalizar a Calcular el total desembolsadfo en tooda la
#lista_entregas.
#=====================================================================================================================================

def calcular_total_desembolsado(MontosEntregados):

    if len(MontosEntregados) == 0:
        return 0
    return MontosEntregados[0] + calcular_total_desembolsado(MontosEntregados[1:])


#=====================================================================================================================================
#TOTALIZAR; Esta funcion revisa que la lista no este vacia, y si no lo esta, llama a la funcion de calcular_total_desembolsado y
#por medio de una cajita emergente muestra un total
#=====================================================================================================================================

# Revisa si hay dinero registrado y muestra el resultado final en pantalla
def totalizar():

    if MontosEntregados == []:
        messagebox.showwarning("EMPTY","No Hay Datos Ingresados para Proseguir con La Accion 'Totalizar Pagos'...")

    else:
        TotalDesembolsado = calcular_total_desembolsado(MontosEntregados)
        messagebox.showinfo("TOTAL",f"El Total Desembolsado Hasta Ahora es: ${TotalDesembolsado}")


#=====================================================================================================================================
#CONSULTAR MATERIAL; Esta def pues ayuda a por medio de un simpledialog que es como un entry que aparece en una ventana emergente
#y solo finaliza cuando el usuario le da a cancelar o busca, esya funcion llama tambien a sumar_kilos_por_material.
#=====================================================================================================================================

# Abre la ventana emergente para pedir el nombre del material a buscar
def consultar_material():
    # 1. Pedir el material en la ventana emergente
    material = simpledialog.askstring("Consulta", "Ingrese el material a buscar:")
    
    # 2. Si el usuario escribió algo y no canceló
    if material:
        total = sumar_kilos_por_material(lista_entregas, material.strip().lower())
        messagebox.showinfo("Resultado", f"Total de '{material}': {total} Kg")


#=====================================================================================================================================
#SUMAR KILOS POR MATERIAL; Esta def recursiva tiene el fin de con el 'material' ingresado en la anterior def, buscar entre toda la
#lista_entregas, y dentro de cada diccionario buscar el 'material' en si e ir sumando la cantidad de Kg que haya en dicha lista.
#=====================================================================================================================================

# Suma recursivamente los kilos del material ingresado
def sumar_kilos_por_material(lista_entregas, tipo_material):

    if len(lista_entregas) == 0:
        return 0

    EntregaActual = lista_entregas[0]

    if EntregaActual ["Tipo Material"] == tipo_material:
        return EntregaActual ["Kg"] + sumar_kilos_por_material(lista_entregas[1:],tipo_material)
    else:
        return sumar_kilos_por_material(lista_entregas[1:],tipo_material)



#=====================================================================================================================================
#CONSULTAR USUARIO; Esta def pide la cedula de un usuario, la valida, y la llama a la funcion contar_entregas_usuarios
# y si ese usuario no existe se lo dice, si por el contrario si existe llama a una funcion que abre una ventana que le muestra
#cuantas veces aparecio el usuario y las transacciones. Esta es como la definicion Base.
#=====================================================================================================================================

def consultar_usuario():

    try:
        cc_a_buscar = simpledialog.askstring("Consulta","Ingrese la Cedula de Ciudadania (C.C) a buscar:")
    except ValueError:
        return messagebox.showwarning("ERROR","La Cedula de Ciudadania (C.C) no puede contener letras...")

    if cc_a_buscar == None:
        return

    if len(cc_a_buscar) < 5 or len(cc_a_buscar) >10:
        messagebox.showwarning("ERROR","La Cedula de Ciudadania (C.C) tiene que tener como minimo 5 digitos o maximo 10 digitos...")
        return
    
    total_entregas = contar_entregas_usuario(lista_entregas,cc_a_buscar)
    if total_entregas == 0:
        messagebox.showinfo("EMPTY",f"No hay registros del usuario con Cedula de Ciudadania (C.C): {cc_a_buscar} ")
    else:
        mostrar_ventana_buscar_cc(cc_a_buscar, total_entregas)


#=====================================================================================================================================
#OBLIGATORIA - CONTAR ENTREGAS USUARIO; Esta funcion de manera recursiva pasa por toda la lista_entregas y cuenta cuantas veces 
#aparece la Cedula buscada por medio de un Acumulador
#=====================================================================================================================================
# Cuenta recursivamente cuantas entregas ha hecho ese numero de cedula
def contar_entregas_usuario(lista_entregas,cc_a_buscar,suma_actual = 0):

    if len(lista_entregas) == 0:
        return 0

    PrimerRegistro = lista_entregas[0]
    if PrimerRegistro["C.C"] == cc_a_buscar:
        suma_actual = 1
    else:
        suma_actual = 0

    return suma_actual + contar_entregas_usuario(lista_entregas[1:],cc_a_buscar)


#=====================================================================================================================================
#MOSTRAR_VENTANA_BUSCAR_CC; Esta es la otra def que llamaba CONSULTAR USUARIO, lo que hace es abrir una ventana emergente con un 
#TopLevel, y con ayuda de la anterior def muestra la cantidad.
#=====================================================================================================================================

# Crea la ventana emergente con el Listbox para mostrar el historial
def mostrar_ventana_buscar_cc(cc_a_buscar, total_entregas):
    
    ventana_historial_cc = tk.Toplevel(MainWindow)
    ventana_historial_cc.title("Historial de Usuario")
    ventana_historial_cc.geometry("500x400")
    ventana_historial_cc.grab_set() #el grab congela la pantalla principal

    lista_para_cc = tk.Label(ventana_historial_cc,text=f"C.C: {cc_a_buscar} | Entregas Encontradas: {total_entregas}")
    lista_para_cc.pack(pady=10)

    lista_historial_usuario = tk.Listbox(
        ventana_historial_cc,                                   
        width=40,
        height=20,
        bg= "#FFFFFF",
        fg= "#263238",
        font= ("Helvetica", 10, "normal")
)
    
    lista_historial_usuario.pack(pady=1)



    #=====================================================================================================================================
    #MOSTRAR HISTORIAL USUARIO; Esta def por medio de recursividad busca los datos que le pertenece a la Cedula encontrada (saca los 
    #datos de lista_entregas) y los mete a la listbox de la anterir def.
    #=====================================================================================================================================
    def mostrar_historial_usuario (lista, cedula_buscada, lista_historial_usuario):

        if len(lista) == 0:
            return
        entrega_actual = lista[0]

        if entrega_actual["C.C"] == cedula_buscada:
            linea = f"C.C: {entrega_actual['C.C']} | Material: {entrega_actual['Tipo Material']} | Kg: {entrega_actual['Kg']} | Total: ${entrega_actual['Total']}"
            lista_historial_usuario.insert(tk.END,linea)   # agrega la fila al final del listbox

        mostrar_historial_usuario(lista[1:], cedula_buscada, lista_historial_usuario)

    mostrar_historial_usuario(lista_entregas, cc_a_buscar, lista_historial_usuario)



#=====================================================================================================================================
#Este Pedazo de codigo organiza la ventana principal, le da estilo, y hace que empiece fullscreen pero si el usuario
#decide achicar la ventana no lo deja pasar de ciertos parametros para que no se rompa el GUI. Tambien Arregla errores de 
#resoluciones y hace que funcione y se vea igual en todas las pantallas. Tambien define que la tecla <escape> sirva para salir de
#la FullScreen.
#=====================================================================================================================================

MainWindow = tk.Tk()
MainWindow.title("Centro de Acopio y Reciclaje 'EcoVerde'")
MainWindow.configure(background="#E9ECEF")


MainWindow.attributes(fullscreen=True)

AnchoPantalla = MainWindow.winfo_screenwidth()#Este pedazo de codigo hace que la ventana se vea igual en cualquier pantalla
AltoPantalla = MainWindow.winfo_screenheight()
AnchoMinimo = int(AnchoPantalla * 3)
AltoMinimo = int(AltoPantalla * 0.9)

MainWindow.minsize(AnchoMinimo,AltoMinimo)
MainWindow.maxsize(AnchoMinimo,AltoMinimo)

MainWindow.bind("<Escape>", lambda event: MainWindow.attributes("-fullscreen",False))#Configutra una tecla para cu,plir una funcion
MainWindow.bind("<Return>", lambda event: verificaciones())#hace que al darle a la tecla return se llene el formulario



#=====================================================================================================================================
#En este pedazo de codigo simplemente se crean los LabelFrames que son la organizacion que se ve en la pantalla, y da un toquesito super
#eselente al GUI dandole color, separaciones y sentido.
#=====================================================================================================================================

frame_EntradasUsuario = tk.LabelFrame(
    MainWindow,
    text="-INGRESAR USUARIOS-",
    font=("Helvetica", 14, "bold"),
    bg="#F4F7F6",
    fg="#2E7D32",
    padx=10,
    pady=10
)

frame_EntradasUsuario.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.48)


frame_HistorialUsuarios = tk.LabelFrame(
    MainWindow,
    text="-HISTORIAL USUARIOS INGRESADOS-",
    font=("Helvetica", 14, "bold"),
    bg="#F4F7F6",
    fg="#2E7D32",
    padx=10,
    pady=10  
)

frame_HistorialUsuarios.place(relx=0.01, rely=0.50, relwidth= 0.58, relheight=0.48)


frame_ConsultasUsuarios = tk.LabelFrame(
    MainWindow,
    text="-CONSULTAS-",
    font=("Helvetica", 14, "bold"),
    bg="#F4F7F6",
    fg="#2E7D32",
    padx=15,
    pady=15 
)

frame_ConsultasUsuarios.place(relx=0.60, rely=0.50, relwidth=0.39, relheight=0.48)


#=====================================================================================================================================
#ACA SE LE DA ESTILOS POR MEDIO DE DICCIONARIOS; Esto para que sea mucho mas sencillo estilizar por asi decirlo cada cosa
#=====================================================================================================================================

config_labels = {
    "bg": "#F4F7F6",
    "fg": "#263238",
    "font": ("Helvetica", 14)
}

config_entrys = {
    "bg": "#FFFFFF",
    "fg": "#263238",
    "insertbackground": "#06570A",
    "font": ("Helvetica", 13)
}

config_CheckButtons = {
    "bg": "#F4F7F6",
    "fg": "#154017",
    "activebackground": "#F4F7F6",
    "font": ("Helvetica", 13, "bold")
}

config_buttons = {
    "bg": "#A5D6A7",
    "highlightbackground": "#A5D6A7",
    "bd": 3,           
    "fg": "#102A14",           
    "activebackground": "#81C784", 
    "activeforeground": "#000000",
    "font": ("Helvetica", 12, "bold")
}

config_button_ConsultarUsuario = {
    "bg": "#D7CCC8",
    "highlightbackground": "#A5D6A7",           
    "fg": "#2D1913",           
    "activebackground": "#BCAAA4",
    "font": ("Helvetica", 12, "bold")
}

config_labelframes = {
    "bg": "#F4F7F6",
    "fg": "#2E7D32",
    "font": ("Helvetica", 14, "bold"),
    "padx": 10,
    "pady": 10
}



#=====================================================================================================================================
#ACA SE DEFINEN LAS ENTRADAS (entry) ; CedUla del usuario, tipo de material, Kg entregados y tarifa por Kg. Y se les
#da una posicion en el FrameLabel Superior (INGRESAR USUARIOS)
#=====================================================================================================================================

tk.Label(frame_EntradasUsuario,text="Cedula:",**config_labels).grid(row=0, column=0, padx=(35,10), pady=(35,10), sticky="e")
cedula = tk.Entry(frame_EntradasUsuario, **config_entrys, relief="solid", highlightbackground="#F4F7F6", highlightcolor="#81C784", width=40)
cedula.grid(row=0, column=1, padx=(35,10), pady=(35,10), sticky="w")


tk.Label(frame_EntradasUsuario,text="Tipo Material:",**config_labels).grid(row=1, column=0, padx=(35,10), pady=(35,10), sticky="e")
TipoDeMaterial = tk.Entry(frame_EntradasUsuario, **config_entrys, relief="solid", highlightbackground="#F4F7F6", highlightcolor="#81C784", width=40)
TipoDeMaterial.grid(row=1, column=1, padx=(35, 10), pady=(35, 10), sticky="w")


tk.Label(frame_EntradasUsuario,text="Cantidad Kg:",**config_labels).grid(row=2, column=0, padx=(35,10), pady=(35,10), sticky="e")
kg = tk.Entry(frame_EntradasUsuario, **config_entrys, relief="solid", highlightbackground="#F4F7F6", highlightcolor="#81C784", width=40)
kg.grid(row=2, column=1, padx=(35, 10), pady=(35, 10), sticky="w")


tk.Label(frame_EntradasUsuario,text="Tarifas por Kg:",**config_labels).grid(row=3, column=0, padx=(35,10), pady=(35,10), sticky="e")
TarifaPorKg = tk.Entry(frame_EntradasUsuario, **config_entrys, relief="solid", highlightbackground="#F4F7F6", highlightcolor="#81C784", width=40)
TarifaPorKg.grid(row=3, column=1, padx=(35, 10), pady=(35, 10), sticky="w")


#=====================================================================================================================================
#ACA SE DEFINE EL CHECKBUTTON Material Clasificado Correctamente. Que tambien se pone en (INGRESAR USUARIOS) yyyy EL logo de EcoVerde.
#=====================================================================================================================================

try:
    directorio_progama_EcoVerde_py = os.path.dirname(os.path.abspath(__file__))#Busca el directprio donde esta el .py
    ruta_logo_EcoVerde = os.path.join(directorio_progama_EcoVerde_py, "EcoVerde_Logo.png")

    logo_pil = Image.open (ruta_logo_EcoVerde)
    logo_pil = logo_pil.resize((300, 100), Image.Resampling.LANCZOS) #Esto redimensiona el logo
    logo_EcoVerde = ImageTk.PhotoImage(logo_pil)

    label_logo = tk.Label(frame_EntradasUsuario, image=logo_EcoVerde, bg = "#F4F7F6")
    label_logo.image = logo_EcoVerde #Esto hace que como que no se borre de memoria
    label_logo.grid(row=0, column=2, columnspan=2, padx=(150, 40), pady=(16,0), sticky="w")

except Exception:
    pass     #Ese try, el exception y el pass es por si da la casualidad de que no esta la imagen, el programa siga normal  

MaterialClasificado = tk.BooleanVar(value = False)
tk.Checkbutton(
    frame_EntradasUsuario, 
    text="Material Clasificado Correctamente (10%)", 
    variable=MaterialClasificado, 
    **config_CheckButtons,
    highlightthickness=2,
    highlightbackground="#2E7D32",
    highlightcolor="#81C784",
    selectcolor="#81C784"
    ).grid(row=1, column=2, columnspan=2, padx=(120, 20), pady=(35, 10), sticky="w")


#=====================================================================================================================================
#ACA SE DEFINEN LOS BUTTONS (Registrar Entrega, Totalizar Pagos y Consultar usuarios).
#=====================================================================================================================================

#Este tmabien se agrega en (INGRESAR USUARIOS)
RegistrarEntrega = tk.Button(
    frame_EntradasUsuario, 
    text="Registrar Entrega", 
    **config_buttons,
    relief = tk.RAISED, 
    height=2,
    width=15,
    cursor="exchange",
)

RegistrarEntrega.grid(row=3, column=2, columnspan=2, padx=(100, 10), pady=(10, 10))
RegistrarEntrega.bind("<Button-1>",lambda event: verificaciones())


# Este se agrega en la esquina inferior derecha
TotalizarPagos = tk.Button(
    frame_ConsultasUsuarios,
    text="Totalizar Pagos",
    **config_buttons,
    relief = tk.RAISED,
    width=30,
    height=3,
    cursor="exchange",
    command=totalizar
)

TotalizarPagos.pack(pady= (50, 12))


#Se agrega abajo de totalizar pagos
TotalKgPorMaterial = tk.Button(
    frame_ConsultasUsuarios,
    text= "Total Kg por Material",
    **config_buttons,
    relief = tk.RAISED,
    width=30,
    height=3,
    cursor="exchange",
    command=consultar_material
)

TotalKgPorMaterial.pack(pady=12)

#Se agrega abajo de Total Kg por Material
ConsultarUsuario = tk.Button(
    frame_ConsultasUsuarios,
    text= "Consultar Usuario",
    **config_button_ConsultarUsuario,
    width=30,
    height=3,
    bd=3,
    cursor="exchange",
    command=consultar_usuario
)

ConsultarUsuario.pack(pady=12)


#=====================================================================================================================================
#ACA SE CODEA LA LISTBOX; lo que hace esta listbox es mostrar todos los Usuarios Ingresados con la ayuda de la def 
#mostrar_historial_usuario, y se configura un scroll en caso de que la lista sea muy larga para mas comodidad.
#=====================================================================================================================================

scrolly = tk.Scrollbar(frame_HistorialUsuarios, orient="vertical")

#Esta lisbox esta en la esquina inferior izquierda
UsuariosIngresados = tk.Listbox(
    frame_HistorialUsuarios,
    width=40,
    height=20,
    bg= "#FFFFFF",
    fg= "#263238",
    font= ("Helvetica", 10, "normal"),
    yscrollcommand=scrolly.set
)

scrolly.config(command=UsuariosIngresados.yview)
scrolly.pack(side="right", fill="y")
UsuariosIngresados.pack(side="left", fill="both", expand=True)

    

#=====================================================================================================================================
#ACA SE DEFINE EL MAIN LOOP; La ventana principal que gracias al loop se va a mantener en pie hasta cerrarse.
#=====================================================================================================================================
MainWindow.mainloop()


