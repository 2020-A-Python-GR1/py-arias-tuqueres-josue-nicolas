class Heroes:
    nombre = None
    health = None
    mana = None
    armor = None
    damage = None
    arcana = None

    def __init__(self, nombre, health, mana, armor, damage, arcana):
        self.nombre = nombre
        self.health = health
        self.mana = mana
        self.armor = armor
        self.damage = damage
        self.arcana = arcana

    def __str__(self):
        return f"{self.nombre};{self.health};{self.mana};{self.armor};{self.damage};{self.arcana}"
    

