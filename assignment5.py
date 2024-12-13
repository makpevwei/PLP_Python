# Assignment 1: Design Your Own Class

# Creating a class for a "Smartphone"
class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery_life = battery_life

    def display_specs(self):
        return f"{self.brand} {self.model}: {self.storage}GB, {self.battery_life} hours battery life."

    def charge(self):
        return f"{self.model} is now charging."

# Adding an inherited class for a "GamingSmartphone"
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, cooling_system):
        super().__init__(brand, model, storage, battery_life)
        self.cooling_system = cooling_system

    def display_specs(self):
        return f"{self.brand} {self.model} (Gaming Edition): {self.storage}GB, {self.battery_life} hours battery life, Cooling System: {self.cooling_system}."

    def enable_gaming_mode(self):
        return f"{self.model}'s gaming mode enabled with enhanced cooling!"

# Demonstration
smartphone = Smartphone("Samsung", "Galaxy S22", 128, 24)
gaming_smartphone = GamingSmartphone("Asus", "ROG Phone 6", 512, 18, "Active Cooling")

print(smartphone.display_specs())
print(smartphone.charge())
print(gaming_smartphone.display_specs())
print(gaming_smartphone.enable_gaming_mode())


# Activity 2: Polymorphism Challenge

# Base class for "Vehicle"
class Vehicle:
    def move(self):
        pass

# Derived classes
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚢"

# Demonstration of polymorphism
vehicles = [Car(), Plane(), Boat()]
for vehicle in vehicles:
    print(vehicle.move())
