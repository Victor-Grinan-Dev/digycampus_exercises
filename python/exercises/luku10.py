import random

from apuluokat import PlayingCard, Suit
from apuluokat import Deck as t_deck

#ex.1
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

class MyEmployee:
    """This version makes more sense to me but the exercise ask different response"""
    days_since_raise = 0
    __salary = 2000
    __total_hours = 0

    def __init__(self, name):
        self.name = name

    def complete_workday(self, hours):
        """Here is the difference with the answer above"""
        self.__total_hours += hours
        self.__hours += hours 
        days = self.__hours // 6
        if self.__hours % 6 > 0:
            self.__hours = self.__hours % 6
            self.days_since_raise += days
    
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
        self.dealt = ()

#ex.4
#The method to add to ex 4:
def find_flush(self):
    is_flush = set()
    for card in self.__cards:
        is_flush.add(card.get_suit())
    if len(is_flush) == 1:
        return True
    return False


#ex.5
class Hand:
    def __init__(self):
        self.__cards = list()
        self.__rank = 20

    def add_card(self, card):
        self.__cards.append(card)

    def adjust_rank(self, new_rank):
        if new_rank < self.__rank:
            self.__rank = new_rank
            return True
        return False

    def get_high_card(self):
        high = -1
        for c in self.__cards:
            if c.get_value() > high:
                high = c.get_value()
            if c.get_value() == 1:
                high = 14
        return high

    def find_pairings(self):
        paria = 0
        kolmosta = 0
        nelosta = 0
        cards_in_hand = []
        
        for card in self.__cards:
            cards_in_hand.append(card.get_value())
        uniques = list(set(cards_in_hand))

        for card in uniques:
            count = cards_in_hand.count(card)   
            if int(count) == 2:
                paria += 1
            elif count == 3:
                kolmosta += 1
            elif count >= 4:
                nelosta += 1
        
        return paria, kolmosta, nelosta
       
    def __str__(self):
        sorted_cards = sorted(self.__cards)
        str_representation = ""
        for c in sorted_cards:
            str_representation += str(c) + ", "
        return str_representation.rstrip(', ')
    
def test_5():
    # cards = 
    my_deck = t_deck(luo_korttipakka(True))
    # print(my_deck)

    for testi in range(100):
        my_deck.shuffle()
        hand = Hand()
        hand.add_card(my_deck.deal())
        hand.add_card(my_deck.deal())
        hand.add_card(my_deck.deal())
        hand.add_card(my_deck.deal())
        hand.add_card(my_deck.deal())
        
        parit, kolmoset, neloset = hand.find_pairings()
        # print(hand.find_pairings())
        if parit > 1 or kolmoset == 1 or neloset == 1:
            print("Käsi nro", testi, ":", hand)
            print("Pareja:", parit)
            print("Kolmosia:", kolmoset)
            print("Nelosia:", neloset)

if __name__ == '__main__':
    # test_ex_1()
    # test_ex_1_once()
    # luo_korttipakka()
    test_5()
    pass