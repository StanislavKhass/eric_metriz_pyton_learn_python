#Упражнение из книги 9.4 Обьявляем класс
class Restaurant():
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Название нашего ресторона {self.restaurant_name}")
        print(f"Кухня в ресторане: {self.cuisine_type}")
        print(f"Количество обслуженных клиентов: {self.number_served}")

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт")

    def change_number_of_served(self, number):
        self.number_served = self.number_served + number



restaurant = Restaurant("My best rest", "Made with love")

restaurant.describe_restaurant()

restaurant.number_served= 50

print("--- Обновили переменную")

restaurant.describe_restaurant()

print("--- Обновили переменную черег метод")

restaurant.change_number_of_served(200)
restaurant.describe_restaurant()
