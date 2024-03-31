from random import choice
#Упражнение 9.14 добавляем класс как аргумент
class Lottery():
    def __init__(self):
        self.lottery_base = [ 1, 2, 3 , 4 , 5 , 6 , 7 ,8 ,9 ,0 , "A" , "B" , "C", "D", "E"]
        self.myticket_base = [ 1, 2, 3 , 4 , 5 , 6 , 7 ,8 ,9 ,0 , "A" , "B" , "C", "D", "E"]
        
    def get_win_numbers(self):
        number_one = choice(self.lottery_base)
        self.lottery_base.remove(number_one)
        
        number_two = choice(self.lottery_base)
        self.lottery_base.remove(number_two)
        
        number_three = choice(self.lottery_base)
        self.lottery_base.remove(number_three)
        
        number_four = choice(self.lottery_base)
        self.lottery_base.remove(number_four)
        return number_one, number_two , number_three , number_four
        
    def get_ticet(self):
        number_one = choice(self.myticket_base)
        self.myticket_base.remove(number_one)
        
        number_two = choice(self.myticket_base)
        self.myticket_base.remove(number_two)
        
        number_three = choice(self.myticket_base)
        self.myticket_base.remove(number_three)
        
        number_four = choice(self.myticket_base)
        self.myticket_base.remove(number_four)
        self.myticket_base = [ 1, 2, 3 , 4 , 5 , 6 , 7 ,8 ,9 ,0 , "A" , "B" , "C", "D", "E"]
        return number_one, number_two , number_three , number_four       
      


lottery_win = Lottery()
numbers_win = lottery_win.get_win_numbers()
print(f"Номера лотереи которые выйграли : {numbers_win}")


iterration_count = 0

while True:
    myticket = lottery_win.get_ticet()
    print(myticket)

    if (myticket[0] == numbers_win[0]) and \
    (myticket[1] == numbers_win[1]) and \
    (myticket[2] == numbers_win[2]) and \
    (myticket[3] == numbers_win[3]):
        break
    

    iterration_count +=1


print(f"Tottal count {iterration_count}")    