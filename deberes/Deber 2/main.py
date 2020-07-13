import numpy as np
from PIL import Image
from matplotlib import pyplot
from tkinter import Tk
from tkinter import messagebox
from Procesamiento import Procesamiento
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
    np_image = np_image[:altura,:anchura]
    print(np_image.shape)
    print("IMAGEN CARGADA!")

    #SELECCIONAR DIMENSIONES DEL ROMPECABEZAS
    filas = my_input.input_filas(altura)
    columnas = my_input.input_columnas(anchura)

    #CREAR EL OBJETO PROCESAMIENTO
    procesamiento = Procesamiento(altura, anchura, filas, columnas)

    #SLICING SEGUN LAS DIMENSIONES
    piezas_rompecabezas = procesamiento.obtener_piezas_rompecabezas(np_image)
    
    #pyplot.imshow(piezas_rompecabezas[1,1])
    #pyplot.show()

    #ARMAR ROMPECABEZAS
    rompecabezas = procesamiento.obtener_rompecabezas(piezas_rompecabezas)
    pyplot.title("ROMPECABEZAS DE " + str(filas) + "x" + str(columnas))
    pyplot.imshow(rompecabezas)
    pyplot.show()

    #SELECCIONAR EL ESPACIO EN BLANCO
    indice_pieza_blanca = [my_input.input_x_pieza_blanca(filas), my_input.input_y_pieza_blanca(columnas)]

    #CREAR PIEZAS DEL ROMPECABEZAS CON ESPACIO EN BLANCO
    piezas_rompecabezas_blanco = piezas_rompecabezas.copy()
    piezas_rompecabezas_blanco[indice_pieza_blanca[0], indice_pieza_blanca[1]] =  np.full([int(altura/filas),int(anchura/columnas),3],255)

    #ARMAR ROMPECABEZAS CON ESPACIO EN BLANCO
    rompecabezas_blanco = procesamiento.obtener_rompecabezas(piezas_rompecabezas_blanco)
    pyplot.imshow(rompecabezas_blanco)
    pyplot.show()

    #COPIAR EL ROMPECABEZAS PARA REALIZAR LA VERIFICACIÓN FINAL
    rompecabezas_blanco_verificar = rompecabezas_blanco.copy()

    #MOVER ALEATORIAMENTE
    piezas_rompecabezas_blanco = procesamiento.mover_piezas_random(1000, indice_pieza_blanca, piezas_rompecabezas_blanco)
    rompecabezas_blanco = procesamiento.obtener_rompecabezas(piezas_rompecabezas_blanco)
    pyplot.imshow(rompecabezas_blanco)
    pyplot.show()


    #MOVER arriba / abajo / derecha / izquierda
    n_mov = 0
    while not(np.array_equal(rompecabezas_blanco, rompecabezas_blanco_verificar)): 
        mover = my_input.input_movimiento()
        if procesamiento.validar_movimiento(indice_pieza_blanca, mover):
            n_mov += 1
            piezas_rompecabezas_blanco = procesamiento.mover(mover, indice_pieza_blanca, piezas_rompecabezas_blanco)
            rompecabezas_blanco = procesamiento.obtener_rompecabezas(piezas_rompecabezas_blanco)
            pyplot.imshow(rompecabezas_blanco)
            pyplot.show()
        else: 
            print("Movimiento no válido")

    #print("FELICIDADES! LO HAS CONSEGUIDO EN " + str(n_mov) + " MOVIMIENTOS")
    window = Tk()
    window.withdraw()
    messagebox.showinfo("¡FELICIDADES!", "LO HAS CONSEGUIDO EN " + str(n_mov) + " MOVIMIENTOS")
    
if __name__ == "__main__":
    main()