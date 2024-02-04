import random


# maa
class Suit:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


# kortti
class PlayingCard:
    def __init__(self, suit, value):
        self.__suit = suit
        self.__value = value

        if 1 < value < 11:  # numerokortti
            self.__name = str(value)
        elif 0 < value < 14:  # kuvakortti
            names = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
            self.__name = names[value]

    def get_value(self):
        return self.__value

    def get_suit(self):
        return self.__suit

    # tätä metodia kutsutaan, kun kutsutaan str(kortti), kortin ollessa PlayingCard-olio
    def __str__(self):
        return self.__name + " of " + self.__suit.get_name() + "s"

    # toteutetaan luokan vertailu merkkijonon perusteella (EI LIITY TEHTÄVÄÄN)
    def __eq__(self, other):
        if str(other) == str(self):
            return True
        else:
            return False

    # luokan hashaaminen (EI LIITY TEHTÄVÄÄN)
    def __hash__(self):
        return hash(str(self))

    # luokan vertaaminen itsensä kanssa (EI LIITY TEHTÄVÄÄN)
    def __gt__(self, other):
        return self.get_value() > other.get_value()


# pakka
class Deck:
    def __init__(self, cards):
        self.__cards = list(cards)
        self.__dealt = set()

    def create_52_deck(self):
        # Maat
        pata = Suit("Spade")
        hertta = Suit("Heart")
        risti = Suit("Club")
        ruutu = Suit("Diamond")

        maat = [pata, hertta, risti, ruutu]
        pakka = list()

        for m in maat:
            for x in range(1, 14):
                kortti = PlayingCard(m, x)
                pakka.append(kortti)
        self.__cards = pakka

    def deal(self):
        if len(self.__dealt) > 40:
            return False

        c = random.choice(self.__cards)
        while c in self.__dealt:
            c = random.choice(self.__cards)
        self.__dealt.add(c)
        return c

    def shuffle(self):
        self.__dealt = set()
    
    def __str__(self):
        for card in self.__cards:
            print(card)
        phrase = f"{len(self.__cards)-len(self.__dealt)} cards left"
        return phrase


class Hand:
    def __init__(self):
        self.__cards = list()
        self.__rank = 20

    def add_card(self, card):
        self.__cards.append(card)

    # metodi joka muuttaa käden arvoa (rank), jos uusi arvo on 
    # parempi (matalampi) kuin vanha
    # palauttaa True jos rank muuttui, False muuten
    def __adjust_rank(self, new_rank):
        if new_rank < self.__rank:
            self.__rank = new_rank
            return True
        return False

    def __get_high_card(self):
        high = -1
        for c in self.__cards:
            if c.get_value() > high:
                high = c.get_value()
            if c.get_value() == 1:
                high = 14
        return high

    # metodi palauttaa käden (Hand) kortit sanakirjassa
    # sanakirjan alkiot ovat arvoja (1-13) ja avaimet listoja (listan alkiot 
    # korttien merkkijonoesityksiä)
    def __get_dict_cards_in_order(self):
        cards_in_order = dict()

        for c in self.__cards:
            value = c.get_value()
            if value in cards_in_order:
                cards_in_order[value].append(str(c))
            else:
                cards_in_order[value] = [(str(c))]
        return cards_in_order

    # metodi, joka etsii käden korteista parit, kolmoset ja neloset ja 
    # palauttaa niiden lukumäärät
    def __find_pairings(self):
        cards_in_order = self.__get_dict_cards_in_order()
        pairs = 0
        threes = 0
        fours = 0
        for val in cards_in_order.keys():
            if len(cards_in_order[val]) == 2:
                pairs += 1
            elif len(cards_in_order[val]) == 3:
                threes += 1
            elif len(cards_in_order[val]) == 4:
                fours += 1
        return pairs, threes, fours

    # palauttaa True jos käsi sisältää värin, False muuten
    def __find_flush(self):
        suits = dict()

        first_suit = -1
        for c in self.__cards:
            suit = c.get_suit()
            if first_suit == -1:
                first_suit = suit
            elif first_suit != suit:
                return False
        return True

    # METODI JOKA PALAUTTAA True/False riippuen siitä, onko kädessä suora
    # argumentti ace_is_high_card(True/False) määrittää käsitelläänkö ässä
    # korkeimpana korttina vai matalimpana
    def __find_straight(self, ace_is_high_card):
        sorted_cards = self.__get_sorted_deck(ace_is_high_card)

        straight = True
        last_val = sorted_cards[0].get_value() \
            if not ace_is_high_card \
            else sorted_cards[0].get_alternate_value()

        for c in sorted_cards[1:]:
            if ace_is_high_card:
                val = c.get_alternate_value()
            else:
                val = c.get_value()

            if val - last_val != 1:
                straight = False
                break
            last_val = val
        return straight

    # metodi, joka palauttaa järjestetyn käden (lista, alkiot PlayingCard-olioita)
    # ace_is_highest (totuusarvo) määrittää ässän tulkinnan
    # True : ässä = 14
    # False : ässä = 1
    def __get_sorted_deck(self, ace_is_high_card):
        if ace_is_high_card:        # ässä = 14
            set_cards = set(self.__cards)
            high_ace_deck = []
            
            while len(set_cards) > 0:
                lowest = 20
                low_card = ""
                for c in set_cards:
                    value = c.get_alternate_value()
                    if value < lowest:
                        lowest = value
                        low_card = c
                set_cards.remove(low_card)
                high_ace_deck.append(low_card)
            return high_ace_deck           
        else:       # ässä = 1
            return sorted(self.__cards)

    # TEHTÄVÄ
    # TÄYDENNÄ METODI SITEN, ETTÄ SE ASETTAA KÄDEN ARVOKSI TEHTÄVÄNANNON 
    # MUKAISEN KOKONAISLUVUN (1-10) JA PALAUTTAA SEN (palautus annettu)
    # VOIT KÄYTTÄÄ APUNASI LUOKAN METODEITA VAPAASTI
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
            #'High Card'
            self.__adjust_rank(10)

        return self.__rank

    def get_rank_string(self):
        ranks = ['Royal Flush',
                 'Straight Flush',
                 'Four of a Kind',
                 'Full House',
                 'Flush',
                 'Straight',
                 'Three of a Kind',
                 'Two Pair',
                 'One Pair',
                 'High Card']

        if 0 < self.__rank < 11:
            return ranks[self.__rank - 1]
        else:
            self.get_rank()
            if not 0 < self.__rank < 11:
                print('Error determining rank (', self.__rank, ')')
                return ''
            return ranks[self.__rank - 1]



        return self.__rank


    # Metodi, joka palauttaa merkkijonoesityksen olion rank-parametrin
    # arvosta
    def get_rank_string(self):
        ranks = ['Royal Flush',
                 'Straight Flush',
                 'Four of a Kind',
                 'Full House',
                 'Flush',
                 'Straight',
                 'Three of a Kind',
                 'Two Pair',
                 'One Pair',
                 'High Card']

        if 0 < self.__rank < 11:
            return ranks[self.__rank - 1]
        else:
            self.get_rank()
            if not 0 < self.__rank < 11:
                print('Error determining rank (', self.__rank, ')')
                return ''
            return ranks[self.__rank - 1]

    # tätä metodia kutsutaan, kun kirjoitetaan str(x), missä x on Hand-luokan esiintymä (instance)
    def __str__(self):
        sorted_cards = sorted(self.__cards)
        str_representation = ""
        for c in sorted_cards:
            str_representation += str(c) + ", "
        return str_representation.rstrip(', ')
