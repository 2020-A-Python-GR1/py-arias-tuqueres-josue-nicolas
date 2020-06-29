import procesamiento
from Heroes import Heroes
from Items import Items
path_heores = "./heroes.txt"
path_items = "./items.txt"
path_builds = "./builds.txt"

def operacion_crud(operacion):
    #OPERACIONES HEROES
    def insertar_heroes():
        while True:
            heroe = Heroes(input("Nombre: "),input("Fuerza: "),input("Mana: "),input("Armadura: "),input("Daño: "),input("Arcana: "))
            if(not(procesamiento.existe_nombre(path_heores, heroe.nombre, 0))):
                break
            else:
                print("El heroe ya está registrado, ingrese otro por favor.")
        return procesamiento.insertar(path_heores, str(heroe))

    def ver_heroes():
        return procesamiento.ver(path_heores)

    def actualizar_heroes():
        while True:
            heroe = Heroes(input("Nombre: "),input("Fuerza: "),input("Mana: "),input("Armadura: "),input("Daño: "),input("Arcana: "))
            if(procesamiento.existe_nombre(path_heores, heroe.nombre, 0)):
                break
            else:
                print("El heroe no se encuentra registrado, ingrese otro por favor.")
        return procesamiento.actualizar(path_heores, str(heroe))

    def eliminar_heroes():
        while True:
            nombre = input("Nombre: ")
            if(procesamiento.existe_nombre(path_heores, nombre, 0)):
                break
            else:
                print("El heroe no se encuentra registrado, ingrese otro por favor.")
        return procesamiento.eliminar(path_heores,nombre)

    #OPERACIOENS ITEMS
    def insertar_items():
        while True:
            item = Items(input("Nombre: "),input("Tipo: "),input("Costo: "),input("Activa: "),input("Pasiva: "))
            if(not(procesamiento.existe_nombre(path_items, item.nombre, 0))):
                break
            else:
                print("El item ya está registrado, ingrese otro por favor.")
        return procesamiento.insertar(path_items, str(item))

    def ver_items():
        return procesamiento.ver(path_items)

    def actualizar_items():
        while True:
            item = Items(input("Nombre: "),input("Tipo: "),input("Costo: "),input("Activa: "),input("Pasiva: "))
            if(procesamiento.existe_nombre(path_items, item.nombre, 0)):
                break
            else:
                print("El item no se encuentra registrado, ingrese otro por favor.")
        return procesamiento.actualizar(path_items, str(item))

    def eliminar_items():
        while True:
            nombre = input("Nombre: ")
            if(procesamiento.existe_nombre(path_items, nombre, 0)):
                break
            else:
                print("El item no se encuentra registrado, ingrese otro por favor.")
        return procesamiento.eliminar(path_items,nombre)

    #OPERACIONES BUILDS
    def insertar_builds():
        agregar_item = 1
        while True:
            nombre_heroe = input("Nombre del heroe: ")
            if(procesamiento.existe_nombre(path_heores, nombre_heroe, 0)):
                break
            else:
                print("El heroe no se encuentra registrado, ingrese otro por favor.")
        lista_items = []
        while(agregar_item):
            while True:
                item = input("Item: ")
                if(procesamiento.existe_nombre(path_items, item, 0)):
                    break
                else:
                    print("El item no se encuentra registrado, ingrese otro por favor.")
            lista_items.append(item)
            agregar_item = int(input("""
            ¿Desea agregar otro item?
            si -> 1
            no -> 0
            """))
        return procesamiento.insertar(path_builds,f"{nombre_heroe};{lista_items}")
        

    def ver_builds():
        return procesamiento.ver(path_builds)

    def actualizar_builds():
        agregar_item = 1
        while True:
            id_build = input("Id de la build que desea actualizar: ")
            if(procesamiento.existe_nombre(path_builds, id_build, 0)):
                break
            else:
                print("La build no se encuentra registrada, ingrese otro por favor.")
        while True:
            nombre_heroe = input("Nombre del heroe: ")
            if(procesamiento.existe_nombre(path_heores, nombre_heroe, 0)):
                break
            else:
                print("El heroe no se encuentra registrado, ingrese otro por favor.")
        lista_items = []
        while(agregar_item):
            while True:
                item = input("Item: ")
                if(procesamiento.existe_nombre(path_items, item, 0)):
                    break
                else:
                    print("El item no se encuentra registrado, ingrese otro por favor.")
            lista_items.append(item)
            agregar_item = int(input("""
            ¿Desea agregar otro item?
            si -> 1
            no -> 0
            """))
        return procesamiento.actualizar(path_builds,f"{id_build};{nombre_heroe};{lista_items}")

    def eliminar_builds():
        while True:
            id_build = input("Id de la build: ")
            if(procesamiento.existe_nombre(path_builds, id_build, 0)):
                break
            else:
                print("La build no se encuentra registrada, ingrese otro por favor.")
        return procesamiento.eliminar(path_builds,id_build)

    def ejecutar_operacion():
        opciones = {
            "1-1" : insertar_heroes,
            "1-2": ver_heroes,
            "1-3": actualizar_heroes,
            "1-4": eliminar_heroes,
            "2-1" : insertar_items,
            "2-2": ver_items,
            "2-3": actualizar_items,
            "2-4": eliminar_items,
            "3-1": insertar_builds,
            "3-2": ver_builds,
            "3-3": actualizar_builds,
            "3-4": eliminar_builds
        }
        return opciones[operacion]()  

    return ejecutar_operacion()