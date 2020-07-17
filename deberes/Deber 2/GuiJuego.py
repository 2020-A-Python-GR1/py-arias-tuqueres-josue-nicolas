from tkinter import Frame, Label, Tk, Button, Toplevel, Entry, filedialog, messagebox
import numpy as np
from PIL import Image, ImageTk
from matplotlib import pyplot
from Puzzle import Puzzle
import time

n_mov = 0

def funcionMover(mov, puzzle, label_image, botonAleatorio, botonArriba, botonAbajo, botonIzquierda, botonDerecha,root):
    global pil_image_tk 
    global n_mov
    n_mov = n_mov + 1
    puzzle.mover(mov)
    pil_image = Image.fromarray(puzzle.obtener_rompecabezas(puzzle.piezas_rompecabezas_blanco))
    pil_image_tk = ImageTk.PhotoImage(pil_image)
    label_image.config(image=pil_image_tk)
    validarMov(puzzle,botonArriba, botonAbajo, botonIzquierda, botonDerecha)
    if np.array_equal(puzzle.piezas_rompecabezas_blanco, puzzle.piezas_rompecabezas_blanco_verificar):
        ventana = Tk()
        ventana.withdraw()
        messagebox.showinfo("¡FELICIDADES!", "LO HAS CONSEGUIDO EN " + str(n_mov) + " MOVIMIENTOS")
        root.destroy()
    #return mov

def validarMov(puzzle, botonArriba, botonAbajo, botonIzquierda, botonDerecha):
    if puzzle.validar_movimiento("arriba"):
        botonArriba.configure(state='normal')
    else: 
        botonArriba.configure(state='disabled')
    if puzzle.validar_movimiento("abajo"):
        botonAbajo.configure(state='normal')
    else: 
        botonAbajo.configure(state='disabled')
    if puzzle.validar_movimiento("izquierda"):
        botonIzquierda.configure(state='normal')
    else: 
        botonIzquierda.configure(state='disabled')
    if puzzle.validar_movimiento("derecha"):
        botonDerecha.configure(state='normal')
    else: 
        botonDerecha.configure(state='disabled')


def generarBlanco(puzzle, label_image, boton, botonAleatorio):
    global pil_image_tk 
    global n_mov
    n_mov = 0
    pil_image = Image.fromarray(puzzle.obtener_rompecabezas(puzzle.piezas_rompecabezas_blanco))
    pil_image_tk = ImageTk.PhotoImage(pil_image)
    label_image.config(image=pil_image_tk)
    botonAleatorio.configure(state='normal')
    boton.destroy()
    #return mov

def moverRandom(puzzle, label_image, boton, btnArriba, btnAbajo, btnIzquierda, btnDerecha):
    global pil_image_tk
    puzzle.mover_piezas_random(1000)
    pil_image = Image.fromarray(puzzle.obtener_rompecabezas(puzzle.piezas_rompecabezas_blanco))
    pil_image_tk = ImageTk.PhotoImage(pil_image)
    label_image.config(image=pil_image_tk)
    if np.array_equal(puzzle.piezas_rompecabezas_blanco, puzzle.piezas_rompecabezas_blanco_verificar):
        moverRandom(puzzle, label_image, boton, btnArriba, btnAbajo, btnIzquierda, btnDerecha)
    else:  
        btnArriba.configure(state='normal')
        btnAbajo.configure(state='normal')
        btnIzquierda.configure(state='normal')
        btnDerecha.configure(state='normal')
        validarMov(puzzle,btnArriba, btnAbajo, btnIzquierda, btnDerecha)
        boton.destroy()


def onClosing(ventanaJuego):
    ventanaJuego.destroy()
    ventana = Tk()
    ventana.withdraw()
    messagebox.showwarning("BASTARDO","ERES UN MANCO POR RENDIRTE")

def abrirVentanaJuego(root, imagenPath, filas, columnas):
    global pil_image_tk 
    
    ventanaJuego = Toplevel(root) 
    ventanaJuego.title("Puzzle") 
    ventanaJuego.protocol("WM_DELETE_WINDOW", lambda:onClosing(ventanaJuego))
    #CARGAR IMAGEN
    pil_image = Image.open(imagenPath)
    pil_image_tk = ImageTk.PhotoImage(pil_image)

    #CONFIGURAR LAS DIMENSIONES DE LA IMAGEN
    altura, anchura = pil_image.size

    #CREAR EL OBJETO PUZZLE
    puzzle = Puzzle(altura, anchura, int(filas), int(columnas), pil_image)

    #FRAME DE LA IMAGEN
    miFrameImagen = Frame(ventanaJuego, width=anchura, height=altura)
    miFrameImagen.pack(side="left")
    label_image = Label(miFrameImagen, image=pil_image_tk)
    label_image.grid(row=0, column=0)


    #FRAME DE LOS BOTONES
    miFrameButones = Frame(ventanaJuego)
    miFrameButones.pack(side="right")

    botonBlanco = Button(miFrameButones, width="20", height="1", text = "GENERAR BLANCO", command = lambda:generarBlanco( puzzle, label_image, botonBlanco, botonAleatorio,))
    botonBlanco.grid(row=0, column=0, padx=10, pady=10)

    botonAleatorio = Button(miFrameButones, width="20", height="1", text = "MOVER RANDOM", command = lambda:moverRandom(puzzle, label_image, botonAleatorio, botonArriba, botonAbajo, botonIzquierda, botonDerecha))
    botonAleatorio.grid(row=1, column=0, padx=10, pady=10)
    botonAleatorio.configure(state='disabled')

    botonArriba = Button(miFrameButones, width="20", height="1", text = "ARRIBA", command = lambda:funcionMover("arriba", puzzle,label_image, botonAleatorio, botonArriba, botonAbajo, botonIzquierda, botonDerecha,root))
    botonArriba.grid(row=2, column=0, padx=10, pady=10)
    botonArriba.configure(state='disabled')

    botonAbajo = Button(miFrameButones, width="20", height="1", text = "ABAJO", command = lambda:funcionMover("abajo", puzzle,label_image, botonAleatorio, botonArriba, botonAbajo, botonIzquierda, botonDerecha,root))
    botonAbajo.grid(row=3, column=0, padx=10, pady=10)
    botonAbajo.configure(state='disabled')

    botonIzquierda = Button(miFrameButones, width="20", height="1", text = "IZQUIERDA", command = lambda:funcionMover("izquierda", puzzle,label_image, botonAleatorio, botonArriba, botonAbajo, botonIzquierda, botonDerecha,root))
    botonIzquierda.grid(row=4, column=0, padx=10, pady=10)
    botonIzquierda.configure(state='disabled')

    botonDerecha = Button(miFrameButones, width="20", height="1", text = "DERECHA", command = lambda:funcionMover("derecha", puzzle,label_image, botonAleatorio, botonArriba, botonAbajo, botonIzquierda, botonDerecha,root))
    botonDerecha.grid(row=5, column=0, padx=10, pady=10)
    botonDerecha.configure(state='disabled')
    
    

    
   