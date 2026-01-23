# Module 1 exercise was completed during an in-class seminar
# Vehicle Management System – Object-Oriented Class Hierarchy
# Seminar 1 Task: Create a class hierarchy for a simple vehicle management system (e.g., Vehicle as a base class, with subclasses like Car, Bike, and Truck)
# Solution: 
from abc import ABC, abstractmethod
from datetime import date
class Vehicle(ABC):
    """Base class for all vehicles demonstrating abstraction"""
    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight  # kg
        self.__mileage = 0  # Private attribute for encapsulation
        self.service_history = []
    
    @abstractmethod
    def get_vehicle_type(self):
        """Abstract method - must be implemented by subclasses"""
        pass    
    def add_mileage(self, km):
        """Demonstrates encapsulation with validation"""
        if km < 0:
            raise ValueError("Mileage cannot be negative")
        self.__mileage += km
    
    def get_mileage(self):
        """Getter for private attribute"""
        return self.__mileage
    
    def add_service_record(self, service_type, date_serviced=date.today()):
        """Adds a service record to history"""
        self.service_history.append({
            'date': date_serviced,
            'service_type': service_type,
            'mileage': self.__mileage
        })
    
    def get_service_history(self):
        """Returns formatted service history"""
        return [f"{record['date']}: {record['service_type']} at {record['mileage']}km" 
                for record in self.service_history]
    
    def __str__(self):
        """String representation of the vehicle"""
        return f"{self.year} {self.make} {self.model} ({self.get_vehicle_type()})"
class Car(Vehicle):
    """Concrete class representing cars"""
    def __init__(self, make, model, year, weight, num_doors, fuel_type):
        super().__init__(make, model, year, weight)
        self.num_doors = num_doors
        self.fuel_type = fuel_type
    
    def get_vehicle_type(self):
        return "Car"
    def calculate_tax(self):
        """Specific to cars - based on weight and fuel type"""
        base = self.weight * 0.5
        if self.fuel_type.lower() == 'electric':
            return base * 0.5  # Discount for electric
        return base
class Bike(Vehicle):
    """Concrete class representing bikes"""
    def __init__(self, make, model, year, weight, bike_type):
        super().__init__(make, model, year, weight)
        self.bike_type = bike_type  # e.g., 'Mountain', 'Road', 'Hybrid'
    def get_vehicle_type(self):
        return f"{self.bike_type} Bike"
    def calculate_tax(self):
        """Bikes have fixed tax rate"""
        return 25
class Truck(Vehicle):
    """Concrete class representing trucks"""
    def __init__(self, make, model, year, weight, max_load, num_axles):
        super().__init__(make, model, year, weight)
        self.max_load = max_load  # kg
        self.num_axles = num_axles
    
    def get_vehicle_type(self):
        return "Truck"
    
    def calculate_tax(self):
        """Truck tax based on axles and max load"""
        return (self.num_axles * 100) + (self.max_load * 0.1)
class FleetManager:
    """Class demonstrating composition and encapsulation"""
    
    def __init__(self):
        self.__vehicles = []
    
    def add_vehicle(self, vehicle):
        if not isinstance(vehicle, Vehicle):
            raise TypeError("Only Vehicle objects can be added")
        self.__vehicles.append(vehicle)
    
    def remove_vehicle(self, make, model, year):
        """Removes vehicle by attributes"""
        for v in self.__vehicles:
            if v.make == make and v.model == model and v.year == year:
                self.__vehicles.remove(v)
                return True
        return False
    
    def get_vehicles_by_type(self, vehicle_type):
        """Returns filtered list of vehicles"""
        return [v for v in self.__vehicles if vehicle_type.lower() in v.get_vehicle_type().lower()]
    
    def get_total_mileage(self):
        """Returns sum of all vehicle mileage"""
        return sum(v.get_mileage() for v in self.__vehicles)
    
    def get_fleet_tax(self):
        """Calculates total tax for all vehicles"""
        return sum(v.calculate_tax() for v in self.__vehicles)
    
    def __str__(self):
        """String representation of fleet"""
        return f"Fleet with {len(self.__vehicles)} vehicles"
# Demonstration
if __name__ == "__main__":
    print("=== Vehicle Management System ===")
    
    # Create some vehicles
    car1 = Car("Toyota", "Camry", 2020, 1500, 4, "Hybrid")
    car2 = Car("Tesla", "Model 3", 2022, 1700, 4, "Electric")
    bike1 = Bike("Trek", "FX 2", 2021, 12, "Hybrid")
    truck1 = Truck("Ford", "F-150", 2019, 2500, 2000, 2)
    
    # Add some mileage and service records
    car1.add_mileage(15000)
    car1.add_service_record("Oil change")
    car1.add_service_record("Tire rotation")
    
    car2.add_mileage(5000)
    car2.add_service_record("Software update")
    bike1.add_mileage(300)
    truck1.add_mileage(45000)
    
    # Create and populate fleet
    fleet = FleetManager()
    fleet.add_vehicle(car1)
    fleet.add_vehicle(car2)
    fleet.add_vehicle(bike1)
    fleet.add_vehicle(truck1)
    
    # Demonstrate functionality
    print("\nAll Vehicles:")
    for vehicle in fleet.get_vehicles_by_type(""):
        print(f"- {vehicle} with {vehicle.get_mileage()}km")
    
    print("\nCars in Fleet:")
    for car in fleet.get_vehicles_by_type("car"):
        print(f"- {car} (Tax: ${car.calculate_tax():.2f})")
    
    print("\nService History for Toyota Camry:")
    for record in car1.get_service_history():
        print(f"  {record}")
    
    print(f"\nFleet Statistics:")
    print(f"Total mileage: {fleet.get_total_mileage()}km")
    print(f"Total annual tax: ${fleet.get_fleet_tax():.2f}")