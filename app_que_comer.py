import random 
import time

comidas = [""]
def menu(comidas):
    flag = False
    print("------------------- MENU -------------------")
    print("""
    1. Ingresar comidas a la lista
      (Ingresa los alimentos ideales que deseas incluir a tu lista)
    
    2. Generar opcion
      (El programa genera una opcion de comida por ti)

    3. Salir de la app
 
""")
    op = int(input("Ingresa alguna opcion:\n"))
    while flag == False:
        if op == 1 or op == 2 or op == 3:
            break
        else:
            op = int(input("\nOPCION NO VALIDA\ningresa alguna opcion correctamente:\n"))
    if op == 1:
        comidas = opcion1() + comidas
        menu(comidas)

    if op == 2:
        opcion2(comidas)
        menu(comidas)

    if op == 3:
        print("Saliendo del programa.")
        time.sleep(1)
        print("saliendo del programa..")
        time.sleep(1)
        print("saliendo del programa...")
        flag = True

def opcion1(): 
    comidas = []
    cant_comida = int(input("-Ingresa el numero de comidas que deseas agregar a la lista-\n"))
    print("-Ingresa las comidas que deseas agregar a tu lista-")
    for i in range (0,cant_comida):
        comida = str(input(""))
        comidas.append(comida)
    print("Cargando los datos...")
    time.sleep(3)
    print("Listo, datos guardados correctamente...\n")
    time.sleep(1)
    
    return comidas

def opcion2(comidas):
    if comidas == []:
        print("No hay comidas disponibles en la lista...\n")
        menu(comidas)
    else:
        print("\nOpcion 1:",random.choice(comidas))
        print()
        print("\nDeseas otra opcion?? (si o no)")
        eleccion = str(input("")).lower()
        
        while True:
            if eleccion == "si" or eleccion == "no":
                break
            else:
                eleccion = str(input("Ingresa la opcion (si o no) correctamente:\n"))
        
        if eleccion == "si":
            print("\nOpcion 2:",random.choice(comidas))
            print()
        


menu(comidas)