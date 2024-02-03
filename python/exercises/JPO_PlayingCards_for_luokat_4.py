# kortin maa (esim. hertta)
import random
random.seed(50)


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