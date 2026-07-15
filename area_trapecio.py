#investigar try catch para delimitar ingresos

def Area_Trapecio():

    respuesta = input("""Tienes Altura(a), Base Mayor(c) y Base Menor(b)?
Responde si/no\n""").lower()

    while True:
        if respuesta == "si" or respuesta == "no":
            break
        else:
            respuesta = input("""ERROR: Esa opcion no existe...
Tienes Altura(a), Base Mayor(c) y Base Menor(b)?
Responde si/no:\n""").lower()

    if respuesta == "si":
        print("""Ingresa Altura(a), Base menor(b) y la Base Mayor(m):
(separa los datos con espacios...)""")
        a, b, c = map(float,input().split())
        while True:
            if a<1 or b<1 or c<1:
                print("ERROR: Los datos no pueden ser menor a 1...")
                print("""Ingresa Altura(a), Base menor(b) y la Base Mayor(m):
(separa los datos con espacios...)\n""")
                a, b, c = map(float,input().split())
            
            else:
                break
                
        while True:
            if b>c:
                print("ERROR: Base Menor no puede ser mayor a Base Mayor...\n")
                c = float(input("Vuelve a ingresar Base Mayor(c)"))
            else:
                break
        area_trapecio = ((c+b)*a)/2
        print(f"""El Area de tu Trapecio es:
    Area = {area_trapecio}""")


    elif respuesta == "no":
        print("""Ingresa Altura(a), Base menor(b) y la Base mediana(m):
(separa los datos con espacios...)\n""")
        a, b, m = map(float,input().split())
        while True:
            if a<1 or b<1 or m<1:
                print("ERROR: Los datos no pueden ser menor a 1...")
                print("""Ingresa Altura(a), Base menor(b) y la Base Mayor(m):
(separa los datos con espacios...)\n""")
                a, b, m = map(float,input().split())
            
            else:
                break
        
        while True:
            if b>m or b==m:
                print("ERROR: Base Menor no puede ser mayor o igual a Base Mediana...")
                m = float(input("Vuelve a ingresar Base Mediana(m)"))
            else:
                break

        c = (2*m)-b
        while True:
            if b>c or b==c:
                print("ERROR: Base Menor no puede ser mayor o igual a Base Mayor...")
                c = float(input("Vuelve a ingresar Base Mediana(m) para calcular Base Mayor(c):  "))
                c = (2*m)-b
            else:
                break
        
        area_trapecio = ((c+b)*a)/2

        print(area_trapecio)
        print()
        menu()

def menu():
    print('*'*92)
    print(f"{'*':<22}BIENVENIDO A TU CALCULADORA DE AREAS DE TRAPECIO{'*':<22}")
    print('*'*92)
    print()
    print("1. Calcular el Area de un Trapecio.")
    print()
    print("2. Salir.")
    print()

    eleccion = int(input("Ingresa alguna opcion (1 o 2):\n"))
    while True:
        if eleccion == 1 or eleccion == 2:
            break
        else:
            print("ERROR: La opcion ingresada no existe...")
            eleccion = input("Ingresa alguna opcion (1 o 2):\n")
    
    if eleccion == 1:
        Area_Trapecio()
    elif eleccion == 2:
        print("Saliendo...")
        print("Exitos... Que te vaya muy bien.")

menu()