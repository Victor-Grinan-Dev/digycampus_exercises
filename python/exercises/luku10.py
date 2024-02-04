import random

from apuluokat import PlayingCard, Suit
from apuluokat import Deck as t_deck
from apuluokat import Hand as t_hand

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
   
    Jani = Employee("Jani")
    Simo = Employee("Simo")
    Tiina = Employee("Tiina")
    Elli = Employee("Elli")

    list_employees = [Jani, Simo, Tiina, Elli]
    # list_employees = [Jani]

    for day in range(365 * 4):
        for employee in list_employees:
            add_hours = random.randint(2, 16)
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
def sel(self):
    is_flush = set()
    for card in self.__cards:
        is_flush.add(card.get_suit())
    if len(is_flush) == 1:
        return True
    return False


#ex.5
#The method to add to ex 5:
def find_pairings(self):
    paria = 0
    kolmosta = 0
    nelosta = 0
    cards_in_hand = []
    for card in self.__cards:
        cards_in_hand.append(card.get_value())
    uniques = list(set(cards_in_hand))
    for card in uniques:
        count = cards_in_hand.coun(card)   
        if int(count) == 2:
            paria += 1
        elif count == 3:
            kolmosta += 1
        elif count >= 4:
            nelosta += 1
    
    return paria, kolmosta, nelosta
       
    
def test_5():
    my_deck = t_deck(luo_korttipakka(True))

    for testi in range(100):
        my_deck.shuffle()
        hand = Hand()
        hand.add_card(my_deck.deal())
        hand.add_card(my_deck.deal())
        hand.add_card(my_deck.deal())
        hand.add_card(my_deck.deal())
        hand.add_card(my_deck.deal())
        
        parit, kolmoset, neloset = hand.find_pairings()

        if parit > 1 or kolmoset == 1 or neloset == 1:
            print("Käsi nro", testi, ":", hand)
            print("Pareja:", parit)
            print("Kolmosia:", kolmoset)
            print("Nelosia:", neloset)


#ex.6
#The method to add to ex 6:
def find_straight(self, ace_is_high_card):
    result = True
    card_values = []
    for card in self.__cards:
        if card.get_value() != 1:
            card_values.append(card.get_value())
        elif card.get_value() == 1 and not ace_is_high_card:
            card_values.append(card.get_value())
        else:
            card_values.append(14)
    card_values.sort()  
    min_value = min(card_values)    
    index = 0
    while result and index < len(card_values):
        if not card_values[index] == index + min_value:
            result = False
            break
        index += 1
    return result


def test_6():
    hand = t_hand()     
    hand.add_card(PlayingCard(Suit("Spade"), 11))
    hand.add_card(PlayingCard(Suit("Diamond"), 12))
    hand.add_card(PlayingCard(Suit("Diamond"), 13))
    hand.add_card(PlayingCard(Suit("Heart"), 10))
    hand.add_card(PlayingCard(Suit("Heart"), 1)) 

    # hand.add_card(PlayingCard(Suit("Spade"), 4))
    # hand.add_card(PlayingCard(Suit("Heart"), 3))
    # hand.add_card(PlayingCard(Suit("Diamond"), 2))
    # hand.add_card(PlayingCard(Suit("Diamond"), 5))
    # hand.add_card(PlayingCard(Suit("Heart"), 1))

    if hand.find_straight(False) or hand.find_straight(True):
        print('löytyi suora!')
    else:
        print('suoraa ei löytynyt!')

#ex.7
#add this method to the class hand
def get_rank(self):

    pairs, threes, fours = self.__find_pairings()
    is_flush = self.__find_flush()
    is_straight = self.__find_straight(True) or self.__find_straight(False)

    if is_flush and is_straight and self.__find_straight(True):
        #'Royal Flush',
        self.__adjust_rank(1)
    elif is_flush and is_straight:
        #'Straight Flush',
        self.__adjust_rank(2)
    elif fours:
        #'Four of a Kind',
        self.__adjust_rank(3)
    elif threes and pairs:
        #'Full House',
        self.__adjust_rank(4)
    elif is_flush:
        #'Flush',
        self.__adjust_rank(5)
    elif is_straight:
        #'Straight',
        self.__adjust_rank(6)
    elif threes and not pairs:
        #'Three of a Kind',
        self.__adjust_rank(7)
    elif pairs == 2:
        #'Two Pair',
        self.__adjust_rank(8)
    elif pairs == 1:
        #'One Pair',
        self.__adjust_rank(9)
    else: 
        self.__adjust_rank(10)

    return self.__rank

def test_ex_7():
    cards = luo_korttipakka(lista=True)
    deck = t_deck(cards)
    deck.create_52_deck()
    testit = 10
    for t in range(testit):
        deck.shuffle()
        hand = Hand() 
        for _ in range(5):
            hand.add_card(deck.deal())
        print('Kierros:', t+1, 'rank:', end=' ')
        print(hand.get_rank_string())
        print(hand, end = '\n\n')

    # TEST CASE 4
    hand = Hand()
    hand.add_card( PlayingCard(Suit("Spade"), 1))
    hand.add_card( PlayingCard(Suit("Spade"), 2))
    hand.add_card( PlayingCard(Suit("Spade"), 3))
    hand.add_card( PlayingCard(Suit("Spade"), 4))
    hand.add_card( PlayingCard(Suit("Spade"), 5))


    print('*****************************************************************************')
    print(hand)
    print(hand.get_rank_string())
    if hand.get_rank() == 2:
        print('oikein!')
    else:
        print('väärin!')

if __name__ == '__main__':
    # test_ex_1()
    # test_ex_1_once()
    # luo_korttipakka()
    # test_6()
    # test_ex_7()
    pass