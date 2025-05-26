class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def get_brand(self):
        return self.brand + "!"
    
    def full_name(self):
        return f"{self.brand} {self.model}"

class Electric_Car(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size 

        
my_car = Car("Nissan", "Ultima")
print(my_car.full_name())

my_new_car = Car("Range-Rover", "Defender")
print(my_new_car.full_name())

my_electric_car = Electric_Car("Tesla", "Model I", "Battery capacity: 50kWh")
print(my_electric_car.full_name())
