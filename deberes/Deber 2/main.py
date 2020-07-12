import numpy as np
from PIL import Image
from matplotlib import pyplot
from random import randint
import procesamiento 
import my_input

def main():
    
    #CARGAR LA IMAGEN CON PILLOW
    print("CARGANDO IMAGEN...")
    pil_image = Image.open("Deber 2/img/goku.png")
    
    #TRANSFORMAR IMAGEN PILLOW NP.ARRAY
    np_image = np.asarray(pil_image)

    #REDIMENCIONAR EN EL CASO DE SER NECESARIO
    altura = 600
    anchura = 600
    #altura = np_image.shape[0]
    #anchura = np_image.shape[1]
    np_image = procesamiento.redimensionar_np_image(np_image, altura, anchura)
    print("IMAGEN CARGADA!")

    #SELECCIONAR DIMENSIONES DEL ROMPECABEZAS
    filas = my_input.input_filas(altura)
    columnas = my_input.input_columnas(anchura)

    #SLICING SEGUN LAS DIMENSIONES
    piezas_rompecabezas = procesamiento.obtener_piezas_rompecabezas(np_image, 
    altura, anchura, filas, columnas)
    
    #pyplot.imshow(piezas_rompecabezas[1,1])
    #pyplot.show()

    #ARMAR ROMPECABEZAS
    rompecabezas = procesamiento.obtener_rompecabezas(piezas_rompecabezas, filas, columnas)

    #pyplot.imshow(rompecabezas)
    #pyplot.show()

    #SELECCIONAR EL ESPACIO EN BLANCO
    indice_pieza_blanca = [my_input.input_x_pieza_blanca(filas), my_input.input_y_pieza_blanca(columnas)]

    #CREAR PIEZAS DEL ROMPECABEZAS CON ESPACIO EN BLANCO
    piezas_rompecabezas_blanco = piezas_rompecabezas.copy()
    piezas_rompecabezas_blanco[indice_pieza_blanca[0], indice_pieza_blanca[1]] =  np.full([int(altura/filas),int(anchura/columnas),3],255)

    #ARMAR ROMPECABEZAS CON ESPACIO EN BLANCO
    rompecabezas_blanco = procesamiento.obtener_rompecabezas(piezas_rompecabezas_blanco, filas, columnas)
    pyplot.imshow(rompecabezas_blanco)
    pyplot.show()

    

    
if __name__ == "__main__":
    main()