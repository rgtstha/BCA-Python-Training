class Car:
    def __init__(self, name, color, fuel_type):
        self.name = name
        self.color = color
        self.fuel_type = fuel_type

    def start(self):
        print(f"Starting car {self.name} {self.color} {self.fuel_type}")
        
 
car_1 = Car("BMW", "red", "petrol")
car_2 = Car("Audi", "blue", "diesel")

car_1.start()
car_2.start()