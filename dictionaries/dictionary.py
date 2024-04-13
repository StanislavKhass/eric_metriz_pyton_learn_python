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

#Словарь голосарий 6.3
golosari = {
    'variable': "значение в памяти компьютера",
    'function': "часть исполняемых шагов кода , где есть входные значения и выходные",
    'condition': 'Условие для выполнения кода',
    'Statment' : 'Инструкция для чего либо, состоящая из шагов , инструкция как делать правильный код',
    'Method' : 'тоже что и функция , только вызывается через точку',
    'Loop' : 'Конструкция позволящая выполнить многократно блок кода',
    'Array' : 'Массив данных' ,
    'Class' : 'структура данных ' ,
    'Object' : 'Обьект' ,
    'Parametr' : ' Обьявление параметра в функции', 
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
empty_dict["indicator"] = [1,2,3,4,5] 

print(empty_dict)

#Упражнение 6.4
for x, y in golosari.items():
    print("Термирн :", x , " , Значение" , y) 

#Упражнение 6.5
print("Упражнение 6.5")
rivers_country= {
    'Volga' : 'Russia',
    'Nil' : 'Egypt' , 
    'Amazonka' : 'Brazil' ,
} 

river_to_chooze = ['Volga','Nil']
country_to_chooze = ['Russia']

for x , y in rivers_country.items():
    if x in river_to_chooze:
        print("Река", x, "протекает в ", y)

for x , y in rivers_country.items():
    if y in country_to_chooze:
        print("Река", x, "протекает в ", y)        

#Упражнение 6.6
print("Упражнение 6.6")
favorite_language = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'Python' ,
}    

list_ppl_for_vote = ['jen','stanislav','bernyly','edward']

#for name , language in favorite_language.items():
#    print(f'{name.title()}s favorite language is {language.title()}')

for i in list_ppl_for_vote:
    if i in favorite_language.keys():
        print(f"Спасибо {i} что приняли участие в опаросе")
    else:
        print(f"Отправляю приглашение на опрос для {i}")
