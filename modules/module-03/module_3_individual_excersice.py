#Individual assignment
#Factory Method Pattern – Vehicle Creation System
from abc import ABC, abstractmethod

# Product
class Car(ABC):
   @abstractmethod
   def drive(self):
       pass

# Concrete Products
class Sedan(Car):
   def drive(self):
       return "Driving a Sedan - smooth and comfortable"

class SUV(Car):
   def drive(self):
       return "Driving an SUV - powerful and fast"

class Hatchback(Car):
   def drive(self):
       return "Driving a Hatchback - compact and efficient"

# Factory
class CarFactory(ABC):
   @abstractmethod
   def create_car(self):
       pass

# Concrete Factories
class SedanFactory(CarFactory):
   def create_car(self):
       return Sedan()

class SUVFactory(CarFactory):
   def create_car(self):
       return SUV()

class HatchbackFactory(CarFactory):
   def create_car(self):
       return Hatchback()

# Client Code
def client_code(factory: CarFactory):
   car = factory.create_car()
   print(car.drive())

# Usage
client_code(SedanFactory())      # Output: Driving a Sedan - smooth and comfortable
client_code(SUVFactory())        # Output: Driving an SUV - powerful and fast
client_code(HatchbackFactory())  # Output: Driving a Hatchback - compact and efficient