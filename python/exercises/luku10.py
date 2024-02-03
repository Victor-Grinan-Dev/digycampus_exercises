import random
from apuluokat import PlayingCard, Suit

class MyEmployee:
   
    days_since_raise = 0
    __salary = 2000
    __total_hours = 0

    def __init__(self, name):
        self.name = name

    def complete_workday(self, hours):
        self.__total_hours += hours
        # self.__hours += hours 
        # days = self.__hours // 6
        # if self.__hours % 6 > 0:
        #     self.__hours = self.__hours % 6
        #     self.days_since_raise += days
        if hours > 6:
            self.days_since_raise += 1
    
    def eligible_for_raise(self):
        return self.days_since_raise > 365 
    
    def give_raise(self, percentage_increase):
        self.__salary += self.salary * (percentage_increase/100)
        self.days_since_raise = 0
        
    @property
    def salary(self):
        return round(self.__salary, 1)
    
    @property
    def hours(self):
        return self.__total_hours

class Employee:
   
    days_since_raise = 0
    salary = 2000
    hours = 0

    def __init__(self, name):
        self.name = name

    def complete_workday(self, hours):
        self.hours += hours
        if hours > 6:
            self.days_since_raise += 1
    
    def eligible_for_raise(self):
        return self.days_since_raise > 365
    
    def give_raise(self, percentage_increase):
        self.salary += self.salary * (percentage_increase/100)
        self.days_since_raise = 0 

def test_ex_1():
    print("Testatan luokan koko toimintokirjoa!")
    Jani = Employee("Jani")
    Simo = Employee("Simo")
    Tiina = Employee("Tiina")
    Elli = Employee("Elli")

    list_employees = [Jani, Simo, Tiina, Elli]
    # list_employees = [Jani]

    for day in range(365 * 4):
        for employee in list_employees:
            add_hours = random.randint(2, 16)
            # print('add hour:', add_hours)
            employee.complete_workday(add_hours)
            if employee.eligible_for_raise():
                print("Day:", day)
                print(employee.name, "is eligible for a raise, after having worked for", employee.hours, "hours!")
                employee.give_raise(5)
                print("His/Her salary is now : ", employee.salary, "(+{}%)".format(5))
                

def test_ex_1_once():
    Jani = Employee("Jani")
    Jani.complete_workday(3000) 
    Jani.give_raise(5)
    print(Jani.salary)

#ex.2
def luo_korttipakka(lista:bool=False):
    suits = ("Spade", "Heart", "Club", "Diamond")
    pack = set()
    
    
    for suit_name in suits:
        suit = Suit(suit_name)
        for card_number in range(1,14):
            new_card = PlayingCard(suit, card_number)
            pack.add(new_card)
    if lista:
        list(pack)
    return pack
            
#ex.3
# add
# discard
# intersection
class Deck:
    dealt = set()
    def __init__(self, card_deck:list):
        self.card_deck = card_deck

    def deal(self):
        if len(self.dealt) > 40:
            return False
        else:
            #compare that choice card is not in dealt
            is_dealt = True
            while is_dealt:
                choice = random.choice(self.card_deck)
                if choice not in self.dealt:
                    is_dealt = False
                    #add choice to dealt 
                    self.dealt.add(choice)
            return choice
        
    def shuffle(self):
        self.dealt = []

if __name__ == '__main__':
    # test_ex_1()
    # test_ex_1_once()
    # luo_korttipakka()
    pass