from crud import operacion_crud
from Heroes import Heroes
from procesamiento import existe_nombre

def main():
    #exit = 0
    #heroe = Heroes("Nombre: ","Fuerza: ","Mana: ","Armadura: ","Daño: ","Resistencia magica: ","Velocidad de movimiento: ","Velocidad de ataque: ")
    while(True):
        option = input("""
        ------ARMA TU PROPIA BUILD ------
        1 -> Heroe
        2 -> Item
        3 -> Build
        4 -> Salir
        ---------------------------------
        """)

        if(option == "4"):
            break

        option_crud = (input("""
        ---------------------------------
        1 -> Insertar
        2 -> Ver
        3 -> Actualizar
        4 -> Eliminar
        ---------------------------------
        """))

        operacion_crud(f"{option}-{option_crud}")

    
if __name__ == "__main__":
    main()