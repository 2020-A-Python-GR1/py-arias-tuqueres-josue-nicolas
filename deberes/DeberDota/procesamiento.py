path_builds = "./builds.txt"
def ver(path):
    try:
        f = open(path, "r")
        for x in f:
            print(x)
        f.close()
    except Exception as Error:
        print(f"Error {Error}")
    

def insertar(path, data):
    if(path == path_builds):
        data = generar_id_builds() + ";" + data
    try:
        f = open(path, "a")
        f.write(f"\n{data}")
        f.close()
    except Exception as Error:
        print(f"Error {Error}")

def actualizar(path, data):
    id = data.split(";")[0]
    try:
        f = open(path, "r")
        lineas = f.readlines()
        f.close()
    except Exception as Error:
        print(f"Error {Error}")
    
    try:
        f = open(path, "w")
        for linea in lineas:
            if(id == linea.split(";")[0]):
                f.write(f"{data}\n")
            else:
                f.write(linea)
        f.close()
    except Exception as Error:
        print(f"Error {Error}")


def eliminar(path, id):
    try:
        f = open(path, "r")
        lineas = f.readlines()
        f.close()
    except Exception as Error:
        print(f"Error {Error}")
    
    try:
        f = open(path, "w")
        for linea in lineas:
            if(id != linea.split(";")[0]):
                f.write(linea)
        f.close()
    except Exception as Error:
        print(f"Error {Error}")


def generar_id_builds():
    id = None
    try:
        f = open(path_builds, "r")
        lineas = f.readlines()[1:]
        if len(lineas) > 0:
            for linea in lineas:
                id = int(linea.split(";")[0]) + 1
        else:
            id = 1
        f.close()
    except Exception as Error:
        print(f"Error {Error}")
    return str(id)
