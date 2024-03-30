#Упражнение 9.12 Переписываем класс администратор

class Users():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f" Имя пользователя {self.first_name}")
        print(f" Фамилия пользователя {self.last_name}")
        print(f" Количество попыток входа пользователя {self.login_attempts}")
        print("---")

    def greet_user(self):
        print(f" Привет {self.first_name}, {self.last_name}. Добро пожаловать в систему.")

    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1

    def reset_login_attempts(self):
        self.login_attempts = 0



