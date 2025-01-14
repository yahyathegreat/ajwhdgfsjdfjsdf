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
def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_numeral = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_numeral += syb[i]
            num -= val[i]
        i += 1
    return roman_numeral

print(int_to_roman(1994))
class Dog:
    def __init__(self, breed, age, name):
        self.breed = breed
        self.age = age
        self.name = name
    
    def display_info(self):
        return f"Dog Name: {self.name}, Breed: {self.breed}, Age: {self.age}"

dog = Dog("Golden Retriever", 3, "Buddy")
print(dog.display_info())
