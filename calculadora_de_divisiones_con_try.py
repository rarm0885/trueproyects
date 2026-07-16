historial = []

def inputs():
    print("""Ingresa el dividendo y el divisor: 
(Separado por espacios. EJ: 3 4 )\n""")
    while True:
        try: 
            dividendo, divisor = map(float,input("-").split())
            break
        except ValueError:
            print("ERROR: Ingresaste una opcion no valida... Vuelve a intentarlo.")
    
    return dividendo, divisor
    

def errores(historial):
    
    dividendo,divisor = inputs()
    try:
        resultado = dividendo/divisor
        print()
        print(f"El resultado es: {resultado} ")
        print()

    except ZeroDivisionError as error:
        print(f"Error al dividir por cero... ")
        while True:
            if divisor == 0:
                divisor = float(input("""Ingresa el divisor correctamente:
(Recuerda que el divisor no puede ser igual a 0)\n"""))
            else:
                break
    except Exception as error:
        print(f"Ha ocurrido un error inesperado: {error}")
    else:
        print("La division se realizo con exito...")
    finally:
        print("Volviendo al menu...")
    
    historial.append(resultado)
    return historial

def menu(historial):
    
    while True:
        try:
            print()
            print("*"*60)
            print("CALCULADORA DE DIVISIONES")
            print("*"*60)
            print()
            print("1. Calcular una division.")
            print()
            print("2. Historial de resultados.")
            print()
            print("3. Salir del programa.")
            print()
            opcion = int(input("""Ingresa alguna de las opciones:
(1,2 o 3...)\n"""))
            
            if opcion>3 or opcion<1:
                print("OPCION NO VALIDA...")
                opcion = int(input("Vuelve a ingresar alguna de las tres opciones:  "))
            
            else:
                break
        
        except ValueError:
            print("ERROR: No ingresaste un numero valido... Vuelve a intentarlo.")

    if opcion == 1: 
        historial = errores(historial)
        menu(historial)
        
    elif opcion == 2:
        print()
        print("*"*30)
        print("HISTORIAL")
        print("*"*30)
        print()
        
        if historial == []:
            print("El historial esta vacio...")
        else:
            acu = 1
            for numeros in historial:
                print(f"{acu}. {numeros}")
                acu = acu + 1
        menu(historial)
    elif opcion == 3:
        print("Muchas gracias por preferir nuestro programa...")
        print("Saliendo...")
        
    return historial

menu(historial)
                
            


