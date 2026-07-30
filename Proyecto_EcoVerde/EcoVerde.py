import tkinter as tk 
from tkinter import simpledialog, messagebox

# Listas globales para guardar las entregas y los montos pagados
lista_entregas = []
MontosEntregados = []


#Atributos de la ventana principal
MainWindow = tk.Tk()
MainWindow.title("Centro de Acopio y Reciclaje 'EcoVerde'")


MainWindow.attributes(fullscreen=True)

AnchoPantalla = MainWindow.winfo_screenmmwidth()#Este pedazo de codigo hace que la ventana se vea igual en cualquier pantalla
AltoPantalla = MainWindow.winfo_screenheight()
AnchoMinimo = int(AnchoPantalla * 3)
AltoMinimo = int(AltoPantalla * 0.9)

MainWindow.minsize(AnchoMinimo,AltoMinimo)
MainWindow.maxsize(AnchoMinimo,AltoMinimo)


MainWindow.bind("<Escape>", lambda event: MainWindow.attributes("-fullscreen",False))#esto hace que la tecla escape salga de pantalla completa
#fin de los atributos

#Entradas
tk.Label(MainWindow,text="Cedula:").pack()#entrada para C.C
cedula = tk.Entry(MainWindow)
cedula.pack()

tk.Label(MainWindow,text="Tipo Material:").pack()#Entrada para el material
TipoDeMaterial = tk.Entry(MainWindow)
TipoDeMaterial.pack()

tk.Label(MainWindow,text="Kg:").pack()#Entrada para los Kg
kg = tk.Entry(MainWindow)
kg.pack()

tk.Label(MainWindow,text="Tarifa/Kg:").pack()#entrada para la Tarifa/kg
TarifaPorKg = tk.Entry(MainWindow)
TarifaPorKg.pack()

MaterialVerificado = tk.BooleanVar(value = False)#Checkbutton para saber si el material esta verificado
tk.Checkbutton(MainWindow,text="Material Clasificado (10%): ", variable=MaterialVerificado).pack()

RegistrarEntrega = tk.Button(MainWindow,text="Registrar Entrega")#Este boton registra al usuario y llama a verificaciones para saber si todo esta correcto
RegistrarEntrega.pack()
RegistrarEntrega.bind("<Button-1>",lambda event: verificaciones())



#Boton para totalizar el dinero desembolsado, con su logica recursiva

# Suma recursivamente todos los valores guardados en la lista de montos
def calcular_total_desembolsado(MontosEntregados):

    if len(MontosEntregados) == 0:
        return 0
    return MontosEntregados[0] + calcular_total_desembolsado(MontosEntregados[1:])

# Revisa si hay dinero registrado y muestra el resultado final en pantalla
def totalizar():

    if MontosEntregados == []:
        messagebox.showwarning("EMPTY","No Hay Datos Ingresados para Proseguir con La Accion 'Totalizar Pagos'...")

    else:
        TotalDesembolsado = calcular_total_desembolsado(MontosEntregados)
        messagebox.showinfo("TOTAL",f"El Total Desembolsado Hasta Ahora es: ${TotalDesembolsado}")


TotalizarPagos = tk.Button(MainWindow,text="Totalizar Pagos")
TotalizarPagos.pack()
TotalizarPagos.bind("<Button-1>",lambda event: totalizar())

#Fin de totalizar


#Boton para consultar un material, su config y su logica recursiva

# Abre la ventana emergente para pedir el nombre del material a buscar
def consultar_material():
    # 1. Pedir el material en la ventana emergente
    material = simpledialog.askstring("Consulta", "Ingrese el material a buscar:")
    
    # 2. Si el usuario escribió algo y no canceló
    if material:
        total = sumar_kilos_por_material(lista_entregas, material.strip().lower())
        messagebox.showinfo("Resultado", f"Total de '{material}': {total} Kg")

# Suma recursivamente los kilos del material ingresado
def sumar_kilos_por_material(lista_entregas, tipo_material):

    if len(lista_entregas) == 0:
        return 0

    EntregaActual = lista_entregas[0]

    if EntregaActual ["Tipo Material"] == tipo_material:
        return EntregaActual ["Kg"] + sumar_kilos_por_material(lista_entregas[1:],tipo_material)
    else:
        return sumar_kilos_por_material(lista_entregas[1:],tipo_material)

TotalKgPorMaterial = tk.Button(
    MainWindow,
    text= "Total Kg por Material",
    command=consultar_material
)
TotalKgPorMaterial.pack()

#Fin de sumar kg por material


#Boton Consultar usuatio, con su logica respectiva

# Pide la cedula, valida que sea un numero de 5 a 10 digitos y llama a la consulta
def consultar_usuario():

    try:
        cc_a_buscar = simpledialog.askinteger("Consulta","Ingrese la Cedula de Ciudadania (C.C) a buscar:")
    except ValueError:
        return messagebox.showwarning("ERROR","La Cedula de Ciudadania (C.C) no puede contener letras...")

    if cc_a_buscar == None:
        return

    if len(str(cc_a_buscar)) < 5 or len(str(cc_a_buscar)) >10:
        messagebox.showwarning("ERROR","La Cedula de Ciudadania (C.C) tiene que tener como minimo 5 digitos o maximo 10 digitos...")
        return
    
    total_entregas = contar_entregas_usuario(lista_entregas,cc_a_buscar)
    if total_entregas == 0:
        messagebox.showinfo("EMPTY",f"No hay registros del usuario con Cedula de Ciudadania (C.C): {cc_a_buscar} ")
    else:
        mostrar_ventana_buscar_cc(cc_a_buscar, total_entregas)

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

# Crea la ventana emergente con el Listbox para mostrar el historial
def mostrar_ventana_buscar_cc(cc_a_buscar, total_entregas):
    
    ventana_historial_cc = tk.Toplevel(MainWindow)
    ventana_historial_cc.title("Historial de Usuario")
    ventana_historial_cc.geometry("450x320")
    ventana_historial_cc.grab_set() #el grab congela la pantalla principal

    lista_para_cc = tk.Label(ventana_historial_cc,text=f"C.C: {cc_a_buscar} | Entregas Encontradas: {total_entregas}")
    lista_para_cc.pack(pady=10)

    lista_historial_usuario = tk.Listbox(ventana_historial_cc,width=55, height=10)
    lista_historial_usuario.pack(pady=5)

    # Agrega cada entrega del usuario
    def mostrar_historial_usuario (lista, cedula_buscada, lista_historial_usuario):

        if len(lista) == 0:
            return
        entrega_actual = lista[0]

        if entrega_actual["C.C"] == cedula_buscada:
            linea = f"C.C: {entrega_actual['C.C']} | Material: {entrega_actual['Tipo Material']} | Kg: {entrega_actual['Kg']} | Total: ${entrega_actual['Total']}"
            lista_historial_usuario.insert(tk.END,linea)   # agrega la fila al final del listbox

        mostrar_historial_usuario(lista[1:], cedula_buscada, lista_historial_usuario)

    mostrar_historial_usuario(lista_entregas, cc_a_buscar, lista_historial_usuario)

ConsultarUsuario = tk.Button(
    MainWindow,
    text= "Consultar Usuario",
    command=consultar_usuario
)
ConsultarUsuario.pack()
    
#Fin consultar usuario


# Valida que todos los campos del formulario esten bien antes de guardar el registro
def verificaciones():
            
    HasCedula = cedula.get()
    HasTipoDeMaterial = TipoDeMaterial.get()
    HasTipoDeMaterial = HasTipoDeMaterial.lower()
    HasKg = kg.get()
    HasTarifaPorKg = TarifaPorKg.get()
    HasMaterialVerificado = MaterialVerificado.get()

    if not HasCedula or not HasTipoDeMaterial or not HasKg or not HasTarifaPorKg:
        return messagebox.showwarning("ERROR","Tienes que rellenar todos los campos para continuar...")
        
    try:
        HasCedula = int(HasCedula)
    except ValueError:
        messagebox.showerror("ERROR","El campo 'C.C' debe ser rellenado solo con numeros...")
        return

    try:
        HasKg = int(HasKg)
    except ValueError:
        messagebox.showerror("ERROR","El campo 'Kg' debe ser rellenado solo con numeros...")
        return

    try:
        HasTarifaPorKg = int(HasTarifaPorKg)
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
        "Tarifa Kg": TarifaPorKg,
        "Material Verificado": HasMaterialVerificado,
        "Total": TotalUsuario
    }

    # Guarda los datos en las listas globales
    MontosEntregados.append(TotalUsuario)
    lista_entregas.append(datos_recolectores_urbanos)

    UsuariosIngresados.delete(0, tk.END)# Limpiael listbox para que no repita elementos anteriores
    MeterUsuariosIngresados(lista_entregas) #Y se vuelve a cargar toda la lista

    messagebox.showinfo("SUCCES",f"Usuario Guardado Correctamente en la Base de Datos, el total fue: {TotalUsuario}")


# Calcula el total multiplicand kilos por la tarifa y suma el 10% si esta verificado        
def calcular_total_usuario(HasKg,HasTarifaPorKg,HasMaterialVerificado):

    TotalUsuario = HasKg * HasTarifaPorKg
    if HasMaterialVerificado == "Si":
        TotalUsuario += TotalUsuario*0.1
    
    return TotalUsuario

#Esto mete todo el historial de usuarios a la listbox global por asi decirlo 
def MeterUsuariosIngresados(lista_entregas):
    #funcion recursiva para mostra y meter todo a la lista
    if len(lista_entregas) == 0:
        return

    entrega_actual = lista_entregas[0]
    linea = f"C.C: {entrega_actual['C.C']} | Material: {entrega_actual['Tipo Material']} | Kg: {entrega_actual['Kg']} | Total: ${entrega_actual['Total']}"
    UsuariosIngresados.insert(tk.END,linea)   # agrega la fila al final del listbox
    
    MeterUsuariosIngresados(lista_entregas[1:])


UsuariosIngresados = tk.Listbox(MainWindow,width=40,height=20)
UsuariosIngresados.pack(pady=5)

MainWindow.mainloop()


