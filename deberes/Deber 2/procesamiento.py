import numpy as np
from PIL import Image
from matplotlib import pyplot
from random import randint


def redimensionar_np_image(np_image, altura, anchura):
    return np_image[:altura,:anchura]

def obtener_piezas_rompecabezas(np_image, altura, anchura, filas, columnas):
    piezas_rompecabezas = []
    for f in range(filas):
        f_1 = int((altura/filas) * f)
        f_2 = int((altura/filas) * (f+1))
        for c in range(columnas):
            c_1 = int((anchura/columnas) * c)
            c_2 = int((anchura/columnas) * (c+1))
            piezas_rompecabezas.append(np_image[f_1:f_2,c_1:c_2])
    piezas_rompecabezas = np.array(piezas_rompecabezas)
    return piezas_rompecabezas.reshape([filas,columnas,int(altura/filas),int(anchura/columnas),3])

def obtener_rompecabezas(piezas_rompecabezas, filas, columnas):
    imagen_recreada_as_array = []  
    rompecabezas = []
    for f in range(filas):
        for c in range(columnas-1):
            if c == 0:
                imagen_recreada_as_array.append(np.concatenate((piezas_rompecabezas[f,c],piezas_rompecabezas[f,c+1]), axis = 1))
            else:
                imagen_recreada_as_array[f] = np.concatenate((imagen_recreada_as_array[f],piezas_rompecabezas[f,c+1]), axis = 1)
    
    for x in range((len(imagen_recreada_as_array)-1)):
        if x == 0:
            rompecabezas = np.concatenate((imagen_recreada_as_array[x], imagen_recreada_as_array[x+1]), axis = 0)
        else:
            rompecabezas = np.concatenate((rompecabezas, imagen_recreada_as_array[x+1]), axis = 0)
    return rompecabezas

def mover(movimiento, indice_pieza, piezas_rompecabezas):
    indice_pieza_anterior = indice_pieza.copy()

    if movimiento == "arriba":
        indice_pieza[0] =  indice_pieza[0]-1
    elif movimiento == "abajo":
        indice_pieza[0] =  indice_pieza[0]+1
    elif movimiento == "izquierda":
        indice_pieza[1] =  indice_pieza[1]-1
    elif movimiento == "derecha":
        indice_pieza[1] =  indice_pieza[1]+1

    aux_pieza_rompecabeza = piezas_rompecabezas[indice_pieza_anterior[0]][indice_pieza_anterior[1]].copy()
    piezas_rompecabezas[indice_pieza_anterior[0]][indice_pieza_anterior[1]] = piezas_rompecabezas[indice_pieza[0]][indice_pieza[1]]
    piezas_rompecabezas[indice_pieza[0]][indice_pieza[1]] = aux_pieza_rompecabeza

    return piezas_rompecabezas


def validar_movimiento(indice_pieza, filas, columnas, movimiento):
    if movimiento == "arriba" and (indice_pieza[0]-1) >= 0 and (indice_pieza[0]-1) < filas:
        return 1
    elif movimiento == "abajo" and (indice_pieza[0]+1) >= 0 and (indice_pieza[0]+1) < filas:
        return 1
    elif movimiento == "izquierda" and (indice_pieza[1]-1) >= 0 and (indice_pieza[1]-1) < columnas:
        return 1
    elif movimiento == "derecha" and (indice_pieza[1]+1) >= 0 and (indice_pieza[1]+1) < columnas:
        return 1
    else:
        return 0


def mover_piezas_random(mov, indice_pieza, filas, columnas, piezas_rompecabezas):
    n_mov = 0
    while n_mov < mov:
        i = randint(0,3)
        if i == 0:
            if validar_movimiento(indice_pieza, filas, columnas, "arriba"):
                piezas_rompecabezas = mover("arriba", indice_pieza, piezas_rompecabezas)
                n_mov += 1
            #else: 
            #    print("Movimiento no válido")
        if i == 1:
            if validar_movimiento(indice_pieza, filas, columnas, "abajo"):
                piezas_rompecabezas = mover("abajo", indice_pieza, piezas_rompecabezas)
                n_mov += 1
            #else: 
            #    print("Movimiento no válido")
        if i == 2:
            if validar_movimiento(indice_pieza, filas, columnas, "derecha"):
                piezas_rompecabezas = mover("derecha", indice_pieza, piezas_rompecabezas)
                n_mov += 1
            #else: 
            #    print("Movimiento no válido")
        if i == 3:
            if validar_movimiento(indice_pieza, filas, columnas, "izquierda"):
                piezas_rompecabezas = mover("izquierda", indice_pieza, piezas_rompecabezas)
                n_mov += 1
            #else: 
            #    print("Movimiento no válido")
    return piezas_rompecabezas