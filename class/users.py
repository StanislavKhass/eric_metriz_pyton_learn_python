#Упражнение 9.3
class Users():
    def __init__(self, first_name, last_name,age, model_of_car):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.model_of_car = model_of_car

    def describe_user(self):
        print(f" Имя пользователя {self.first_name}")
        print(f" Фамилия пользователя {self.last_name}")
        print(f" Возраст пользователя {self.age}")
        print(f" Модель машины у пользователя {self.model_of_car}")

    def greet_user(self):
        print(f" Привет {self.first_name}, {self.last_name}. Добро пожаловать в систему.")


user_first = Users("Stas","Khass","38","Tesla")

user_second = Users("Evgeni","Kosuhin","40","Zil")


user_first.describe_user()
user_first.greet_user()
print("")
user_second.describe_user()
user_second.greet_user()
