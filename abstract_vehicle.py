from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    def __init__(self, tires ):
            self.tires = tires
            
            
    
    def start(self):
            pass
            
    def display(self):
        print("vehicle with", self.tires, "tires")
        
@abstractmethod
            
class Bike(Vehicle):
    
    def __init__(self, color):
        super().__init__(2)
        self.color = color
        
    def start(self):
        print("start with kick")
        
class scooty(Vehicle):
    
    def __init__(self):
        super().__init__(2)
        
    def start(self):
        print("self start")
        
        
class Car(Vehicle):
    
    def __init__(self):
        super().__init__(4)
        
    def start(self):
        print("start with key")
      
      
class Truck(Vehicle):

    def __init__(self):
        super().__init__(8)

    def start(self):
        print("truck starts with button")
        
bike = Bike("Black")
bike.start()
bike.display()

scooty = scooty()
scooty.start()

Car = Car()
Car.start()

truck = Truck()
truck.start()
truck.display()
