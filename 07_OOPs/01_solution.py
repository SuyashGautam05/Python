class Car:  #class

    total_car = 0

    #constructor
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car = Car.total_car + 1

    # def get_brand(self):
    #     return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def fuel_type(self):
        return "Petrol and Diesel"

my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())


my_new_car = Car("Tata", "Safari")
# print(my_new_car.model)

#inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric Charge"

my_tesla = ElectricCar("tesla", "Model s", "85kwh")
# print(my_tesla.model)
# print(my_tesla.full_name())
# print(my_tesla.battery_size)
print(my_tesla.fuel_type())


safari = Car("Tata", "Safari")
safariThree = Car("Tata", "Nexon")
print(safari.fuel_type())
print(Car.total_car)
