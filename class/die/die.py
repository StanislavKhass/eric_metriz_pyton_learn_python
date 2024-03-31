from random import randint

#Упражнение 9.13 добавляем класс как аргумент
class Die():
    def __init__(self,number_of_die):
        self.sides = number_of_die


    def roll_die(self):
        number = randint(1, self.sides)
        return number
        
    def get_dies(self):
        number = self.sides
        return number
        
        
my_die_six = Die(6)
for x in range(1,11):
    print(f"Номер броска: {x} , выповшая сторона: {my_die_six.roll_die()} из граней {my_die_six.get_dies()}")

print(" ")    

my_die_ten = Die(10)
for x in range(1,11):
    print(f"Номер броска: {x} , выповшая сторона: {my_die_ten.roll_die()} из граней {my_die_ten.get_dies()}") 

print(" ")      
    
my_die_twen = Die(20)
for x in range(1,11):
    print(f"Номер броска: {x} , выповшая сторона: {my_die_twen.roll_die()} из граней {my_die_twen.get_dies()}")      


