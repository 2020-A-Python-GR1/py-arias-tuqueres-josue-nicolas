def input_filas(altura):
    while True: 
        filas = int(input("Ingrese numero de filas del rompecabezas: "))
        if altura%filas == 0:
            break
    return filas

def input_columnas(anchura):
    while True: 
        columnas = int(input("Ingrese numero de columnas del rompecabezas: "))
        if anchura%columnas == 0:
            break
    return columnas

def input_x_pieza_blanca(filas):
    while True:
        x = int(input("Indice del cuadro blanco en x: "))
        if x >= 0 and x < filas:
            break
    return x

def input_y_pieza_blanca(columnas):
    while True:
        y = int(input("Indice del cuadro blanco en y: "))
        if y >= 0 and y < columnas:
            break
    return y