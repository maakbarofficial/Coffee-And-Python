class Car:
    total_cars = 0  # Variables

    def __init__(self, brand, model):
        self.__brand = brand  # private
        self.__model = model
        Car.total_cars += 1

    def get_brand(self):
        return self.__brand + " !"  # Encapsulation

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
        return "Petrol or Diesel"  # Polymorphism

    @staticmethod
    def general_description():
        return "Cars are means of transport"

    @property
    def model(self):
        return self.__model


my_car = Car("Toyota", "Corolla")
# my_car1 = Car("Toyota", "Corolla")
# print(my_car.brand)
# my_car.model = "Safari"
print(my_car.model)
print(my_car.full_name())

# print(my_car.general_description())
print(Car.general_description())


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)  # to access brand and model of Car Class
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"


tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(tesla.battery_size)
print(tesla.full_name())
# print(tesla.__brand)
print(tesla.get_brand())

print(my_car.fuel_type())
print(tesla.fuel_type())

print(Car.total_cars)

print(isinstance(tesla, Car))
print(isinstance(tesla, ElectricCar))


class Battery:
    def battery_info(self):
        return "This is battery"


class Engine:
    def engine_info(self):
        return "This is engine"


class ElectricCarPlus(Battery, Engine, Car):
    pass


my_new_tesla = ElectricCarPlus("Tesla", "Model S")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())
