#Упражнение 9.9
class Cars():
    #Простая модель машины
    def __init__(self, make, model, year):
        #Инициализируем атрибуты автомобиля
        #Имеем доступ на пряму к ним...
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_discriptive_name(self):
        #Возращает аккуратно отформатированное описание
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        #Выводит пробег машины в милях
        print(f"This car has {self.odometer_reading} mile on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        #Переопределяем значение в классе наследуемом
        print("This car use gas tank")

class ElectricCar(Cars):
    #Тут описывем электро мобили
    #Атрибуты специфические для автомобиля
    def __init__(self, make , model , year):
        super().__init__(make , model , year)
        self.battery_size = 75

    def describe_battery(self):
        #Выводим информацию о мощьости аккамулятрра
        print(f"This car has a {self.battery_size}-kWh battery")

    def fill_gas_tank(self):
        #У электро мобиля нет бензобака
        print("This car doesn't need a gas tank!")

my_new_car = Cars('Audi', 'a4', '2019')
print(my_new_car.get_discriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_new_car.update_odometer(10)
my_new_car.read_odometer()


my_used_car = Cars('Subaru', 'outback', 2015)
print(my_used_car.get_discriptive_name())

my_used_car.increment_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()


my_tesla = ElectricCar("Testla", "model s", 2019 )
print(my_tesla.get_discriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
