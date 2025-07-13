# class Student:
#     def __init__(self, name, grade, password):
#         self.name = name
#         self._grade = grade
#         self.__password = password
        
#     def change_password(self, new_pass):
#         self.__password = new_pass
    
#     def get_info(self):
#         return print(f"Name:{self.name}, your grade: {self._grade}")
    
    
# student = Student("Anvar", 4, 12334)
# student.get_info()
# print(student._Student__password)    

# student.change_password(78906)    
# print(student._Student__password)
        
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Car moving")

    def stop(self):
        print("Car stopped")

class Bike(Vehicle):
    def move(self):
        print("Bike moving")

    def stop(self):
        print("Bike stopped")

car = Car()
car.move()
car.stop()

bike = Bike()
bike.move()
bike.stop()

           