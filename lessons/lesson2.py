#Наследование


#Родительский класс или супер класс
class Hero:
    
    def __init__(self, name, lvl, age, hp):
        self.name = name
        self.lvl = lvl
        self.age = age
        self.hp = hp
        
    def action(self):
        return print(f"Base action")
    
#П
    
#Дочерний класс
class MegaHero(Hero):
    
    
    def __init__(self, name, lvl, age, hp, mp):
        super().__init__(name, lvl, age, hp)
        self.mp = mp        
hero = MegaHero("Hero1", 100, 26, 1000, 100)
print(hero)




