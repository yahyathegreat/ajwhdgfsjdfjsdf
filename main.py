class Vehicle:
    def __init__(self, name, base_fare):
        self.name = name
        self.base_fare = base_fare
    
    def display_info(self):
        return f"Vehicle: {self.name}, Base Fare: {self.base_fare}"

class Bus(Vehicle):
    def __init__(self, name, base_fare, num_passengers):
        super().__init__(name, base_fare)
        self.num_passengers = num_passengers
    
    def total_fare(self):
        return self.base_fare * self.num_passengers
    
    def display_info(self):
        return f"Bus: {self.name}, Base Fare: {self.base_fare}, Passengers: {self.num_passengers}, Total Fare: {self.total_fare()}"

bus = Bus("City Bus", 2, 50)
print(bus.display_info())
