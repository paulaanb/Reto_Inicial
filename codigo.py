#Creamos el tablero con los movimientos que puede realizar cada numero dentro del tablero
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
#Definimos una  funcion para averiguar los movimientos dependiendo del punto de partida
def calcularmovimientos(puntoinicial, pasos):
    movimiento = 0
    if pasos:
        for movimientosiguiente in movimiento_tablero[puntoinicial]:
            print(f"{pasos}: {puntoinicial} -> {movimientosiguiente}")
            movimiento += 1 + calcular(movimientosiguiente, pasos - 1)

    return movimiento

#Funcion para ver el recorrido de cada celda de partida,movimientos y de el resultado final
def totalpasos(pasos):
    total = 0
    for i in range(10):
        total += calcular(i, pasos)
    return total

#Solucion del reto
print(totalpasos(1))
print("/n")
print(totalpasos(2))
print("/n")
print(totalpasos(3))
print("/n")
print(totalpasos(4))
print("/n")
print(totalpasos(5))
print("/n")
print(totalpasos(6))
print("/n")
print(totalpasos(7))
print("/n")
print(totalpasos(8))
print("/n")
print(totalpasos(9))

