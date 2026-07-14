coste_original = 20000
vida_util = 6
valor_de_recuperacion = 2000
año = 2026
depreciacion = (coste_original - valor_de_recuperacion)/vida_util
depreciacion_acumulada = 0

for i in range (0,6):

    depreciacion_acumulada = depreciacion_acumulada + depreciacion
    valor_anual = coste_original - depreciacion_acumulada
    print (f"""Año:   Depreciacion:    Depreciacion Acumulada:   Valor Anual:
{año}    {depreciacion}                 {depreciacion_acumulada}                {valor_anual}
    """)
    año = año + 1

