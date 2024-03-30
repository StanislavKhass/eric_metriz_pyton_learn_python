#Упражнение 9.12 Переписываем класс администратор
from multi_users_module import Users

class Admin(Users):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


class Privileges():
    def __init__(self):
        self.privileges = ["Разрешенно добавлять сообщения","Разрешенно удалять пользователей","Разрешенно менять пароль","Разрешенно банить пользователей"]

    def show_privileges(self):
        for i in range(0,len(self.privileges)):
            print(f"Уровень доступа:{self.privileges[i]}")



