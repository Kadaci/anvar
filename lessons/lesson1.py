class Hero:
    #конструктор класса
    def __init__(self, name, lvl, hp):
        # снизу это атрибуты класса, они также как переменные хранят в себе что-то
        self.name = name
        self.lvl = lvl
        self.hp = hp
    #методы класса
    def introduce(self):
        return print(f"hello, i'm {self.name}")
    
    
kirito = Hero("kirito", 100, 1000)
kirito.introduce()
print(kirito.name, kirito.lvl)