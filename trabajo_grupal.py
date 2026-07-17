import time

def calcularAceleracion():#
    #Anderson 
    # Calcula la tasa a la que un objeto cambia su rapidez. primero halla la diferencia obteniendo el incremento
    # o perdida de la velocidad (restando la inicial a la final), y luego divide ese cambio entre el lapso transcurrido
    velocidadInicial = float(input("Ingresa la Velocidad Inicial:  "))
    velocidadFinal = float(input("Ingresa la Velocidad Final:  "))
    tiempoSegundos = float(input("Ingresa el Tiempo en Segundos:  "))

    
    while True:
        if velocidadFinal < 0 or velocidadInicial < 0  or tiempoSegundos < 0:
            print("Las Velocidades inicial y final y el tiempo no pueden ser < de 0")
            break
        else:
            tasaCambio = (velocidadFinal - velocidadInicial)/tiempoSegundos
            return tasaCambio
    

def calcularPresion():#
    #JacoboGonzalezMurillo
    fuerzaNewtons = float(input("Ingresa la Fuerza en Newtons:  "))
    areaM2 = float(input("Ingresa el Area en M2"))
    if areaM2>0:
        Presion= fuerzaNewtons/areaM2
        return Presion
    else:
        return("el area debe ser mayor a 0")
    
def calcularCaudal ():#
# julio cesar vidal bran--2651359
    volumenM3 = float(input("Ingrese el Volumen en M3:  "))
    tiempoSegundos = float(input("Ingrese el tiempo en Segundos:  "))

    if volumenM3 > 0 and tiempoSegundos > 0:

        Caudal = volumenM3/tiempoSegundos

        return Caudal
    
    else: 
        return ("VolumenM3 o TiempoSegundos es incorrecto")
    
def calcularPeso():#
    #julian David Hernandez Arce
    #es calcular la fuerza de la gravedad con la que atrae un cuerpo
    masakg = float(input("Ingresa la Masa en KG:  "))
    gravedadMs2 = float(input("Ingresa la gravedad en M/s2:  "))

    con=0
    mensaje_error=("la masa no puede ser menor o igual a 0")
    mensaje_error2=("la gravedad no puede ser negativa")
    A=masakg*gravedadMs2
    amplitud=("la fuerza de atraccion del planeta es", A)
    if masakg <=0:
        return mensaje_error
    if gravedadMs2<=0:
        return mensaje_error2
    return amplitud

def calcularPotencia():#
    # Daniel Romero 
    # lo que me pide mi ejercicio es determinar la potencia de trabajo
    # de una maquina repartiendo la enrgia de trabajo
    # en el intervalo temporal que tomo terminar el trabajo 
    # operacion de calculo de potencia 

    trabajoJoules = float(input("Ingresa el Trabajo en Joules:  "))
    tiempoSegundos = float(input("Ingresa el tiempo en segundos:  "))
    
    if tiempoSegundos > 0:
        potencia = (trabajoJoules / tiempoSegundos)
        return potencia
    else:
        return ("ERROR el valor debe ser mayor que cero ")

def calcularEnergiaCinetica():#
    #juan ortiz
    masakg = float(input("Ingresa la masa en KG:  "))
    velocidadMs = float(input("Ingresa la velocidad en Ms"))

    EnergiaI = 0
    if masakg <0  or velocidadMs <0:
        return "ingrese otro valor que no sea 0"
    else:
        calculo = masakg*(velocidadMs**2)*0.5
        EnergiaI+=calculo
    
    return EnergiaI 

def calcularDensidad(): #
    #Calculo de densidad con su masa y volumen.

        m= "Dato fuera de los parametros, debe de ser mayor a 0..."
        Masa,Volumen=map(float,input("Ingresa su Masa(Kg) y Volumen(M³) separados con espacio: ").split())
        if Masa > 0 and Volumen >0:
            Densidad= Masa/Volumen
            return Densidad    
        else:
            return(m)
        
def calcularDistancia():#
    #Andrea Herrera Patiño - 202651161
    velocidadMs = float(input("Ingrese la velocidad en metros por segundo: "))
    #la velocidad puede ser un valor negativo, depende cual sera el sentido que uno le da.
    tiempoSegundos = float(input("Ingrese el tiempo en segundos: "))

    if tiempoSegundos < 0:
        return"Error: El tiempo debe ser un valor positivo."
    else:
        distancia = velocidadMs * tiempoSegundos
        return distancia
    

def calcularVelocidad():#
    #Modulo de fisica-Estudiante-Daniel Gonzalez Cortes
    #velocidad(MRU)
    #entrada de datos distancia por metros y tiempo por segundos
    distanciaMetros = float(input("Ingresa la distancia en Metros:  "))
    tiempoSegundos = float(input("Ingresa el Tiempo en segundos:  "))

    if tiempoSegundos>0 and distanciaMetros>0:
        #dividimos la distancia por segundos para optener 
        rapidez=distanciaMetros/tiempoSegundos
        #devolvemos la rapidez con los valores
        return rapidez
    else:
        print("no se puede dividir por 0")
        #se imprime solo en errores, el tiempo y los segundos deben ser mayores a 0


def convertirCelsiusAKelvin():#
    gradosCelsius = float(input("Ingresa los Grados en C (celsius):  "))
    # Karoll Monsalve
    MotivoFalla= "La temperatura en Celsius es menor a -273.15."

    # Si la temperatura en celsius es mayor a -273.15, se hace la siguiente suma
    # y se retorna el resultado (gradosCelsius)
    if gradosCelsius>-273.15:
        gradosCelsius = gradosCelsius + 273.15

        return gradosCelsius
    
    # Si la temperatura en celsius es menor a -273.15, sale el error
    # y retorna el motivo del problema (MotivoFalla)
    return MotivoFalla


def calcularCostoElectrico():#
    #funcion calcular costo electrico(potencia watts,horas de uso, precio por kWh)
    #John Alejandro Reyes Isaza
    potenciaWatts = float(input("Ingresa la Potencia en Watts:  "))
    horas = float(input("Ingresa las Horas:  "))
    precioKwh = float(input("Ingresa el Precio en KwH"))
    # Convertir potencia de watts a kilowatts
    potenciaKw = potenciaWatts / 1000
    
    # Calcular el consumo en kWh
    consumoKwh = potenciaKw * horas
    
    # Calcular el costo total
    costoTotal = consumoKwh * precioKwh

    #costo unitario
    costoUnitario = costoTotal / 600
    
    # Validar que los valores ingresados sean positivos
    if potenciaWatts <= 0:

        return ("Error: La potencia no puede ser negativa.")
    elif horas <= 0:
        return ("Error: Las horas de uso no pueden ser negativas.")  
    elif precioKwh <= 0:
        return ("Error: El precio por kWh no puede ser negativo.")
    else:   
        return (f"El costo unitario es: ${costoUnitario:.2f}")
    

def calcular_fuerza():#
    #Modulo de fisica - Estudiante 4 - Daniel Alejandro Sanchez 
    #Fuerza(2da Ley de Newton)
    masaKG = float(input("Ingresa la masa en KG:  "))
    aceleracionms2 = float(input("Ingresa la Aceleracion en Ms2:  "))

    if masaKG > 0 and aceleracionms2 > 0:
        # Multiplicamos la masa por la aceleración para obtener la fuerza
        fuerzaN = masaKG * aceleracionms2  
        # Devolvemos la fuerza calculada junto con los valores de entrada
        return fuerzaN, masaKG, aceleracionms2    
    else:
        print("Error: La masa y la aceleración deben ser valores positivos mayores que cero.")
    

def calcularTiempo():#
    #Sebastian Angulo
    #la velocidad no puede ser negativa o 0, si es asi retornamos un mensaje de error
    distanciaMetros = float(input("Ingresa la Distancia en metros:  "))
    velocidadMs = float(input("Ingresa la Velocidad en Ms:  "))

    if velocidadMs <= 0:
        return "la velocidad no puede ser 0 o negativa"
        # dividimos la distancia entre la velocidad para obtener el tiempo
    else:
        tiempo = distanciaMetros / velocidadMs
    return tiempo

# Ricardo Coronel Bonilla
def calcularFriccion ():#
    
    while  True:
        coeficienteFriccion = float(input("ingrese el coeficiente de friccion, que sea entre 0 y 1:  "))
        masa = float(input("ingrese la masa del objeto en kg, que sea mayor que 0 porfavor: "))
        fuerzaNormal = masa * 9.8 # Calcular la fuerza normal
        if (coeficienteFriccion >= 0 and coeficienteFriccion <= 1) or fuerzaNormal>0:
            resistencia = coeficienteFriccion * fuerzaNormal # se calcula la resistencia
            print ("La resistencia es: ",resistencia,"")
            return resistencia
        else:
            print ("Dato erroneo, porfavor ingrese los valores correctos")


def CalcularTrabajo():#
    fuerzaNewtons = float(input("Ingresa La fuerza en N:  "))
    distanciaMetros = float(input("Ingresa la Distancia en M:  "))

    F = (fuerzaNewtons)
    D = (distanciaMetros)
    E = (F * D)
    #el resultado es en joules
    if fuerzaNewtons < 0 or distanciaMetros < 0:
        return "los valores deben ser mayor que cero"
    else:
        return E
    
    #juan felipe jaramillo



def menu():
    print()
    print("*"*30)
    print("PROGRAMA DE FISICA")
    print("*"*30)
    print()
    print("1. Calcular Aceleracion.")
    print("2. Calcular Presion.")
    print("3. Calcular Caudal.")
    print("4. Calcular Peso.")
    print("5. Calcular Potencia.")
    print("6. Calcular Energia Cinetica.")
    print("7. Calcular Densidad.")
    print("8. Calcular Distancia.")
    print("9. Calcular Velocidad.")
    print("10. Convertir Grados Celsious a Kelvin.")
    print("11. Calcular Costo Electrico.")
    print("12. Calcular Fuerza.")
    print("13. Calcular Tiempo.")
    print("14. Calcular Friccion.")
    print("15. Calcular Trabajo.")
    print("16. Salir.")
    print()

    
    while True:
        try:
            eleccion  = int(input("""Ingresa alguna opcion del menu:  
(Del 1 al 16. No se pueden Usar letras...)\n"""))
            if eleccion>16 or eleccion<1:
                print("ERROR: La opcion ingresada no existe...")
                eleccion  = int(input("Ingresa alguna opcion del menu de nuevo:  "))
            else:
                break
        
        except ValueError:
            print("")

            
    
    if eleccion == 1:
        print()
        calcular_aceleracion = calcularAceleracion()
        print()
        print(f"Este es tu resultado :{calcular_aceleracion}")
        print()
        time.sleep(3)
        menu()

    elif eleccion == 2:
        print()
        calcular_presion = calcularPresion()
        print()
        print(f"Este es tu resultado :{calcular_presion}")
        print()
        time.sleep(3)
        menu()

    elif eleccion == 3:
        print()
        calcular_caudal = calcularCaudal()
        print()
        print(f"Este es tu resultado :{calcular_caudal}")
        print()
        time.sleep(3)
        menu()
    
    elif eleccion == 4:
        print()
        calcular_peso = calcularPeso()
        print()
        print("Este es tu resultado: ",calcular_peso)
        print()
        time.sleep(3)
        menu()
    
    elif eleccion == 5:
        print()
        calcular_potencia = calcularPotencia()
        print()
        print("Este es tu resultado: ",calcular_potencia)
        print()
        time.sleep(3)
        menu()
    
    elif eleccion == 6:
        print()
        energia_cinetica = calcularEnergiaCinetica()
        print()
        print("Este es tu resultado: ",energia_cinetica)
        print()
        time.sleep(3)
        menu()

    elif eleccion == 7:
        print()
        calcular_densidad = calcularDensidad()
        print()
        print("Este es tu resultado: ",calcular_densidad)
        print()
        time.sleep(3)
        menu()

    elif eleccion == 8:
        print()
        calcular_distancia = calcularDistancia()
        print()
        print("Este es tu resultado: ",calcular_distancia)
        print()
        time.sleep(3)
        menu()

    elif eleccion == 9:
        print()
        calcular_velocidad = calcularVelocidad()
        print()
        print("Este es tu resultado: ",calcular_velocidad)
        print()
        time.sleep(3)
        menu()
    
    elif eleccion == 10:
        print()
        convertir_c_k = convertirCelsiusAKelvin()
        print()
        print("Este es tu resultado en grados Kelvin: ",convertir_c_k)
        print()
        time.sleep(3)
        menu()
    
    elif eleccion == 11:
        print()
        calcular_costo_electrico = calcularCostoElectrico()
        print()
        print("Este es tu resultado: ",calcular_costo_electrico)
        print()
        time.sleep(3)
        menu()
    
    elif eleccion == 12:
        print()
        calcularFuerza = calcular_fuerza()
        print()
        print("Este es tu resultado: ",calcularFuerza)
        print()
        time.sleep(3)
        menu()
    
    elif eleccion == 13:
        print()
        calcular_tiempo = calcularTiempo()
        print()
        print("Este es tu resultado: ",calcular_tiempo)
        print()
        time.sleep(3)
        menu()

    elif eleccion == 14:
        print()
        calcular_friccion = calcularFriccion()
        print()
        print("Este es tu resultado: ",calcular_friccion)
        print()
        time.sleep(3)
        menu()
    
    elif eleccion == 15:
        print()
        calcular_trabajo = CalcularTrabajo()
        print()
        print("Este es tu resultado: ",calcular_trabajo)
        print()
        time.sleep(3)
        menu()
    
    elif eleccion == 16:
        print()
        print("Muchas gracias por tu Confianza.")
        time.sleep(2)
        print("Saliendo del programa...")


menu()

        





