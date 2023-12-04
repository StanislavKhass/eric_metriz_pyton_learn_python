#Упражнение из книги 9.1 Обьявляем класс
class Restaurant():
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Название нашего ресторона {self.restaurant_name}")
        print(f"Кухня в ресторане: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт")

#Создаем экземпляп
restaurant = Restaurant("Happy Hour" , "Russian street food")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
print(" ")
restaurant.describe_restaurant()
restaurant.open_restaurant()

print(" ")

#9.2 Создаем 3 экземпдяра
daveOnDrive_restaurant = Restaurant("Dave On Drive" , "American Street food")

indianBliss_restaurant = Restaurant("Indian Bliss" , "Indian food")

mahito_restaurant = Restaurant("Mahito" , "Mexican food")


daveOnDrive_restaurant.describe_restaurant()
print(" ")
indianBliss_restaurant.describe_restaurant()
print(" ")
mahito_restaurant.describe_restaurant()
