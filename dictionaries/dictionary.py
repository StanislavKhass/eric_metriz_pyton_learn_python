#Работа со словарями

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


#Упражнение 6.7
print("\nУпражнение 6.7")

user01 = {
    'first_name' : 'Stas',
    'last_name' : 'Khass',
    'age': '38',
    'town': 'New York'
}

user02 = {
    'first_name' : 'Evgeny',
    'last_name' : 'Gricenko',
    'age': '39',
    'town': 'Taskkent'
}

user03 = {
    'first_name' : 'Nadejda',
    'last_name' : 'Gricenko',
    'age': '39',
    'town': 'Tashkent'
}

people = [user01,user02,user03]

for i in people:
    print("Вывод данных о пользователе:")
    for key, value in i.items():
        print(f"Поле {key} , значение поля :{value}" )


#Упражнение 6.8

print("\nУпражнение 6.8")

pet01 = {
    'name_of_pet' : 'Kair',
    'owner' : 'Stanislav Khass',
    'type_of_pet': 'Dog'
}

pet02 = {
    'name_of_pet' : 'Nusha',
    'owner' : 'Ekaterina Khass',
    'type_of_pet': 'Cat'
}

pets = [pet01,pet02]

for cur_pet in pets:
    print("Выводим информацию о животном:")
    for key, value in cur_pet.items():
        print(f"Поле {key} , значение поля :{value}" )

#Упражнение 6.9

print("\nУпражнение 6.9")

favorite_places = {
    "New York" : "Соеденные Штаты Америки",
    "Moscow" : "Россиская федерация",
    "Berlin" : "Германия",
    "Paris" : "Париж"
}

person1 = {
    "first-name" : "Stas",
    "last-name" : "Khass",
    "favorite_place" : [favorite_places['New York'],favorite_places['Moscow']]
}

person2 = {
    "first-name" : "Ekaterina",
    "last-name" : "Khass",
    "favorite_place" : [favorite_places['Berlin']]
}

ppl_with_places = [person1,person2]

for ppl in ppl_with_places:
    print("Новый человек")
    for key , value in ppl.items():
        if key == "first-name" or key == "favorite_place":
            print(f"Ключ {key} , значение ключа {value}")


#Упражнение 6.10
print("\nУпражнение 6.10")
favorit_numbers2 = {
    'Стас':[11,12],
    'Катя': [12,13],
    'Елена': [13,14,15],
    'Евгений': [14],
    'Алена':[15] ,   
}      

for key , value in favorit_numbers2.items():
     print(f"Имя человека {key} ")
     for cur_like_number_index in range(len(value)):
         print(f"- Любимое число  {value[cur_like_number_index]}")

#Упражнение 6.11
print("\nУпражнение 6.11")       

dic_New_york = {
    "country" : "USA",
    "population" : 8_500_000,
    "fact" : "Покупка острова манхент произведена у индейцев в 1626 за 24 доллара"
}
     

dic_Berlin = {
    "country" : "Germany",
    "population" : 3_560_000,
    "fact" : "Самый большой железно дорожный вокзал в европе"
}     

dic_Paris = {
    "country" : "France",
    "population" : 2_200_000,
    "fact" : "Самая посещаемая страна туристами из других стран"
}  

cities = {
    "Нью Йорк" : dic_New_york,
    "Берлин" : dic_Berlin,
    "Париж" : dic_Paris
}

for key , value in cities.items():
    print(f"\nНащ город называется : {key}")
    for key_in, vlaue_in in value.items():
        if key_in == "country":
            print(f"Название страны {vlaue_in}")
        if key_in == "population":
            print(f"Население города {vlaue_in}")       
        if key_in == "fact":
            print(f"Инересный факт о городе {vlaue_in}")                 
