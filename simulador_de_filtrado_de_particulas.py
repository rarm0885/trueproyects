import time

energia_cinetica = float ( input("Ingresa la Energia Cinetica (Ec) en unidade Joules (J):\n") )

energia_inicial = float ( input("Ingresa la Energia Inicial (Eo)\n") )
while True:
    if energia_inicial<=0:
        print("ERROR: La Energia Inicial  no puede ser <= 0...")
        energia_inicial = float ( input("Ingresa la Energia Inicial (Eo) Correctamente:\n") )
    else:
        break
energia_actual = energia_inicial

trabajo_disipado = float ( input("Ingresa el Trabajo Disipado (Wdisipado) :\n") )

energia_final = energia_inicial - trabajo_disipado
#si la energia no es suficiente en la activacion de la compuerta se reduce el impulso neto a la mitad

energia_impulso = float ( input('Ingresa la Energia de Impulso (Eimp):\n') )

def compuerta_tipo_A(energia_actual,energia_impulso):
    print("##################################-COMPUERTA TIPO A-##################################")
    print(f"La energia de entrada Fue: {energia_actual}")

    #incrementa la energia de la particula sumando el valor constante de Eimp
    if energia_actual < 15.0:
        #Perdida de eficiencia del 50% si la energia actual es <15
        energia_impulso += 0.5 * energia_impulso
    else:
        #si no es <15 entonces se le suma Eimp
        energia_actual = energia_actual + energia_impulso

    print("Procesando...")
    time.sleep(3)
    print(f"La energia de salida Fue: {energia_actual}")
    print()
    
    return energia_actual,energia_impulso

energia_freno = float ( input('Ingresa la Energia de Freno (Efreno):\n') )

def compuerta_tipo_P(energia_actual, energia_freno):
    print("##################################-COMPUERTA TIPO P-##################################")
    print(f"La energia de entrada Fue: {energia_actual}")

    energia_actual = energia_actual - energia_freno
    
    print("Procesando...")
    time.sleep(3)
    print(f"La energia de salida Fue: {energia_actual}")
    print()

    return energia_actual

def compuerta_tipo_R(energia_actual):
    print("##################################-COMPUERTA TIPO R-##################################")
    print(f"La energia de entrada Fue: {energia_actual}")

    if int(energia_actual) % 2 == 0:
        #Si el valor entero de la energia actual es par se le multiplica 1,2
        energia_actual = energia_actual * 1,2
    else:
        #sino se le resta 5
        energia_actual = energia_actual - 5.0
    
    print("Procesando...")
    time.sleep(3)
    print(f"La energia de salida Fue: {energia_actual}")
    print()
        
    return energia_actual

compuertas = []
particula = True

#se pregunta por cuantas (numero) de compuertas va a pasar 
numero_compuertas = int ( input ('Ingresa El numero de compuertas por el que va a pasar la Particula:\n') )
#se pregunta el tipo de compuertas, se hace la restriccion y se agrega a la lista
print(""""RECUERDA que las compuertas son: 
      - A (aceleradora).
      - P (pasiva/freno).
      - R (resonante).
 """)
for i in range (0,numero_compuertas):
    tipo_de_compuertas = str ( input ("Ingresa SOLO la letra de la compuerta en mayusculas: ") )
    while True:
        if tipo_de_compuertas == "A" or tipo_de_compuertas == "P" or tipo_de_compuertas == "R":
            break
        else:
            print("ERROR, Esa compuerta no existe...")
            tipo_de_compuertas = str ( input ("Intentalo de nuevo: ") )
    compuertas.append(tipo_de_compuertas)

for letra in compuertas:
        if letra == "A":
            energia_actual,energia_impulso = compuerta_tipo_A (energia_actual,energia_impulso)
            if energia_actual <= 0:
                print("La particula no sobrevivio...")
                print("Cargando detalles...")
                time.sleep(3)
                print(f"""Detalles Finales: 
                - La Energia (E) quedo en: {energia_actual}J
                """)
                break

        elif letra == "P":
            energia_actual = compuerta_tipo_P (energia_actual,energia_freno)
            if energia_actual <= 0 or 1<= energia_actual <= 5:
                print("La particula no sobrevivio...")
                print("Cargando detalles...")
                time.sleep(3)
                print(f"""Detalles Finales: 
                - La Energia (E) quedo en: {energia_actual}J
                """)
                particula = False
                break
        
        elif letra == "R":
            energia_actual1 = compuerta_tipo_R (energia_actual)
            if energia_actual1 <= 0:
                print("La particula no sobrevivio...")
                print("Cargando detalles...")
                time.sleep(3)
                print(f"""Detalles Finales: 
                - La Energia (E) quedo en: {energia_actual1}J
                """)
                break


if energia_actual>0 and particula == True:
    print()
    print("La particula Sobrevivio...")
    print("Cargando detalles...")
    time.sleep(3)
    print(f"""Detalles Finales: 
    - La Energia (E) quedo en: {energia_actual}J
    Felicidades.
    """)
