class Transport:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        
    def move(self):
        print("Transport is moving")
    
class Car(Transport):
    def __init__(self, name, speed, color):
        super().__init__(name, speed)
        self.color = color

    def move(self):
        super().move()
        print("Car is driving")


class Plane(Transport):
    def __init__(self, name, speed, fuel):
        super().__init__(name, speed)
        self.fuel = fuel

    def move(self):
        super().move()
        print("Plane is flying")


class Boat(Transport):
    def __init__(self, name, speed, sail):
        super().__init__(name, speed)
        self.sail = sail

    def move(self):
        super().move()
        print("Boat is sailing")


car = Car("Porshe", 350, "Black")
plane = Plane("Boeing", 900, "Jet Fuel")
boat = Boat("Yacht", 40, "White Sail")

car.move()
plane.move()
boat.move()