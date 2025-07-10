class Car:
    def __init__(self, speed, price, color):
        self.speed = speed
        self.price = price
        self.color = color
    
    def present(self):
        return print(f"Characteristics og your car {self.speed, self.price, self.color}")
    
porshe = Car(350, 240000, "black" )
bmw = Car(240, 50000, "green")

porshe.present()
bmw.present()