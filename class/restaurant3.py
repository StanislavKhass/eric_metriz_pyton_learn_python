#Упражнение из книги 9.6 Обьявляем класс
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

#Это то что называется наследованием класса.
#Особая разновидность ресторна - Киоск с мороженным
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Кокосовое","Фисташковое","Клубника"]

    def show_all_flavors(self):
        for i in range(0,len(self.flavors)):
                print(f"Сорт мороженного:{self.flavors[i]}")


resaurant_of_my_dream = IceCreamStand("Мечта", "Италия")

resaurant_of_my_dream.show_all_flavors()

#test
