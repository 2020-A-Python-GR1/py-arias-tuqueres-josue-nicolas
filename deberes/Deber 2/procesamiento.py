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
