import numpy as np
from PIL import Image
from matplotlib import pyplot
from tkinter import Tk
from tkinter import messagebox
from Procesamiento import Procesamiento
from Puzzle import Puzzle
from random import randint
import my_input

def main():
    
    #CARGAR LA IMAGEN CON PILLOW
    print("CARGANDO IMAGEN...")
    pil_image = Image.open("Deber 2/img/goku.png")

    #CONFIGURAR LAS DIMENSIONES DE LA IMAGEN
    altura = 600
    anchura = 600
    #altura = np_image.shape[0]
    #anchura = np_image.shape[1]

    #CONFIGURAR LAS DIMENSIONES DEL PUZZLE
    filas = my_input.input_filas(altura)
    columnas = my_input.input_columnas(anchura)

    #CREAR EL OBJETO PUZZLE
    puzzle = Puzzle(altura, anchura, filas, columnas, pil_image)

    #ARMAR ROMPECABEZAS
    pyplot.title("ROMPECABEZAS DE " + str(filas) + "x" + str(columnas))
    pyplot.imshow(puzzle.obtener_rompecabezas(puzzle.piezas_rompecabezas))
    pyplot.show()

    #ARMAR ROMPECABEZAS
    pyplot.title("ROMPECABEZAS DE " + str(filas) + "x" + str(columnas))
    pyplot.imshow(puzzle.obtener_rompecabezas(puzzle.piezas_rompecabezas_blanco))
    pyplot.show()    

    #MOVER ALEATORIAMENTE
    #puzzle.mover_piezas_random(1000)

    #ARMAR ROMPECABEZAS
    pyplot.title("ROMPECABEZAS DE " + str(filas) + "x" + str(columnas))
    pyplot.imshow(puzzle.obtener_rompecabezas(puzzle.piezas_rompecabezas_blanco))
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