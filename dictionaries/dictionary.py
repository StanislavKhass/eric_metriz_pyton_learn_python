#словарь содержащий данные пользователе
person_user = {
    'first_name' : 'Stas',
    'last_name' : 'Khass',
    'age': '38',
    'town': 'New York'
}

#словать содержащий значения любимых чисел
favorit_numbers = {
    'stas':11,
    'katy-sister': 12,
    'father': 13,
    'mother': 14,
    'alena':15    
}

#Словарь голосарий
golosari = {
    'variable': "значение в памяти компьютера",
    'function': "часть исполняемых шагов кода , где есть входные значения и выходные",
    'condition': 'Условие для выполнения кода',
    'Statment' : 'Инструкция для чего либо, состоящая из шагов , инструкция как делать правильный код',
    'Method' : 'тоже что и функция , только вызывается через точку'
}

#способы при котором мы достаем ключ и значение

print("Выводим значения словаря person_user\n")
for x , y in person_user.items():
    print("Ключ :", x, "Значение :", y)

#способ при котором достаем значение ключа
print("Выводим значения словаря favorit_numbers\n")    
for x in favorit_numbers.keys():
    print("Ключ :", x)

#способ при котором достаем значение значения
print("Выводим значения словаря golosari \n")    
for x in golosari.values():
    print("Значение :", x)    

#Обьявление пустого словаря и создание вложенных словарей
empty_dict = {} 
empty_dict["first_name"] = "Stanislav"
empty_dict["last_name"] = "Khass"
empty_dict["favorit_book"] = {}
empty_dict["favorit_book"]["1book"] = "Python"
empty_dict["favorit_book"]["2book"] = "c++"
empty_dict["favorit_book"]["3book"] = "test.com"

print(empty_dict)