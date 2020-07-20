import numpy as np
from PIL import Image
from matplotlib import pyplot
from random import randint

class Puzzle:
    altura = None
    anchura = None
    filas = None
    columnas = None
    pil_image = None
    np_image = None
    piezas_rompecabezas = None
    indice_pieza_blanca = None
    piezas_rompecabezas_blanco = None
    piezas_rompecabezas_blanco_verificar = None

    def __init__(self, altura, anchura, filas, columnas, pil_image):
        self.altura = altura
        self.anchura = anchura
        self.filas = filas
        self.columnas = columnas
        self.pil_image = pil_image
        self.np_image = np.asarray(self.pil_image)
        self.piezas_rompecabezas = self.obtener_piezas_rompecabezas()
        self.indice_pieza_blanca = [randint(0,self.filas - 1), randint(0,self.columnas-1)]
        self.piezas_rompecabezas_blanco = self.obtener_piezas_rompecabezas_blanco()
        self.piezas_rompecabezas_blanco_verificar = self.piezas_rompecabezas_blanco.copy()
        self.mover_piezas_random(1000)
        
    def obtener_piezas_rompecabezas(self):
        piezas_rompecabezas = []
        for f in range(self.filas):
            f_1 = int((self.altura/self.filas) * f)
            f_2 = int((self.altura/self.filas) * (f+1))
            for c in range(self.columnas):
                c_1 = int((self.anchura/self.columnas) * c)
                c_2 = int((self.anchura/self.columnas) * (c+1))
                piezas_rompecabezas.append(self.np_image[f_1:f_2,c_1:c_2])
        piezas_rompecabezas = np.array(piezas_rompecabezas)
        return piezas_rompecabezas.reshape([self.filas,self.columnas,int(self.altura/self.filas),int(self.anchura/self.columnas),3])

    def obtener_piezas_rompecabezas_blanco(self):
        piezas_rompecabezas_blanco = self.piezas_rompecabezas.copy()
        piezas_rompecabezas_blanco[self.indice_pieza_blanca[0], self.indice_pieza_blanca[1]] =  np.full([int(self.altura/self.filas),int(self.anchura/self.columnas),3],255)
        return piezas_rompecabezas_blanco

    def obtener_rompecabezas(self, piezas_rompecabezas):
        imagen_recreada_as_array = []  
        rompecabezas = []
        for f in range(self.filas):
            for c in range(self.columnas-1):
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

    def mover(self, movimiento):
        indice_pieza_anterior = self.indice_pieza_blanca.copy()
    
        if movimiento == "arriba":
            self.indice_pieza_blanca[0] =  self.indice_pieza_blanca[0]-1
        elif movimiento == "abajo":
            self.indice_pieza_blanca[0] =  self.indice_pieza_blanca[0]+1
        elif movimiento == "izquierda":
            self.indice_pieza_blanca[1] =  self.indice_pieza_blanca[1]-1
        elif movimiento == "derecha":
            self.indice_pieza_blanca[1] =  self.indice_pieza_blanca[1]+1

        aux_pieza_rompecabeza = self.piezas_rompecabezas_blanco[indice_pieza_anterior[0]][indice_pieza_anterior[1]].copy()
        self.piezas_rompecabezas_blanco[indice_pieza_anterior[0]][indice_pieza_anterior[1]] = self.piezas_rompecabezas_blanco[self.indice_pieza_blanca[0]][self.indice_pieza_blanca[1]]
        self.piezas_rompecabezas_blanco[self.indice_pieza_blanca[0]][self.indice_pieza_blanca[1]] = aux_pieza_rompecabeza



    def validar_movimiento(self, movimiento):
        if movimiento == "arriba" and (self.indice_pieza_blanca[0]-1) >= 0 and (self.indice_pieza_blanca[0]-1) < self.filas:
            return 1
        elif movimiento == "abajo" and (self.indice_pieza_blanca[0]+1) >= 0 and (self.indice_pieza_blanca[0]+1) < self.filas:
            return 1
        elif movimiento == "izquierda" and (self.indice_pieza_blanca[1]-1) >= 0 and (self.indice_pieza_blanca[1]-1) < self.columnas:
            return 1
        elif movimiento == "derecha" and (self.indice_pieza_blanca[1]+1) >= 0 and (self.indice_pieza_blanca[1]+1) < self.columnas:
            return 1
        else:
            return 0


    def mover_piezas_random(self, mov):
        n_mov = 0
        while n_mov < mov:
            i = randint(0,3)
            if i == 0:
                if self.validar_movimiento("arriba"):
                    self.mover("arriba")
                    n_mov += 1
                #else: 
                #    print("Movimiento no válido")
            if i == 1:
                if self.validar_movimiento("abajo"):
                    self.mover("abajo")
                    n_mov += 1
                #else: 
                #    print("Movimiento no válido")
            if i == 2:
                if self.validar_movimiento("derecha"):
                    self.mover("derecha")
                    n_mov += 1
                #else: 
                #    print("Movimiento no válido")
            if i == 3:
                if self.validar_movimiento("izquierda"):
                    self.mover("izquierda")
                    n_mov += 1
                #else: 
                #    print("Movimiento no válido")

    def intercambiar(self, indice_pieza):

        if self.verificarMovimiento(indice_pieza):
            aux_pieza = self.piezas_rompecabezas_blanco[indice_pieza[0]][indice_pieza[1]].copy()

            self.piezas_rompecabezas_blanco[indice_pieza[0]][indice_pieza[1]] = self.piezas_rompecabezas_blanco[self.indice_pieza_blanca[0]][self.indice_pieza_blanca[1]]

            self.piezas_rompecabezas_blanco[self.indice_pieza_blanca[0]][self.indice_pieza_blanca[1]] = aux_pieza

            self.indice_pieza_blanca = indice_pieza
            return True
        else:
            print("Movimiento no permitido")
            return False


    def verificarMovimiento(self, indice_pieza):
        if (indice_pieza[0] == self.indice_pieza_blanca[0]-1 
        and indice_pieza[1] == self.indice_pieza_blanca[1] or 
        
        indice_pieza[0] == self.indice_pieza_blanca[0]+1 
        and indice_pieza[1] == self.indice_pieza_blanca[1] or

        indice_pieza[1] == self.indice_pieza_blanca[1]-1 
        and indice_pieza[0] == self.indice_pieza_blanca[0] or

        indice_pieza[1] == self.indice_pieza_blanca[1]+1 
        and indice_pieza[0] == self.indice_pieza_blanca[0]):

            return True

        return False
        
