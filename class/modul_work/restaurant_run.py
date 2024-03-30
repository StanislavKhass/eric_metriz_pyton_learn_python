#Упражнение из книги 9.10 Импортирование из модуля
from restaurant_module  import Restaurant


my_restorant = Restaurant("Вкусно и точка", "Американская")

my_restorant.change_number_of_served(2)
my_restorant.change_number_of_served(4)
my_restorant.change_number_of_served(2)
my_restorant.change_number_of_served(6)

my_restorant.describe_restaurant()