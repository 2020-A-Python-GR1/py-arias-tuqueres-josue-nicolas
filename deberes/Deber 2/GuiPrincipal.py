
from tkinter import Frame, Label, Tk, Button, Toplevel, Entry, filedialog, messagebox
from GuiJuego import abrirVentanaJuego
from PIL import Image
imagenPath = None

def abrirArchivo():
    global imagenPath
    imagenPath = filedialog.askopenfilename(initialdir="/NICOLAS/EPN/7 SEMESTRE/Github/py-arias-tuqueres-josue-nicolas/deberes/Deber 2/img", title= "Selecciona un archivo",filetypes = (("all files","*.*"),("jpeg files","*.jpg")))

def enviar(root, imagenPath, Filas, Columnas):
    if validar(imagenPath, Filas, Columnas):
        abrirVentanaJuego(root,imagenPath, Filas, Columnas)
    else:
        ventana = Tk()
        ventana.withdraw()
        messagebox.showerror("ERROR","DATOS DE ENTRADA ERRONEOS")

def validar(imagenPath, Filas, Columnas):
    if imagenPath and Filas and Columnas:
        pil_image = Image.open(imagenPath)
        anchura = pil_image.size[0]
        altura = pil_image.size[1] 
        if anchura%int(Columnas) == 0 and altura%int(Filas) == 0:
            return True
        else:
            print(pil_image.size)
            print(anchura/int(Columnas), altura/int(Filas))
    return False


def main():
    global imagenPath

    root = Tk() 
    root.title("Puzzle") 
    # sets the geometry of main  
    # root window 
    #root.geometry("400x200") 
    root.resizable(False, False)
    miFrameInicio = Frame(root)
    miFrameInicio.pack(side="top")

    botonSeleccionar = Button(miFrameInicio, width="20", text = "Seleccionar archivo", command=abrirArchivo)
    botonSeleccionar.grid(row=0, column=0, padx=10, pady=5)

    labelFilas = Label(miFrameInicio, text ="Filas") 
    labelFilas.grid(row=1, column=0, padx=10, pady=5) 

    entryFilas = Entry(miFrameInicio)
    entryFilas.grid(row=2, column=0, padx=10, pady=5) 

    labelColumnas = Label(miFrameInicio, text ="Columnas") 
    labelColumnas.grid(row=3, column=0, padx=10, pady=5)

    entryColumnas = Entry(miFrameInicio)
    entryColumnas.grid(row=4, column=0, padx=10, pady=5) 

    botonEnviar = Button(miFrameInicio,text ="JUGAR", width="20", command=lambda:enviar(root,imagenPath, entryFilas.get(), entryColumnas.get())) 
    botonEnviar.grid(row=5, column=0, padx=10, pady=10)

    root.mainloop() 

if __name__ == "__main__":
    main()

