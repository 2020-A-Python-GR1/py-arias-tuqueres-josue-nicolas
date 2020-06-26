class Items:
    nombre = None
    tipo = None
    costo = None
    activa = None
    pasiva = None

    def __init__(self, nombre, tipo, costo, activa, pasiva):
        self.nombre = nombre
        self.tipo = tipo
        self.costo = costo
        self.activa = activa
        self.pasiva = pasiva


    def __str__(self):
        return f"{self.nombre};{self.tipo};{self.costo};{self.activa};{self.pasiva}"
    

