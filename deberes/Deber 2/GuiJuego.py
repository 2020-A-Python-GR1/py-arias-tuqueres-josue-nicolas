from tkinter import Frame, Label, Tk, Button, Toplevel, Entry, filedialog, messagebox
import numpy as np
from PIL import Image, ImageTk
from matplotlib import pyplot
from Puzzle import Puzzle
import time

n_mov = 0
arrLabels = [[]]
miFrameImagen = None
puzzle = None


def intercambiarPiezas(event,root):
    global arrLabels
    global imagetk_pieza
    global miFrameImagen
    global puzzle
    global n_mov
    x = event.x_root - miFrameImagen.winfo_rootx() 
    y = event.y_root - miFrameImagen.winfo_rooty() 
    z = miFrameImagen.grid_location(x, y) 
    if puzzle.verificarMovimiento([z[1],z[0]]):
        puzzle.intercambiar([z[1],z[0]])
        n_mov = n_mov + 1
        for f in range(puzzle.filas):
            for c in range(puzzle.columnas):
                nparray_pieza = puzzle.piezas_rompecabezas_blanco[f][c]
                pil_pieza = Image.fromarray(nparray_pieza)
                imagetk_pieza[f][c] = ImageTk.PhotoImage(pil_pieza)
                arrLabels[f][c].config(image=imagetk_pieza[f][c])
        if np.array_equal(puzzle.piezas_rompecabezas_blanco, puzzle.piezas_rompecabezas_blanco_verificar):
            ventana = Tk()
            ventana.withdraw()
            messagebox.showinfo("¡FELICIDADES!", "LO HAS CONSEGUIDO EN " + str(n_mov) + " MOVIMIENTOS")
            root.destroy()

def onClosing(ventanaJuego):
    global n_mov
    ventanaJuego.destroy()
    ventana = Tk()
    ventana.withdraw()
    messagebox.showwarning("BASTARDO","ERES UN MANCO POR RENDIRTE")
    n_mov = 0

def abrirVentanaJuego(root, imagenPath, filas, columnas):
    global pil_image_tk 
    global arrLabels
    global imagetk_pieza
    global miFrameImagen
    global puzzle
    ventanaJuego = Toplevel(root) 
    ventanaJuego.title("Puzzle") 
    ventanaJuego.resizable(False, False)
    ventanaJuego.protocol("WM_DELETE_WINDOW", lambda:onClosing(ventanaJuego))
    
    #CARGAR IMAGEN
    pil_image = Image.open(imagenPath)
    pil_image_tk = ImageTk.PhotoImage(pil_image)

    #CONFIGURAR LAS DIMENSIONES DE LA IMAGEN
    anchura, altura  = pil_image.size

    #CREAR EL OBJETO PUZZLE
    puzzle = Puzzle(altura, anchura, int(filas), int(columnas), pil_image)
    arrLabels = [[0 for x in range(puzzle.columnas)] for y in range(puzzle.filas)] 
    imagetk_pieza = [[0 for x in range(puzzle.columnas)] for y in range(puzzle.filas)] 
    #FRAME DE LA IMAGEN
    miFrameImagen = Frame(ventanaJuego, width=anchura, height=altura)
    miFrameImagen.pack(side="left")
    #label_image = Label(miFrameImagen, image=pil_image_tk)
    
    for f in range(puzzle.filas):
        for c in range(puzzle.columnas):
            nparray_pieza = puzzle.piezas_rompecabezas_blanco[f][c]
            pil_pieza = Image.fromarray(nparray_pieza)
            imagetk_pieza[f][c] = ImageTk.PhotoImage(pil_pieza)
            arrLabels[f][c] = Label(miFrameImagen, image=imagetk_pieza[f][c])
            arrLabels[f][c].grid(row=f, column=c)
    ventanaJuego.bind("<Button-1>", lambda event:intercambiarPiezas(event, root)) 



    

    
   