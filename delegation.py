class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def get_brand(self):
        return self.brand + "!"
    
    def full_name(self):
        return f"{self.brand} {self.model}"

class ElectricCar:
    def __init__(self, car, battery_size):
        self.car = car
        self.battery_size = battery_size

    def get_brand(self):
        return self.car.get_brand()

    def full_name(self):
        return self.car.full_name()

my_car = Car("Nissan", "Ultima")
print(my_car.full_name())

my_new_car = Car("Range-Rover", "Defender")
print(my_new_car.full_name())

my_electric_car = ElectricCar(Car("Tesla", "Model I"), "Battery capacity: 50kWh")
print(my_electric_car.full_name())
print(my_electric_car.battery_size)
