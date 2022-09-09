# Creamos un diccionario que guarda los movimientos posibles en cada posición del tablero.
movimiento_tablero = {
    0: [6, 4],
    1: [6, 8],
    2: [7, 9],
    3: [4, 8],
    4: [3, 9, 0],
    5: [],
    6: [1, 7, 0],
    7: [2, 6],
    8: [1, 3],
    9: [2, 4]
}

# Definimos una funcion para averiguar los movimientos dependiendo del punto de partida
def calcularmovimientos(puntoinicial, pasos):
    movimiento = 0
    if pasos:
        for movimientosiguiente in movimiento_tablero[puntoinicial]:
            movimiento += 1 + calcularmovimientos(movimientosiguiente, pasos - 1)
    return movimiento

# Función para ver el recorrido de cada celda de partida, movimientos y de el resultado final
def totalpasos(pasos):
    total = 0
    for i in range(10):
        total += calcularmovimientos(i, pasos)
    return total

# Solución del reto
print("Si hago un  sólo movimiento, tengo " + str(totalpasos(1)) + " posibilidades.")
print("Si hago dos movimientos, tengo " + str(totalpasos(2)) + " posibilidades.")
print("Si hago tres movimientos, tengo " + str(totalpasos(3)) + " posibilidades.")
print("Si hago cuatro movimientos, tengo " + str(totalpasos(4)) + " posibilidades.")
print("Si hago cinco movimientos, tengo " + str(totalpasos(5)) + " posibilidades.")
print("Si hago seis movimientos, tengo " + str(totalpasos(6)) + " posibilidades.")
print("Si hago siete movimientos, tengo " + str(totalpasos(7)) + " posibilidades.")
print("Si hago ocho movimientos, tengo " + str(totalpasos(8)) + " posibilidades.")
print("Si hago nueve movimientos, tengo " + str(totalpasos(9)) + " posibilidades.")

#Ponemos los test para comprobar los errores
python3 -m doctest -v my_submission.py